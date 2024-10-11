from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import render
from django.contrib.auth import logout
from django.views import generic


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'  # Redirigir a la página de administración para el inicio de sesión

#def logout_view(request):
   # logout(request)  # Cierra la sesión del usuario
    #return redirect('bases:login')  # Redirige al formulario de login después del logout


# sirver para forzar la redireccion Admin
#def dispatch(self, *args, **kwargs):
       # if not self.request.user.is_authenticated:
      #      return redirect(self.login_url)
      #  return super().dispatch(*args, **kwargs)
