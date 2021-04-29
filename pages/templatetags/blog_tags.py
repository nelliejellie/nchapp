from django import template
from ..models import Corper_blog
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

#creating a simple tag

register = template.Library()

#markdown function
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))