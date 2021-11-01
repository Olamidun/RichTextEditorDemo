from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm

# Create your views here.

def home(request):
    articles = Article.objects.all()

    return render(request, 'richtexteditor/home.html', {'articles': articles})

def create_post(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('richtexteditor:home')
    else:
        form = ArticleForm()
    return render(request, 'richtexteditor/create_article.html', {'form':form})
