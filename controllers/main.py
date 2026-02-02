from odoo import http
from odoo.http import request

class AIAgentController(http.Controller):

    @http.route('/ai_agent/chat', type='jsonrpc', auth='user')
    def chat(self, prompt, **kw):

        prompt = (prompt or "").lower()

        if "stock" in prompt or "inventario" in prompt:
            return self._inventory()

        if "crm" in prompt or "lead" in prompt:
            return self._crm()

        return "Puedo ayudarte con inventario o CRM."

    def _inventory(self):

        products = request.env['product.product'].sudo().search([], limit=5)

        res = "Inventario:\n"

        for p in products:
            res += f"{p.name} → {p.qty_available}\n"

        return res

    def _crm(self):

        leads = request.env['crm.lead'].sudo().search([], limit=5)

        res = "Oportunidades:\n"

        for l in leads:
            res += f"{l.name}\n"

        return res
