from odoo import models, fields, api, _l



class BsServiceDeskRequest(models.Model):
    _name = 'bs.service.desk.request'
    _description = 'BS Service Desk Request'
    

    name = fields.Char(string='Name', required=True)

    number = fields.Char(string="Number", 
                        default='New number',
                    #    index='trigram',
                        copy=False, 
                        required=True,
                        readonly=True
                        )
    active = fields.Boolean(default=True)
    description = fields.Html(translate=True, sanitize_style=True)
    attachment_file = fields.Binary(attachment=False)
    deadline = fields.Date(string="Deadline")
    type_request = fields.Selection(default='service_application',  
                            selection=[('service_application', 'Service application'),
                                        ('request_for_spare_parts', 'Request for spare parts'),
                                        ('technical_consultation', 'Technical consultation'),
                                        ('other', 'Other')])

    product_ids = fields.Many2many(        
        comodel_name='product.template',
        string="Products",
    #    required=True,
    )

    company_id = fields.Many2one(
        comodel_name="res.partner",
        string="Сlient",
        required=True,
        domain=[("company_type", "in", ['company', 'person'])] # , 'person'
    )

    address_id = fields.Many2one(
        comodel_name="res.partner",
        string="Address",
        domain="[('parent_id', '=', company_id)]", # , '|', ('type', '=', contact)
    )

    # contact_company_id = fields.Many2one(
    #     comodel_name="res.partner",
    #     string="Address",
    #     domain="[('parent_id', '=', company_id), '|', ('type', '=', contact)]",
    # )
    
    responsible_manager = fields.Many2one(
        string="Responsible manager",
        comodel_name='hr.employee',
    #    required=True,
    )

    stage_id = fields.Many2one(
        string="Stage",
        comodel_name='bs.service.desk.stage',
        required=True,
        default=lambda self: self.env['bs.service.desk.stage'].search([('sequence', '=', 1)], limit=1)
    )  


    @api.model
    def create(self, vals):
        if vals.get('number', 'New') == 'New':
            vals['number'] = self.env['ir.sequence'].next_by_code('bs.service.desk.request.sequence') or 'New'
      
        return super(BsServiceDeskRequest, self).create(vals)
    
    # @api.depends('product_ids')
    # def _compute_product_info(self):
    #     for record in self:
    #         product_info = ""
    #         for product in record.product_ids:
    #             product_info += f"<b>Name:</b> {product.name}<br/><b>Barcode:</b> {product.barcode}<br/><b>Available Quantity:</b> {product.qty_available}<br/><br/>"
    #         record.product_info = product_info

# •	Номер заявки (автоматично генерується системою).
# •	Тип заявки (з варіантами: "Сервісна заявка", "Запит на запчастини", "Технічна консультація").
# •	Клієнт (поле для обрання клієнта з бази даних, має підтягнутися адреси яку менеджер сам обере та номер телефону контактної особи).
# •	Товар (поле для обрання товару з бази даних).
# •	Опис проблеми або запиту.
# •	Призначений менеджер (поле для обрання відповідального менеджера). #
# •	Стан заявки (відповідно до визначених станів заявок). #