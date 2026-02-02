from odoo import http
from odoo.http import request


class AIAgentController(http.Controller):

    @http.route("/ai_agent/chat", type="json", auth="user")
    def chat(self, message):
        return {
            "response": f"AI Response to: {message}"
        }
