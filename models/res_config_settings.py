from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ai_api_key = fields.Char(string="API Key IA", config_parameter='ai_agent.api_key')
    ai_system_prompt = fields.Text(string="Instrucciones", config_parameter='ai_agent.system_prompt', 
                                  default="Eres un asistente experto en Odoo. Puedes consultar inventario y CRM.")