from odoo import api, fields, models


class Sale_order(models.Model):
    _inherit = 'sale.order'

    sale_description = fields.Char(string='about')

class Sale_order_line(models.Model):
    _inherit = 'sale.order.line'
    line_number=fields.Integer(string="number")



    def _prepare_procurement_values(self,group_id=False):
        res=super(Sale_order_line,self)._prepare_procurement_values(group_id)
        res.update({'line_number':self.line_number})
        return res
        

class Stock_rule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id,values):
        res=super(Stock_rule,self)._get_stock_move_values( product_id, product_qty, product_uom, location_id, name, origin, company_id,
                               values)
        res['line_number']=values.get('line_number',False)
        return res