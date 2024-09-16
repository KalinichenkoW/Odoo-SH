

# import logging
# import re

# from odoo import api, fields, models, tools, _
#from odoo.exceptions import UserError, ValidationError
# from odoo.osv import expression
from odoo.exceptions import ValidationError
from odoo import models, fields, api, _



# from odoo.tools import float_compare, float_round

# _logger = logging.getLogger(__name__)



class HospitalDiseasesCategory(models.Model):
    _name = "hr.hospital.disease.category"
    _description = "Diseases Category"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char('Name', index=True, required=True)
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)
    parent_id = fields.Many2one('hr.hospital.disease.category', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    
    # child_id = fields.One2many('hr.hospital.disease.category', 'parent_id', 'Child Categories')
    child_id = fields.One2many(comodel_name='hr.hospital.disease.category', inverse_name="parent_id")
    
    disease_count = fields.Integer(compute='_compute_disease_count')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_disease_count(self):
        for obj in self:
            obj.product_count = self.env["hr.hospital.disease"].search_count([('category_id', 'child_of', obj.id)])

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))

