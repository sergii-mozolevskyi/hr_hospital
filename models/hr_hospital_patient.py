import logging

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

_logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = 'hr.hospital.person.mixin'
    _description = 'Patient'

    name = fields.Char(
        string='Name',
    )

    active = fields.Boolean(
        default=True,
        groups='base.group_no_one',
        copy=False,
    )

    description = fields.Text(
        index=True,
        translate=True,
    )

    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contact'
    )

    personal_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Personal doctor'
    )

    birthday_date = fields.Date(
        string='Date of birthday',
        required=True,
    )

    passport_data = fields.Char(
        string='Passport data'
    )

    age_count = fields.Char(
        string='Age',
        compute='_compute_age',
        store=True,
    )

    @api.depends('birthday_date')
    def _compute_age(self):
        date_today = fields.Date.today()
        for patient in self:
            patient.age_count = str(relativedelta(
                date_today, patient.birthday_date).years)
