/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ChatBubble } from "../components/chat_bubble/chat_bubble";

try {
    registry.category("main_components").add("AIChatBubble", {
        Component: ChatBubble,
    });
} catch (e) {
    console.warn("AI Chat no pudo registrarse:", e);
}
