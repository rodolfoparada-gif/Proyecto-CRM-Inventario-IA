{
    'name': 'Agente IA-CRM-Inventario',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Asistente IA para Inventario y CRM en todo Odoo',
    'author': 'Rodolfo Parada',
    'depends': ['base', 'web', 'stock', 'crm', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'Proyecto-CRM-Inventario-IA/static/src/components/**/*.js',
            'Proyecto-CRM-Inventario-IA/static/src/components/**/*.xml',
            'Proyecto-CRM-Inventario-IA/static/src/components/**/*.scss',
            'Proyecto-CRM-Inventario-IA/static/src/js/chat_loader.js',
        ],
        'website.assets_frontend': [
            'Proyecto-CRM-Inventario-IA/static/src/components/**/*.js',
            'Proyecto-CRM-Inventario-IA/static/src/components/**/*.xml',
            'Proyecto-CRM-Inventario-IA/static/src/components/**/*.scss',
            'Proyecto-CRM-Inventario-IA/static/src/js/chat_loader.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}