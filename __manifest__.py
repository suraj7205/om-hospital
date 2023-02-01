# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'hospital management',
    'version' : '1.0',
    'summary': 'hospital management software',
    'sequence': -100,
    'description': """hospital management software""",
    'category': 'Productivity',
    'depends' : ['sale','product','stock'],
    'data': ['security/ir.model.access.csv',
             'data/data.xml',
             'wizard/wiz.xml',
             'views/patient.xml',
             'views/sale.xml',
             'views/app.xml',
             'views/stock.xml',
             'report/report.xml',
             'report/patient_template.xml',
             ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
