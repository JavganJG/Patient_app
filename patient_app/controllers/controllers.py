# -*- coding: utf-8 -*-
# from odoo import http


# class PatientApp(http.Controller):
#     @http.route('/patient_app/patient_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/patient_app/patient_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('patient_app.listing', {
#             'root': '/patient_app/patient_app',
#             'objects': http.request.env['patient_app.patient_app'].search([]),
#         })

#     @http.route('/patient_app/patient_app/objects/<model("patient_app.patient_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('patient_app.object', {
#             'object': obj
#         })
