from django.urls import path
from .views import signup_view, login_view, dashboard_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', dashboard_view, name='dashboard'),
]