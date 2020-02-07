# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StockScrap(models.Model):
    _inherit = "account.analytic.account"

    proyecto = fields.Many2one('project.project', string='Proyecto')
    identificador = fields.Char(string='Identificador', store=True)

class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    proyecto_rel = fields.Char(related='account_id.proyecto.name', string = 'Proyecto')
    identificador_rel = fields.Char(related='account_id.identificador', string= 'Identificador', store=True)
