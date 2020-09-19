from django.db import models

# Create your models here.
class MyUser(models.Model):
    """ Default user model """
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='testing@testing.com')
    photo = models.ImageField(upload_to='user_img')

    def __str__(self):
        return f"{self.name}"