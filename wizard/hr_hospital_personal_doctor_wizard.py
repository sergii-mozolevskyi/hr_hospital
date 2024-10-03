import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalPersonalDoctor(models.TransientModel):
    _name = 'hr.hospital.personal.doctor.wizard'
    _description = 'Mass redefinition of the personal doctor for patients'

    personal_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Personal doctor'
    )

    def change_personal_doctor(self):
        active_model = self.env.context.get('active_model')
        active_ids = self.env.context.get('active_ids')
        for active_id in active_ids:
            patient = self.env[active_model].browse(active_id)
            patient.personal_doctor_id = self.personal_doctor_id
