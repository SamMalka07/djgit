from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .forms import ReviewsForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

class ReviewsView(FormView):
    form_class = ReviewsForm
    template_name = "reviews/reviews.html"

# class ReviewsView(View):
#     def get(self, request):
#         form = ReviewsForm()
#         return render(request, "reviews/reviews.html", {"form": form})
#
#     def post(self, request):
#         form = ReviewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             print(form.cleaned_data)
#             return HttpResponseRedirect("/thankyou")
#
#         return render(request, "reviews/reviews.html", {"form": form})

# def review(request):
#     # if request.method == 'POST':
#     #     entered_username = request.POST['username']
#     #     if entered_username == '' and len(entered_username) >= 20:
#     #         return render(request, "reviews/reviews.html", {"has_error": True})
#     #     return HttpResponseRedirect('/thankyou')
#
#     if request.method == "POST":
#         form = ReviewsForm(request.POST)
#         if form.is_valid():
#             # review = Review(user_name=form.cleaned_data['user_name'],review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save()
#
#             print(form.cleaned_data)
#             return HttpResponseRedirect("/thankyou")
#     else:
#         form = ReviewsForm()
#     return render(request, "reviews/reviews.html", {"form": form})

    # return render(request, "reviews/reviews.html", {"has_error": False})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Thank you for your feedback.'
        return context

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context['reviews'] = reviews
    #     return context

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request

        favorite_id = request.session['favorite_review']
        context['is_favourite'] = favorite_id == str(loaded_review.id)
        return context
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     selected_review = Review.objects.get(pk=review_id)
    #     print(selected_review)
    #     context['review'] = selected_review
    #     return context

# class SingleReviewView(DetailView):
#     template_name = "reviews/single_review.html"
#     model = Review

class AddFavorite(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/'+review_id)

# def thankyou(request):
#     return render(request, "reviews/thank_you.html")
