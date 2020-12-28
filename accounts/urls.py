from django.urls import path

from . import views


app_name = 'accounts'


urlpatterns = [
    path('user/', views.UserDetails.as_view({'get': 'get_single'})),
]
