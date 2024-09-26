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
          data = request.POST
          serializer = ArticleSerializer(data=data)
          if serializer.is_valid():
               return Response('ok')
          else:
               return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def detail(request, pk):
     queryset = get_object_or_404(Article, pk=pk)
     serializer = ArticleDetailSerializer(queryset)
     data = serializer.data
     return Response(data)