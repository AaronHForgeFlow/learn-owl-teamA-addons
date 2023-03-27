# -*- coding: utf-8 -*-

import logging
import random

from odoo import http
from odoo.http import request, Response
from odoo.http import request
import json
logger = logging.getLogger(__name__)
import time


class AwesomeTshirt(http.Controller):

    @http.route(['/padel_app/get_partner'], type='http', auth='none')
    def get_partner(self, is_club=False):
        """
        Renders the public page to make orders
        """
        partner_dicc= {}
        response = Response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
        response.headers['Connection'] = 'close'
        response.headers['Date'] = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime())
        response.headers['Expires'] = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(time.time() + 604800*60))
        partners = request.env["res.partner"].sudo().search([('is_club', '=', is_club)])
        for partner in partners:
            partner_dicc[partner.id] = {"name": partner.name, "email": partner.email}
        response.data = json.dumps(partner_dicc)
        return response
