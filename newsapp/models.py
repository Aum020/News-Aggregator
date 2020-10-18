from django.db import models

# Create your models here.

class Mainart(models.Model):
    title = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class Article(Mainart):
    desc = models.TextField( blank=True, null=True)


class Sports(Mainart):
    desc = models.TextField( blank=True, null=True)


class Entertainment(Mainart):
    desc = models.TextField( blank=True, null=True)


class Politics(Mainart):
    desc = models.TextField( blank=True, null=True)
