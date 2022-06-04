from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Author, Kind, Genre, Book


class BookListView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'page/listBook.html'

    def get_queryset(self):
        if 'genre_name' in self.kwargs:
            return Book.objects.filter(genres__name=self.kwargs['genre_name']).all()
        elif 'kind_name' in self.kwargs:
            return Book.objects.filter(kinds__name=self.kwargs['kind_name']).all()
        elif 'author_name' in self.kwargs:
            return Book.objects.filter(author__name=self.kwargs['author_name']).all()
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_books'] = len(self.get_queryset())
        if 'genre_name' in self.kwargs:
            context['view_title'] = f"Žánr: {self.kwargs['genre_name']}"
            context['view_head'] = f"Žánr knih: {self.kwargs['genre_name']}"
        elif 'kind_name' in self.kwargs:
            context['view_title'] = f"Druh: {self.kwargs['kind_name']}"
            context['view_head'] = f"Druh knih: {self.kwargs['kind_name']}"
        elif 'author_name' in self.kwargs:
            context['view_title'] = f"Autor: {self.kwargs['author_name']}"
            context['view_head'] = f"Knihy: {self.kwargs['author_name']}"
        else:
            context['view_title'] = 'Knihy'
            context['view_head'] = 'Přehled knih'
        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'books_detail'
    template_name = 'page/detailBook.html'


class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors_list'
    template_name = 'page/listAuthor.html'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'authors_detail'
    template_name = 'page/detailAuthor.html'


def index(request):
    num_books = Book.objects.all().count()
    books = Book.objects.order_by('publication_year')
    authors = Author.objects.all()
    genres = Genre.objects.all()
    kinds = Kind.objects.all()

    PoslatVen = {
        'num_books':num_books,
        'books':books,
        'authors':authors,
        'genres':genres,
        'kinds':kinds
    }

    return render(request, 'index.html', context=PoslatVen)