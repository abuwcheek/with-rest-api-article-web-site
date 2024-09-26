from django.urls import path
from .views import category, category_list, home, detail



urlpatterns =[
     path('categories/', category),
     path('categories/<int:pk>/', category_list),
     path('list/', home),
     path('detail/<int:pk>/', detail),
]