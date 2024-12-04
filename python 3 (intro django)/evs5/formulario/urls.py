from django.urls import path
from .views import boardsform_view

urlpatterns = [
    path('modelform',boardsform_view,name='modelform')
]