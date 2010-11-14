from django import template
from extra.models import Quote

register = template.Library()

@register.simple_tag
def random_quote():
    '''
    This simply returns a random quote from
    the database of quotes.

    :returns: A new random quote
    '''
    quote = Quote.objects.order_by('?')[0]
    return '''
        <blockquote>%s</blockquote>
        <cite>%s</cite>
    ''' % (quote.quote, quote.author)
