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