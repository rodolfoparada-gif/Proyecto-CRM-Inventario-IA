/** @odoo-module **/

import { Component, useState, useRef, onPatched } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class ChatBubble extends Component {

    static template = "agente_ia.ChatBubble";

    setup() {
        this.rpc = useService("rpc");

        this.state = useState({
            isOpen: false,
            currentInput: "",
            isTyping: false,
            messages: [
                { id: 1, role: "assistant", text: "Hola, soy tu asistente IA." }
            ]
        });

        this.chatScrollRef = useRef("chatScroll");

        onPatched(() => {
            if (this.chatScrollRef.el) {
                this.chatScrollRef.el.scrollTop = this.chatScrollRef.el.scrollHeight;
            }
        });
    }

    toggleChat() {
        this.state.isOpen = !this.state.isOpen;
    }

    async onInputKeydown(ev) {
        if (ev.key === "Enter" && this.state.currentInput.trim()) {

            const text = this.state.currentInput;
            this.state.currentInput = "";

            this.state.messages.push({
                id: Date.now(),
                role: "user",
                text,
            });

            try {
                const res = await this.rpc("/ai_agent/chat", { prompt: text });

                this.state.messages.push({
                    id: Date.now() + 1,
                    role: "assistant",
                    text: res,
                });

            } catch (e) {
                console.error(e);
            }
        }
    }
}
