from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book_outlet/index.html', {
        'books': books,
        "total_number_of_books": books.count(),
        "average_rating": books.aggregate(Avg('rating'))['rating__avg'],
    })


def book_detail(request, slug):

    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'book': book
    })
