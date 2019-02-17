from django.db import models

from tinymce import models as tinymce_models
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=60)
    content = tinymce_models.HTMLField()

    def __str__(self):
        return self.title

class Image(models.Model):
    description = models.CharField(max_length=60, blank=True)
    file_name = models.ImageField(upload_to='blogpics', blank=True)
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
