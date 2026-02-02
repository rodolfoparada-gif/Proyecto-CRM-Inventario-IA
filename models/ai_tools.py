from odoo import models


class AITools(models.AbstractModel):
    _name = "ai.tools"
    _description = "AI Tools"

    def get_stock(self, product_name):
        product = self.env["product.product"].search(
            [("name", "ilike", product_name)], limit=1
        )
        return product.qty_available if product else 0
