from rest_framework import viewsets

from .models import (
    User,
    UserProfile,
    UserRelationship
)

from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    UserRelationshipSerializer
)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserRelationshipViewSet(viewsets.ModelViewSet):

    queryset = UserRelationship.objects.all()
    serializer_class = UserRelationshipSerializer
