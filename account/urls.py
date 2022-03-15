from django.urls import path, include
from .views import add_student, forgot_password, add_user, list_students, list_users, profile, reset_password

urlpatterns = [
    path('add_user/', add_user),
    path('add_student/', add_student),
    path('forgot_password/', forgot_password),
    path('reset_password/', reset_password),
    path('list_users/', list_users),
    path('list_students/', list_students),
    path('profile/', profile),
]
