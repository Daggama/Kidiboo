from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=50)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    description = models.TextField(max_length=1000)

    def str(self):
        return self.title


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    def str(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Language(models.Model):

    name = models.CharField(max_length=200)

    def str(self):
        return self.name


class Genre(models.Model):

    name = models.CharField(max_length=50)

    def str(self):
        return self.name