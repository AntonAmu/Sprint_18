from django.shortcuts import render, redirect
from .models import Author
from django.views.generic import View
from .forms import AuthorForm, UpdateAuthorForm


def all_authors(request):
    list_of_authors = Author.get_all()
    return render(request, "author\\all_authors.html", {"list_of_authors": list_of_authors})


def delete(request, id):
    Author.delete_by_id(id)
    return redirect('author:all_authors')


class CreateAuthor(View):

    def get(self, request):
        form = AuthorForm()
        return render(request, 'author\\create_author_form.html', {'form': form})

    def post(self, request):
        bound_form = AuthorForm(request.POST)
        if bound_form.is_valid():
            new_user = bound_form.save()
            return redirect('author:all_authors')
        return render(request, 'author\\create_author_form.html', {'form': bound_form})


class UpdateAuthor(View):
    def get(self, request, id):
        author = Author.get_by_id(id)
        form = UpdateAuthorForm(instance=author)
        return render(request, 'author\\update_author_form.html', {'form': form, "author": author})

    def post(self, request, id):
        author = Author.get_by_id(id)
        bound_form = UpdateAuthorForm(request.POST, instance=author)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('author:all_authors')
        print('-' * 90)
        return render(request, 'author\\update_author_form.html', {'form': bound_form})
