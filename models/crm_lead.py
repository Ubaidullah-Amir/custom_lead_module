from odoo import models, fields, api
import datetime

class CustomLead(models.Model):
    _inherit = 'crm.lead'

    def write(self, vals):
        res = super(CustomLead, self).write(vals)
        
        if ('stage_id' in vals) and (vals["stage_id"] == 4):
            for lead in self:
                
                activity_type_id = lead.env.ref('mail.mail_activity_data_todo').id
                summary = "Automated activity creation through code by overriding the write method"
                note = "This activity is created automatically thorugh code."
                date_deadline = datetime.date.today()
                user_id = lead.user_id.id
                res_model_id = lead.env.ref('crm.model_crm_lead').id

                activity_vals = {
                    'activity_type_id': activity_type_id,
                    'summary': summary,
                    'note': note,
                    'date_deadline': date_deadline,
                    'user_id': user_id,
                    'res_model_id': res_model_id,
                    'res_id': lead.id,
                }
                lead.env['mail.activity'].create(activity_vals)
            
        return res
