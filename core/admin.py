from django.contrib import admin
from .models import Resume




@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = [
        "end_date",
        "start_date",
        "image",
        "technologies",
        "description",
        "title",
        "name",
        "description",
        "end_date",
        "start_date",
        "location",
        "company",
        "job_title",
        "courses",
        "year",
        "address",
        "institution",
        "degree",
        "professional_summary",
        "linkedin_link",
        "github_link",
        "address",
        "email",
        "contact_number",
        "last_name",
        "first_name",
        "user",
    ][::-1]
