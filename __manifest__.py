{
    'name': 'HR hospital',
    'version': '17.0.1.0.0',
    'description': 'Hospital: records of doctors and patients',
    'author': 'Sergii Mozolevskyi',
    'website': 'https://www.odoo.com/apps',
    'category': 'Human Resources',
    'license': 'OPL-1',

    'depends': {
        'base',
    },

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'security/hr_hospital_groups.xml',
        'security/ir.model.access.csv',
        'security/hr_hospital_security.xml',
        'data/disease_data.xml',

        'wizard/hr_hospital_personal_doctor_wizard_views.xml',
        'wizard/hr_hospital_report_diseases_wizard_views.xml',

        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_doctor_speciality_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_patient_visit_views.xml',
        'views/hr_hospital_diagnosis_views.xml',

        'report/hr_hospital_doctor_report.xml',

    ],

    'demo': [
        'demo/res_partner_demo.xml',
        'demo/hr.hospital.doctor.csv',
        'demo/hr_hospital_patient_demo.xml',
        'demo/hr_hospital_patient_visit_demo.xml',
        'demo/hr_hospital_diagnosis_demo.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],

}
