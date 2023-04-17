"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import post_list,post_list_api_view,post_details,create_post,delete_post,update_post,update_with_patch
from review.views import toggle_like,comments
from account.serializers import UserListView
from account.views import RegisterUserAPIView
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('listing/',post_list),
    path('api/listing/',post_list_api_view),
    path('api/details/<int:id>/',post_details),
    path('api/create/',create_post),
    path('api/delete/<int:id>/',delete_post),
    path('api/update/<int:id>/',update_post),
    path('api/updatepatch/<int:id>/',update_with_patch),
    path('api/like/<int:id>/',toggle_like),
    path('api/comments/<int:id>/',comments),
    path('api/register/', RegisterUserAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/users/',UserListView.as_view()),

]
