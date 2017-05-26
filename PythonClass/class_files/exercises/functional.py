class gps(object):
	@classmethod
	def current_location(cls):
		return 'yup'
def get_weather_data(time, location):
	return

# coding: utf-8

'''
Functional programming

Functional programming means creating code with no "side effects".
That means that a function should be predictable and not do anything
the caller doesn't have control over.

As it happens, making a function "functional" also makes it testable.
'''


# A pure function is one that has no side effects.
# This is pure because the result is always predictable given the same input.
def add_one(number):
	return number + 1


'''
# This is not a pure function -- the caller has no control over the time or location.
# The result will change based on the time and location that this is called.
def weather_report():
	time = datetime.now()
	location = gps.current_location()

	report = 'Weather report for ' + str(location) + ': ' + str(time)
	report += get_weather_data(time, location)
	return report

# A better version of this function would parameterize the time and location:
def weather_report(time = datetime.now(), location = gps.current_location()):
	report = 'Weather report for ' + str(location) + ': ' + str(time)
	report += get_weather_data(time, location)
	return report
'''











