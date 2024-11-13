from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This function will cut oyt all values of "arg" from the string
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
