from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Like,Comment

from post.models import Post, User
from post.serializers import CommentSerializer

from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView



@api_view(['POST'])
def toggle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    post = get_object_or_404(Post, id= id)
    if Like.objects.filter(user=user, post = post).exists():
        #если лайк есть, то удаляем
        Like.objects.filter(user=user, post = post).delete()
    else:
        #если нет, то создаем
        Like.objects.create(user=user, post=post)
    return Response(status=201)



@api_view(['POST'])
def comments(request, id):
    user_id = request.data.get('user')
    content = request.data.get('content')

    if not user_id:
        return Response({"user":'this field is required'}, status=400)

    user = get_object_or_404(User, id=user_id)
    post = get_object_or_404(Post, id=id)
    comment = Comment.objects.create(user=user, post=post, content=content)

    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=201)

class Create_CommentAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class UpdateCommentAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class DeleteCommentAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]