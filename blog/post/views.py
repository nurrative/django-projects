from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    queryset = Post.objects.all()
    return render(request, 'listing.html', {"posts":queryset})



"REST"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def post_list_api_view(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_details(request, id):
    post = get_object_or_404(Post,id=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

