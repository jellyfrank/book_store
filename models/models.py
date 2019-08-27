# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
from datetime import date
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'book_store.book'

    name = fields.Char('名称', help='书名')
    author = fields.Many2one(
        'book_store.author', string='作者', help='作者', delegate=True)
    date = fields.Date("出版日期", help="日期",default=date.today())
    price = fields.Float("定价", help="定价")
    ref = fields.Reference(
        selection=[('book_store.author', '作者'), ('book_store.publisher', '出版商')])
    age = fields.Integer('书龄', compute="_get_book_age", search="_search_ages")

    @api.one
    def btn_test(self):
        """测试方法"""
        _logger.info(f"测试创建出版商和作者")
        self.env['book_store.publisher'].sudo().create({
            "name": "超新星出版社",
            "signed_authors": [(0, 0, {'name': '本杰明 巴顿', 'age': 90}), (0, 0, {'name': '刘天然', 'age': 28})]
        })

    @api.depends('date')
    def _get_book_age(self):
        self.age = (date.today() - self.date).days

    @api.model
    def _search_ages(self, operator, operand):
        """search方法"""
        if operator not in ('>', '>=', '<', '<=', '='):
            return []
        if type(operand) not in (float, int):
            return []
        start_date = datetime.now().date() - timedelta(days=operand)
        ops = {
            ">": "<",
            ">=": "<=",
            "<": ">",
            "<=": ">=",
            "=": "="
        }
        return [('date', ops[operator], start_date)]

    @api.multi
    def write(self, vals):
        _logger.info(f"write:{vals}")
        _logger.info(f"self:{self}")
        res = super(Book, self).write(vals)
        return res

    


class eBook(models.Model):
    _inherit = "book_store.book"
    _name = "book_store.ebook"

    etype = fields.Selection(selection=[('mobi', 'Mobi'), ('epub', 'Epub'), (
        'awz', 'Awz3')], string='电子书格式', default='epub', help='')


class sBook(models.Model):

    _name = "book_store.sbook"
    _inherits = {'book_store.ebook': 'ebook_id'}

    ebook_id = fields.Many2one(
        'book_store.ebook', string='ebook', ondelete='restrict', required=True, help='')


class Author(models.Model):

    _name = 'book_store.author'

    name = fields.Char('名称', help='作者名称')
    age = fields.Integer('年龄')
    publisher_id = fields.Many2one(
        'book_store.publisher', string='签约出版商', ondelete='no action', required=True, help='')


class Publisher(models.Model):

    _name = "book_store.publisher"

    name = fields.Char('名称', help='出版商名称')
    signed_authors = fields.One2many(
        'book_store.author', 'publisher_id', string="签约作者")
