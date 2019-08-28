
from odoo import api, fields, models, _


class Category(models.Model):
    _inherit = "book_store.book"

    category = fields.Char("分类")
