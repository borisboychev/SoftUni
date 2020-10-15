from django.shortcuts import render, redirect

# Create your views here.
from books.forms import BookForm
from books.models import Book


def create(request):
    return persist(request, Book(), 'create')


def edit(request, pk):
    return persist(request, Book.objects.get(pk=pk), 'edit')


def persist(request, book, template_name):
    if request.method == 'GET':
        context = {
            'form': BookForm(instance=book)
        }

        return render(request, f'books/{template_name}.html', context)
    else:
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('books index')
        else:
            context = {
                'form': form
            }
            return render(request, f'books/{template_name}.html', context)


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/index.html', context)
