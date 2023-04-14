from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post, Comment

# class PostSerializer(ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'

#     def to_representation(self, instance):
#         rep = super().to_representation(instance)
#         rep['likes'] = instance.likes.all().count()
#         rep['comments'] = instance.comments.all()
#         return rep
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.all().count()
        return rep
