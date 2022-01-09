from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class visitModel(models.Model):
    _name = 'patient_app.visit_model'
    _description = 'Visit Model'


    patient = fields.Many2one("patient_app.patient_model",string="Patient",help="Patient of the visit")
    date =fields.Datetime("Last Change", compute="_createDate",store=True)
    detalle = fields.Html(string="Detalle")

    @api.depends("date")
    def _createDate(self):
        self.date = datetime.now() 
        return True

