from django.shortcuts import render, redirect
from .models import Book
from django.views.generic import View
from .forms import BookForm, UpdateBookForm


def all_books(request):
    list_of_books = Book.get_all()
    return render(request, "book\\all_books.html", {"list_of_books": list_of_books})


def delete(request, id):
    Book.delete_by_id(id)
    return redirect('book:all_books')


class CreateBook(View):

    def get(self, request):
        form = BookForm()
        return render(request, 'book\\create_book_form.html', {'form': form})

    def post(self, request):
        bound_form = BookForm(request.POST)
        if bound_form.is_valid():
            new_book = bound_form.save()
            return redirect('book:all_books')
        return render(request, 'book\\create_book_form.html', {'form': bound_form})


class UpdateBook(View):
    def get(self, request, id):
        book = Book.get_by_id(id)
        form = UpdateBookForm(instance=book)
        return render(request, 'book\\update_book_form.html', {'form': form, "book": book})

    def post(self, request, id):
        book = Book.get_by_id(id)
        bound_form = UpdateBookForm(request.POST, instance=book)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('book:all_books')
        print('-' * 90)
        return render(request, 'book\\update_book_form.html', {'form': bound_form})