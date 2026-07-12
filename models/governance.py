from odoo import models, fields


class EcosphereGovernance(models.Model):
    _name = 'ecosphere.governance'
    _description = 'Governance ESG Data'

    organization_name = fields.Char(string='Organization Name', required=True)

    board_members = fields.Integer(string='Board Members')
    independent_directors = fields.Integer(string='Independent Directors')

    anti_corruption_policy = fields.Boolean(string='Anti-Corruption Policy')
    whistleblower_policy = fields.Boolean(string='Whistleblower Policy')

    compliance_score = fields.Float(string='Compliance Score')

    remarks = fields.Text(string='Remarks')