# -*- coding: utf-8 -*-
{
    'name': "西西弗斯书店",

    'summary': """
        odoo开发从入门到精通示例模块""",

    'description': """
        本模块为 odoo技术开发白皮书 的配套教学模块.
        如果有问题欢迎在github中给作者提issue. 
    """,

    'author': "KevinKong",
    'website': "http://www.odoomommy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tutorial',
    'version': '15.1.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    "qweb":[
        "static/src/xml/page.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True
}