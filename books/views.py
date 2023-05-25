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
        return context


def review_form(request, pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            book = Book.objects.get(id=pk)
            review = Review(review=form.cleaned_data['review'], author=request.user, book=book)
            review.save()
            book.reviews.add(review)
            return render(request, 'htmx/review_form_success.html')
    else:
        form = ReviewForm()

    return render(request, 'htmx/review_form.html', {'form': form})


def get_user_review(request):
    pass