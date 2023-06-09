# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_club = fields.Boolean()

    location = fields.Char(string="Location of the Club")

    nivel_padel = fields.Selection(
        [("paquete","Paquete"),
        ("amateur","Amateu"),
        ("prof","Profesional"),
        ("top", "TOP 10")])
    # date_padel = fields.Date()

    def create_padel_partner(self, data_list, other_list):
        partners_created = []
        for dicc in data_list:
            email = dicc["email"]   
            partner = self.env["res.partner"].search([("email", "=", email)])
            if not partner:
                partner = self.env["res.partner"].create({
                    "name": dicc["nombre"],
                    "email": dicc["email"],
                    "nivel_padel": other_list[0],
                    "location": other_list[1],
                })
