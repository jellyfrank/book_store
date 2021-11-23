#!/usr/bin/python3
# @Time    : 2021-11-23
# @Author  : Kevin Kong (kfx2007@163.com)

from datetime import datetime, timedelta, date
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Book(models.Model):

    _name = 'book_store.book'
    _description = "图书"

    name = fields.Char('名称', help="书名")
    author = fields.Char("作者", help="作者")
    date = fields.Date("出版日期", help="出版日期")
    price = fields.Float("定价", help="定价")
