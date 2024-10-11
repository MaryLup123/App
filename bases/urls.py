from django.urls import path
from django.contrib.auth import views as auth_views
from bases.views import Home

app_name = 'bases'

urlpatterns = [
    path('', Home.as_view(), name='home'),  # Vista principal protegida
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),  # Página de login
    path('logout/', auth_views.LogoutView.as_view(next_page='bases:login'), name='logout'),  # Página de logout
]
