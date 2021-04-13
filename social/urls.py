from django.urls import path,re_path
from django.views.generic.base import RedirectView
from social import views


app_name='social'

urlpatterns = [
   path('home/',views.HomeView.as_view(),name='home'),
   path('index/',views.IndexView.as_view(),name='index'),
   path('profile/edit/<int:pk>',views.ProfileUpdateView.as_view(),name='edit'),
   path('post/create',views.PostCreateView.as_view(),name='postCreate'),
   path('post/delete/<int:pk>',views.PostDeleteView.as_view(),name='postDelete'),
   path('post/',views.PostListView.as_view(),name='postList'),
   path('post/detail/<int:pk>',views.PostDetailView.as_view(),name='postDetail'),
   path('post/like/<int:pk>',views.postlike,name='postlike'),
   path('post/unlike/<int:pk>',views.postunlike,name='postdislike'),
   path('post/comments/add/<int:pk>',views.CommentAddView,name='commentadd'),




   path('profile/',views.ProfileListView.as_view(),name='profileList'),
   path('profile/detail/<int:pk>',views.ProfileDetailView.as_view(),name='profileDetail'),
   path('profile/follow/<int:pk>',views.follow_user,name='follow'),
   path('profile/unfollow/<int:pk>',views.unfollow_user,name='unfollow'),

   path('',RedirectView.as_view(url="index/")),

]
