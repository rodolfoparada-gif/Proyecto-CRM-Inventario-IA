from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    crm_inventory_ai_enabled = fields.Boolean(
        string="Activar Agente IA"
    )
