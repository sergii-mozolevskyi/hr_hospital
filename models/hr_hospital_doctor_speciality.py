import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDoctorSpeciality(models.Model):
    _name = 'hr.hospital.doctor.speciality'
    _description = 'Doctor speciality'

    name = fields.Char(
        string='Name',
    )

    active = fields.Boolean(
        default=True,
        copy=False,
    )

    description = fields.Text(
        index=True,
        translate=True,
    )
