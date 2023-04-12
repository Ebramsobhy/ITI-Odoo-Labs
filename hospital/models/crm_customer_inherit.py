from odoo import models, fields , api
from datetime import date
from odoo.exceptions import UserError

class ITIProductTemplateInherit(models.Model):

    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient')
    
    @api.constrains('related_patient_id')
    def valid_email(self):
        if self.email == self.related_patient_id.email:
            raise UserError('Email is already assigned to a different customer')

    def unlink(self):
        if self.related_patient_id:
            raise UserError('This Customer linked with patient')
        return super().unlink()     
        
    vat = fields.Char(string='Tax ID', required=True)