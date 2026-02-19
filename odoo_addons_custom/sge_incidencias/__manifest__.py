# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Incidencias',
    'version': '19.0.1.0.0',
    'summary': 'Basic issue tracking module',
    'author': 'Manuel Ruiz Gutierrez',
    'category': 'Productivity',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/incidencia_views.xml',
    ],
    'installable': True,
    'application': True,
}
