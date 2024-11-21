from django.urls import path
from . import views
from .views import IndexPageView

urlpatterns = [
    path('', views.index, name='index'),
    path('jeje', IndexPageView.as_view(), name='index'),
]
