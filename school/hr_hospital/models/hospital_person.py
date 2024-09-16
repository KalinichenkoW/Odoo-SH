from odoo import models, fields


class HospitalPerson(models.AbstractModel):
    _name = 'hr.hospital.person'
    _description = 'Hospital Person'

    name = fields.Char(string='Full name', required=True)
    phone = fields.Char(string='Phone')
    mail = fields.Char(string='Mail')
    image_1920 = fields.Image(string='Image', max_width=1920, max_height=1920, store=True)
    # resized fields stored (as attachment) for performance
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)


    gender = fields.Selection(
                            string='Gender',                            
                            selection=[
                                ('male', 'Male'),
                                ('female', 'Female')
                            ])


    