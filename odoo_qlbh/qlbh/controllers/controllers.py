# -*- coding: utf-8 -*-
# from odoo import http


# class Qlbh(http.Controller):
#     @http.route('/qlbh/qlbh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qlbh/qlbh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qlbh.listing', {
#             'root': '/qlbh/qlbh',
#             'objects': http.request.env['qlbh.qlbh'].search([]),
#         })

#     @http.route('/qlbh/qlbh/objects/<model("qlbh.qlbh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qlbh.object', {
#             'object': obj
#         })
