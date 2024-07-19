from rest_framework import serializers
from .models import Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
        
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.count() > 0:
            return sum(review.rating for review in reviews) / reviews.count()
        return 0