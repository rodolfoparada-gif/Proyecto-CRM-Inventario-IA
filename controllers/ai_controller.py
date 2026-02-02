from odoo import http
from odoo.http import request


class AIAgentController(http.Controller):

    @http.route("/ai_agent/chat", type="json", auth="user")
    def ai_chat(self, message):
        service = request.env["ai.tool.service"].sudo()
        reply = service.run(message)
        return {"reply": reply}



    @http.route("/ai/chat", type="json", auth="user")
    def ai_chat(self, message):
        response = request.env["ai.agent.engine"].sudo().process_message(message)
        return {"response": response}
