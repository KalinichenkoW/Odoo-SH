from odoo import models, fields, api, _
from datetime import datetime

class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['hr.hospital.person']

    # patient_name = fields.Char(string='Full name', required=True)
    #patient_person_id = fields.Many2one(comodel_name='hr.hospital.person')

    
    date_of_birth = fields.Date(string='Patient date of birth', )
    age = fields.Integer(compute="_compute_age")
    passport_data = fields.Char(string='Patient Passport', )
    contact_person = fields.Char(string='Contact Person', )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        inverse_name='patient_id',
        string='Attending doctor'
    )

    @api.depends('date_of_birth')
    def _compute_age(self) -> None:
        for record in self:
            today = datetime.today().date()
            birthday = record.date_of_birth or today
            diff = ((today.month, today.day) < (birthday.month, birthday.day))
            record.age = today.year - birthday.year - diff

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
