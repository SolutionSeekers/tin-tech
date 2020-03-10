# -*- coding: utf-8 -*-

from odoo import models, fields, api

class quoteFields(models.Model):
    _inherit="sale.order.line"

    line_number = fields.Char(string="Item")
