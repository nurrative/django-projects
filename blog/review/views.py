from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Like
from post.models import Post, User, Comment
from post.serializers import CommentSerializer


@api_view(['POST'])
def toggle_like(request, id):
    user_id = request.data.get('user')
    if not user_id:
        return Response({"user":'this field is required'}, status=400)
    
    user = get_object_or_404(User,id=user_id)
    post = get_object_or_404(Post, id= id)
    if Like.objects.filter(user=user, post = post).exists():
        #если лайк есть, то удаляем
        Like.objects.filter(user=user, post = post).delete()
    else:
        #если нет, то создаем
        Like.objects.create(user=user, post=post)
    return Response(status=201)

# @api_view(['POST'])
# def comments(request, id):
#     user_id = request.data.get('user')
#     if not user_id:
#         return Response({"user":'this field is required'}, status=400)
    
#     user = get_object_or_404(User,id=user_id)
#     post = get_object_or_404(Post, id= id)

#     if Comments.objects.filter(user=user, post=post).exists():
#         Comments.objects.create(user=user, post=post)
#     else :
#         Comments.objects.create(user=user, post=post)
#     return Response(status=201)

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