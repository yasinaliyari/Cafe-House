from django.urls import path
from menu.views import MenuPageView

urlpatterns = [
    path("", MenuPageView.as_view(), name="menu"),
]
