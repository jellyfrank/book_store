#!/usr/bin/python3
# @Time    : 2021-11-23
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class book_store_author(models.Model):

    _name = "book_store.author"
    _description = "图书作者"

    name = fields.Char("姓名")
