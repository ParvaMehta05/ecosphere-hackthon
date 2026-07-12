from odoo import models, fields

class EsgEmissionFactor(models.Model):
    _name = 'ecosphere.emission.factor'
    _description = 'Carbon Emission Factor'

    name = fields.Char(string='Factor Name (e.g., Electricity, Flight)', required=True)
    carbon_value = fields.Float(string='Carbon Equivalent (kg CO2e)', required=True)
    unit = fields.Char(string='Unit of Measurement (e.g., kWh, km)', required=True)

class EsgProductProfile(models.Model):
    _name = 'ecosphere.product.profile'
    _description = 'Product ESG Profile'

    # Assuming linkage to standard Odoo product if installed, or standalone for the MVP
    name = fields.Char(string='Product/Material Name', required=True)
    emission_factor_id = fields.Many2one('ecosphere.emission.factor', string='Emission Factor')

class EsgGoal(models.Model):
    _name = 'ecosphere.environmental.goal'
    _description = 'Sustainability Goal'

    name = fields.Char(string='Goal Name', required=True)
    target_value = fields.Float(string='Target Metric')
    deadline = fields.Date(string='Deadline')
    department_id = fields.Many2one('ecosphere.department', string='Owning Department')

class EsgPolicy(models.Model):
    _name = 'ecosphere.policy'
    _description = 'ESG Governance Policy'

    name = fields.Char(string='Policy Name', required=True)
    document_url = fields.Char(string='Document Link')
    effective_date = fields.Date(string='Effective Date')
    active = fields.Boolean(string='Status', default=True)