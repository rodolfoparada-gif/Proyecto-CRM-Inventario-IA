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
            
            # Lógica de Inventario
            if any(w in prompt_lower for w in ['stock', 'inventario', 'producto', 'cuanto']):
                return self._handle_inventory(prompt_lower)
            
            # Lógica de CRM
            if any(w in prompt_lower for w in ['crm', 'lead', 'oportunidad', 'venta']):
                return self._handle_crm(prompt_lower)

            # Respuesta por defecto
            return "🤖 Hola, Mi señor. Puedo darle información sobre el stock de productos o las oportunidades en su CRM. ¿Qué desea consultar?"
            
        except Exception as e:
            _logger.error("Error en Agente IA: %s", str(e))
            return "Lo siento, ocurrió un error técnico en el servidor."

    def _handle_inventory(self, prompt):
        # Buscamos productos que se puedan vender
        products = request.env['product.product'].sudo().search([('sale_ok', '=', True)], limit=5)
        if not products:
            return "No encontré productos con stock registrado."
            
        res = "📦 **Reporte de Inventario:**\n"
        for p in products:
            res += f"• {p.name}: {p.qty_available} unidades disponibles.\n"
        return res

    def _handle_crm(self, prompt):
        # Buscamos oportunidades abiertas
        leads = request.env['crm.lead'].sudo().search([('type', '=', 'opportunity'), ('probability', '<', 100)], limit=5)
        if not leads:
            return "No hay oportunidades activas en el CRM."
            
        res = "🤝 **Oportunidades en CRM:**\n"
        for l in leads:
            res += f"• {l.name} (Cliente: {l.partner_id.name or 'Nuevo'})\n"
        return res