from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.detail, name='detail.question'),
    path('question/<int:question_id>/<int:choice_id>/', views.choice, name='api.detail.choice')
]