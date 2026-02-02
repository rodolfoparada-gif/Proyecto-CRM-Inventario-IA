/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ChatComponent } from "../components/chat/chat";

registry.category("main_components").add("crm_inventory_ai_chat", {
    Component: ChatComponent,
});
