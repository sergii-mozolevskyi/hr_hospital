from odoo import models, fields


class HrHospitalPersonMixin(models.AbstractModel):
    _name = 'hr.hospital.person.mixin'
    _description = 'Person'

    person_name = fields.Char(
        string='Surname, First name (Full)',
    )

    phone = fields.Char(
        string='Phone number'
    )

    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        default='other',
    )

    photo = fields.Image(
        string='Photo',
    )
