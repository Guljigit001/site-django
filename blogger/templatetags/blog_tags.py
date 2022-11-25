from django import template

register = template.Library()

from ..models import Post




@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blogger/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}