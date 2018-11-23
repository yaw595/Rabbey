from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    product = models.BooleanField(default=False)
    souvenir = models.BooleanField(default=False)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cart:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    souvenir = models.BooleanField(default=False)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cart:product_detail', args=[self.id, self.slug])


class Review(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    product = models.ForeignKey(Product, related_name='review', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at', )

    def __unicode__(self):
        return self.text
