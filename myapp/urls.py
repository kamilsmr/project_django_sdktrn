
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('details', views.details, name="details"),
    path('<int:category_id>', views.getProductsByCategoryId),
    # eğer int aşağıda olursa çalışmaz çünkü sayıda string olarak kabul edilir.
    path('<str:category>', views.getProductsByCategory),
    


    
]