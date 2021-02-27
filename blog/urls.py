from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # post/정수값/ 에 해당하는 모든 url은 post_detail 뷰로 전송한다.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
