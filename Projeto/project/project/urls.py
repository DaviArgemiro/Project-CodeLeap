"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from accounts.views import login_view
from postSite.views import post_view, new_post_view, delete_post_view, edit_post_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('posts/', post_view, name='post_list'),
    path('new_post/', new_post_view, name='new_post'),
    path('delete_post/<int:pk>', delete_post_view, name='delete_post'),
    path('edit_post/<int:pk>', edit_post_view, name='edit_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
