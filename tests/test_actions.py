from dateutil.relativedelta import relativedelta

from odoo.addons.hr_hospital.tests.common import TestCommon
from odoo.exceptions import UserError
from datetime import datetime


class TestBaseModelActions(TestCommon):

    def test_01_action_compute_age(self):
        age_computed = int(self.hr_h_patient.age_count) > 0
        self.assertTrue(age_computed,
                        msg='Age computed')

    def test_02_action_constrains_scheduled(self):

        with self.assertRaises(UserError):
            self.env['hr.hospital.patient.visit'].create({
                'name': 'Test visit #2',
                'state': 'scheduled',
                'scheduled_visit_date': datetime.now(),
                'visit_date': datetime.now(),
                'doctor_id': self.hr_h_doctor.id,
                'patient_id': self.hr_h_patient.id,
            })

    def test_03_action_constrains_active(self):

        with self.assertRaises(UserError):
            self.hr_h_visit_1.write({'active': False})

    def test_04_action_completed_visit(self):

        with self.assertRaises(UserError):
            self.hr_h_visit_2.write({
                'state': 'completed',
                'scheduled_visit_date': datetime.now() - relativedelta(days=3)
            })
