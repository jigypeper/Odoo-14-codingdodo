# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate property data'

    name = fields.Char(required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    fascades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            # tuple is a set of value and name,
            # value is stored in the db, name is shown on front end
            ("north", "North"),
            ("east", "East"),
            ("south", "South"),
            ("west", "West")
        ]
    )
    # reserved field active is a Boolean
    active = fields.Boolean(default=True)
    state = fields.Selection(
        required=True,
        copy=False,
        selection=[
            ("new", "New"),
            ("offer recieved", "Offer Recieved"),
            ("offer accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled")
        ],
        default="new",
    )

    salesman = fields.Many2one("res.partner", string="Salesman")
    buyer = fields.Many2one("res.partner", string="Buyer")
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
