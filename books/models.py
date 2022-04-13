from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


def poster_book_path(instance, filename):
    return "books/" + str(instance.id) + "/book_poster/" + filename


def poster_author_path(instance, filename):
    return "authors/" + str(instance.id) + "/author_poster/" + filename


class Author(models.Model):
    name = models.CharField(max_length=250, unique=True)
    photo = models.ImageField(upload_to=poster_author_path,blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Kind(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name="Title")
    rate = models.FloatField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True, null=True, help_text="Enter between 1 - 100")
    photo = models.ImageField(upload_to=poster_book_path, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    kinds = models.ManyToManyField(Kind)
    genres = models.ManyToManyField(Genre, help_text="Select genre")
    publication_year = models.DateField(help_text="Ve formátu DD.MM.YYYY")
    pages = models.IntegerField()
    author = models.ManyToManyField(Author)

    class Meta:
        ordering = ["-publication_year","-pages", "name"]

    def __str__(self):
        return f"{self.name}, year: {str(self.publication_year.year)},pages: {str(self.pages)}"

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


