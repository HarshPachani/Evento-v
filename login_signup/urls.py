from django.urls import path
from . import views
urlpatterns = [
    path('', views.loginOrSignup, name="loginOrSignup"),
    path('postSignIn', views.signedIn, name = "signedIn"),
    path('postSignUp', views.signedUp, name = "signedUp"),
    path('forgetPassword', views.forgetPwd, name="forgetPass")
]