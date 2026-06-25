<<<<<<< HEAD
from django.urls import path
from .views import RegisterView, DashboardView

urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),

    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard'
    ),
=======
from django.urls import path
from .views import RegisterView, DashboardView

urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),

    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard'
    ),
>>>>>>> 62db3cca611d52196f5336fa87f9758769f211b4
]