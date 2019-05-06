# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'book_store.book'

    name = fields.Char('名称', help='书名')
    author = fields.Many2one(
        'book_store.author', string='作者', help='作者', delegate=True)
    date = fields.Date("出版日期", help="日期")
    price = fields.Float("定价", help="定价")
    ref = fields.Reference(
        selection=[('book_store.author', '作者'), ('book_store.publisher', '出版商')])

    @api.one
    def btn_test(self):
        """测试方法"""
        _logger.info(f"测试创建出版商和作者")
        self.env['book_store.publisher'].sudo().create({
            "name": "超新星出版社",
            "signed_authors": [(0, 0, {'name': '本杰明 巴顿', 'age': 90}),(0,0, {'name': '刘天然', 'age': 28})]
        })


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
