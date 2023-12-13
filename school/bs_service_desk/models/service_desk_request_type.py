from odoo import api, fields, models


class BsServiceDeskRequestType(models.Model):
    _name = "bs.service.desk.request.type"
    _description = "BS Service request type"
    _order = "sequence, id"

    name = fields.Char(string="Type name", required=True, translate=True)    
    sequence = fields.Integer(default=1)
    active = fields.Boolean(default=True)
    description = fields.Text(translate=True)
