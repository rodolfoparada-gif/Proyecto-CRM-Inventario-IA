# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class AIAgentController(http.Controller):

    @http.route('/ai_agent/chat', type='json', auth='user')
    def chat(self, prompt, **post):
        # 1. Validación de parámetros de configuración
        params = request.env['ir.config_parameter'].sudo()
        api_key = params.get_param('ai_agent.api_key')
        
        # Si no hay API Key, avisamos al usuario (puedes quitar esto si pruebas local sin OpenAI)
        if not api_key or api_key == "TU_API_KEY_AQUI":
            _logger.warning("IA Agent: API Key no configurada.")

        try:
            prompt_lower = prompt.lower()

            # 2. Gestión de Inventario (Búsqueda y Stock)
            if any(word in prompt_lower for word in ['stock', 'inventario', 'producto', 'cuanto']):
                return self._handle_inventory_query(prompt_lower)

            # 3. Gestión de CRM (Oportunidades)
            if any(word in prompt_lower for word in ['crm', 'lead', 'oportunidad', 'cliente']):
                return self._handle_crm_query(prompt_lower)

            # 4. FUNCIONALIDAD EXTRA: Modificación simple (Ejemplo: Actualizar nombre)
            # Si el usuario dice: "actualizar producto 5 a Martillo"
            if "actualizar producto" in prompt_lower:
                return self._handle_product_update(prompt_lower)

            return ("🤖 Hola, soy tu asistente. Puedo darte stock de productos o informarte sobre leads en el CRM. "
                    "Prueba con: '¿Qué stock tenemos?' o 'Dime las oportunidades del CRM'.")

        except Exception as e:
            _logger.error("Error en el Agente IA: %s", str(e))
            return "Lo siento, 'Mi señor', ocurrió un error técnico en el servidor."

    def _handle_inventory_query(self, prompt):
        """Busca productos filtrando mejor el nombre"""
        # Extraer posible nombre: si el usuario dice "stock de tornillo", buscamos "tornillo"
        search_term = prompt.replace('stock', '').replace('de', '').replace('del', '').replace('producto', '').strip()
        
        domain = [('sale_ok', '=', True)]
        if search_term and len(search_term) > 2:
            domain.append(('name', 'ilike', search_term))

        # Usamos sudo() para evitar problemas de permisos durante la prueba
        products = request.env['product.product'].sudo().search(domain, limit=5)
        
        if not products:
            return f"No encontré productos que coincidan con '{search_term}'."

        response = "📦 **Estado de Inventario:**\n"
        for prod in products:
            # qty_available es un campo calculado, Odoo lo maneja bien con sudo
            response += f"• {prod.name}: {prod.qty_available} unidades disponibles.\n"
        return response

    def _handle_crm_query(self, prompt):
        """Consulta oportunidades activas"""
        leads = request.env['crm.lead'].sudo().search([
            ('type', '=', 'opportunity'),
            ('probability', '<', 100)
        ], limit=5, order="priority desc, create_date desc")

        if not leads:
            return "No hay oportunidades abiertas actualmente."

        response = "🤝 **Oportunidades prioritarias:**\n"
        for lead in leads:
            response += f"• {lead.name} | Ingreso esperado: {lead.expected_revenue} {lead.currency_id.symbol}\n"
        return response

    def _handle_product_update(self, prompt):
        """Ejemplo de gestión: Actualizar un registro"""
        # Esto es una prueba de concepto para 'Gestionar'
        try:
            # Espera algo como "actualizar producto 10"
            parts = prompt.split()
            prod_id = int(parts[parts.index('producto') + 1])
            product = request.env['product.product'].sudo().browse(prod_id)
            if product.exists():
                # Aquí podrías poner lógica de actualización real
                return f"He localizado el producto {product.name} (ID: {prod_id}). ¿Qué cambio deseas realizar?"
            return "No encontré el ID del producto."
        except:
            return "Para actualizar, dime el ID: 'actualizar producto [ID]'"