import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HrHospitalDiagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()

    active = fields.Boolean(
        default=True,
        groups='base.group_no_one',
        copy=False,
    )

    patient_visit_id = fields.Many2one(
        comodel_name='hr.hospital.patient.visit',
        string='Patient visit',
    )

    patient_id = fields.Many2one(
        related='patient_visit_id.patient_id',
        store=True,
    )

    doctor_id = fields.Many2one(
        related='patient_visit_id.doctor_id',
        store=True,
    )

    is_intern = fields.Boolean(
        related='patient_visit_id.doctor_id.is_intern',
        store=True,
    )

    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string='Disease',
    )

    disease_category = fields.Many2one(
        related='disease_id.category_id',
        store=True,
    )

    appointment_treatment = fields.Text()

    is_approved = fields.Boolean(
        string='Approved by mentor',
    )

    @api.model
    def create(self, vals_list):
        res = super().create(vals_list)
        if not res.is_intern:
            res.update({'is_approved': True})
        return res
