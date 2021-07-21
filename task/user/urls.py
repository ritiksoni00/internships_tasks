from django.urls import path

from . import views


urlpatterns = [
    path('',views.auth_form, name='auth_form'),
    path('post/', views.show_post_form, name='show_post_form')
]
