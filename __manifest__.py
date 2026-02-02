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
            "crm_inventory_ai/static/src/js/chat_loader.js",
          
        ],
    },
    "installable": True,
    "application": False,
}
