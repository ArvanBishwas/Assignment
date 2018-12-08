from django.urls import path
from .views import create, detail, upvote

urlpatterns = [
    path('create',create, name='create'),
    path('<int:idea_id>',detail, name='detail'),
    path('<int:idea_id>/upvote', upvote,name='upvote'),
]
