from django.db import models


# Create your models here.

class Mainart(models.Model):
    title = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    desc = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class Article(Mainart):
    pass


class Sports(Mainart):
    pass


class Entertainment(Mainart):
    pass


class Politics(Mainart):
    pass
