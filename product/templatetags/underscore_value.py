from django import template

register = template.Library()

@register.filter(name="dict_")
def dict_(d, name):
    try:
        value = d.get(name, None)
    except KeyError:
        value = 'N/A'
    return value