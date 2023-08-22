"""capsule URL Configuration

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
from capsuleapi.views.auth import check_user, register_user
from django.urls import path, include
from rest_framework import routers
from capsuleapi.views import CategoryView, ItemView, CapsuleUserView, OutfitItemView, OutfitView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'capsule_users', CapsuleUserView, 'capsule_user')
router.register(r'categories', CategoryView, 'category')
router.register(r'items', ItemView, 'item')
router.register(r'outfit_items', OutfitItemView, 'outfit_item')
router.register(r'outfits', OutfitView, 'outfit')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),

]
