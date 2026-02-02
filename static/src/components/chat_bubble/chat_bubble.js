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
                { id: 1, role: "assistant", text: "¡Hola! ¿En qué puedo ayudarte hoy?" }
            ]
        });

        this.chatScrollRef = useRef("chatScroll");

        onPatched(() => {
            if (this.chatScrollRef.el) {
                this.chatScrollRef.el.scrollTop =
                    this.chatScrollRef.el.scrollHeight;
            }
        });
    }

    toggleChat() {
        this.state.isOpen = !this.state.isOpen;
    }

    async onInputKeydown(ev) {
        if (
            ev.key === "Enter" &&
            this.state.currentInput.trim() &&
            !this.state.isTyping
        ) {
            const userText = this.state.currentInput.trim();

            this.state.messages.push({
                id: Date.now(),
                role: "user",
                text: userText,
            });

            this.state.currentInput = "";
            this.state.isTyping = true;

            try {
                const response = await this.rpc("/ai_agent/chat", {
                    prompt: userText,
                });

                this.state.messages.push({
                    id: Date.now() + 1,
                    role: "assistant",
                    text: response,
                });
            } catch (e) {
                this.state.messages.push({
                    id: Date.now() + 1,
                    role: "assistant",
                    text: "Error conectando con Odoo.",
                });
            } finally {
                this.state.isTyping = false;
            }
        }
    }
}
