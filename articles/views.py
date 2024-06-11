from django.shortcuts import get_object_or_404, redirect, render
from .models import Article
from .forms import SearchForm


def index(request):
    """
    Renders the index page that lists all available articles if method is GET.
    Filters to search field input if method is POST.

    :param request: HttpRequest object.
    :return: HttpResponse object with the rendered template.
    """
    articles = Article.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            articles = articles.filter(title__icontains=query) | articles.filter(text__icontains=query)
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form, 'articles': articles})


def add(request):
    """
    Renders the add page if the method is POST.
    Creates a new articel if the method is POST

    :param request: HttpRequest object.
    :return: HttpResponse object with the rendered template.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, text=text, author=author)
        return redirect('article_detail', id=article.id)
    return render(request, "add.html")


def agb(request):
    """
    Renders the agb page.

    :param request: HttpRequest object.
    :return: HttpResponse object with the rendered template.
    """
    return render(request, "agb.html")


def legal_notice(request):
    """
    Renders the legal notice page.

    :param request: HttpRequest object.
    :return: HttpResponse object with the rendered template.
    """
    return render(request, "legal-notice.html")


def article_detail(request, id):
    """
    Renders the article detail page.

    :param request: HttpRequest object.
    :param id: id of rendered article.
    :return: HttpResponse object with the rendered template.
    """
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})
