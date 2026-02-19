# -*- coding: utf-8 -*-
from odoo import models, fields

class Incidencia(models.Model):
    _name = 'gestion.incidencia'
    _description = 'Incidencia'

    name = fields.Char(string='Título', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha')
