from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'audience', 'release_date',
                    'genre', 'score', 'poster_url', 'description')


admin.site.register(Movie, MovieAdmin)


"""
Username : movies
Email address : qooktree@naver.com
Password : 1234
"""
