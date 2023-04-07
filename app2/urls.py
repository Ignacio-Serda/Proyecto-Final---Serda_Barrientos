from django.urls import path
from app2.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/signup/', register_account, name="REGISTER"),
    path('accounts/login/', login_account, name="LOGIN"),
    path('login_exitoso/', succesful_login, name="SUCCESFUL_LOGIN"),
    path('logout/', LogoutView.as_view(template_name="app2/log-out.html"), name="LOGOUT"),
    path('accounts/profile/', profile, name="PROFILE"),
    path('accounts/profile2/', profile2, name="PROFILE2")
]
