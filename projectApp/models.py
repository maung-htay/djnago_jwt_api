from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Book Name")
    description = models.CharField(max_length=255)
    published = models.BooleanField()

    class Meta:
        db_table = "book"
