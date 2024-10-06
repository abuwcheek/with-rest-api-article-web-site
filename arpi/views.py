from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article, Category
from .serializer import ArticleSerializer, ArticleDetailSerializer, CategorySerializer



@api_view()
def category(request):
     queryset = Category.objects.all()
     serializer = CategorySerializer(queryset, many=True)
     data = serializer.data
     return Response(data)

@api_view()
def category_list(request, pk):
     ctg = get_object_or_404(Category, pk=pk)
     serializer = ArticleSerializer(ctg.category_article.all(), many=True)
     data = serializer.data
     return Response(data)


@api_view(['GET', 'POST'])
def home(request):
     if request.method == 'GET':
          queryset = Article.objects.all()
          serializer = ArticleSerializer(queryset, many=True)
          data = serializer.data
          return Response(data)
     
     elif request.method == 'POST':
          data = request.data
          serializer = ArticleSerializer(data=data)
          # if serializer.is_valid():
          #      serializer.save()
          #      return Response(serializer.data, status=status.HTTP_200_OK)
          # else:
          #      return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
     


@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, pk):
     queryset = get_object_or_404(Article, pk=pk)
     if request.method == 'GET':
          serializer = ArticleDetailSerializer(queryset)
          data = serializer.data
          return Response(data)
     elif request.method == 'PUT':
          serializer = ArticleDetailSerializer(instance=queryset, data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
     elif request.method == 'DELETE':
          queryset.delete()
          return Response("Article o'chirildi", status=status.HTTP_204_NO_CONTENT)