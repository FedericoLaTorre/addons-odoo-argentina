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
from odoo import api, SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)


def sync_padron_afip(cr, registry):
    """ Try to sync data from padron """
    _logger.info('Syncking afip padron data')
    env = api.Environment(cr, SUPERUSER_ID, {})
    try:
        account_config = env['res.config.settings']
        account_config.refresh_from_padron("impuestos")
        account_config.refresh_from_padron("conceptos")
        account_config.refresh_from_padron("actividades")
    except Exception:
        pass


def post_init_hook(cr, registry):
    """Loaded after installing the module """
    _logger.info('Post init hook initialized')
    sync_padron_afip(cr, registry)
