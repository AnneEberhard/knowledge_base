from django.test import TestCase
from django.urls import reverse
from .models import Article
from .forms import SearchForm


class IndexViewTest(TestCase):
    def setUp(self):
        self.article1 = Article.objects.create(title='Test Article 1', text='Test text 1', author='Author 1')
        self.article2 = Article.objects.create(title='Test Article 2', text='Test text 2', author='Author 2')

    def test_index_view_get(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIsInstance(response.context['form'], SearchForm)
        self.assertQuerySetEqual(
            response.context['articles'].order_by('id'),
            Article.objects.all().order_by('id'),
            transform=lambda x: x
        )

    def test_index_view_post(self):
        response = self.client.post(reverse('index'), {'query': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIsInstance(response.context['form'], SearchForm)
        self.assertQuerySetEqual(
            response.context['articles'].order_by('id'),
            Article.objects.filter(title__icontains='Test').order_by('id') | Article.objects.filter(text__icontains='Test').order_by('id'),
            transform=lambda x: x
        )


class AddViewTest(TestCase):
    def test_add_view_get(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add.html')

    def test_add_view_post(self):
        data = {'title': 'Test Title', 'text': 'Test Text', 'author': 'Test Author'}
        response = self.client.post(reverse('add'), data)
        self.assertEqual(response.status_code, 302)  # 302 for redirect
        article = Article.objects.get(title='Test Title')
        self.assertRedirects(response, reverse('article_detail', kwargs={'id': article.id}))


class ArticleDetailViewTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(title='Test Article', text='Test text', author='Test Author')

    def test_article_detail_view(self):
        response = self.client.get(reverse('article_detail', kwargs={'id': self.article.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_detail.html')
        self.assertEqual(response.context['article'], self.article)

    def test_article_detail_view_nonexistent(self):
        response = self.client.get(reverse('article_detail', kwargs={'id': 999}))
        self.assertEqual(response.status_code, 404)
