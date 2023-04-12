from odoo import models, fields , api
from datetime import date
from odoo.exceptions import ValidationError
import re

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
    email      =  fields.Char(required=True)
    image      =  fields.Binary()
    address    =  fields.Text()
    age        =  fields.Integer(compute='compute_age')

    department_id = fields.Many2one(comodel_name='hms.department')
    department_capacity = fields.Integer(related = 'department_id.capacity') 

    doctor_ids = fields.Many2many(comodel_name='hms.doctor', read_only=True)
    states = fields.Selection([('state1' , 'Undetermined') , ('state2' , 'Good') , ('state3', 'Fair'), ('state4', 'Serious')])
    
    states_log = fields.One2many('hms.loghistory', 'patient_ids')

    def button_clicked(self):
        self.states = 'state2'
  
    @api.onchange('age')
    def _age_onchange(self):
        if self.age<30 and self.age != 0:
            self.pcr = True
            return {
                'warning': {
                    'title': 'PCR Message',
                    'message': 'PCR IS CHECKED'
                }
                }
        else:
            self.pcr  = False
        
    @api.onchange('states')
    def create_log_state(self):
        vals = {
            'description' : 'State changed to %s'%(self.states),
            'patient_ids' : self.id
        } 
        self.env['hms.loghistory'].create(vals)

    _sql_constraints = [
        ('Unique_email' , 'UNIQUE(email)' , 'This Email already assigned to another patient')
    ]    

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid Email')    

    @api.constrains('age')
    def check_age(self):
        if self.age <= 0 :
            raise ValidationError('The age must be positive number greater than 0')
    
    @api.depends('birth_date')
    def compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                        (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 0
    