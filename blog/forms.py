from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['full_name', 'email', 'text']
        labels = {
            'full_name': 'ФИО',
            'email': 'Email',
            'text': 'Текст отзыва',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
