from urllib import request

from django import template


register = template.Library()

@register.filter(name="rq")
def rq(value,val2):
    if(val2):
        return  '&'+value+'='
    else:
        return  '?'+value+'='

@register.filter(name='get_list')
def get_list(querydict, key):
    return querydict.getlist(key)