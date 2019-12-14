from odoo import models, fields, api, exceptions, _
from . import ConsutlationTools as ct

Format = ct.formatter('%Y-%m-%d %H:%M:%S')


class Consultation(models.Model):

    _name = "hopital.consultation"

    patient_id = fields.Many2one(
        'hopital.patient', string='Patient', required=True)
    medecin_id = fields.Many2one(
        'hopital.medecin', string='Medecin', required=True)
    prescriptions_ids = fields.Many2many(
        'hopital.prescription', string='Les médicaments sur ordonnance')
    date = fields.Datetime(
        required=True, string="Date de rendez-vous")
    date_end = fields.Datetime(
        compute="_compute_date_end", store=True)
    next_date = fields.Date(string='Next appointment')
    duration = fields.Integer(
        required=True, string="Durée estimée (min.)",
                              default=30)
    symptoms = fields.Text()
    indications = fields.Text()

    @api.multi
    def _compute_now(self):
        for r in self:
            r.now = ct.now()
    now = fields.Datetime(compute="_compute_now", required=True)

    def _get_consultas(self, current, fn):
        rs = self.search([
            ['medecin_id', '=', self.medecin_id.id], ['id', '!=', current]
            ], order="date ASC")
        return [(fn(r.date), r.duration) for r in rs]

    @api.depends('date', 'duration')
    def _compute_date_end(self):
        for record in self:
            record.date_end = ct.sum(Format(record.date), record.duration)

    @api.constrains('date', 'duration')
    def _depends_check_end(self):
        for record in self:
            record.date_end = ct.sum(Format(record.date), record.duration)
            if record.date:
                date = Format(record.date)
                dates = record._get_consultas(record.id, Format)
                if not ct.is_placeable(
                        (date, record.duration),
                        record.medecin_id.break_duration, dates):
                    raise exceptions.ValidationError(
                        _("""Cette date interfère avec un autre rendez-vous
                        nt. Modifiez-le ou attribuez un autre Dr."""))

    @api.onchange('medecin_id', 'duration')
    def _del_dur_doc(self):
        self.date = False
        if self.duration < 1:
            return {
                'warning': {
                    'title': 'Error',
                    'message': _('La durée ne peut pas être inférieure à 0.')
                }
            }

    @api.onchange('date')
    def _del_date(self):
        if self.date:
            if Format(self.date) < ct.now():
                return {
                    'warning': {
                        'title': 'Error',
                        'message': 'Le rendez-vous est déjà arrivé.'
                    }
                }
            if self.next_date and self.date > self.next_date:
                self.next_date = False
                return {
                    'warning': {
                        'title': 'Error',
                        'message': _(('Les dates doivent être commandées'
                                      'chronologiquement'))
                    }
                }

    @api.onchange('next_date')
    def _del_next_date(self):
        if self.date and self.next_date:
            if self.date >= self.next_date:
                self.next_date = False
                return {
                    'warning': {
                        'title': 'Error',
                        'message': _(('Les dates doivent être commandées'
                                      'chronologiquement'))
                    }
                }
