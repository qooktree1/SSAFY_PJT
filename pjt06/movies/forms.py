from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    GENRE_A = 'COMEDY'
    GENRE_B = 'HORROR'
    GENRE_C = 'ROMANCE'
    GENRE_CHOICES = [
        (GENRE_A, '코미디'),
        (GENRE_B, '공포'),
        (GENRE_C, '로맨스'),
    ]

    audience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 0,
            }),
    )

    genre = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        choices=GENRE_CHOICES)

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 0,
                'max': 5,
                'step': 0.5,
            }),
    )

    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }),
    )

    class Meta:
        model = Movie
        fields = '__all__'
