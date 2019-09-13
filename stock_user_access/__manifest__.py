# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Stock User Access',
    'version': '12.0.1.0.0',
    'summary': 'Hide the Quantity On Hand and Forecasted Quantity of products for users sale/purchase/inventory.',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://bit.ly/numigi-com',
    'license': 'LGPL-3',
    'category': 'Stock',
    'depends': ['stock', 'purchase', 'sale'],
    'data': [
        'views/product_views.xml',
    ],
    'installable': True,
}
