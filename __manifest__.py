{
    'name': 'Agente IA-CRM-Inventario',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Asistente IA para Inventario y CRM en todo Odoo',
    'depends': ['base', 'web', 'stock', 'crm', 'website'], # Dependencias clave
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        # Esto lo carga en el Backend (Administración)
        'web.assets_backend': [
            'ai_agent_universal/static/src/components/**/*.js',
            'ai_agent_universal/static/src/components/**/*.xml',
            'ai_agent_universal/static/src/components/**/*.scss',
        ],
        # Esto lo carga en el Sitio Web público
        'website.assets_frontend': [
            'ai_agent_universal/static/src/components/**/*.js',
            'ai_agent_universal/static/src/components/**/*.xml',
            'ai_agent_universal/static/src/components/**/*.scss',
        ],
    },
    'installable': True,
    'application': True,
}