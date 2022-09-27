from django.db import models

# Create your models here.
class AccessLog(models.Model):
    class Meta:
        db_table = "acess_log"

    location = models.CharField("접속 경로", max_length=50, null=False)
    created_at = models.DateTimeField("접속시간", auto_now_add=True)
    
def __str__(self):
    return f"(self.created.at) / (self.location)"