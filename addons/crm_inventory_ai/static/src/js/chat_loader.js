/** @odoo-module **/
import { registry } from "@web/core/registry";
import { ChatBubble } from "@Proyecto-CRM-Inventario-IA/components/chat_bubble/chat_bubble";

registry.category("main_components").add("AIChatBubble", {
    Component: ChatBubble,
}); 