/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";
import { jsonrpc } from "@web/core/network/rpc_service";

class AIChat extends Component {

    setup() {
        this.state = useState({
            messages: [],
            input: ""
        });
    }

    async sendMessage() {
        if (!this.state.input) return;

        const userMessage = this.state.input;
        this.state.messages.push({ from: "user", text: userMessage });

        const result = await jsonrpc("/ai/chat", {
            message: userMessage
        });

        this.state.messages.push({
            from: "ai",
            text: result.response
        });

        this.state.input = "";
    }
}

AIChat.template = "crm_inventory_ai.AIChat";

registry.category("main_components").add("ai_chat", {
    Component: AIChat
});
