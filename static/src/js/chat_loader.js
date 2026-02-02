/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ChatBubble } from "../components/chat_bubble/chat_bubble";

// SAFE REGISTER
try {
    registry.category("main_components").add("AIChatBubble", {
        Component: ChatBubble,
    });
} catch (e) {
    console.warn("AI ChatBubble already registered or failed", e);
}
