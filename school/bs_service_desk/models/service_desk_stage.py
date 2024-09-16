from odoo import api, fields, models


class BsServiceDeskStage(models.Model):
    _name = "bs.service.desk.stage"
    _description = "BS Service Desk Stage"
    _order = "sequence, id"

    name = fields.Char(string="Stage Name", required=True, translate=True)    
    sequence = fields.Integer(default=1)
    active = fields.Boolean(default=True)
    description = fields.Html(translate=True, sanitize_style=True)
