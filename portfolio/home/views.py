# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import About, Education, Skill, Project, ContactMessage



def index(request):
    about = About.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect("index")

    return render(request, "index.html", {
        "about": about,
        "education": education,
        "skills": skills,
        "projects": projects
    })






