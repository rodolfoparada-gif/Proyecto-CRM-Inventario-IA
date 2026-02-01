{
    'name': 'Agente IA-CRM-Inventario',
    'version': '19.0.1.0',
    'category': 'Productivity',
    'summary': 'Asistente IA para Inventario y CRM en todo Odoo',
    'author': 'Mi señor',
    'depends': ['base', 'web', 'stock', 'crm', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'agente_ia/static/src/components/chat_bubble/chat_bubble.xml',
            'agente_ia/static/src/components/chat_bubble/chat_bubble.scss',
            'agente_ia/static/src/components/chat_bubble/chat_bubble.js',
            'agente_ia/static/src/js/chat_loader.js',
        ],
        'website.assets_frontend': [
            'agente_ia/static/src/components/chat_bubble/chat_bubble.xml',
            'agente_ia/static/src/components/chat_bubble/chat_bubble.scss',
            'agente_ia/static/src/components/chat_bubble/chat_bubble.js',
            'agente_ia/static/src/js/chat_loader.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}