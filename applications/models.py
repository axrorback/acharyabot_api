from django.db import models

class Application(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("review", "Under Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )

    telegram_id = models.BigIntegerField(blank=True,null=True)
    application_number = models.CharField(unique=True,max_length=50)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    faculty = models.ForeignKey("faculties.Faculty",on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.application_number

class ApplicationDocument(models.Model):
    application = models.ForeignKey(Application,on_delete=models.CASCADE)
    file = models.FileField(upload_to="applications/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.application.application_number