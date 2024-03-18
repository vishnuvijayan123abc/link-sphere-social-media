"""
URL configuration for linksphere project.

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
from socialapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignUpView.as_view(),name='sign-up'),
    path('',views.SignInView.as_view(),name='sign-in'),
    path('index/',views.IndexView.as_view(),name='index'),
    path('logout/',views.SignOutView.as_view(),name='sign-out'),
    path('profiles/<int:pk>/change',views.ProfileUpdateView.as_view(),name='profile-update'),
    path('profiles/<int:pk>',views.ProfileDetailView.as_view(),name='profile-detail'),
    path('profiles/all',views.ProfileListView.as_view(),name='profile-list'),
    path('profiles/<int:pk>/follow',views.FollowView.as_view(),name='follow'),
    path('post/<int:pk>/like/',views.PostLikeView.as_view(),name="like"),
    path('post/<int:pk>/comments/add/',views.ComentView.as_view(),name="comment"),
    path('profile/<int:pk>/block',views.ProfileBlockView.as_view(),name="block"),
    path("stories/add/",views.StoryView.as_view(),name="story_created")

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
