from odoo import models , fields

class ITIStudent(models.Model):
    _name = 'iti.student'
    
    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([('Male', 'male') , ('Female' , 'female')])
    accepted = fields.Boolean()