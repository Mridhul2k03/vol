from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserRegisterForm,UserLoginForm
from django.views import View
from django.views.generic import TemplateView,CreateView,UpdateView,ListView,DeleteView,DetailView
from django.contrib.auth import login,logout,authenticate
from .models import Footwears,Footwearimages

# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'
    
class UserRegisterView(CreateView):
    template_name = 'user_reg.html'
    form_class = UserRegisterForm
    model = User
    
    def form_valid(self, form):
        User.objects.create_user(**form.cleaned_data)
        return redirect('landinghome')

class UserLogin(View):
    def get(self,request,*args, **kwargs):
        form=UserLoginForm()
        return render(request,'userlogin.html',{'form':form})
    
    def post(self,request,*args, **kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return render(request,'userindex.html')
        else:
            form=UserLoginForm()
            return render(request,'userlogin.html',{'form':form})

class UserLogout(View):
    def get(self,request):
        logout(request)
        return redirect('enter_home')       
    

class UserIndex(TemplateView):
    template_name = 'userindex.html'
    
class ProductsView(ListView):
    template_name = 'gentspro.html'
    model = Footwears
    context_object_name = 'products'

class ProductDetailView(DetailView):
    template_name = 'ii.html'
    model = Footwearimages
    context_object_name = 'products'
    pk_url_kwarg = 'id'
    
    