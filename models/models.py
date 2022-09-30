#!/usr/bin/python3
# @Time    : 2021-11-23
# @Author  : Kevin Kong (kfx2007@163.com)

from datetime import datetime, timedelta, date
from odoo.exceptions import AccessDenied, ValidationError
from odoo import models, fields, api
from odoo.fields import Command
import logging
from dateutil.relativedelta import relativedelta

_logger = logging.getLogger(__name__)


class Book(models.Model):

    _name = 'book_store.book'
    _description = "图书"

    @api.constrains("name")
    def _check_name(self):
        """检查名称长度"""
        if len(self.name) > 10:
            raise ValidationError("图书名称必须限制在10个字符以内")

    @api.depends("date")
    def _is_new(self):
        """出版日期小于3月"""
        now = datetime.now()
        if self.date + relativedelta(months=3) < now():
            self.is_new = False
        else:
            self.is_new = True

    name = fields.Char('名称', help="书名")
    serial = fields.Many2one("book_store.serial", string="丛书")
    serial_name = fields.Char("丛书名称", related="serial.name")
    authors = fields.Many2many("book_store.author", string="作者")
    date = fields.Date("出版日期", help="出版日期")
    price = fields.Float("定价", help="定价")
    is_new = fields.Boolean("是否新书", compute="_is_new")

    def button_create(self):
        """创建作者方法"""
        self.authors = [Command.create({
            "name": "云天河"
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
