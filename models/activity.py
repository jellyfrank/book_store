#!/usr/bin/python3
# @Time    : 2021-11-26
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class book_store_activity(models.Model):

    _name = "book_store.activity"

    @api.depends("lines.special")
    def _get_all_special(self):
        self.all_special = all(self.lines.mapped("special"))

    name = fields.Char("名称")
    lines = fields.Many2many("book_store.activity.line",
                             'activity_id', string="活动图书")
    all_special = fields.Boolean("是否全部特价",compute="_get_all_special")

    def button_test(self):
        print('-----------------')
        print(self.all_special)
        # lines = self.lines
        for line in self.lines:
            line.special = True
        
        self.lines.modified(["special"])
        print('==============')
        print(self.all_special)



class book_store_activity_line(models.Model):

    _name = "book_store.activity.line"

    activity_id = fields.Many2one("book_store.activity")
    book = fields.Many2one("book_store.book", string="图书")
    special = fields.Boolean("特价")
