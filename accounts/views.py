from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.core.mail import send_mail

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        code = user.generate_otp()
        send_mail(
            'Ваш OTP-код',
            f'Ваш код подтверждения: {code}',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )

class VerifyOTPView(generics.GenericAPIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('otp_code')
        try:
            user = User.objects.get(email=email)
            if user.otp_code == code:
                user.is_verified = True
                user.otp_code = None
                user.save()
                
                refresh = RefreshToken.for_user(user)
                return Response({'detail': 'Подтверждено успешно', 'user': UserSerializer(user).data, 'tokens': {'refresh': str(refresh), 'access': str(refresh.access_token),}})
            else:
                return Response({'detail': 'Неверный код'}, status=400)
        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден'}, status=404)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if not user.is_verified:
            return Response({'detail': 'Подтвердите email через OTP'}, status=403)
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        })

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")
        if refresh_token is None:
            return Response({"error": "Refresh token is required"}, status=400)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"})
        except Exception as e:
            return Response({"error": str(e)}, status=400)