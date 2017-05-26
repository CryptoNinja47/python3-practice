# coding: utf-8

from apple import Product

class iPhone(Product):
	def __init__(self):
		# To call a superclass method, use the super() function and provide your class name and a pointer to yourself.
		parent = super(iPhone, self)
		parent.__init__('iPhone', 200)

	def price(self):
		base_price = super(iPhone, self).price()
		return base_price * 2


phone = iPhone()
print phone