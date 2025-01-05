from django.db import models

# Create your models here.
class Contactus(models.Model):
    Name = models.CharField(max_length=30,default="anonymous")
    Email = models.EmailField()
    Phone = models.IntegerField(null=False)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return self.Name