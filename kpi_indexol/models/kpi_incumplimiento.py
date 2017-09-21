# -*- coding: utf-8 -*-
from openerp import fields, models

class Kpi_incumplimiento(models.Model):
	_name = 'kpi.incumplimientos'

	name = fields.Char(string="Causa del incumplimiento",
		help="Causa del incumplimiento",
		required="True")

	fecha_incumplimiento = fields.Date(string="Fecha",
		help="Fecha",
		required="True")

	accion_incumplimiento = fields.Char(string="Acción",
		help="Acción a realizar",
		required="True")

	#Pendiente a revisar
	responsable_incumplimiento = fields.Many2one('hr.job',
		string="Responsable del incumplimiento",
		required="True")