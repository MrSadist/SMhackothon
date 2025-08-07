from django.urls import path
from .views import RegisterView, LoginView, VerifyOTPView, ProfileView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'), 
    path('verify-otp/', VerifyOTPView.as_view(), name='ver0ify-otp'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name="logout")
]
