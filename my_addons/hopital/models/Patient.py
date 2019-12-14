from odoo import models, fields, _


class Patient(models.Model):
    _name = "hopital.patient"

    name = fields.Char(required=True)
    birthdate = fields.Date(required=True)
    sex = fields.Selection([(_('Male'), 'M'), (_('Female'), 'F')], required=True)
    consults_id = fields.One2many('hopital.consultation', 'patient_id', string='Consultations des patients',readonly=True)
