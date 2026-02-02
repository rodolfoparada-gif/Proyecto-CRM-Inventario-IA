/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ChatComponent } from "../components/chat/chat";

registry.category("actions").add("crm_inventory_ai.chat", ChatComponent);
