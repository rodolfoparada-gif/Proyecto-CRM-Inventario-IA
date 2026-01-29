from odoo import models, api

class AITools(models.AbstractModel):
    _name = 'ai.tools'
    _description = 'Herramientas de Odoo para la IA'

    @api.model
    def get_stock_info(self, product_name):
        # Lógica para buscar en stock.quant o product.product
        pass

    @api.model
    def get_crm_leads(self, partner_name):
        # Lógica para buscar en crm.lead
        pass