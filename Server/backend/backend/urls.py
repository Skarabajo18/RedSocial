from django.contrib import admin
from django.urls import (path, include)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.views import LoginView


# urlpatterns = [
#     path("admin/", admin.site.urls),

#     path('', include('app.urls')),
# ]


schema_view = get_schema_view(
    openapi.Info(
        title="Red ApiDocs",
        default_version='v1',
        description="Documentacion de la api",
        terms_of_service="https://www.lanuevaredsocial.com",
        contact=openapi.Contact(email="red@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,

)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
                                      cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
                                        cache_timeout=0), name='schema-redoc'),
    path('', include('app.urls')),
]
