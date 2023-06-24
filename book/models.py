from datetime import datetime

from django.db import models


# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)


class CatalogCategory(models.Model):
    catalog = models.ForeignKey('Catalog',
                                related_name='categories', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    def __unicode__(self):
        if self.parent:
            return u'%s: %s - %s' % (self.catalog.name,
                                     self.parent.name,
                                     self.name)


class Books(models.Model):
    category = models.ForeignKey('CatalogCategory',
                                 related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    description = models.TextField()

    slug = models.SlugField(max_length=150)

    photo = models.ImageField(upload_to='book_photo',
                              blank=True)
    manufacturer = models.CharField(max_length=300,
                                    blank=True)
    price_in_dollars = models.DecimalField(max_digits=6,
                                           decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class BookDetail(models.Model):
    '''
    The ``ProductDetail`` model represents information unique to a
    specific product. This is a generic design that can be used
    to extend the information contained in the ``Product`` model with
    specific, extra details.
    '''
    product = models.ForeignKey('Books',
                                related_name='details', on_delete=models.CASCADE)
    attribute = models.ForeignKey('BookAttribute', on_delete=models.CASCADE)

    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s: %s - %s' % (self.product,
                                 self.attribute,
                                 self.value)


class BookAttribute(models.Model):
    '''
    The ``BookAttribute`` model represents a class of feature found
    across a set of products. It does not store any data values
    related to the attribute, but only describes what kind of a
    product feature we are trying to capture. Possible attributes
    include things such as materials, colors, sizes, and many, many
    more.
    '''
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name

