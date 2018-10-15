from django import template

register = template.Library()
@register.filter(name='cut')

def cut(value,arg):

    return value.replace(arg,'F')

# register.filter('cut',cut)
