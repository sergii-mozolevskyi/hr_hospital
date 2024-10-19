import logging
import string

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _inherit = 'hr.hospital.person.mixin'
    _description = 'Doctor'

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

    speciality_id = fields.Many2one(
        comodel_name='hr.hospital.doctor.speciality',
        string='Speciality',
    )

    is_intern = fields.Boolean(
        default=False,
        copy=False,
        string='Intern',
    )

    mentor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Mentor',
        domain=[
            ('is_intern', '=', False)
        ],
    )

    mentor_phone = fields.Char(
        related='mentor_id.phone',
        string='Mentor phone',
    )

    mentor_photo = fields.Image(
        related='mentor_id.photo',
        string='Mentor photo',
    )

    intern_ids = fields.One2many(
        comodel_name='hr.hospital.doctor',
        inverse_name='mentor_id',
        string='Interns',
        readonly=True,
    )

    def _get_report_base_filename(self):
        """
        Return name of file report for current doctor
        """
        file_name = string.Template('$name($speciality)')
        return file_name.substitute(
            name=self.name,
            speciality=self.speciality_id.name,)

    def add_visit(self):
        """
        Add visit command that use in the main view
        """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Quick create visit',
            'res_model': 'hr.hospital.patient.visit',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {
                'quick_create': True,
            },
        }
