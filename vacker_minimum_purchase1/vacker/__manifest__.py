# -*- coding: utf-8 -*-
{
    'name': "vacker",

    'summary': """
        Minimum Purchase price for each product""",

    'description': """
        This module is used to display the Minimum Purchase Price from n number of vendors for single product
    """,

    'author': "Madhusoodanan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product_Minimum_Purchase_Price',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',
        'purchase',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/minimum_purchase_value_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
