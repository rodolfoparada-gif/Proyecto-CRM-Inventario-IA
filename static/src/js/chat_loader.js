/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ChatBubble } from "../components/chat_bubble/chat_bubble";

// Registramos el componente ChatBubble en la categoría 'main_components'
// Esto hace que Odoo lo renderice automáticamente en el layout principal
registry.category("main_components").add("AIChatBubble", {
    Component: ChatBubble,
});