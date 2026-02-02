from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    ai_agent_enabled = fields.Boolean("Enable AI Agent")
