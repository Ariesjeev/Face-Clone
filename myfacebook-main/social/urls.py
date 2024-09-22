from django.urls import path

# from .views import index, home, profile, signout, register, update_profile, create_post, delete_post

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('logout',views.signout,name='logout'),
    path('register',views.register,name='register'),
    path('update',views.update_profile,name='update'),
    path('addpost',views.create_post,name='addpost'),
    # path('deletepost/<int:post_id>', views.delete_post, name='deletepost')
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
 ]
