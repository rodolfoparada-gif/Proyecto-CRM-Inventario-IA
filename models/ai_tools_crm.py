from odoo import models

class AIToolCRM(models.AbstractModel):
    _name = "ai.tool.crm"
    _description = "AI CRM Tools"

    def get_leads_summary(self):
        leads = self.env["crm.lead"].search([], limit=5)

        if not leads:
            return "No hay leads en CRM."

        result = "Leads recientes:\n"
        for l in leads:
            result += f"- {l.name}\n"

        return result

    def create_demo_lead(self):
        lead = self.env["crm.lead"].create({
            "name": "Lead creado por IA",
        })

        return f"Lead creado correctamente: {lead.name}"
