from django.db import models

from tinymce import models as tinymce_models
# Create your models here.



class TestModel(models.Model):
    my_field = tinymce_models.HTMLField()
