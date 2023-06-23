from django.urls import include, path
from . import views

api_patterns = [
    path("test/", views.configure, name="configure")
]

urlpatterns = [
    path("", include(api_patterns)),
]
