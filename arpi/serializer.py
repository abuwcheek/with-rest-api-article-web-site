from rest_framework import serializers
from .models import Article, Category


class CategorySerializer(serializers.Serializer):
     id = serializers.IntegerField()
     name = serializers.CharField()
     # a_count = serializers.IntegerField()
     a_count = serializers.SerializerMethodField(method_name='get_count')


     def get_count(self, obj: Category):
          return obj.category_article.count()



# /////////////////////////////////////////////////////////////////////////////////////////////////////////


# class ArticleSerializer(serializers.Serializer):
#      id = serializers.IntegerField()
#      category = serializers.CharField()
#      ctg_id = serializers.IntegerField(source='category_id')
#      name = serializers.CharField(source='title')


class ArticleSerializer(serializers.ModelSerializer):
     class Meta:
          model = Article
          fields = ['id', 'category', 'title','subtitle', 'body']


# /////////////////////////////////////////////////////////////////////////////////////////////////////////

# class ArticleDetailSerializer(serializers.Serializer):
#      id = serializers.IntegerField()
#      category = serializers.CharField()
#      ctg_id = serializers.IntegerField(source='category_id')
#      title = serializers.CharField()
#      subtitle = serializers.CharField()
#      body = serializers.CharField()
#      image = serializers.ImageField()
#      created_at = serializers.DateTimeField()



class ArticleDetailSerializer(serializers.ModelSerializer):
     class Meta:
          model = Article
          # fields = ('__all__')
          fields = ['id', 'title', 'category', 'category_name', 'subtitle', 'body', 'image', 'created_at', 'updated_at']
          
     category_name = serializers.SerializerMethodField(method_name='ctg_name',)
     def ctg_name(self, obj: Article):
          return obj.category.name

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////