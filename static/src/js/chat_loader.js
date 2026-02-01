/** @odoo-module **/
import { registry } from "@web/core/registry";
import { ChatBubble } from "@agente_ia/components/chat_bubble/chat_bubble";

// Usamos el alias del módulo definido en el manifest
registry.category("main_components").add("AIChatBubble", {
    Component: ChatBubble,
});