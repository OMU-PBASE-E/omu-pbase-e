from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListFacilityView.as_view(), name='facility-list'),
    #path('<int:pk>/detail/', views.DetailFacilityView.as_view(), name='detail-facility'), # 森ノ宮キャンパスを表示するページのURL
]