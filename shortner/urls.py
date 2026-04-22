from django.urls import path
from . import views

app_name = 'shortner'

urlpatterns = [
    path('', views.create, name='create'),
    path('r/<str:code>/', views.redirect_url, name='redirect'),
]