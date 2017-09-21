# -*- coding: utf-8 -*-
from openerp import fields, models

class Kpi_campos(models.Model):
	_name = 'kpi.campos'

	name = fields.Char(string="Objetivo",
		 required="True",
		 help="Objetivo del indicador")

        fecha_emision = fields.Date(string="Fecha de emisión",
                help="Fecha de emisión")

        fecha_actualizacion = fields.Datetime(string="Fecha de actualización",
                related='__last_update',
                readonly=True, help="Fecha de actualización")

        anio = fields.Integer(string="",required="True",
            size=4, help="Año de los reales")

	responsable = fields.Many2one('hr.job',
		string="Responsable",
		help="Departamento responsable del objetivo",
		required="True")

	indicador = fields.Char(string="Indicador",
		help="Indicador",
		required="True")

        calculo = fields.Text(string="Calculo",
    	     help="Formula para obtener el resultado",
    	     required="True")

        meta = fields.Integer(string="Meta",
    	     help="Meta del objetivo",
        	 required="True", size=3)

        mesagosto = fields.Integer(string="Agosto",
    	    help="Real del mes de agosto")

        messeptiembre = fields.Integer(string="Septiembre",
    	     help="Real del mes de septiembre")

        mesoctubre = fields.Integer(string="Octubre",
    	     help="Real del mes de octubre")

        mesnoviembre = fields.Integer(string="Noviembre",
    	     help="Real del mes de noviembre")

        mesdiciembre = fields.Integer(string="Diciembre",
    	     help="Real del mes de diciembre")

        mesenero = fields.Integer(string="Enero",
    	     help="Real del mes de enero")

        mesfebrero = fields.Integer(string="Febrero",
    	     help="Real del mes de febrero")

        mesmarzo = fields.Integer(string="Marzo",
    	     help="Real del mes de marzo")

        mesabril = fields.Integer(string="Abril",
    	     help="Real del mes de abril")

        mesmayo = fields.Integer(string="Mayo",
    	     help="Real del mes de mayo")

        mesjunio = fields.Integer(string="Junio",
    	     help="Real del mes de mayo")

        mesjulio = fields.Integer(string="Julio",
    	     help="Real del mes de julio")

        encasoincumplimiento = fields.Many2many('kpi.incumplimientos',
            string="Incumplimientos",
            help="Qué hacer en caso de incumplimeinto")
