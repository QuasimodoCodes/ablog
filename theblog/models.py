from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    snippet = models.CharField(max_length=255, default='Click link above to see full post')
    header_video = models.FileField(null=True, blank=True, upload_to="videos/")

    def __str__(self):
        return f'{self.title} | {self.author}'

    def get_absolute_url(self):
        return reverse('home')

    def header_image_tag(self):
        if self.header_image:
            return mark_safe('<img src="%s" width="50" height="50" />' % self.header_image.url)
        else:
            return 'No Image Found'
    header_image_tag.short_description = 'Image'
