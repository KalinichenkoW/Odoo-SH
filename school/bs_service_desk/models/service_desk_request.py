from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class BsServiceDeskRequest(models.Model):
    _name = 'bs.service.desk.request'
    _description = 'BS Service Desk Request'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    

    name = fields.Char(string='Name', required=True, tracking=True)

    number = fields.Char(string="Number", 
                        default='New number',
                    #    index='trigram',
                        copy=False, 
                        required=True,
                        readonly=True
                        )
    active = fields.Boolean(default=True)
    description = fields.Html(translate=True, sanitize_style=True, tracking=True)
    attachment_file = fields.Binary(attachment=False, tracking=True)
    deadline = fields.Date(string="Deadline", tracking=True)
    request_type = fields.Many2one(
        string="Request type",
        comodel_name='bs.service.desk.request.type',
        default=lambda self: self.env['bs.service.desk.request.type'].search([('sequence', '=', 1)], limit=1),
        widget='selection',
        tracking=True
    )

    priority_id = fields.Many2one(
        string='Priority',
        comodel_name='bs.service.desk.request.priority',
        default=lambda self: self.env['bs.service.desk.request.priority'].search([('priority', '=', 1)], limit=1),
        tracking=True, 
    )

    product_ids = fields.Many2many(        
        comodel_name='product.template',
        string="Products",
        tracking=True
    )

    company_id = fields.Many2one(
        comodel_name="res.partner",
        string="Сlient",
        required=True,
        domain=[("company_type", "in", ['company', 'person'])],
        tracking=True
    )

    address_id = fields.Many2one(
        comodel_name="res.partner",
        string="Address",
        domain="[('parent_id', '=', company_id)]",
        tracking=True
    )

    stage_id = fields.Many2one(
        string="Stage",
        comodel_name='bs.service.desk.stage',
        required=True,
        default=lambda self: self.env['bs.service.desk.stage'].search([('sequence', '=', 1)], limit=1),
        tracking=True
    )   


    @api.model
    def create(self, vals):
        if vals.get('number', 'New') == 'New':
            vals['number'] = self.env['ir.sequence'].next_by_code('bs.service.desk.request.sequence') or 'New'
      
        return super(BsServiceDeskRequest, self).create(vals)
