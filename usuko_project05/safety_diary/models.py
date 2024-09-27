from django.db import models

class SafetyDiary(models.Model):
    date = models.DateField()
    site_name = models.CharField(max_length=100)
    contractor_name = models.CharField(max_length=100)
    work_description = models.TextField()
    planned_personnel = models.IntegerField()
    actual_personnel = models.IntegerField()
    safety_notes = models.TextField()
def __str__(self):
        return f"{self.date} - {self.site_name}"

