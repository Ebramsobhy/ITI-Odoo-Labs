from odoo import models, fields

class Patient(models.Model):
    _name = 'hms.patient'
    _rec_name = 'first_name'
    
    first_name =  fields.Char()
    last_name  =  fields.Char()
    birth_date =  fields.Date()
    history    =  fields.Html()
    cr_ratio   =  fields.Float()
    blood_type = fields.Selection([
        ('A', 'a'),
        ('B', 'b'),
        ('C', 'c'),
        ('O', 'o'),
    ])
    pcr        =  fields.Boolean()
    image      =  fields.Binary()
    address    =  fields.Text()
    age        =  fields.Integer()
