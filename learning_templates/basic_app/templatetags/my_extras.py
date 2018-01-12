from django import template

register = template.Library()

@register.filter(name='mein')
def mein(value, arg):
	"""
	Cuts out all values of arg from string
	"""
	return value.replace(arg, '')