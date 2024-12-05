from django.urls import path
from .views import registroView
urlpatterns = [
    path('signup', registroView, name='signupform'),
]
