from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Hospita Doctor'

    name = fields.Char(string='Name doctor', required=True)
