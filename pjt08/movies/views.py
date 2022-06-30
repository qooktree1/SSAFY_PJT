from django.shortcuts import get_list_or_404, get_object_or_404, render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from movies.serializers import ActorListSerializer, ActorSerializer, MovieDetailSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer
from .models import Actor, Movie, Review


# List
@api_view(['GET'])
def actor_list(request):
    actor = get_list_or_404(Actor)
    serializer = ActorListSerializer(actor, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movie = get_list_or_404(Movie)
    serializer = MovieListSerializer(movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    review = get_list_or_404(Review)
    serializer = ReviewListSerializer(review, many=True)
    return Response(serializer.data)


# Detail


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'데이터 {review_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# Create

@api_view(['POST'])
def create_review(request, movie_pk):
    review = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
