# products/forms.py
from django import forms
from .models import ProductReview

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search Products')

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['user_name', 'comment', 'rating']