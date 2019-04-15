# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    comision_id = fields.Many2one('comision.config', string='Reglas de Comision')


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    num_lavador = fields.Char('Num lavador')
    num_ticket = fields.Char('Num Ticket')
    supervisor = fields.Many2one('res.users', string='Supervisor')

