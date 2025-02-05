from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('room/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
