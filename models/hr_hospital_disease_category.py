import logging

from odoo import models, fields, api, exceptions

_logger = logging.getLogger(__name__)


class HrHospitalDiseaseCategory(models.Model):
    _name = 'hr.hospital.disease.category'
    _description = 'Disease category'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(
        string='Name',
        index='trigram',
        required=True,
        translate=True,
    )

    complete_name = fields.Char(
        string='Complete Name',
        compute='_compute_complete_name',
        recursive=True,
        store=True,
        translate=True,
    )

    parent_id = fields.Many2one(
        comodel_name='hr.hospital.disease.category',
        string='Parent Category',
        index=True,
        ondelete='cascade'
    )

    parent_path = fields.Char(
        index=True,
        unaccent=False
    )

    child_id = fields.One2many(
        comodel_name='hr.hospital.disease.category',
        inverse_name='parent_id',
        string='Child Categories'
    )

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        """
        Check when user try to create recursion category
        :return exception.ValidationError:
        """
        if not self._check_recursion():
            raise exceptions.ValidationError(
                ('You cannot create recursive categories.')
            )

    @api.model
    def name_create(self, name):
        """
        Creates a category (parent or child) by name
        :params name: The name of new category
        :return tuple: [category.id, category.display_name]
        """
        category = self.create({'name': name})
        return category.id, category.display_name

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        """
        Forms the final name taking into account the subordination
        """
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (
                    category.parent_id.complete_name, category.name
                )
            else:
                category.complete_name = category.name
