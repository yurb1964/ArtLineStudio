# -*- coding: utf-8 -*-
{
    'name': "sale_with_test_field",

    'summary': "Add field TEST",
        
    'description': """
        Long description of module's purpose
    """,

    'author': "YurB",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/sale_report_templates.xml',
        'views/sale_order_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': False,
}
