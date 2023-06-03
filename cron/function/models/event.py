from odoo import models, fields, api


class Celebration(models.Model):
    _inherit = 'celebration.event'

    # def create_email_template(self):
    #     template = self.env['mail.template'].create({
    #         'name': 'My Email Template',
    #         'subject': 'Hello {{ .name }}',
    #         'body_html': '<p>Dear {{ object.partner_id.display_name }},</p>'
    #                      '<p>This is an example email template.</p>'
    #                      '<p>Regards,</p>'
    #                      '<p>Your Company</p>'
    #     })

    @api.model
    def set_email(self):
        today = fields.Date.today()
        anniversary_event = self.search([('event_date', '=', today)])
        template = self.env.ref('function.email_template_anniversary_mail')

        for event in anniversary_event:
            template.send_mail(event.id, force_send=True)


