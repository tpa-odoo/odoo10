# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ComisionConf(models.Model):
    _name = 'comision.config'
    _description = 'POS Commision Config'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string='Activo', default=True)
    line_ids = fields.One2many('comision.config_line', 'config_id')


class ComisionConfLines(models.Model):
    _name = 'comision.config_line'
    _description = 'POS Commision Config Lines'

    config_id = fields.Many2one('comision.conf')

    product_id = fields.Many2one('product.product', string='Producto')
    tasa_lavador = fields.Float(string='% Comision Lavador')
    tasa_supervisor = fields.Float(string='% Comision Supervisor')


class ResUsers(models.Model):
    _inherit = 'res.users'

    supervisor_pos = fields.Boolean(string='Supervisor')
