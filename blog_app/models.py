from django.db import models

# Create your models here.
class Blog (models.Model):
    date=models.DateField(auto_now=True)
    title=models.CharField (max_length=100)
    body=models.TextField()

    def __str__(self):
        return self.title