from django.urls import path
from . import views

app_name = "features"

urlpatterns = [
    path("api/", views.FindSimilarApiView.as_view(), name="api"),
]
