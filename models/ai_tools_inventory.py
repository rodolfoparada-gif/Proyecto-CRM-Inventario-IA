from odoo import models

class AIToolInventory(models.AbstractModel):
    _name = "ai.tool.inventory"
    _description = "AI Inventory Tools"

    def get_stock_summary(self):
        products = self.env["product.product"].search([], limit=5)

        if not products:
            return "No hay productos en inventario."

        result = "Productos en inventario:\n"
        for p in products:
            result += f"- {p.name}: {p.qty_available}\n"

        return result
