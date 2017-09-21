# -*- coding: utf-8 -*-
{
    'name': "Modulo de KPI",

    'summary': """
        Desarrollado a partir de las especificaciones para los indicadores""",

    'description': """
       Indicadores creados a partir del documento recibido
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'views/kpi_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
