from django import template
from ..models import Corper_blog
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

#creating a simple tag

register = template.Library()

#simple tags returns a string
@register.simple_tag
def total_posts():
    return Corper_blog.published.count()


#simple tags that returns the most commented post
@register.simple_tag
def get_most_commented_posts(count=5):
    return Corper_blog.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

#markdown function
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))