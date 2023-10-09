from odoo import models, fields


class HospitalPatientVisit(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Hospital Patient visit'

    name = fields.Char(string='Full name', required=True)
    patient_id = fields.Many2many(comodel_name='hr.hospital.patient')
    doctor_id = fields.Many2many(comodel_name='hr.hospital.doctor')
    disease_id = fields.Many2many(comodel_name='hr.hospital.disease')
