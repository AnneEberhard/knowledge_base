from django import template

register = template.Library()

@register.filter
def truncate_words(value, num_words):
    words = value.split()[:num_words]
    return ' '.join(words) + '...'
