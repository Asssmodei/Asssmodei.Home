from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    print(request)
    news = News.objects.all()
    context = {'news': news, 'title': 'Cписок новостей'}
    return render(request, 'news/index.html', context)
# Create your views here.
