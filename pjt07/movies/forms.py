from .models import Movie, Comment
from django import forms


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('user', 'movie',)


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        exclude = ('user',)