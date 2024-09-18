import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalPatientVisit(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Patient visits'

    name = fields.Char()

    active = fields.Boolean(
        default=True,
    )

    description = fields.Text()

    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contact'
    )

    checkin_datetime = fields.Datetime()
