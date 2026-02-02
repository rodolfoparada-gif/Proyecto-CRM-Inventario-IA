/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class ChatComponent extends Component {

    setup() {
        this.rpc = useService("rpc");
        this.state = useState({
            open: false,
            messages: [],
            input: "",
        });
    }

    toggle() {
        this.state.open = !this.state.open;
    }

    async send() {
        if (!this.state.input) return;

        const text = this.state.input;
        this.state.messages.push({ from: "user", text });

        const res = await this.rpc("/ai_agent/chat", {
            message: text,
        });

        this.state.messages.push({
            from: "bot",
            text: res.reply,
        });

        this.state.input = "";
    }
}

ChatComponent.template = "crm_inventory_ai.ChatComponent";

