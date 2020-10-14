from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
	path('home/', views.home, name="home"),
]