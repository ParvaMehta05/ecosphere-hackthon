from odoo import models, fields


class EcosphereEnvironmental(models.Model):
    _name = 'ecosphere.environmental'
    _description = 'Environmental ESG Data'

    organization_name = fields.Char(string='Organization Name', required=True)

    electricity_usage = fields.Float(string='Electricity Usage (kWh)')
    water_usage = fields.Float(string='Water Usage (Litres)')
    carbon_emission = fields.Float(string='Carbon Emission (kg CO₂)')
    waste_generated = fields.Float(string='Waste Generated (kg)')

    reporting_year = fields.Integer(string='Reporting Year')
    remarks = fields.Text(string='Remarks')