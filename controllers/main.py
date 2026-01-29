# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)

class AIAgentController(http.Controller):

    @http.route('/ai_agent/chat', type='json', auth='user')
    def chat(self, prompt):
        # 1. Obtener parámetros configurados por el usuario
        params = request.env['ir.config_parameter'].sudo()
        api_key = params.get_param('ai_agent.api_key')
        system_prompt = params.get_param('ai_agent.system_prompt', default="Eres un asistente útil de Odoo.")

        if not api_key:
            return "Error: Por favor, configura la API Key en los ajustes de Odoo."

        try:
            # 2. Lógica de consulta al Inventario
            # Si el usuario pregunta por stock o productos
            if any(word in prompt.lower() for word in ['stock', 'inventario', 'producto', 'cuantos']):
                return self._handle_inventory_query(prompt)

            # 3. Lógica de consulta al CRM
            # Si el usuario pregunta por leads, clientes o ventas
            if any(word in prompt.lower() for word in ['crm', 'lead', 'oportunidad', 'cliente']):
                return self._handle_crm_query(prompt)

            # 4. Respuesta General (Aquí podrías conectar con la API de OpenAI)
            # Por ahora, devolvemos una respuesta de guía si no detecta intención
            return ("No estoy seguro de qué módulo consultar. "
                    "Prueba preguntando: '¿Cuál es el stock de [producto]?' o "
                    "'¿Qué oportunidades tengo en el CRM?'")

        except Exception as e:
            _logger.error("Error en el Agente IA: %s", str(e))
            return "Lo siento, ocurrió un error al procesar tu solicitud."

    def _handle_inventory_query(self, prompt):
        """Busca productos y su stock disponible"""
        # Intentamos extraer un nombre de producto (búsqueda simple)
        words = prompt.split()
        search_name = words[-1] if len(words) > 1 else ""
        
        domain = [('sale_ok', '=', True)]
        if len(search_name) > 2:
            domain.append(('name', 'ilike', search_name))

        products = request.env['product.product'].sudo().search(domain, limit=5)
        
        if not products:
            return "No encontré productos con ese nombre en el inventario."

        response = "📦 **Información de Inventario:**\n"
        for prod in products:
            response += f"- {prod.name}: {prod.qty_available} {prod.uom_id.name} disponibles.\n"
        return response

    def _handle_crm_query(self, prompt):
        """Busca oportunidades abiertas en el CRM"""
        leads = request.env['crm.lead'].sudo().search([
            ('type', '=', 'opportunity'),
            ('probability', '<', 100)
        ], limit=5, order="create_date desc")

        if not leads:
            return "No hay oportunidades activas en el CRM en este momento."

        response = "🤝 **Oportunidades en CRM:**\n"
        for lead in leads:
            response += f"- {lead.name} (Cliente: {lead.partner_id.name or 'Nuevo'})\n"
        return response