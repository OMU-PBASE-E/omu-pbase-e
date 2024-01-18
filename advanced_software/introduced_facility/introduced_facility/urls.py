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
from .views import FacilityListClass, MorinomiyaClass, EngineeringClass, ScienceClass

# 新しくページを追加するときはここにURLパターンを追加
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FacilityListClass.as_view(), name='facility-list'), # 施設一覧を表示するページのURL
    path('morinomiya/', MorinomiyaClass.as_view(), name='morinomiya'), # 森ノ宮キャンパスを表示するページのURL
    path('engineering/', EngineeringClass.as_view(), name='engineering'), # 新工学部棟を表示するページのURL
    path('science/', ScienceClass.as_view(), name='science'), # 新理学部棟を表示するページのURL
]
