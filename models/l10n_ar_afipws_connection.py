# -*- coding: utf-8 -*-
#    Copyright (C) 2007  pronexo.com  (https://www.pronexo.com)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################## # 
from odoo import fields, models, api, _




class L10nArAfipwsConnection(models.Model):


    _inherit = "afipws.connection"

    def _get_l10n_ar_afip_ws(self):
        """ Return the list of values of the selection field. """
        res = super()._get_l10n_ar_afip_ws()
        return [('ws_sr_padron_a5', _('Servicio de Consulta de Padrón Alcance 5'))] + res

    @api.model
    def _l10n_ar_get_afip_ws_url(self, afip_ws, environment_type):
        """ extend to add ws_sr_padron_a5 webservice """
        res = super()._l10n_ar_get_afip_ws_url(afip_ws, environment_type)
        if res:
            return res

        ws_data = {
            'ws_sr_padron_a5': {
                'production': 'https://aws.afip.gov.ar/sr-padron/webservices/personaServiceA5?wsdl',
                'testing': 'https://awshomo.afip.gov.ar/sr-padron/webservices/personaServiceA5?wsdl',
        }}
        return ws_data.get(afip_ws, {}).get(environment_type)
