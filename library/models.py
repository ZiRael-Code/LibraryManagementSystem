import uuid

from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def list_genres(self):

        return


class BookInstances(models.Model):
    AVAILABLE = "A"
    UNAVAILABLE = "U"
    STATUS_CHOICES = [(AVAILABLE, 'Available'),
                      (UNAVAILABLE, 'Unavailable'), ()]

    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
