from django.db import models


class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     is_active = models.BooleanField(default=True)

     class Meta:
          abstract = True



class Category(BaseModel):
     name = models.CharField(max_length=100)


     def __str__(self):
          return self.name

     # @property
     # def a_count(self):
     #      return self.category_article.count()



class Article(BaseModel):
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_article')
     image = models.ImageField(upload_to='images/', null=True, blank=True)
     title = models.CharField(max_length=255)
     subtitle = models.TextField()
     body = models.TextField()


     def __str__(self):
          return self.title