from django.db import models

class ContactMessage(models.Model):
    telegram_id = models.BigIntegerField()
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)
    answer = models.TextField(blank=True,null=True)
    answered_at = models.DateTimeField(blank=True,null=True)
    answered_by = models.ForeignKey("accounts.User",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.full_name