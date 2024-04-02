from django import template
from tb.models import Table

register = template.Library()

@register.simple_tag
def get_tables():
    return Table.objects.all()
