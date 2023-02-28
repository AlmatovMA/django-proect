from django.urls import path
from homepage.views import homePageView, HomePgWiew, AbautWiew


urlpatterns = [
    path('helloword/',homePageView, name='hello'),
    path('', HomePgWiew.as_view(), name='home.html'),
    path('abaut', AbautWiew.as_view(), name='abaut.html'),
]