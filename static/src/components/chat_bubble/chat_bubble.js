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
            isTyping: false, // Nuevo: indicador de carga
            messages: [
                { id: 1, role: "assistant", text: "¡Hola, Mi señor! ¿En qué puedo ayudarte con el inventario o el CRM hoy?" }
            ]
        });
        
        // Referencia para el scroll automático
        this.chatScrollRef = useRef("chatScroll");

        // Cada vez que el componente se actualiza (nuevo mensaje), bajamos el scroll
        onPatched(() => {
            this.scrollToBottom();
        });
    }

    toggleChat() {
        this.state.isOpen = !this.state.isOpen;
        if (this.state.isOpen) {
            this.scrollToBottom();
        }
    }

    scrollToBottom() {
        if (this.chatScrollRef.el) {
            this.chatScrollRef.el.scrollTop = this.chatScrollRef.el.scrollHeight;
        }
    }

    async onInputKeydown(ev) {
        if (ev.key === "Enter" && this.state.currentInput.trim() && !this.state.isTyping) {
            const userText = this.state.currentInput.trim();
            
            // 1. Agregar mensaje del usuario
            this.state.messages.push({ 
                id: Date.now(), 
                role: "user", 
                text: userText 
            });
            
            this.state.currentInput = "";
            this.state.isTyping = true; // Bloqueamos entrada mientras la IA responde

            try {
                // 2. Llamada al controlador Python
                // Importante: El segundo objeto son los params que recibe el 'chat(self, prompt, **post)'
                const response = await this.rpc("/ai_agent/chat", { 
                    prompt: userText 
                });

                // 3. Agregar respuesta de la IA
                this.state.messages.push({ 
                    id: Date.now() + 1, 
                    role: "assistant", 
                    text: response 
                });
            } catch (e) {
                this.state.messages.push({ 
                    id: Date.now() + 1, 
                    role: "assistant", 
                    text: "Lo siento, hubo un error de comunicación con el servidor." 
                });
            } finally {
                this.state.isTyping = false;
            }
        }
    }
}

// Registro global para que aparezca en todo Odoo (Backend)
registry.category("main_components").add("AIChatBubble", { Component: ChatBubble });