from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


class Meta(Books):
    indexes = [
        models.Index(fields=['price']),
    ]
