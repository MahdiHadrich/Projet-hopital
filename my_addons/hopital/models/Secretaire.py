from odoo import models, fields, api, _


class Secretaire(models.Model):
    _name = "hopital.secretaire"
    _inherits = {
        'res.users': 'user_id'
    }

    user_id = fields.Many2one('res.users', auto_join=True, required=True, ondelete='cascade')
    birthdate = fields.Date(required=True)
    sex = fields.Selection([(_('Male'), 'M'), (_('Female'), 'F')], required=True)

    @api.model
    def create(self, vals):
        did = super(Secretaire, self).create(vals)
        did.groups_id |= self.env.ref('hopital.secretaire_group')
        return did
