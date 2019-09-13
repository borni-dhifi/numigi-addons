# Copyright 2017 ACSONE SA/NV
# Copyright 2018 Tecnativa - Sergio Teruel
# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Move Line Auto Fill',
    'summary': "Stock Move Line auto fill",
    'version': '12.0.2.0.1',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,'
              'Tecnativa,'
              'Numigi,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/stock-logistics-workflow/',
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_picking.xml',
        'views/stock_picking_type_views.xml',
    ],
}
