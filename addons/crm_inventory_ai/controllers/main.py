@http.route('/ai_agent/chat', type='jsonrpc', auth='user')
    def chat(self, prompt, **post):
        try:
            prompt_lower = prompt.lower()
            
            # Lógica de Inventario
            if any(w in prompt_lower for w in ['stock', 'inventario', 'producto']):
                return self._handle_inventory(prompt_lower)
            
            # Lógica de CRM
            if any(w in prompt_lower for w in ['crm', 'lead', 'oportunidad']):
                return self._handle_crm(prompt_lower)

            return "🤖 Hola, Mi señor. Puedo ayudarte con el stock o tus leads del CRM. ¿Qué prefieres?"
        except Exception as e:
            _logger.error("Error en Agente IA: %s", str(e))
            return "Error técnico en el servidor de Odoo."

    def _handle_inventory(self, prompt):
        products = request.env['product.product'].sudo().search([('sale_ok', '=', True)], limit=5)
        if not products: return "No hay productos con stock."
        res = "📦 **Inventario:**\n"
        for p in products:
            res += f"• {p.name}: {p.qty_available} uds.\n"
        return res

    def _handle_crm(self, prompt):
        leads = request.env['crm.lead'].sudo().search([('type', '=', 'opportunity')], limit=5)
        if not leads: return "No hay leads activos."
        res = "🤝 **CRM:**\n"
        for l in leads:
            res += f"• {l.name} ({l.expected_revenue or 0.0} USD)\n"
        return res