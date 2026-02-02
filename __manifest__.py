{
    "name": "CRM Inventory AI Agent",
    "version": "1.0",
    "category": "Productivity",
    "summary": "AI Agent for CRM and Inventory",
    "author": "Rodolfo Parada",

    "depends": [
        "base",
        "web",
        "stock",
        "crm",
        "website",
    ],

    "data": [
        "security/ir.model.access.csv",
        "views/res_config_settings_views.xml",
    ],

    "assets": {
        "web.assets_backend": [
            "crm_inventory_ai/static/src/js/chat_loader.js",
            "crm_inventory_ai/static/src/components/chat/chat.js",
            "crm_inventory_ai/static/src/components/chat/chat.xml",
            "crm_inventory_ai/static/src/components/chat/chat.scss",
        ],
        "website.assets_frontend": [
            "crm_inventory_ai/static/src/js/chat_loader.js",
            "crm_inventory_ai/static/src/components/chat/chat.js",
            "crm_inventory_ai/static/src/components/chat/chat.xml",
            "crm_inventory_ai/static/src/components/chat/chat.scss",
        ],
    },

    "installable": True,
    "application": True,
}
