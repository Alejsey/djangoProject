from django.urls import  path

from .views import Articles, CommentsView

urlpatterns = [
    path('post/', Articles.as_view()),
    path('Com/', CommentsView.as_view()),
]