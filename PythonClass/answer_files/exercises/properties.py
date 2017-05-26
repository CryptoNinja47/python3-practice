# coding: utf-8

class Person(object):
	def __init__(self, atts):
		self.atts = atts

	def email(self):
		return self.atts['email']

	def set_email(self, email):
		if '@' not in email:
			raise Exception("{} not a valid email address!".format(email))
		self.atts['email'] = email

	email = property(email, set_email)


tim_atts = {'name': 'Tim Cook', 'email': 'tcook@apple.com'}

tim = Person(tim_atts)

tim.email = 'tcook_ac2@apple.com'
print tim.email