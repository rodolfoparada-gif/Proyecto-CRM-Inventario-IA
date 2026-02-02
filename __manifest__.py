
    # 'installable': True,
    # 'application': True,
    # 'license': 'LGPL-3',





{
    'name': 'Agente IA CRM Inventario',
    'version': '1.0',
    'depends': ['base', 'web', 'stock', 'crm', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'crm_inventory_ai/static/src/js/chat_loader.js',
            'crm_inventory_ai/static/src/components/chat_bubble/chat_bubble.js',
            'crm_inventory_ai/static/src/components/chat_bubble/chat_bubble.xml',
            'crm_inventory_ai/static/src/components/chat_bubble/chat_bubble.scss',
        ],
        'website.assets_frontend': [
            'crm_inventory_ai/static/src/js/chat_loader.js',
            'crm_inventory_ai/static/src/components/chat_bubble/chat_bubble.js',
            'crm_inventory_ai/static/src/components/chat_bubble/chat_bubble.xml',
            'crm_inventory_ai/static/src/components/chat_bubble/chat_bubble.scss',
        ],
    },
    'installable': True,
}
