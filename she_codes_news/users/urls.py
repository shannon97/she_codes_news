from django.urls import path
from .views import CreateAccountView, UserAccountView, EditAccountView

app_name ='users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', UserAccountView.as_view(), name='myAccount'),
    path('<int:pk>/edit-account/', EditAccountView.as_view(), name='editAccount'),
    ]

