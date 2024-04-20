from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('usuario/', user, name='user'),
    path('carrinho/', carrinho, name='carrinho'),
]
