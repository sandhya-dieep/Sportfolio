from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import About, Education, Skill, Project, ContactMessage

admin.site.register(About)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactMessage)

