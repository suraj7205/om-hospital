from odoo import api, fields, models
from datetime import date

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    # _rec_name = "patient_id"

    patient_id = fields.Many2one("hospital.patient", string="Patients")
    gender1 = fields.Char(string='gender')
    age = fields.Integer(string='age')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    pharma_ids=fields.One2many('appointment.pharma','app_id',string='pharma')

    @api.onchange('patient_id')
    def onchange_gender(self):
        for rec in self:
            rec.gender1 = rec.patient_id.gender
            rec.age=rec.patient_id.age

    def wiz2(self):
        view_id = self.env.ref('hospital.view_create_wiz').id

        p=[]
        for l in self.pharma_ids:
            p.append((0,0,{
                'product_id':l.product_id.id,
                'price':l.price,
                'qty':l.qty

            }))

        ctx={
            'default_pharma_ids':p

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


class AppFarmacy(models.Model):
    _name = "appointment.pharma"
    _description = "App Pharmacy"


    product_id=fields.Many2one('product.product')
    qty=fields.Integer(string='quantity')
    price=fields.Float(string='price')
    app_id=fields.Many2one("hospital.appointment",string='appointment')

    @api.onchange('product_id')
    def onchange_pharma_id(self):
        print("onchange done")
        self.price = self.product_id.lst_price
