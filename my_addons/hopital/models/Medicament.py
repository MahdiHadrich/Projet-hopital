from odoo import models, fields


class Medicament(models.Model):
    _name = "hospital.medicament"

    name = fields.Char(required=True)
    branch = fields.Char(required=True)
    active_substance = fields.Char(required=True, string='Substance active')
    price = fields.Float()
