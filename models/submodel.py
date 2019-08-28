
from odoo import fields, _, api, models
import logging

_logger = logging.getLogger(__name__)


class SubBook(models.Model):

    _inherit = "book_store.book"

    @api.one
    def log_book_name(self):
        """重载父类方法"""
        # res = super(SubBook,self).log_book_name()
        _logger.info(f"SubBook的方法：图书名称{self.name},作者：{self.author.name}")
        super(SubBook,self).log_book_name()

    # def __log_book_name(self):
    #     print('SubBook私有方法')
    #     _logger.info(f"图书名称{self.name},作者：{self.author.name}")

class SubBook2(models.Model):

    _inherit = "book_store.book"

    @api.one
    def log_book_name(self):
        """重载父类方法"""
        # res = super(SubBook,self).log_book_name()
        _logger.info(f"SubBook2的方法：图书名称{self.name},作者：{self.author.name}")
        super(SubBook,self).log_book_name()
