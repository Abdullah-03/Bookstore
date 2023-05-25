from django.contrib.auth import get_user_model
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, Review
from .forms import ReviewForm


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        book = Book.objects.get(id=self.kwargs['pk'])
        review = book.reviews.filter(author=self.request.user)
        if review:
            context["user_review"] = review
        else:
            context["user_review"] = None
        return context


def review_form(request, pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            book = Book.objects.get(id=pk)
            review = Review(review=form.cleaned_data['review'], author=request.user, book=book)
            review.save()
            book.reviews.add(review)
            res = render(request, 'htmx/review_form_success.html')
            res.headers["HX-Trigger"] = "new_review"
            return res
    else:
        form = ReviewForm()

    return render(request, 'htmx/review_form.html', {'form': form})


def get_user_review(request):
    user = request.user
    review = user.reviews.last()
    return render(request, "htmx/user_review.html", {'review': review})
