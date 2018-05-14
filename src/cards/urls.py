# -*- encoding: utf-8 -*-

# django apps
from django.urls import path

# our apps
from . import views


urlpatterns = [
    path('', views.hello),

    path('cards_class_list/', views.CardList.as_view()),
    # path('cards_class_detail/<int:card_id>', views.CardDetail.as_view()),
    path('cards_view/', views.CardView.as_view()),

    # 存钱
    path('put_money/', views.put_money_view),
]