from odoo import fields, models, api
from random import randint


class BsServiceDeskRequestPriority(models.Model):
    _name = "bs.service.desk.request.priority"
    _description = "BS Service request priority"

    def _default_color(self):
        return randint(1, 11)

    name = fields.Char(string='Priority', required=True)
    active = fields.Boolean(default=True, invisible=True)
    color = fields.Integer('Color', default=_default_color)
    dev_name = fields.Char(invisible=True)
    priority = fields.Integer(invisible=True)
