# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class AIAgentController(http.Controller):

    @http.route('/ai_agent/chat', type='jsonrpc', auth='user')
    def chat(self, prompt, **post):
        try:
            prompt_lower = prompt.lower()
            
            # Gestión de Inventario
            if any(w in prompt_lower for w in ['stock', 'inventario', 'producto']):
                return self._handle_inventory()
            
            # Gestión de CRM
            if any(w in prompt_lower for w in ['crm', 'lead', 'oportunidad']):
                return self._handle_crm()

            return "🤖 Hola, Mi señor. Puedo ayudarle con el stock de productos o revisar sus leads del CRM. ¿Qué desea consultar?"
        except Exception as e:
            _logger.error("Error en Agente IA: %s", str(e))
            return "Error técnico en el servidor de Odoo."

    def _handle_inventory(self):
        # Buscamos los primeros 5 productos con stock
        products = request.env['product.product'].sudo().search([('sale_ok', '=', True)], limit=5)
        if not products:
            return "No encontré productos con stock disponible."
        res = "📦 **Inventario Actual:**\n"
        for p in products:
            res += f"• {p.name}: {p.qty_available} uds.\n"
        return res

    def _handle_crm(self):
        # Buscamos las oportunidades abiertas
        leads = request.env['crm.lead'].sudo().search([('type', '=', 'opportunity')], limit=5)
        if not leads:
            return "No hay leads activos en el CRM."
        res = "🤝 **Oportunidades:**\n"
        for l in leads:
            res += f"• {l.name} ({l.expected_revenue or 0.0} USD)\n"
        return res