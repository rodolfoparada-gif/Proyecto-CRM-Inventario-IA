/** @odoo-module **/
import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class ChatBubble extends Component {
    static template = "agente_ia.ChatBubble";

    setup() {
        this.rpc = useService("rpc");
        this.state = useState({
            isOpen: false,
            currentInput: "",
            messages: [{ id: 1, role: "assistant", text: "¡Hola, Mi señor! ¿Consultamos el stock?" }]
        });
    }

    toggleChat() {
        this.state.isOpen = !this.state.isOpen;
    }

    async onInputKeydown(ev) {
        if (ev.key === "Enter" && this.state.currentInput.trim()) {
            const userText = this.state.currentInput;
            this.state.messages.push({ id: Date.now(), role: "user", text: userText });
            this.state.currentInput = "";

            const response = await this.rpc("/ai_agent/chat", { prompt: userText });
            this.state.messages.push({ id: Date.now() + 1, role: "assistant", text: response });
        }
    }
}