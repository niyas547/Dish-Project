"""dishtable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from dishes.views import DishAddView,DishListView,DishDetailView,DishDeleteView
from dishes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_dish',views.DishAddView.as_view(),name="dish-add"),
    path('list_dishes',views.DishListView.as_view(),name="dish-all"),
    path('dishes/<int:id>',views.DishDetailView.as_view(),name="dish-detail"),
    path('dishes/<int:id>/remove',views.DishDeleteView.as_view(),name="dish-delete"),
    path('signup',views.RegistrationView.as_view(),name="register"),
    path('',views.LoginView.as_view(),name="login")

]
