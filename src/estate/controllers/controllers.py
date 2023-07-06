# -*- coding: utf-8 -*-
# from odoo import http


# class CodingdodoAddons/moduleName(http.Controller):
#     @http.route('/codingdodo_addons/module_name/codingdodo_addons/module_name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/codingdodo_addons/module_name/codingdodo_addons/module_name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('codingdodo_addons/module_name.listing', {
#             'root': '/codingdodo_addons/module_name/codingdodo_addons/module_name',
#             'objects': http.request.env['codingdodo_addons/module_name.codingdodo_addons/module_name'].search([]),
#         })

#     @http.route('/codingdodo_addons/module_name/codingdodo_addons/module_name/objects/<model("codingdodo_addons/module_name.codingdodo_addons/module_name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('codingdodo_addons/module_name.object', {
#             'object': obj
#         })
