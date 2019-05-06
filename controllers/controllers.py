# -*- coding: utf-8 -*-
from odoo import http

# class BookStore(http.Controller):
#     @http.route('/book_store/book_store/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/book_store/book_store/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('book_store.listing', {
#             'root': '/book_store/book_store',
#             'objects': http.request.env['book_store.book_store'].search([]),
#         })

#     @http.route('/book_store/book_store/objects/<model("book_store.book_store"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('book_store.object', {
#             'object': obj
#         })