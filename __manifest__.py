# -*- coding: utf-8 -*-
{
    'name': "AI Meeting Assistant",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Student project (first odoo custom app) to create an AI Meeting Assistant that can transcribe, summarize and extract action points from meeting audio recordings.
    """,

    'author': "Romain Fochon",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
}

