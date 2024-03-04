from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic import RedirectView
from django.shortcuts import redirect, render
import appWeb.settings.base as setting

# Create your views here.
class Loginformv1(LoginView):
    template_name = 'log_sing.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request,*args, **kwargs)
        
    def form_invalid(self, form):
        # Limpia los campos antes de volver a renderizar el formulario
        form.data = form.data.copy()
        form.data['username'] = ''
        form.data['password'] = ''
        return render(self.request, self.template_name, self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'LOGEARTE/REGISTRARTE'
        return context 

class logoutformv2(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    