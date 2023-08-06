# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"

    price = fields.Float()
    status = fields.Selection(
        copy=False,
        selection=[
            ("accepted", "Offer Accepted"),
            ("refuse", "Offer Refused")
        ]
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
