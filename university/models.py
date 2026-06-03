from django.db import models

class ContactInfo(models.Model):

    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address_uz = models.TextField()
    address_en = models.TextField()
    address_ru = models.TextField()
    google_map_url = models.URLField()
    yandex_map_url = models.URLField()
    working_hours = models.CharField(max_length=255)

    def __str__(self):
        return "Contact Info"