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
from postSite.views import post_view, post_list, new_post_view, post_login, confirm_delete, confirm_edit, delete_post, edit_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', post_view),
    path('loginPage/', post_view, name='loginPage'),
    path('login/', post_login, name='login'),
    path('admin/', admin.site.urls),
    path('posts/<str:user>', post_list, name="post_list"),
    path('new_post/', new_post_view, name='new_post'),
    path('confirm_del/<int:pk>', confirm_delete, name='confirm_del'),
    path('confirm_edit/<int:pk>', confirm_edit, name='confirm_edit'),
    path('delete/<int:pk>', delete_post, name='delete_post'),
    path('edit/<int:pk>', edit_post, name='edit_post')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
