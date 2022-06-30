from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)
    

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST) # form 에 받은 정보를 저장
        if form.is_valid():  # 유효성 검사
            movie = form.save(commit=False)  # 받은 정보를 DB에 저장 -> movie 인스턴스
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context ={
        'movie': movie,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'movies/detail.html', context)

# @require_safe
# def detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     comment_form = CommentForm()
#     # 조회한 article의 모든 댓글 조회(역참조)
#     comments = article.comment_set.all() 
#     context = {
#         'article': article,
#         'comment_form': comment_form,
#         'comments': comments,
#     }
#     return render(request, 'articles/detail.html', context)



def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')

    return render(request, 'movies/detail.html', movie.pk)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)

    else:
        form = MovieForm(instance=movie)
    context = {
        'form' : form,
        'movie' : movie,
    }

    return render(request, 'movies/update.html', context)


def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.movie = movie
                comment.user = request.user
                comment.save()
        return redirect('movies:detail', movie.pk)


    return redirect('accounts:login')


def comments_delete(request, pk, comment_pk):
    movie = Movie.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = Comment.objects.get(pk=comment_pk)
            if comment.user == request.user:
                comment.delete()
        return redirect('movies:detail', movie.pk)

# @require_POST
# def comment_create(request, pk):
#     if request.user.is_authenticated:
#         # article = Article.objects.get(pk=pk)
#         article = get_object_or_404(Article, pk=pk)
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.article = article
#             comment.user = request.user
#             comment.save()
#         return redirect('articles:detail', article.pk)
#     return redirect('accounts:login')