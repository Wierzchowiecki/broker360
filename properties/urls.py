from django.urls import path

from .views import home, property_detail


urlpatterns = [
    path(
        "",
        home,
        name="home",
    ),
    path(
        "oferty/<slug:slug>/",
        property_detail,
        name="property_detail",
    ),
]