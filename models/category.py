
from odoo import api, fields, models, _


class Book(models.Model):
    _inherit = "book_store.book"

    category = fields.Char("分类")
