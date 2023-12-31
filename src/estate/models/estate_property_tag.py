# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate property tags'

    name = fields.Char(required=True)