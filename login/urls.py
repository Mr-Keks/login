from django.contrib import admin
from django.urls import path, include

from .views import LoginCreateView, index

urlpatterns = [
	path('login', LoginCreateView.as_view(), name = 'login_form'),
	path('', index.as_view(), name = 'index'),
]
