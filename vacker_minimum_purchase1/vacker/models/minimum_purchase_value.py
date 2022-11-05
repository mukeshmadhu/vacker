import logging

from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class MinimumPurchaseValue(models.Model):
    _inherit = 'product.template'

    minimum_purchase_price = fields.Float(string='Minimum Purchase Price', compute='_compute_minimun_purchase')

    def _compute_minimun_purchase(self):
        for record in self:
            if record.seller_ids:
                record.minimum_purchase_price = min(record.seller_ids.mapped('price'))
            else:
                record.minimum_purchase_price = 0
