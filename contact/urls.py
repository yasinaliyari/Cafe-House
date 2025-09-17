from django.urls import path
from contact.views import ContactUsView

urlpatterns = [
    path("", ContactUsView.as_view(), name="contact"),
]
