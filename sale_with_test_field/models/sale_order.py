# -*- coding: utf-8 -*-

from odoo import models, fields, api, _





# class sale_with_test_field(models.Model):
class SaleOrder(models.Model):


    _inherit = 'sale.order'
    
    
    

    @api.depends('date_order','order_line.price_total')
    def _myconcat(self):
        for record in self:

            amount_untaxed = amount_tax = 0.0
            for line in record.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax

            ordr_tot = str(amount_untaxed + amount_tax)


            test_dat = fields.Datetime.to_string(record.date_order) if record.date_order !=False else fields.Datetime.to_string(datetime.now())

            record.mytestfield = "Total1 - " + ordr_tot + "   Date - " + test_dat
        return
        
        
        
    @api.onchange('mytestfield')
    def _onchange_mytestfield(self):

        if self.mytestfield !=False and len(self.mytestfield)>=50:
            return {
                    'warning': {
                        'title': _('Field Test '),
                        'message': _("The length of the TEST FIELD must be less 50 char." )
                    }
                }
        

    mytestfield = fields.Char(string='Test Field',size=50, compute='_myconcat', store=True )
    

