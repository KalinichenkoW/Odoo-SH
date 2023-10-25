from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Hospital Patient'
    _inherit = {'hr.hospital.person'}

    patient_name = fields.Char(string='Full name', required=True)
    #patient_person_id = fields.Many2one(comodel_name='hr.hospital.person')

    patient_treating_doctor = fields.Many2many(comodel_name='hr.hospital.doctor')
    patient_birthday = fields.Date()
    patient_age = fields.Char()
    patient_passport_data =fields.Char()


"""
Дата народження
Вік, поле повинно бути розрахунковим від поточної дати
Паспортні дані
Контактна особа
Персональний лікар
"""

    # # _inherit = {'hr.hospital.person'}


    # # patient_person_ids = fields.Many2many(string='Patient' comodel_name='hr.hospital.person')

    
    # patient_name = fields.Char()#fields.Many2one(string='Full name', comodel_name='hr.hospital.person')
    # patient_treating_doctor = fields.Many2many(comodel_name='hr.hospital.doctor')
    # # patient_birthday = fields.Date()
    # # patient_age = fields.Char()
    # # patient_passport_data =fields.Char()
