from odoo import models, fields, api


class ConsultationWizzard(models.TransientModel):
    _name = "hopital.consultation_wizzard"

    consultations_ids = fields.Many2many(
        'hopital.consultation', string="Consultations",
        default=lambda self: self.env['hopital.consultation'].browse(
            self._context.get('active_ids')))
    medecin_id = fields.Many2one('hopital.medecin', string="Medecins")

    @api.multi
    def add(self):
        for record in self.consultations_ids:
            record.medecin_id = self.medecin_id
        return {}
