from django.urls import path
from .views import signUpView, loginView, indexView, logoutView
urlpatterns = [
    path('', indexView, name='index'),
    path('signup', signUpView, name='signupform'),
    path('login', loginView, name='loginform'),
    path('logout', logoutView, name='logoutpath'),
]
