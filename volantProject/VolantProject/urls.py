"""
URL configuration for VolantProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from VolantApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='landinghome'),
    path('userregister/',views.UserRegisterView.as_view(),name='user_register'),
    path('userlogin/',views.UserLogin.as_view(),name='user_login'),
    path('index/',views.UserIndex.as_view(),name='user_index'),
    path('view',views.ProductsView.as_view(),name='view'),
    path('detail/<int:id>',views.ProductDetailView.as_view(),name='detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
