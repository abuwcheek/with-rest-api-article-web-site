from django.urls import path
# from .views import category, category_list, home, detail
from .views import ArticlesAPIView, ArticlesDetailAPIView, CategoryAPIView, CategoryListAPIView



urlpatterns = [
     path('list/', ArticlesAPIView.as_view()), 
     path('detail/<int:pk>/', ArticlesDetailAPIView.as_view()), 
     path('categories/', CategoryAPIView.as_view()), 
     path('categories/<int:pk>/', CategoryListAPIView.as_view()), 
]



# urlpatterns =[
#      path('categories/', category),
#      path('categories/<int:pk>/', category_list),
#      path('list/', home),
#      path('detail/<int:pk>/', detail),
# ]