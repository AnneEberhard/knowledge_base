from django import template

register = template.Library()

@register.filter
def truncate_words(value, num_words):
    """
    Template-Filter zum Kürzen eines Textes auf eine bestimmte Anzahl von Wörtern.

    Args:
        value (str): Der Eingabetext.
        num_words (int): Die maximale Anzahl von Wörtern, die im gekürzten Text enthalten sein sollen.

    Returns:
        str: Der gekürzte Text.

    Example:
        {{ article.text|truncate_words:100 }}
    """
    words = value.split()[:num_words]
    return ' '.join(words) + '...'
