from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from django.conf import settings

# Create your models here.
class Item(models.Model):
    itemName = models.CharField(max_length = 20)
    qty = models.IntegerField(default = 0)
    favorite = models.BooleanField(default = False)
    price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = 'post_images', default = 'default.jpg')
    tags = models.CharField(max_length=100, blank = True, null = True)

    def get_tags(self):
        return self.tags.split(',')
    
    def set_tags(self, tags_list):
        tags_list = property(get_tags, set_tags)

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 500 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        elif img.height < 200 :
            output_size = (300, 300)
            img.thumbnail (output_size)
            img.save(self.image.path)
        # width = img.width
        # height = width
        # SInce width is the same
        output_size = (500,500)
        # print('width is ', width)
        # print('Original height is ', img.height)
        img.thumbnail (output_size)
        img.save(self.image.path)

        super().save()
        img = Image.open(self.image.path)
        width, height = img.size
        
        # Define the output size to be 500x500
        output_size = (500, 500)
        max_height = 500
        max_width = 500
    
    # Calculate the new dimensions while maintaining the aspect ratio
        if height > max_height or width > max_width:
            ratio = max_height / height
            output_size = (int(width * ratio), max_height)
            img.thumbnail(output_size)
        # Resize the image while maintaining the aspect ratio
        if height > max_height or width > max_width:
            if width > height:
                ratio = max_width / width
                output_size = (max_width, int(height * ratio))
            else:
                ratio = max_height / height
                output_size = (int(width * ratio), max_height)
            img.thumbnail(output_size)
        img.thumbnail(output_size)

        # Create a new image with a white background and paste the thumbnail onto it
        # new_img = Image.new('RGB', output_size, (229, 231, 235))
        new_img = Image.new('RGB', output_size, (255, 255, 255))
        new_img.paste(img, ((output_size[0] - img.size[0]) // 2, (output_size[1] - img.size[1]) // 2))

        # Save the new image to disk
        new_img.save(self.image.path)

    def __str__ (self):
        return self.itemName