
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Article, Comments
from .serializers import *

'''class ListUsers(APIView):
    def get(self, requests, format=None):
        Получение списка всех пользователей
        username = [user.username for user in User.objects.all()]
        return Response(username)
'''


class Articles(APIView):
    def get(self, request):
        articls = Article.objects.all()
        serializer = ArticleSerializer(articls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CommentsView(APIView):

    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


