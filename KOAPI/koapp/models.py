from django.db import models
from django.contrib.auth.models import User


""" myappmodelinheridedfromclassmodel.model """

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.CharField(max_length = 100)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
   
 

    def __str__(self):
        return self.description
    class Meta:
        ordering = ['-upload_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,description):
        descriptioned = Image.objects.filter(id=id).update(description= description)
        return descriptioned

    @classmethod
    def get_images(cls):
        image = Image.objects.all()
        return image

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=Image.id)
        return image