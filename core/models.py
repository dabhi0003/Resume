from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    professional_summary = models.CharField(max_length=350,blank=True,null=True)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    int_address = models.CharField(max_length=100,blank=True,null=True)
    year = models.CharField(max_length=10)
    courses = models.TextField()
    job_title = models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=200,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    description = models.CharField(max_length=150,null=True,blank=True)
    name = models.CharField(max_length=150,blank=True,null=True)
    title = models.CharField(max_length=100,blank=True)
    project_description = models.CharField(max_length=150,blank=True,null=True)
    technologies = models.CharField(max_length=200,blank=True,null=True)
    image=models.ImageField(upload_to='profile/',null=True,blank=True)
    

    def __str__(self) -> str:
        return self.first_name
    