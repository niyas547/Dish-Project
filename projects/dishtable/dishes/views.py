from django.shortcuts import render,redirect
from django.views.generic import View
from dishes.models import Dishes
from django.contrib.auth.models import User
from dishes.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(data=request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            # form.save()
            messages.success(request,"registration completed")
            return redirect("dish-all")
        else:
            messages.error(request,"registration failed")
            return render(request,"register.html",{"form":form})
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                messages.success(request,"login success")
                return redirect("dish-all")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})
class DishAddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add-dish.html")
    def post(self,request,*args,**kwargs):
        name=request.POST.get("name")
        category=request.POST.get("category")
        price=request.POST.get("price")
        rating=request.POST.get("rating")
        Dishes.objects.create(name=name,category=category,price=price,rating=rating)
        messages.success(request,"dish added successfully")
        return redirect("dish-all")
class DishListView(View):
    def get(self,request,*args,**kwargs):
        all_dishes=Dishes.objects.all()
        return render(request,"list-dish.html",{"dishes":all_dishes})
class DishDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dish=Dishes.objects.get(id=id)
        return render(request,"dish-detail.html",{"dish":dish})
class DishDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dish=Dishes.objects.get(id=id)
        dish.delete()
        messages.success(request,"dish item deleted")
        return redirect("dish-all")
