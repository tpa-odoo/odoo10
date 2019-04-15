# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WizardCommisionReport(models.Model):
    _name = 'wizard.comision.report'
    _description = 'Wizard POS Commision Report'

    date_from = fields.Date(string='Desde')
    date_to= fields.Date(string='Hasta')

    @api.multi
    def generate_report(self):

        df = '%s 00:00:00' % self.date_from
        dt = '%s 23:59:59' % self.date_from

        order_lines = self.env['pos.order.line'].search(
            [('order_id.date_order', '>=', df),
             ('order_id.date_order', '<=', dt)]
        ).filtered(lambda l: len(l.num_lavador) > 1)

        data = []

        for l in order_lines:
            comision_obj = l.order_id.session_id.config_id.commision_id
            if comision_obj:
                tasas = comision_obj.line_ids.search(
                    [('product_id', '=', l.product_id.id)]
                )

                data.append({
                    'product_code': l.product_id.default_code,
                    'product_name': l.product_id.name,
                    'product_price': l.price_subtotal,
                    'tasa_lavador': tasas.tasa_lavador,
                    'tasa_supervisor': tasas.tasa_supervisor,
                    'ticket': l.num_ticket,
                    'lavador': l.num_lavador,
                    'supervisor': l.supervisor,
                    'order_date': l.order_id.date_order,
                    'order_ncf': l.order_id.ncf_invoice_related,
                    'order_name': l.order_id.name,
                })