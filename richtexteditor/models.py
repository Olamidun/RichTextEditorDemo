from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=1000)
    number_of_times_viewed = models.PositiveIntegerField(default=0)
    content = RichTextUploadingField()
    date_published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
