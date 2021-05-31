from django.urls import path
from . import views as core_views

from .views import CommentFormPost, tools, forget, signupp, login, Edu, search

urlpatterns = [
    path('', CommentFormPost, name='home'),
    path('signup/', core_views.signupp, name='signup'),
    path('tools/', tools, name = 'tools'),
    path('forget/', forget, name = 'forget-pass'),
    path('sign-up/', signupp, name = 'sign-up'),
    path('Educational/', Edu, name = 'Educational-concepts'),
    path('login/', login, name = 'login'),
    path('search/', search, name = 'search_results'),
]