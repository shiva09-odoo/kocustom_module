# -*- coding: utf-8 -*-
import json
import re
import uuid
from functools import partial
from lxml import etree
from dateutil.relativedelta import relativedelta
from werkzeug.urls import url_encode
from odoo import api, exceptions, fields, models, _
from odoo.tools import email_re, email_split, email_escape_char, float_is_zero, float_compare, \
    pycompat, date_utils
from odoo.tools.misc import formatLang
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo.addons import decimal_precision as dp
import logging
from datetime import datetime

_logger = logging.getLogger(__name__)



class SaleOrder(models.Model):
    _inherit = 'sale.order'


   #QUERY Sale Order POST API      
    @api.multi
    def sale_order_log(self):
        if self.estimated_delivery_date == False:
            print("=====shhhhhh======")
            sale_data = {}
            sale_data.create({
                    "name" : self.name,
		    "partner_id":self.partner_id.name,	

                })
            double_quote_sale = json.dumps(sale_data)
            # Connection from sale
            URL = 'http://sale_order/create'
	    autontication_key = 'XXXXXXXXXXXXXXXXXXXX'
            autontication_key = self.env['ir.config_parameter'].sudo().get_param('autontication_key')
            if not autontication_key:
                raise Warning(_('Please Add Authontication for Rest API in General Settings.'))
            if autontication_key:
                headers = {
                            'Content-Type': 'application/json',
                            'Authorization': autontication_key,
                         }
                try:  
                    sale_request = requests.post(URL, data=double_quote_sale, headers=headers)
                    print("=====sale_request==",sale_request)
                    request_data = sale_request.json()


                    if str(sale_request) == "<Response [200]>" and request_data and request_data.get('Costs'):
                        # Update sale order
                        for line in request_data.get('Costs'):
                            sale_lines = {                
                                        "prodcut_id": line.get("prodcut_id"),
                                        "qty": line.get("qty"),
        
                                    }
                            self.order_line = [(0, 0, sale_lines)]

       
               

                except Exception as e:
                    _logger.exception('connection failed')


















