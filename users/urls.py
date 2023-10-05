from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='update_profile'),
    path('profile/delete/', UserDeleteView.as_view(), name='delete_profile'),
]
