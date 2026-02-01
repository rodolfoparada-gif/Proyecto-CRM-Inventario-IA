/** @odoo-module **/
import { Component, useState, useRef, onPatched } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class ChatBubble extends Component {
    setup() {
        this.rpc = useService("rpc");
        this.state = useState({
            isOpen: false,
            currentInput: "",
            isTyping: false,
            messages: [
                { id: 1, role: "assistant", text: "¡Hola, Mi señor! ¿En qué puedo ayudarle hoy?" }
            ]
        });
        
        this.chatScrollRef = useRef("chatScroll");

        onPatched(() => {
            this.scrollToBottom();
        });
    }

    toggleChat() {
        this.state.isOpen = !this.state.isOpen;
    }

    scrollToBottom() {
        if (this.chatScrollRef.el) {
            this.chatScrollRef.el.scrollTop = this.chatScrollRef.el.scrollHeight;
        }
    }

    async onInputKeydown(ev) {
        if (ev.key === "Enter" && this.state.currentInput.trim() && !this.state.isTyping) {
            const userText = this.state.currentInput.trim();
            
            // Mensaje del usuario
            this.state.messages.push({ id: Date.now(), role: "user", text: userText });
            this.state.currentInput = "";
            this.state.isTyping = true;

            try {
                // Llamada al backend
                const response = await this.rpc("/ai_agent/chat", { prompt: userText });
                
                this.state.messages.push({ 
                    id: Date.now() + 1, 
                    role: "assistant", 
                    text: response 
                });
            } catch (e) {
                this.state.messages.push({ 
                    id: Date.now() + 1, 
                    role: "assistant", 
                    text: "Error de conexión con el servidor." 
                });
            } finally {
                this.state.isTyping = false;
            }
        }
    }
}

// Importante: No registramos aquí para evitar circularidad si se carga en bundles distintos.
// El registro se hace en el chat_loader.js