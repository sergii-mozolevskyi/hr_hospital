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
        'security/ir.model.access.csv',

        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_patient_visit_views.xml',
    ],

    'demo': [
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],

}
