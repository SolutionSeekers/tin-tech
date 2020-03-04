<<<<<<< HEAD
# # -*- coding: utf-8 -*-
# {
#     'name': "Tin-Tech",
#     'author': "Indboo",
#     'summary': """
#         Módulos de Tin-Tech.
#     """,
#     'website': "http://www.indboo.com",
#     "license": "LGPL-3",
#     'category': 'Grupo Lara Villalobos',
#     'version': '13.0.1.0.1',
#     'depends': [],
#     'data': [
#         #'views/account_analytic.xml',
#         ],
# }

{
    "name": "Tin-Tech",
    "summary": "Tin-tech indboo modules",
    "version": "13.0.1.1.0",
    "author": "Indboo",
    "depends": [
        "stock_account",
        "analytic",
        "web",
	    "sale",
    ],
    "data": [
        'views/account_analytic.xml',
        'views/external_layout.xml',
	    'views/saleorder_views.xml',
    ],
    'installable': True,
=======
# -*- coding: utf-8 -*-
{
    'name': "Tin-tech",

    'summary': """
        Basic configuration for Tin-tech's Odoo instance
    """,

    'description': """
        Basic configuration for Tin-tech's Odoo instance
    """,

    'author': "Indboo",
    'website': "https://indboo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        # Mexican accounting
        # US accounting
        # Installed apps
        'web',
	'sale',
        ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/external_layout.xml',
	'views/saleorder_views.xml',
	],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
>>>>>>> 57d61af... [ADD] external_layout view for tin-tech, line_number field
}
