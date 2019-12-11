# -*- coding: utf-8 -*-
from odoo import http

# class Hopital(http.Controller):
#     @http.route('/hopital/hopital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hopital/hopital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hopital.listing', {
#             'root': '/hopital/hopital',
#             'objects': http.request.env['hopital.hopital'].search([]),
#         })

#     @http.route('/hopital/hopital/objects/<model("hopital.hopital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hopital.object', {
#             'object': obj
#         })