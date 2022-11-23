# -*- coding: utf-8 -*-
# from odoo import http


# class SaleWithTestField(http.Controller):
#     @http.route('/sale_with_test_field/sale_with_test_field', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_with_test_field/sale_with_test_field/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_with_test_field.listing', {
#             'root': '/sale_with_test_field/sale_with_test_field',
#             'objects': http.request.env['sale_with_test_field.sale_with_test_field'].search([]),
#         })

#     @http.route('/sale_with_test_field/sale_with_test_field/objects/<model("sale_with_test_field.sale_with_test_field"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_with_test_field.object', {
#             'object': obj
#         })
