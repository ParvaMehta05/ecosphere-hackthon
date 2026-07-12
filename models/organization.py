from odoo import models, fields, api

class EsgDepartment(models.Model):
    _name = 'ecosphere.department'
    _description = 'ESG Department'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    head_id = fields.Many2one('res.users', string='Department Head')
    parent_id = fields.Many2one('ecosphere.department', string='Parent Department')
    child_ids = fields.One2many('ecosphere.department', 'parent_id', string='Sub-Departments')
    
    # Employee count could be a computed field based on an HR module or a simple integer for the MVP
    employee_count = fields.Integer(string='Employee Count', default=0)
    active = fields.Boolean(string='Status', default=True)

class EsgCategory(models.Model):
    _name = 'ecosphere.category'
    _description = 'Shared ESG Category'

    name = fields.Char(string='Name', required=True)
    category_type = fields.Selection([
        ('csr', 'CSR Activity'),
        ('challenge', 'Challenge')
    ], string='Type', required=True)
    active = fields.Boolean(string='Status', default=True)