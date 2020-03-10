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
}
