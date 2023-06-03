from odoo import models, fields


class Celebration(models.Model):
    _name = "celebration.event"

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    event_date = fields.Date(string='Event Date')


