from django.urls import path
from .views import (register, 
                    UserLogin,
                    UserLogout,
                    update_profile,
                    profile,
                    UserPasswordChangeView,
                    UserPasswordResetView,
                    UserPasswordResetConfirmView
                    )

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('update/', update_profile, name='update'),
    path('password/change/', UserPasswordChangeView.as_view(), name='change_password'),
    path('password_reset/',UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]