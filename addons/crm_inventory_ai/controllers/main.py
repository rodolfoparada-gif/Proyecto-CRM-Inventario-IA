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
            
            if any(w in prompt_lower for w in ['stock', 'inventario', 'producto']):
                return self._handle_inventory(prompt_lower)
            
            if any(w in prompt_lower for w in ['crm', 'lead', 'oportunidad']):
                return self._handle_crm(prompt_lower)

            return "🤖 Hola, Mi señor. Puedo ayudarle con el Inventario o el CRM. ¿Qué desea consultar?"
        except Exception as e:
            _logger.error("Error en Agente IA: %s", str(e))
            return "Error técnico en el servidor de Odoo."

    def _handle_inventory(self, prompt):
        products = request.env['product.product'].sudo().search([('sale_ok', '=', True)], limit=5)
        if not products:
            return "No encontré productos con stock disponible."
        res = "📦 **Estado de Inventario:**\n"
        for p in products:
            res += f"• {p.name}: {p.qty_available} uds.\n"
        return res

    def _handle_crm(self, prompt):
        leads = request.env['crm.lead'].sudo().search([('type', '=', 'opportunity'), ('probability', '<', 100)], limit=5)
        if not leads:
            return "No hay oportunidades activas en el CRM."
        res = "🤝 **Oportunidades CRM:**\n"
        for l in leads:
            res += f"• {l.name} ({l.expected_revenue or 0.0} {l.company_currency_id.symbol})\n"
        return res