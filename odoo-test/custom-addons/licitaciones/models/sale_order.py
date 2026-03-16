from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    numero_licitacion = fields.Char(string="Número de Licitación")
    entidad_estatal = fields.Char(string="Entidad Estatal")
    fecha_adjudicacion = fields.Date(string="Fecha de Adjudicación")