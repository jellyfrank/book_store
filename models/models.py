#!/usr/bin/python3
# @Time    : 2021-11-23
# @Author  : Kevin Kong (kfx2007@163.com)

from datetime import datetime, timedelta, date
from odoo.exceptions import AccessDenied
from odoo import models, fields, api
from odoo.fields import Command
import logging

_logger = logging.getLogger(__name__)


class Book(models.Model):

    _name = 'book_store.book'
    _description = "图书"

    name = fields.Char('名称', help="书名")
    authors = fields.Many2many("book_store.author", string="作者")
    date = fields.Date("出版日期", help="出版日期")
    price = fields.Float("定价", help="定价")

    def button_create(self):
        """创建作者方法"""
        self.authors = [Command.create({
            "name": "瑶瑶"
        })]

    def button_update(self):
        """更新作者方法"""
        self.authors = [Command.update(author.id, {
            "name": f"❤{author.name}"
        }) for author in self.authors]

    def button_delete(self):
        """删除一个作者"""
        if not self.authors:
            raise AccessDenied("没有更多作者了")
        author_id = self.authors[0]
        self.authors = [Command.delete(author_id.id)]

    def button_clear(self):
        """"删除所有作者"""
        self.authors = [Command.clear()]
