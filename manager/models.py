from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_contact = models.EmailField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.FileField(blank=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manager:detail', kwargs={'pk': self.pk})
