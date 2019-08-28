import odoorpc

host = "192.168.88.128"
port = 8069
db = "demo"
user = "admin"
password = "admin"

odoo = odoorpc.ODOO(host=host, port=port)
odoo.login(db, user, password)

# 调用log_book_name方法

book_obj = odoo.env['book_store.book']
book = book_obj.browse(1)

book.log_book_name()
