from django.db import models

class AdmissionProcess(models.Model):

    PROCESS_TYPES = (
        ("direct", "Direct Admission"),
        ("auet", "AUET"),
        ("dtm", "DTM"),
    )

    process_type = models.CharField(max_length=50,choices=PROCESS_TYPES)
    title_uz = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)

    content_uz = models.TextField()
    content_en = models.TextField()
    content_ru = models.TextField()

    def __str__(self):
        return self.title_uz


class TuitionFee(models.Model):

    faculty = models.ForeignKey("faculties.Faculty",on_delete=models.CASCADE)
    national_fee = models.DecimalField(max_digits=12,decimal_places=2)
    international_fee = models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return self.faculty.title_uz


class Scholarship(models.Model):

    title_uz = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)

    percentage = models.PositiveIntegerField()

    content_uz = models.TextField()
    content_en = models.TextField()
    content_ru = models.TextField()