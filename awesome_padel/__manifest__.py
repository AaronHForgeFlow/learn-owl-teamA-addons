# -*- coding: utf-8 -*-
{
    'name': "Awesome Padel",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        This app helps you to manage a business of printing customized t-shirts
        for online customers. It offers a public page allowing customers to make
        t-shirt orders.

        Note that this is just a toy app intended to learn the javascript
        framework.
    """,

    'author': "FF & CB",
    'website': "https://www.github.com/AaronHForgeFlow/owl-learning-teamA",

    'category': 'Productivity',
    'version': '0.1',
    'application': True,
    'installable': True,
    'data': ["views/res_partner_view.xml"],

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

}
