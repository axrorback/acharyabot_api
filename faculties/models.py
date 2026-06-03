from django.db import models

class Faculty(models.Model):

    slug = models.SlugField(unique=True)

    image = models.ImageField(upload_to='faculties')

    title_uz = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)

    description_uz = models.TextField()
    description_en = models.TextField()
    description_ru = models.TextField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)