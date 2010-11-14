from django.db import models

class Quote(models.Model):
    '''
    Just a collection of quotes to make someone's day a
    little bit better.
    '''
    quote = models.TextField(help_text="Enter the quote")
    author = models.CharField(max_length=30, help_text="Enter the author of the quote")
    slug = models.SlugField()

    def __unicode__(self):
        return self.quote

