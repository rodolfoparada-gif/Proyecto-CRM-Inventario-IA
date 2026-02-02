from odoo import http
from odoo.http import request


class AIAgentController(http.Controller):

    @http.route("/ai_agent/chat", type="json", auth="user")
    def ai_chat(self, message):
        service = request.env["ai.tool.service"].sudo()
        reply = service.run(message)
        return {"reply": reply}
