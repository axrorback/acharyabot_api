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

class Hostel(models.Model):

    title_uz = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)

    description_uz = models.TextField()
    description_en = models.TextField()
    description_ru = models.TextField()

    image = models.ImageField(upload_to="hostel_images/")

    def __str__(self):
        return "Hostel"

class AcademicCalendar(models.Model):

    academic_year = models.CharField(max_length=50)
    semester_start = models.DateField()
    semester_end = models.DateField()

    def __str__(self):
        return "Academic Calendar"

class VisaSupport(models.Model):

    title_uz = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)

    description_uz = models.TextField()
    description_en = models.TextField()
    description_ru = models.TextField()

    def __str__(self):
        return "Visa Support"

class IncubationCenter(models.Model):

    title_uz = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)

    description_uz = models.TextField()
    description_en = models.TextField()
    description_ru = models.TextField()

    image = models.ImageField(upload_to="incubation_center_images/")

    def __str__(self):
        return "Incubation Center"