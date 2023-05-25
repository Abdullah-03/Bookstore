from django.urls import path

from .views import BookListView, BookDetailView, review_form, get_user_review

urlpatterns = [
    path("", BookListView.as_view(), name='book_list'),
    path("<uuid:pk>/", BookDetailView.as_view(), name='book_detail'),
    path("ajax/review/<uuid:pk>/", review_form, name="review_form"),
    path("ajax/get_user_review/", get_user_review, name='get_user_review')
]
