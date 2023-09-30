from django.shortcuts import render,redirect,HttpResponse
from app.models import *



def index(request):

    return render(request, 'index.html')


def blog(request):

    portfolio = Portfolio.objects.all()

    print(portfolio)

    context = {
        'portfolios' : portfolio
    }
    


    return render (request, 'blog.html',context)


def about(request):

    return render(request, 'about.html')


def resume(request):

    return render(request, 'resume.html')


def contact(request):

    return render(request, 'contact.html')


def project(request):

    return render(request, 'projects.html')