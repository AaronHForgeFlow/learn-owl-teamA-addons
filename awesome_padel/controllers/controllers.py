# -*- coding: utf-8 -*-

import logging
import random

from odoo import http
from odoo.http import request, Response
from odoo.http import request
import json
logger = logging.getLogger(__name__)
import time


class AwesomePadel(http.Controller):


    @http.route(['/padel_app/get_players'], type='http', auth='none')
    def get_players(self):
        partner_dicc = {}
        response = Response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET'
        response.headers['Connection'] = 'close'
        response.headers['Date'] = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime())
        response.headers['Expires'] = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(time.time() + 604800*60))
        players = request.env["res.partner"].sudo().search([('is_club', '=', False)])
        for player in players:
            partner_dicc[player.id] = {"name": player.name, "email": player.email, "nivel": player.nivel_padel}
        response.data = json.dumps(partner_dicc)
        return response

    @http.route(['/padel_app/get_clubs'], type='http', auth='none')
    def get_club(self):
        club_dicc = {}
        response = Response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET'
        response.headers['Connection'] = 'close'
        response.headers['Date'] = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime())
        response.headers['Expires'] = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(time.time() + 604800 * 60))
        clubs = request.env["res.partner"].sudo().search([('is_club', '=', True)])
        for club in clubs:
            club_dicc[club.id] = {"name": club.name, "email": club.email, "location": club.location}
        response.data = json.dumps(club_dicc)
        return response

    @http.route('/padel_app/save_player', auth='none', type='json', methods=['POST', 'GET'], cors="*", csrf=False)
    def save_player(self, **kwargs):
        data = json.loads(request.httprequest.data)
        # TODO:  do smth with data
        return json.dumps({})
