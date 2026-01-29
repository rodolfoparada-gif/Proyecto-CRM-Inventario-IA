/** @odoo-module **/
import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class ChatBubble extends Component {
    setup() {
        this.state = useState({
            isOpen: false,
            currentInput: "",
            messages: [{ id: 1, role: "assistant", text: "¡Hola! ¿En qué puedo ayudarte hoy?" }]
        });
        this.rpc = useService("rpc");
    }

    toggleChat() {
        this.state.isOpen = !this.state.isOpen;
    }

    async onInputKeydown(ev) {
        if (ev.key === "Enter" && this.state.currentInput.trim()) {
            const userText = this.state.currentInput;
            this.state.messages.push({ id: Date.now(), role: "user", text: userText });
            this.state.currentInput = "";

            try {
                const response = await this.rpc("/ai_agent/chat", { prompt: userText });
                this.state.messages.push({ id: Date.now() + 1, role: "assistant", text: response });
            } catch (e) {
                this.state.messages.push({ id: Date.now() + 1, role: "assistant", text: "Error de conexión." });
            }
        }
    }
}

// Inyectar el componente en el cuerpo de la página
registry.category("main_components").add("AIChatBubble", { Component: ChatBubble });