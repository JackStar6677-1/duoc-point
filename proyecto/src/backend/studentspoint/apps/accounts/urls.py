"""Rutas de la aplicación de cuentas."""

from django.urls import path

from .views import me, update_profile, check_email, login, register
from .oauth_views import (
    google_login, google_callback, google_login_redirect, 
    google_callback_web, google_user_info, disconnect_google
)
from .teachers_views import TeachersListView, TeacherDetailView


urlpatterns = [
    # Autenticación tradicional
    path("auth/login/", login, name="login"),
    path("auth/register/", register, name="register"),
    path("auth/me/", me, name="me"),
    path("auth/me/update/", update_profile, name="update_profile"),
    path("auth/check-email/", check_email, name="check_email"),
    
    # OAuth de Google
    path("auth/google/login/", google_login, name="google_login"),
    path("auth/google/callback/", google_callback, name="google_callback"),
    path("auth/google/redirect/", google_login_redirect, name="google_redirect"),
    path("auth/google/callback/web/", google_callback_web, name="google_callback_web"),
    path("auth/google/user-info/", google_user_info, name="google_user_info"),
    path("auth/google/disconnect/", disconnect_google, name="disconnect_google"),
    
    # Directorio de profesores
    path("teachers/", TeachersListView.as_view(), name="teachers-list"),
    path("teachers/<int:pk>/", TeacherDetailView.as_view(), name="teacher-detail"),
]

