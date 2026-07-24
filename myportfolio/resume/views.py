from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import ContactMessage


# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")


def projects (request):
    projects_show=[
        {
            'title': 'Website Portfolio',
            'path': 'images/portfolio.png',
        },
        {
            'title': 'Authenticated Notes',
            'path': 'images/notes.png',
        },

        {
            'title': 'Customer Relationship Management',
            'path': 'images/dcrm.png',
        },
        {
            'title': 'Number Guessing Game',
            'path': 'images/numberguess.png',
        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})


def experience(request):
    experience=[
        {"company":"Nextvas | Los Banos, Laguna",
         "position":"Healthcare Customer Service Representative"},
        {"company":"Furukawa Automotive Systems LIMA Phils., Inc. | Lipa City, Batangas ",
         "position":"Engineer Office Personnel (On-the-Job Training)"},
        {"company":"Telay Store 888 | Masapang, Laguna",
         "position":"Store Staff & Cashier"}
    ]
    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)