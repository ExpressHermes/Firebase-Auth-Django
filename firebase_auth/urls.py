from django.urls import path
from . import views

app_name = 'firebase_auth'

urlpatterns = [
    path('', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout_view, name="logout"),
]
