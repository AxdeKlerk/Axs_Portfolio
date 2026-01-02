import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.staticfiles import finders
from django.conf import settings
from .models import About, Blog, Project, CV
from django.http import FileResponse, Http404
import mimetypes
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    return render(request, 'portfolio/home.html', {'page': 'home'})


def about(request):
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {'page': 'about', 'about': about})


def projects(request):
    project_list = Project.objects.all().order_by('-submission_date')
    paginator = Paginator(project_list, 3)

    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    return render(request, 'portfolio/projects.html', {'page': 'project', 'projects' : projects})


def blog_list(request):
    posts = Blog.objects.all().order_by('-published_date')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    
    return render(request, 'portfolio/blog.html', {'page': 'blog', 'blogs': blogs })


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'page': 'blog', 'blog': blog})


def cv(request):
    cv = CV.objects.first()
    return render(request, 'portfolio/cv.html', {'page': 'cv', 'cv': cv})


def download_cv_pdf(request):
    file_path = finders.find("cv/Ax_de_Klerk_-_CV.pdf")
    if not file_path:
        raise Http404("CV not found.")
    return FileResponse(open(file_path, "rb"), filename="Ax_de_Klerk_-_CV.pdf")


def download_cv_doc(request):
    file_path = finders.find("cv/Ax_de_Klerk_-_CV.docx")
    if not file_path:
        raise Http404("CV not found.")
    return FileResponse(open(file_path, "rb"), filename="Ax_de_Klerk_-_CV.docx")


def contact(request):
    if request.method == "POST":
        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        full_message = f"""
        New message from your portfolio contact form:

        Name: {first} {last}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
                """

        send_mail(
            subject="New Portfolio Contact Form Submission",
            message=full_message,
            from_email="axdeklerk@gmail.com",   # your email
            recipient_list=["axdeklerk@gmail.com"],  # where it should arrive
        )

        # For now: just show a success message  
        messages.success(request, "Thank you — your message has been sent! I will reply as soon as humanly possible.")

        return redirect("portfolio:contact")

    return render(request, "portfolio/contact.html", {"page": "contact"})


def cicd(request):
    return render(request, "portfolio/cicd.html")
