from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class PanelPrimarioView(TemplateView):
    template_name = 'panelprimario/controlprimario.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí puedes agregar cualquier contexto adicional que desees enviar a tu plantilla
        context['custom_data'] = 'Este es un dato personalizado para la plantilla'
        return context