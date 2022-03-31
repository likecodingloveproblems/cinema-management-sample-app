from django.urls import path
from my_auth.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
