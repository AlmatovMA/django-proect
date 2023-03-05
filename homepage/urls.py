from django.urls import path
from .views import (homePageView,
                    HomePgWiew,
                    AbautWiew,
                    lsview,
                    HomeDetailView,
                    HomeCreateView,
                    HomeUpdateView,
                    HomeDeleteView,
                    )


urlpatterns = [
    path('helloword/',homePageView, name='hello'),
    path('', lsview.as_view(), name='home.html'),
    path('abaut', AbautWiew.as_view(), name='abaut.html'),
    path('post/<int:pk>/', HomeDetailView.as_view(), name='post_detail'),
    path('post/new/>', HomeCreateView.as_view(), name='post_new.html'),
    path('post/<int:pk>/edit', HomeUpdateView.as_view(), name='post_edit.html'),
    path('post/<int:pk>/delete', HomeDeleteView.as_view(), name='post_delete.html'),

]