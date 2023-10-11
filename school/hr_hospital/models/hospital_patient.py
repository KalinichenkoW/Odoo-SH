from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Full name', required=True)
    treating_doctor = fields.Many2many(comodel_name='hr.hospital.doctor')
