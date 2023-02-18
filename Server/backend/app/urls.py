from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework import routers


from .viewsets import (
    UserViewSet,
    UserProfileViewSet,
    UserRelationshipViewSet,
)

from .views import (
    index
)
###################################################################
# Registro de las clases para la creacion de las url de API	  #
###################################################################

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'user-profile', UserProfileViewSet)
router.register(r'user-relationship', UserRelationshipViewSet)


urlpatterns = [
    # URL de API
    path('', view=index),
    path('api/', include(router.urls), name='api'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
