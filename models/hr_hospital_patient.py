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

    diagnosis_count = fields.Integer(
        compute='_compute_diagnosis',
    )

    patient_visit_count = fields.Integer(
        compute='_compute_patient_visits',
    )

    @api.depends('birthday_date')
    def _compute_age(self):
        date_today = fields.Date.today()
        for patient in self:
            patient.age_count = str(relativedelta(
                date_today, patient.birthday_date).years)

    def show_patient_visits(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Patient visits',
            'res_model': 'hr.hospital.patient.visit',
            'target': 'current',
            'view_mode': 'list',
            'view_type': 'form',
            'domain': [
                ["patient_id", "=", self.id],
            ],
        }

    def show_history_diagnosis(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'List diagnosis',
            'res_model': 'hr.hospital.diagnosis',
            'target': 'current',
            'view_mode': 'list',
            'view_type': 'form',
            'domain': [
                ["patient_id", "=", self.id],
            ],
            'context': {'group_by': 'disease_id'},
        }

    def add_visit(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Quick create visit',
            'res_model': 'hr.hospital.patient.visit',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {
                'default_patient_id': self.id,
                'quick_create': True, },
        }

    def _compute_diagnosis(self):
        for patient in self:
            model_name = 'hr.hospital.diagnosis'
            patient.diagnosis_count = self.env[model_name].search_count(
                domain=[
                    ('patient_id', '=', patient.id),
                ],
            )

    def _compute_patient_visits(self):
        for patient in self:
            model_name = 'hr.hospital.patient.visit'
            patient.patient_visit_count = self.env[model_name].search_count(
                domain=[
                    ('patient_id', '=', patient.id),
                ],
            )
