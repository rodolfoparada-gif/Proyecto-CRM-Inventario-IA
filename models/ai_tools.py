from odoo import models, api


class AITools(models.AbstractModel):
    _name = "ai.tools"
    _description = "Herramientas IA"

    @api.model
    def get_stock_info(self, product_name):
        product = self.env["product.product"].search(
            [("name", "ilike", product_name)], limit=1
        )
        return product.qty_available if product else 0

    @api.model
    def get_crm_leads(self, name):
        leads = self.env["crm.lead"].search(
            [("name", "ilike", name)], limit=5
        )
        return leads.mapped("name")
