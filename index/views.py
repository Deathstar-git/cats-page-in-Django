from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Cat
from .forms import CatForm


def index(request):
    cats = Cat.objects.all()
    return render(request, 'index/index.html', locals())


def create(request):
    error = ''
    if request.method == 'POST':
        f = CatForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('index')
        else:
            error = 'Форма некорректна'

    form = CatForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'index/create.html', context)


def delete(request, name):
    try:
        p = Cat.objects.get(name=name)
        p.delete()
        return HttpResponseRedirect("/")
    except Cat.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
