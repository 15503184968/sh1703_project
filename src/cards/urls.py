# -*- encoding: utf-8 -*-

# django apps
from django.urls import path, include
from rest_framework import routers

# our apps
from . import views, serializers


router = routers.DefaultRouter()
router.register('cards', views.CardViewSet)


urlpatterns = [
    path('', views.hello),

    path('cards_class_list/', views.CardList.as_view()),
    # path('cards_class_detail/<int:card_id>', views.CardDetail.as_view()),
    path('cards_view/', views.CardView.as_view(), name='card_view'),

    # 存钱
    path('put_money/', views.put_money_view),


    # rest framework
    path('cards/', include(router.urls)),
]
