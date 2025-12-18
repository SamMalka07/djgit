from django import forms
from .models import Review

# class ReviewsForm(forms.Form):
#     user_name = forms.CharField(label="Username", max_length=20, error_messages={"required": "Please enter your username"})
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {'review_text':'Review Text','rating':'Your Rating'}