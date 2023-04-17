from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.all().count()
        rep['comments'] = instance.comments
        print(rep['comments'])
        return rep