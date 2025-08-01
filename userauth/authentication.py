from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomUser

class CustomUserJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token.get("user_id")
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None