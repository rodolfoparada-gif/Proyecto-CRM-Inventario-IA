/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class ChatComponent extends Component {

    setup() {
        this.state = useState({
            open: false,
            messages: [],
            input: ""
        });

        this.rpc = useService("rpc");
    }

    toggle() {
        this.state.open = !this.state.open;
    }

    async send() {

        if (!this.state.input) return;

        const msg = this.state.input;

        this.state.messages.push({
            from: "user",
            text: msg
        });

        this.state.input = "";

        const response = await this.rpc(
            "/crm_inventory_ai/chat",
            { message: msg }
        );

        this.state.messages.push({
            from: "bot",
            text: response.reply
        });
    }
}

ChatComponent.template = "crm_inventory_ai.ChatComponent";
