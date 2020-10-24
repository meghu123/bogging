from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.homeview,name='home'),
    path('login/',views.loginview,name='login'),
    path('register/', views.registerview, name='register'),
path('allpost/', views.postview, name='postview'),
path('logout/', views.logoutview, name='logout'),
path('comment/<int:pk>/', views.commentView, name='comment'),
    path('search/',views.searchview,name='search'),
    path('delete/<int:pk>/', views.deleteview, name='delete'),
    path('update/<int:pk>/', views.updateview, name='update'),
    path('profile/', views.Profileview, name='profile'),

]