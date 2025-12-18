from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewsView.as_view(), name='reviews'),
    path("thankyou", views.ThankYouView.as_view(), name='thankyou'),
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/favorite", views.AddFavorite.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view()),
]