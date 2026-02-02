from odoo import models


class AIToolService(models.AbstractModel):
    _name = "ai.tool.service"
    _description = "AI Tool Service"

    def run(self, message):
        message = message.lower()

        if "stock" in message or "inventario" in message:
            return self._inventory_info()

        if "lead" in message or "crm" in message:
            return self._crm_info()

        if "crear lead" in message:
            return self._create_lead()

        return "No entendí la solicitud."

    def _inventory_info(self):
        products = self.env["product.product"].search([], limit=5)
        return f"Hay {len(products)} productos en inventario."

    def _crm_info(self):
        leads = self.env["crm.lead"].search([], limit=5)
        return f"Hay {len(leads)} oportunidades CRM."

    def _create_lead(self):
        lead = self.env["crm.lead"].create({
            "name": "Lead creado por IA",
        })
        return f"Lead creado ID {lead.id}"
