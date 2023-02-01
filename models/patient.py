from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError


class patientsOfHospital(models.Model):
    _name = 'hospital.patient'
    _description = "hospital patient"
    _inherit = []

    age = fields.Integer(string='AGE')
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


    def browse_api(self):
        name = self.env['hospital.patient'].browse([])
        print(name)

    def search_api(self):
        name = self.env['hospital.patient'].search([])
        print(name)

    def create_api(self):
        name = self.env['hospital.patient'].create([])
        print(name)

    def searchcount(self):
        name = self.env['hospital.patient'].search_count([])

        print(name)

    @api.model
    def create(self, values):
        if not values.get('note'):
            values['note'] = 'N/A'
        return super(patientsOfHospital, self).create(values)

    @api.onchange('responsible_id')
    def onchange_responsible_id(self):
        print("onchange done")
        # if self.responsible_id:
        self.number = self.responsible_id.phone

    @api.depends('age', 'dob')
    def patient_age_cal(self):
        for i in self:
            today = date.today()
            if i.dob:
                i.age = today.year - i.dob.year
            else:
                i.age = "dob required"

    @api.constrains("name")
    def check_name(self):
        for i in self:
            patients = self.env["hospital.patient"].search([('name', '=', i.name), ('id', '!=', i.id)])
            if patients:
                raise ValidationError("already exist")

    @api.model
    def create(self, value):
        if not value.get('note'):
            value['note'] = 'new'
        if value.get('reference', _('new')) == ('new'):
            value['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('new')
            return super(patientsOfHospital, self).create(value)

    def action_open_app(self):
        return {
            'name': 'Appointment',
            'view_mode': 'tree,form',
            'res_model': 'hospital.appointment',
            'type': 'ir.actions.act_window',
            'domain': [('patient_id', '=', self.id)],
            'target': "current"
        }

    def wiz_button(self):
        view_id = self.env.ref('hospital.view_create_wiz').id
        lines = []
        line = []
        for j in self.responsible2_ids:
            line.append(j.id)

        print('@@@@@@@@@@@@@@@@@@@@@@@@@',self.id)
        ctx = {
            'default_name': self.name,
            'default_age': self.age,
            'default_gender': self.gender,
            'default_dob': self.dob,
            'default_note': self.note,
            # 'default_responsible_id': self.responsible_id
            'default_responsible2_ids':line,
            'default_number': self.number,
            'default_responsible_id': self.responsible_id.id


        }

        return {
            'type': 'ir.actions.act_window',
            'name': 'create.wizard',
            'res_model': 'create.wizard',
            'view_id': view_id,
            'target': 'new',
            'view_mode': 'form',
            'context': ctx

        }




