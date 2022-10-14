from django.shortcuts import render
from django.views.generic import View
from dishes.models import Dishes


# Create your views here.

class DishAddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add-dish.html")
    def post(self,request,*args,**kwargs):
        name=request.POST.get("name")
        category=request.POST.get("category")
        price=request.POST.get("price")
        rating=request.POST.get("rating")
        Dishes.objects.create(name=name,category=category,price=price,rating=rating)
        return render(request,"add-dish.html")
class DishListView(View):
    def get(self,request,*args,**kwargs):
        all_dishes=Dishes.objects.all()
        return render(request,"list-dish.html",{"dishes":all_dishes})
