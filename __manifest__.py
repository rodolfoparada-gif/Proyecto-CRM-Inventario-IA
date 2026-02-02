
    # 'installable': True,
    # 'application': True,
    # 'license': 'LGPL-3',

{
    "name": "Agente IA CRM Inventario",
    "version": "1.0",
    "category": "Productivity",
    "summary": "Asistente IA para Inventario y CRM en todo Odoo",
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
        "data/ir_config_parameter.xml",
        "views/res_config_settings_views.xml",
    ],

    "assets": {
        "web.assets_backend": [
            "crm_inventory_ai/static/src/js/chat_loader.js",
            "crm_inventory_ai/static/src/components/chat/chat_bubble.js",
            "crm_inventory_ai/static/src/components/chat/chat_bubble.xml",
            "crm_inventory_ai/static/src/components/chat/chat_bubble.scss",
        ],
        "website.assets_frontend": [
            "crm_inventory_ai/static/src/js/chat_loader.js",
            "crm_inventory_ai/static/src/components/chat/chat_bubble.js",
            "crm_inventory_ai/static/src/components/chat/chat_bubble.xml",
            "crm_inventory_ai/static/src/components/chat/chat_bubble.scss",
        ],
    },

    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
