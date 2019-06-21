# -*- coding: utf-8 -*-
{
    'name': "book_store",

    'summary': """
        demo module for tutorial.""",

    'description': """
        This module is writing for who wants learn odoo developments.
    """,

    'author': "KevinKong",
    'website': "http://mixoo.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tutorial',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/inherit_view.xml'
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True
}