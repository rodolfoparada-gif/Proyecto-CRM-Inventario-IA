from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class AIAgentController(http.Controller):

    @http.route("/ai_agent/chat", type="json", auth="user")
    def chat(self, prompt, **post):
        try:
            prompt_lower = prompt.lower()

            if any(w in prompt_lower for w in ["stock", "inventario", "producto"]):
                return self._handle_inventory()

            if any(w in prompt_lower for w in ["crm", "lead", "oportunidad"]):
                return self._handle_crm()

            return "Hola 👋 Puedo ayudarte con inventario o CRM."

        except Exception as e:
            _logger.error("AI Agent Error: %s", str(e))
            return "Error en servidor Odoo"

    def _handle_inventory(self):
        products = request.env["product.product"].sudo().search([], limit=5)

        if not products:
            return "No hay productos disponibles"

        res = "📦 Inventario:\n"
        for p in products:
            res += f"• {p.name}: {p.qty_available}\n"

        return res

    def _handle_crm(self):
        leads = request.env["crm.lead"].sudo().search([], limit=5)

        if not leads:
            return "No hay oportunidades"

        res = "🤝 CRM:\n"
        for l in leads:
            res += f"• {l.name}\n"

        return res
