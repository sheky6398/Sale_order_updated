from odoo import models,fields,api
import logging

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    total_weight = fields.Float(compute='_compute_total_weight',store=False)
    

    @api.depends('product_uom_qty')
    def _compute_total_weight(self):
        for rec in self:
            if rec.product_id.type == 'consu' or rec.product_id.type == 'product':
                rec.total_weight = rec.product_id.weight*rec.product_uom_qty
            else:
                rec.total_weight = 0

    



