from rest_framework.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Custom mixin classes
class JWTAuthenticationMixin:
    authentication_classes = [JSONWebTokenAuthentication]

class IsAuthenticatedMixin:
    permission_classes = [IsAuthenticated]