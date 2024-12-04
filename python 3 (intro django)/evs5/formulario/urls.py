from django.urls import path
from .views import boardsform_view, registro_view, login_view, logout_view

urlpatterns = [
    path('modelform',boardsform_view,name='modelform'),
    path('signup',registro_view,name='signup'),
    path('signin',login_view,name='signin'),
    path('logout',logout_view,name='logout'),
]