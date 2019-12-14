from odoo import models, fields, api, _


class Medecin(models.Model):
    _name = "hopital.medecin"
    _inherits = {
        'res.users': 'user_id'
    }

    user_id = fields.Many2one('res.users', auto_join=True, required=True, ondelete='cascade')
    medicines_ids = fields.Many2many('hopital.medicine', string='Médicaments sur ordonnance')
    birthdate = fields.Date(required=True)
    sex = fields.Selection([(_('Male'), 'M'), (_('Female'), 'F')], required=True)
    break_duration = fields.Integer(required=True, default=15)
    phd = fields.Char(string='Médecin de philosophie')

    @api.model
    def create(self, vals):
        did = super(Medecin, self).create(vals)
        did.groups_id |= self.env.ref('hopital.medecin_group')
        return did
