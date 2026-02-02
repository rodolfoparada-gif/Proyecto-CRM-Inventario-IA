from odoo import http
from odoo.http import request


class AIAgentController(http.Controller):

    @http.route("/ai_agent/chat", type="json", auth="user")
    def ai_chat(self, message):
        products = request.env["product.product"].sudo().search([], limit=5)
        leads = request.env["crm.lead"].sudo().search([], limit=5)

        return {
            "reply": f"Productos: {len(products)} | Leads: {len(leads)}"
        }
