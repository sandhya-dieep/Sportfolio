from django.db import models

# Create your models here.
# from django.db import models

# About Section
class About(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_image = models.ImageField(upload_to="about/")
    cv_file = models.FileField(upload_to="cv/", null=True, blank=True)

    def __str__(self):
        return self.name


# Education
class Education(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    image = models.ImageField(upload_to="education/")

    def __str__(self):
        return f"{self.title} - {self.institution}"


# Skills
class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


# Projects
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# Contact Messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
