/** @odoo-module **/

import { Component, useState, useRef, onPatched } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class ChatBubble extends Component {

    setup() {
        this.rpc = useService("rpc");

        this.state = useState({
            isOpen: false,
            currentInput: "",
            isTyping: false,
            messages: [
                { id: 1, role: "assistant", text: "Hola 👋 Soy tu asistente IA." }
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

        if (ev.key !== "Enter") return;
        if (!this.state.currentInput.trim()) return;
        if (this.state.isTyping) return;

        const userText = this.state.currentInput.trim();

        this.state.messages.push({
            id: Date.now(),
            role: "user",
            text: userText
        });

        this.state.currentInput = "";
        this.state.isTyping = true;

        try {

            const response = await this.rpc(
                "/ai_agent/chat",
                { prompt: userText }
            );

            this.state.messages.push({
                id: Date.now() + 1,
                role: "assistant",
                text: response || "Sin respuesta"
            });

        } catch (e) {

            this.state.messages.push({
                id: Date.now() + 2,
                role: "assistant",
                text: "Error conectando con Odoo"
            });

            console.error(e);

        } finally {
            this.state.isTyping = false;
        }
    }
}

ChatBubble.template = "crm_inventory_ai.ChatBubble";
