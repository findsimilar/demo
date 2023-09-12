from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = "examples"

router = SimpleRouter()
router.register('examples', views.ExampleViewSet, 'examples')

urlpatterns = [
    path("", include(router.urls)),
]
