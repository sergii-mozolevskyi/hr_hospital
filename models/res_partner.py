import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    hr_hospital_doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor',
        string='Hospital Doctors',
    )

    hr_hospital_patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient',
        string='Hospital Patients',
    )
