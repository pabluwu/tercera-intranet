from django import template

register = template.Library()

@register.filter
def replace_doc(value):
    result_string = str(value).replace('uploads/documentos/', '')
    return result_string