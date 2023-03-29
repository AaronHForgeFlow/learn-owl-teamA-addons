# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_club = fields.Boolean()

    location = fields.Char(string="Location of the Club")

    nivel_padel = fields.Selection(
        [("paquete","Paquete"),
        ("amateur","Amateu"),
        ("prof","Profesional"),
        ("top", "TOP 10")])
