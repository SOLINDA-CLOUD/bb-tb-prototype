from odoo import fields, api, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    order_notes = fields.Html(string='Order Notes')
    collection_product = fields.Many2one('product.collections', string='Collection')
    launch_date = fields.Date(string='Launch Date')

class ProductCollections(models.Model):
    _name = 'product.collections'
    _description = 'Product Collections'

    name = fields.Char(string='Name')