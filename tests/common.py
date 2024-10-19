from dateutil.relativedelta import relativedelta

from odoo import Command
from odoo.tests.common import TransactionCase
from datetime import datetime


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.group_hr_hospital_admin = self.env.ref(
            'hr_hospital.group_hr_hospital_admin'
        )
        self.hr_hospital_admin = self.env['res.users'].create({
            'name': 'HR Hospital admin',
            'login': 'hr_hospital_admin',
            'groups_id': [
                (Command.link(self.env.ref('base.group_user').id)),
                (Command.link(self.group_hr_hospital_admin.id)),
            ]
        })
        self.hr_h_patient = self.env['hr.hospital.patient'].create({
            'name': 'Angelo Brun',
            'description': 'Patient for tests',
            'birthday_date': '2004-08-14',
        })
        self.hr_h_doctor = self.env['hr.hospital.doctor'].create({
            'name': 'John Dee',
            'gender': 'male',
        })
        self.hr_h_visit_1 = self.env['hr.hospital.patient.visit'].create({
            'name':                 'Test visit #1',
            'state':                'scheduled',
            'scheduled_visit_date': datetime.now(),
            'visit_date':           datetime.now(),
            'doctor_id':            self.hr_h_doctor.id,
            'patient_id':           self.hr_h_patient.id,
        })
        self.hr_h_diagnosis_1 = self.env['hr.hospital.diagnosis'].create({
            'name': 'Test diagnosis',
            'patient_visit_id': self.hr_h_visit_1.id,
            'patient_id': self.hr_h_patient.id,
            'doctor_id': self.hr_h_doctor.id,
        })
        self.hr_h_visit_2 = self.env['hr.hospital.patient.visit'].create({
            'name': 'Test visit #2',
            'state': 'completed',
            'scheduled_visit_date': datetime.now() + relativedelta(days=1),
            'visit_date': datetime.now() + relativedelta(days=1),
            'doctor_id': self.hr_h_doctor.id,
            'patient_id': self.hr_h_patient.id,
        })
