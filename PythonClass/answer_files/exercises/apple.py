# coding: utf-8


class Product(object):

	_names = []

	def __init__(self, name, cost_to_produce):
		self.name = name

		'''
		TODO: If the name is already in the list,
		raise an exception with a message. Then in iPhone.py,
		try creating the same product twice.
		'''
		if name not in Product._names:
			Product._names.append(name)
		else:
			raise Exception("Product name already in use: {}".format(name))

		self.cost_to_produce = cost_to_produce

	@classmethod
	def names(cls):
		return cls._names

	def __str__(self):
		# __str__ is what Python will show if someone prints this object.
		return "{} (only ${}!)".format(self.name, self.price())

	def price(self):
		return self.cost_to_produce * 3
