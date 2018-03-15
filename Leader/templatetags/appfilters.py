from django import template

register = template.Library()
@register.filter(name='getattribute')
def getattribute(obj,name):
    return getattr(obj,name)