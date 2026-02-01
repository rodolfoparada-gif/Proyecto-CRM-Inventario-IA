# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import logging
import requests

_logger = logging.getLogger(__name__)

class AIAgentController(http.Controller):

    @http.route('/ai_agent/chat', type='json', auth='user')
    def chat(self, prompt, **post):
        # 1. Obtener configuración
        params = request.env['ir.config_parameter'].sudo()
        api_key = params.get_param('ai_agent.api_key')
        system_prompt = params.get_param('ai_agent.system_prompt', default="Eres un asistente experto en Odoo.")

        if not api_key or api_key == "TU_API_KEY_AQUI":
            return "⚠️ 'Mi señor', por favor configure una API Key válida en los ajustes."

        try:
            # 2. Decisión de Intención (Aquí simulamos el cerebro de la IA)
            # Para un nivel pro, enviaríamos el prompt a OpenAI para clasificar la intención.
            prompt_lower = prompt.lower()

            # Lógica de ruteo
            if any(w in prompt_lower for w in ['stock', 'inventario', 'cuantos']):
                return self._handle_inventory_query(prompt_lower)
            
            if any(w in prompt_lower for w in ['crm', 'lead', 'oportunidad', 'venta']):
                return self._handle_crm_query(prompt_lower)

            # 3. Llamada a la IA para respuestas generales (OpenAI API)
            return self._call_openai_api(api_key, system_prompt, prompt)

        except Exception as e:
            _logger.error("Error en Agente IA: %s", str(e))
            return "Hubo un error en la comunicación con el servidor de IA."

    def _call_openai_api(self, api_key, system_prompt, user_prompt):
        """Conexión real con OpenAI"""
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "model": "gpt-3.5-turbo", # O gpt-4 si tienes acceso
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.7
        }
        
        try:
            response = requests.post(url, headers=headers, json=data, timeout=10)
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                return f"Error de la API: {response.status_code}. Revise su API Key."
        except Exception as e:
            return f"Error de conexión: {str(e)}"

    def _handle_inventory_query(self, prompt):
        """Búsqueda avanzada de productos"""
        # Limpieza básica para extraer nombre
        target = prompt.replace('cuantos', '').replace('stock', '').replace('de', '').strip()
        
        domain = [('sale_ok', '=', True)]
        if target and len(target) > 2:
            domain.append(('name', 'ilike', target))

        products = request.env['product.product'].sudo().search(domain, limit=5)
        
        if not products:
            return f"No encontré productos similares a '{target}' en el inventario."

        res = "📦 **Reporte de Inventario:**\n"
        for p in products:
            res += f"• {p.name}: {p.qty_available} {p.uom_id.name}\n"
        return res

    def _handle_crm_query(self, prompt):
        """Consulta de CRM filtrada por prioridad"""
        leads = request.env['crm.lead'].sudo().search([
            ('type', '=', 'opportunity'),
            ('probability', '<', 100)
        ], limit=5, order="priority desc")

        if not leads:
            return "No hay oportunidades abiertas."

        res = "🤝 **CRM - Oportunidades Clave:**\n"
        for l in leads:
            res += f"• {l.name} | {l.expected_revenue} {l.currency_id.symbol}\n"
        return res