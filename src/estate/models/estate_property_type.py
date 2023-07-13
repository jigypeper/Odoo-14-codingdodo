# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate property Type'

    name = fields.Char(required=True)