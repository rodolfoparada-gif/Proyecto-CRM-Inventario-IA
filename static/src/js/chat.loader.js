/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ChatBubble } from "../components/chat/chat_bubble";

registry.category("main_components").add("crm_inventory_ai.ChatBubble", {
    Component: ChatBubble,
});
