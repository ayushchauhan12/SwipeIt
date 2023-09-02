from django import template
register = template.Library()

@register.simple_tag
def setvar(val=None):
  return val


@register.filter(name='sub')
def sub(a,b):
  if a>b:
    c='got '
    d=a-b
    c+=str(d)
    return c
  else:
    c='redeemed a reward from '
    d=b-a
    c+=str(d)
    return c
    
  return int(a)-int(b)
e=0
@register.filter(name='inc')
def inc(previous):
  previous=previous+1
  return previous
