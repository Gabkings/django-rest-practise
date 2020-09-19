from django.db import models

# Create your models here.


class JobsModel(models.Model):
    '''Job board model'''
    company_name = models.CharField(max_length=200)
    company_email = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    salary = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    createdAt = models.DateField(auto_now_add=True)
    available = models.BooleanField(max_length=200)

    def __str__(self):
        return f"{self.company_name} --> {self.job_title}"

