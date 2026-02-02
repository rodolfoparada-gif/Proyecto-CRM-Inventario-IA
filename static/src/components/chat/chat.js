/** @odoo-module **/

import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class ChatComponent extends Component {

    setup() {
        this.rpc = useService("rpc");
    }

    async sendMessage(message) {
        return await this.rpc("/ai_agent/chat", {
            message: message
        });
    }
}

ChatComponent.template = "crm_inventory_ai.ChatComponent";
