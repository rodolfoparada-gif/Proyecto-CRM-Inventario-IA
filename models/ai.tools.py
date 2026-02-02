from odoo import models


class AITools(models.AbstractModel):
    _name = "crm_inventory_ai.tools"
    _description = "AI Tools"

    def get_products(self):
        products = self.env["product.product"].search([], limit=10)
        return [{"name": p.name, "qty": p.qty_available} for p in products]

    def get_leads(self):
        leads = self.env["crm.lead"].search([], limit=10)
        return [{"name": l.name} for l in leads]
