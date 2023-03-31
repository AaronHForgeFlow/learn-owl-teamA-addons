# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PadelLog(models.Model):
    _name = 'padel.log'
    _description = 'Padel Log'

    partner_ids = fields.Many2many(comodel_name="res.partner")
    date_log = fields.Datetime()




