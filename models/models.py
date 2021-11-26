#!/usr/bin/python3
# @Time    : 2021-11-23
# @Author  : Kevin Kong (kfx2007@163.com)

from datetime import datetime, timedelta, date
from odoo.exceptions import AccessDenied, ValidationError
from odoo import models, fields, api
from odoo.fields import Command
import logging

_logger = logging.getLogger(__name__)


class Book(models.Model):

    _name = 'book_store.book'
    _description = "图书"

    def _get_constrains_fields(self):
        return ['name', 'date']

    @api.constrains(_get_constrains_fields)
    def _check_name(self):
        """检查名称长度"""
        if len(self.name) > 10:
            raise ValidationError("图书名称必须限制在10个字符以内")
        if self.date < date(2000,1,1):
            raise ValidationError("只能添加2000年以后的图书")

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
