{
    "name": "CRM Inventory AI",
    "version": "1.0",
    "category": "Tools",
    "summary": "AI assistant for CRM and Inventory",
    "depends": [
        "base",
        "web",
        "stock",
        "crm",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [

            # JS Loader
            "crm_inventory_ai/static/src/js/chat_loader.js",

            # OWL Component JS
            "crm_inventory_ai/static/src/components/chat/chat.js",

            # OWL Template XML
            "crm_inventory_ai/static/src/components/chat/chat.xml",

            # Styles
            "crm_inventory_ai/static/src/components/chat/chat.scss",
        ],
    },
    "installable": True,
    "application": False,
}
