from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import ArticlesForm


def articles_home(request):
    newsArt = Articles.objects.order_by('-date')
    return render(request, 'articles/articles_HP.html', {'newArt': newsArt})


class fullArticlePageGen(DetailView):
    model = Articles
    template_name = 'articles/fullArticlePageGen.html'
    context_object_name = 'articleKey'


def create(request):
    errorText = ''

    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles_home')
        else:
            print(form.errors)
            errorText = "Fill forms properly"

    form = ArticlesForm()
    data = {
        'form': form,
        'errorText': errorText,
    }
    return render(request, 'articles/createPage.html', data)


class fullArticlePageEdit(UpdateView):
    model = Articles
    template_name = 'articles/createPage.html'
    form_class = ArticlesForm

class fullArticlePageDelete(DeleteView):
    model = Articles
    template_name = 'articles/deletePage.html'
    success_url = '/article/'