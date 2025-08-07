from django.urls import path
from .views import ChatbotAPIView

urlpatterns = [
    path('AIchat/', ChatbotAPIView.as_view(), name='chatbot')
]
