from odoo import models, api


class AIAgent(models.AbstractModel):
    _name = "ai.agent"
    _description = "AI Agent Main Service"

    # =====================================================
    # PUBLIC ENTRY POINT
    # =====================================================

    @api.model
    def process(self, message, user_id=None):
        """
        Punto principal de entrada del agente IA.
        Decide qué hacer con el mensaje del usuario.
        """

        if not message:
            return "No recibí ningún mensaje."

        message_lower = message.lower()

        # =============================
        # INVENTARIO
        # =============================
        if self._is_inventory_question(message_lower):
            return self.env["ai.tool.inventory"].get_stock_summary()

        # =============================
        # CRM
        # =============================
        if self._is_crm_question(message_lower):
            return self.env["ai.tool.crm"].get_leads_summary()

        # =============================
        # CREAR LEAD
        # =============================
        if self._is_create_lead(message_lower):
            return self.env["ai.tool.crm"].create_demo_lead()

        # =============================
        # DEFAULT
        # =============================
        return self._default_response()

    # =====================================================
    # INTENT DETECTION (MVP SIMPLE)
    # =====================================================

    def _is_inventory_question(self, msg):
        keywords = [
            "stock",
            "inventario",
            "productos",
            "producto",
            "almacen",
            "bodega",
        ]
        return any(k in msg for k in keywords)

    def _is_crm_question(self, msg):
        keywords = [
            "crm",
            "lead",
            "leads",
            "oportunidad",
            "oportunidades",
            "ventas",
        ]
        return any(k in msg for k in keywords)

    def _is_create_lead(self, msg):
        keywords = [
            "crear lead",
            "nuevo lead",
            "crear oportunidad",
        ]
        return any(k in msg for k in keywords)

    # =====================================================
    # DEFAULT RESPONSE
    # =====================================================

    def _default_response(self):
        return (
            "Puedo ayudarte con:\n"
            "- Inventario / Stock\n"
            "- Leads CRM\n"
            "- Crear Leads\n"
            "\nEjemplo:\n"
            "👉 ¿Qué stock hay?\n"
            "👉 Muéstrame los leads\n"
            "👉 Crear lead"
        )
