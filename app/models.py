from django.db import models

# Create your models here.



class City(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='city_images')
    about = models.TextField(max_length=1000)
    rating = models.CharField(max_length=2)
    comments=models.CharField(max_length=1000) 
    def __str(self):
        return self.name

    # def __str__(self):
    #     return f"{self.name} - {self.city}"
    # # save the new comment object
