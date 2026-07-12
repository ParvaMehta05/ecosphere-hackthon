from odoo import models, fields

class EsgBadge(models.Model):
    _name = 'ecosphere.badge'
    _description = 'Gamification Badge'

    name = fields.Char(string='Badge Name', required=True)
    description = fields.Text(string='Description')
    unlock_rule = fields.Char(string='Unlock Rule', help="Logic or threshold required to unlock (e.g., '500 XP')")
    icon = fields.Image(string='Badge Icon', max_width=128, max_height=128)

class EsgReward(models.Model):
    _name = 'ecosphere.reward'
    _description = 'Redeemable Reward'

    name = fields.Char(string='Reward Name', required=True)
    description = fields.Text(string='Description')
    points_required = fields.Integer(string='Points Required', required=True)
    stock_status = fields.Selection([
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock')
    ], string='Stock Status', default='in_stock')