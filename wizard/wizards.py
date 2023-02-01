from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError


class Createwizard(models.TransientModel):
    _name = 'create.wizard'
    _description = "hospital patient"
    # _inherit = ["hospital.patient"]

    age = fields.Integer(string='AGE')
    # ref = fields.Char(string='ref', required=True)

    name = fields.Char(string='NAME', required=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others')
    ], required=True, default='male')
    note = fields.Text(string='note/about')
    number = fields.Char(string='number of driver')
    dob = fields.Date(string='dob')
    age = fields.Char(string='age', compute='patient_age_cal')
    responsible_id = fields.Many2one('res.partner', string="ambulance driver")
    responsible2_ids = fields.Many2many('res.partner.category', string='patient job')

    # @api.model
    # def default_get(self, fields):
    #     result = super(Createwizard, self).default_get(fields)
    #     result['name'] = self._context.get('active_id')
    #     # result['note'] = self._context.get('active_id')
    #
    #     return result
    # def action_print_report(self):
    #     patient=self.env['hospital.patient'].search_read([])
    #     data={
    #         'form':self.read()[0],
    #         'patient': patient
    #     }
    #     return self.env.ref("hospital.action_report_appointment").report_action(self,data=data)
