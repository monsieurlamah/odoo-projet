# -*- coding: utf-8 -*-
# from odoo import http


# class AccessRightsProject(http.Controller):
#     @http.route('/access_rights_project/access_rights_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/access_rights_project/access_rights_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('access_rights_project.listing', {
#             'root': '/access_rights_project/access_rights_project',
#             'objects': http.request.env['access_rights_project.access_rights_project'].search([]),
#         })

#     @http.route('/access_rights_project/access_rights_project/objects/<model("access_rights_project.access_rights_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('access_rights_project.object', {
#             'object': obj
#         })
