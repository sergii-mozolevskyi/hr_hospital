import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDisease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Types of diseases (diseases)'

    name = fields.Char(
        translate=True,
    )

    active = fields.Boolean(
        default=True,
        copy=False,
    )

    description = fields.Text(
        index=True,
        translate=True,
    )

    category_id = fields.Many2one(
        comodel_name='hr.hospital.disease.category',
        string='Disease category',
        required=True
    )
