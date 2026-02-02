from odoo import http
from odoo.http import request


class AIAgentController(http.Controller):

    @http.route("/crm_inventory_ai/chat", type="json", auth="user")
    def ai_chat(self, message):
        return {
            "reply": f"Recibí tu mensaje: {message}"
        }

