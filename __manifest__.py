###################################################################################
#    Created By Shiva SIngh
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
###################################################################################

{
    "name": "Sale Management", 
    "summary": """Sale Management""",
    "version": '12.0',   
    "category": 'Sale Management',   
    "license": "AGPL-3",
    "website": "http://www.shiva.in",
    "author": "Shiva Singh",
    "contributors": ["Shiva Singh"],
    "depends": ['web', 'base', 'mail', 'sale', 'stock', 'product'],
    "data": [
        'views/ko_sale_order_view.xml',

    ],
    "demo": [
    ],
    "qweb": [
    ],
    'images': ['static/description/icon.png'],
    "application": True,
    "installable": True,
}
