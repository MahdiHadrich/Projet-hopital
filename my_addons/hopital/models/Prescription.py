from odoo import models, fields


class Prescription(models.Model):
    _name = "hopital.prescription"

    medicament_id = fields.Many2one('hopital.medicament', required=True)
    quantity = fields.Integer(required=True, string='Quantité (g/ml)')
    lapse = fields.Float(required=True, string='Temps entre les applications (hrs)')
    comments = fields.Text(required=True)
