from odoo import models, fields


class HospitalDisease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Hospital Disease'

    name = fields.Char(string='Disease prevalence', required=True)
