import logging

from odoo import models, fields, api, exceptions

_logger = logging.getLogger(__name__)


class HrHospitalPatientVisit(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Patient visits'

    name = fields.Char()

    active = fields.Boolean(
        default=True,
        groups='base.group_no_one',
        copy=False,
    )

    description = fields.Text(
        index=True,
        translate=True,
    )

    state = fields.Selection(
        selection=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('canceled', 'Cancelled'),
        ],
        default='scheduled',
    )

    scheduled_visit_date = fields.Datetime(
        string='The planned date and time of the visit',
    )

    visit_date = fields.Datetime(
        string='Visit date and time',
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
    )

    diagnosis_id = fields.One2many(
        comodel_name='hr.hospital.diagnosis',
        inverse_name='patient_visit_id',
        string='Diagnosis',
    )

    @api.ondelete(at_uninstall=False)
    def _ondelete(self):
        self.ensure_one()
        if self.diagnosis_id:
            raise exceptions.UserError(
                ("You cannot delete visit with diagnosis."))

    @api.constrains('scheduled_visit_date', 'doctor_id', 'patient_id')
    def _constrains_scheduled_visit_date_doctor_patient(self):
        self.ensure_one()
        start_date = self.scheduled_visit_date.strftime("%Y-%m-%d 00:00:00")
        end_date = self.scheduled_visit_date.strftime("%Y-%m-%d 23:59:59")
        result_count = self.env['hr.hospital.patient.visit'].search_count(
            domain=[
                ('doctor_id', '=', self.doctor_id.id),
                ('patient_id', '=', self.patient_id.id),
                ('scheduled_visit_date', '>', start_date),
                ('scheduled_visit_date', '<', end_date),
                ('id', '!=', self.id),
            ]
        )
        if result_count != 0:
            raise exceptions.UserError(
                ("One patient could not be booked "
                 "with the same doctor more than once on the same day"))

    @api.constrains('visit_date', 'doctor_id', 'state')
    def _constrains_visit_date_doctor_id_state(self):
        self.ensure_one()
        today_date = fields.Datetime.today().strftime("%Y-%m-%d 00:00:00")
        start_date = self.scheduled_visit_date.strftime("%Y-%m-%d 23:59:59")
        if self.state == 'completed' and start_date < today_date:
            raise exceptions.ValidationError(
                ("It is forbidden to edit, after the visit has taken place"))

    @api.constrains('active')
    def _constrains_active(self):
        self.ensure_one()
        if not self.active and self.diagnosis_id:
            raise exceptions.UserError(
                ("You cannot archive visit with diagnosis."))
