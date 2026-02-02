from odoo import api, models

class AIAgentEngine(models.AbstractModel):
    _name = "ai.agent.engine"
    _description = "AI Agent Engine"

    @api.model
    def process_message(self, message):
        message_lower = message.lower()

        if "stock" in message_lower or "inventario" in message_lower:
            return self.env["ai.tool.inventory"].get_stock_summary()

        if "lead" in message_lower or "crm" in message_lower:
            return self.env["ai.tool.crm"].get_leads_summary()

        if "crear lead" in message_lower:
            return self.env["ai.tool.crm"].create_demo_lead()

        return "No entendí la consulta. Puedes preguntar por stock, inventario o leads."
