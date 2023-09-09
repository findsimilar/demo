"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

DESCRIPTION = ("This is Demo Project API to FindSimilar."
               " FindSimilar is user-friendly library to find similar objects")

schema_view = get_schema_view(
    openapi.Info(
        title="FindSimilar Demo API",
        default_version="v1",
        description=DESCRIPTION,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="quill@craftsman.lol"),
        license=openapi.License(name="MIT License"),
        url="/api/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_schema = schema_view.with_ui("swagger", cache_timeout=0)

urlpatterns = [
    path("", swagger_schema, name="docs"),
    path("admin/", admin.site.urls),
    path("", include("features.urls")),
    path("api-auth/", include("rest_framework.urls")),
    # open api docs
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path("swagger/", swagger_schema, name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
