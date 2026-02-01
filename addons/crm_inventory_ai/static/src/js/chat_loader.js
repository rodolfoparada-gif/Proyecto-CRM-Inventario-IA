/** @odoo-module **/
import { registry } from "@web/core/registry";
import { ChatBubble } from "@crm_inventory_ai/components/chat_bubble/chat_bubble";

// Registramos el componente en el WebClient global
registry.category("main_components").add("AIChatBubble", {
    Component: ChatBubble,
});