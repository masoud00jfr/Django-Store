from dj_rest_auth.views import PasswordResetConfirmView
from django.urls import path, include
from .views import register_view

app_name = 'customers'

urlpatterns = [
    path('register', register_view, name='register'),
    path('rest-auth/', include('dj_rest_auth.urls')),
    # path('rest-auth/ password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # --> must add to project urls
]
