from django.urls import path
from .views import UserView, UserDetail, ClientView, ClientDetail, AuthUserRegistrationView, UserLoginView, \
    DriverView, DriverDetail, OrderView, OrderDetail

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('users/drivers/', DriverView.as_view()),
    path('users/<int:pk>/drivers/<int:pk>/', DriverDetail.as_view()),

    path('order/', OrderView.as_view()),
    path('order/<int:pk>/', OrderDetail.as_view()),
    path('order/<int:pk>/clients',  ClientView.as_view()),
    path('order/<int:pk>/clients/<int:pk>/',  ClientDetail.as_view()),

    path('register/', AuthUserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
]
