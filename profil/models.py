from django.db import models

# Create your models here.

class MyProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)

    def _str_(self):
        return self.title

class GuestBook(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    pesan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama