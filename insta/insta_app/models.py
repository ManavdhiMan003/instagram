from django.db import models

# Create your models here.

class posts(models.Model):
    name = models.CharField(max_length=122,null=True)
    desc = models.TextField()
    new_img = models.ImageField(upload_to='images/') 

    def __str__(self):
        return self.name
    