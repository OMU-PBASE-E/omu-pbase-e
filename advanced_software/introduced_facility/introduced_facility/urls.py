"""introduced_facility URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import FacilityListClass, Facility1Class, Facility2Class

# 新しくページを追加するときはここにURLパターンを追加
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FacilityListClass.as_view(), name='facility-list'), # 施設一覧を表示するページのURL
    path('facility1/', Facility1Class.as_view(), name='facility1'), # 施設1を表示するページのURL
    path('facility2/', Facility2Class.as_view(), name='facility2'), # 施設2を表示するページのURL
]
