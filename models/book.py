#!/usr/bin/python3
# @Time    : 2021-12-17
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class SerialBookName(models.Model):

    _name ="book_store.serial"

    name = fields.Char("丛书名称")