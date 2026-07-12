from odoo import models, fields


class EcosphereSocial(models.Model):
    _name = 'ecosphere.social'
    _description = 'Social ESG Data'

    organization_name = fields.Char(string='Organization Name', required=True)

    total_employees = fields.Integer(string='Total Employees')
    female_employees = fields.Integer(string='Female Employees')
    training_hours = fields.Float(string='Training Hours')
    volunteer_hours = fields.Float(string='Volunteer Hours')

    employee_satisfaction = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Employee Satisfaction')

    remarks = fields.Text(string='Remarks')