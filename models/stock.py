from odoo import api, fields, models


class Stock_picking(models.Model):
    _inherit = 'stock.picking'


    sale_description = fields.Char(string='about')



class Stock_picking_line(models.Model):
    _inherit = 'stock.move'
    line_number=fields.Integer(string="number")




