from odoo import models


class AITools(models.AbstractModel):
    _name = "crm_inventory_ai.tools"
    _description = "AI Tools"

    def get_products(self):
        return self.env["product.product"].search([], limit=5).mapped("name")
