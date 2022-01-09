from xmlrpc.client import DateTime
from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError
import re

class PatientModel(models.Model):
    _name = 'patient_app.patient_model'
    _description = 'Patient Model'


    dni = fields.Char(string='Patient DNI',help="DNI of the patient", required=True)
    name = fields.Char(string='Patient Name', help="Name of the patient", required=True)
    surnames = fields.Char(string='Patient Surnames',help="Surnames of the patient",  required=True)
    phone = fields.Char(string='Patient phone', help="Phone of the patient")
    date = fields.Datetime(string='Birthdate', help="Birthdate of the patient", required=True)
    email = fields.Char(string='Patient email' ,help="Email of the patient")
    image = fields.Image(help="Image of the patient")
    numVisits =fields.Integer(help="Number of visits of the patient",string="Number of visits", compute="_addVisits")
    visits= fields.One2many("patient_app.visit_model","patient",string="Visits",help="Visits of the patient")

    @api.depends("visits")
    def _addVisits(self):
        self.numVisits = len(self.visits)
        return True

    @api.constrains("dni")

    def _check_dni(self):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        nif = self.dni
        respuesta = "No ha introducido un NIF valido"
        if (len(nif) == 9):
            letraControl = nif[8].upper()
            dn = nif[:8]
            if ( len(dn) == len( [n for n in dn if n in numeros] ) ):
                if tabla[int(dn)%23] == letraControl:
                    respuesta="El NIF introducido es correcto"
                else:
                    raise ValidationError("The DNI is not valid")
        return True

    @api.constrains("date")

    def _check_birthday(self):
        nowdate = datetime.now().today()
        birthdate =  fields.datetime.now().today()
        
        age_in_years = nowdate.year - birthdate.year - ((nowdate.month, nowdate.day) < (birthdate.month, birthdate.day))
        if age_in_years < 18:

            """raise ValidationError("The patient not's older than 18")"""

        return True
  

    """@api.constrains("email")

    def _check_email(self):
        pEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(pEmail,self.email):

            raise ValidationError("Email is not correct!")

        return True"""