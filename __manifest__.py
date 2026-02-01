{
    'name': 'Agente IA-CRM-Inventario',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Asistente IA para Inventario y CRM en todo Odoo',
    'author': 'Mi señor', # Un toque personal
    'depends': ['base', 'web', 'stock', 'crm', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter.xml', # IMPORTANTE: Carga los valores por defecto
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        # Cargamos en el Backend
        'web.assets_backend': [
            'ai_agent_universal/static/src/components/**/*.js',
            'ai_agent_universal/static/src/components/**/*.xml',
            'ai_agent_universal/static/src/components/**/*.scss',
            'ai_agent_universal/static/src/js/chat_loader.js', # IMPORTANTE: Carga el disparador
        ],
        # Cargamos en el Sitio Web
        'website.assets_frontend': [
            'ai_agent_universal/static/src/components/**/*.js',
            'ai_agent_universal/static/src/components/**/*.xml',
            'ai_agent_universal/static/src/components/**/*.scss',
            'ai_agent_universal/static/src/js/chat_loader.js', # IMPORTANTE: Carga el disparador
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}