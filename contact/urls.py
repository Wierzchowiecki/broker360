from django.urls import path

from .views import contact, contact_success, privacy_policy


app_name = "contact"

urlpatterns = [
    path("", contact, name="form"),
    path(
        "dziekujemy/",
        contact_success,
        name="success",
    ),
    path(
        "polityka-prywatnosci/",
        privacy_policy,
        name="privacy_policy",
    ),
]