from odoo import models, fields, api

class Hmsloghistory(models.Model):
    _name = 'hms.loghistory'
    # _rec_name = 'description'

    description = fields.Text()
    patient_ids = fields.Many2one('hms.patient')


