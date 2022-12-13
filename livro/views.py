from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro

def ver_livros(request):

    search = request.GET.get('search')
    if search:
        livros = Livro.objects.filter(titulo__icontains=search)
    else:
        livros = Livro.objects.all()

    return render(request, 'ver_livros.html', {'livros': livros})    


def romance(request):
    romance = Livro.objects.filter(categoria__icontains='romance')
    return render(request, 'romance.html', {'romance': romance})


def ficcao(request):
    ficcao = Livro.objects.filter(categoria__icontains='ficção')
    return render(request, 'ficcao.html', {'ficcao': ficcao})

def terror(request):
    terror = Livro.objects.filter(categoria__icontains='terror')
    return render(request, 'terror.html', {'terror': terror})
    
    
