from django.shortcuts import render

from .models import Article

def index(request):
    """
    Renders the index page that lists all available articles.

    :param request: HttpRequest object.
    :return: HttpResponse object with the rendered template.
    """
    articles = Article.objects.all()
    return render(request, "index.html", {'articles': articles})

def add(request):
    """
    Renders the add page.

    :param request: HttpRequest object.
    :return: HttpResponse object with the rendered template.
    """
    articles = Article.objects.all()
    return render(request, "add.html")


def agb(request):
    """
    Renders the agb page.

    :param request: HttpRequest object.
    :return: HttpResponse object with the rendered template.
    """
    articles = Article.objects.all()
    return render(request, "agb.html")


def legal_notice(request):
    """
    Renders the legal notice page.

    :param request: HttpRequest object.
    :return: HttpResponse object with the rendered template.
    """
    articles = Article.objects.all()
    return render(request, "legal-notice.html")