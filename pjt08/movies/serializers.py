from rest_framework import serializers
from .models import Actor, Movie, Review

# ListSerializer 들


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)

# ----------------------------------------------------------


class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'


class ActorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


class MovieDetailSerializer(serializers.ModelSerializer):
    review_set = ReviewDetailSerializer(many=True, read_only=True)
    actors = ActorDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('id', 'movie',)


'''
은우님 조 코드
===============

from rest_framework import serializers
# from .actor import ActorNameSerializer
from .review import ReviewSerializer, ReviewListSerializer
from ..models import Movie, Actor



class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

    
class MovieSerializer(serializers.ModelSerializer):
    class ActorNameSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('name',)
    
    review_set = ReviewSerializer(many=True, read_only=True)
    actors = ActorNameSerializer(many=True, read_only=True)
    

    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('actors',)




from rest_framework import serializers
from ..models import Review, Movie


class ReviewSerializer(serializers.ModelSerializer):

    class MovieNameSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieNameSerializer(read_only=True)

    # movie = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('movie',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)
        read_only_fields = ('movie',)
'''
