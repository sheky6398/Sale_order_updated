from odoo import models,fields,api
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def cron_action_state(self):
        schedule = self.search([
            ('state', '=', 'draft')])
        if schedule:
            schedule.action_confirm()
            


    total_weighted = fields.Float(compute='_compute_total_weighted',store=False,string="Total Weight")

    @api.depends('order_line.product_template_id','order_line.product_uom_qty')
    def _compute_total_weighted(self):
        for order in self:
            total = 0.0
            for line in order.order_line:
                total += line.total_weight
            order.total_weighted = total
