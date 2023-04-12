from odoo import models, fields

class Doctor(models.Model):
    _name = "hms.doctor"
    _rec_name = "first_name"
    first_name = fields.Text()
    last_name = fields.Text()
    image = fields.Image()

    # Relations 
    patient_ids = fields.Many2many(comodel_name='hms.patient', read_only=True)
    department_id = fields.Many2one(comodel_name='hms.department', read_only=True)
    department_name = fields.Char(related="department_id.name")

   