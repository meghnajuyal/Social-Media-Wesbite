"""SocialWebsiteClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from . import settings
from django.contrib.auth import views as auth_view
from social import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/',include("social.urls")),
    path('',RedirectView.as_view(url="accounts/login/")),
    path('accounts/login/',auth_view.LoginView.as_view(),name='login'),
    path('accounts/logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('accounts/register/',views.RegisterView.as_view(),name='register'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
