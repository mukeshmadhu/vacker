# -*- coding: utf-8 -*-
# from odoo import http


# class Vacker(http.Controller):
#     @http.route('/vacker/vacker/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vacker/vacker/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vacker.listing', {
#             'root': '/vacker/vacker',
#             'objects': http.request.env['vacker.vacker'].search([]),
#         })

#     @http.route('/vacker/vacker/objects/<model("vacker.vacker"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vacker.object', {
#             'object': obj
#         })
