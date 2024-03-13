from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from APP.admins.models import Clientes
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from APP.admins.forms import ClientForm

class ClientListView(ListView):

    model = Clientes
    template_name = 'client/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for cliente in Clientes.objects.all():
                    cliente_data = cliente.toJSON()
                    # Agregar el nombre del vendedor al JSON de cliente
                    cliente_data['vendedor'] = cliente.vendedor.username if cliente.vendedor else ''
                    data.append(cliente_data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'TODOS LOS CLIENTES/ C VENDEDOR'
        context["url_list"] = reverse_lazy('lst02_cliente')
        return context

class ClientListPersonalView(ListView):

    model = Clientes
    template_name = 'client/list_personal_client.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST.get('action', None)
            if action == 'searchdata':
                vendedor_id = request.user.id              
                clientes = Clientes.objects.select_related('vendedor').filter(vendedor_id=vendedor_id)               
                data = []
                for cliente in clientes:
                    cliente_data = cliente.toJSON()
                    cliente_data['vendedor'] = cliente.vendedor.username if cliente.vendedor else ''
                    data.append(cliente_data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'LISTA DE CLIENTES PERSONALES' 
        context['last_client']  =  Clientes.objects.order_by('-id').first()
        context['url_form'] = reverse_lazy('form02_clientes')
        context['url_list'] = reverse_lazy('lst03_personal_cliente')
        return context
    
class CreateClientView(CreateView):

    model = Clientes
    form_class = ClientForm
    template_name = 'client/form_client.html'
    success_url = reverse_lazy('lst03_personal_cliente')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        """Este método pasa el usuario logueado al formulario."""
        kwargs = super(CreateClientView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pasamos el usuario logueado al formulario
        return kwargs

    def post(self, request, *args, **kwargs):
          data = {}
          try:
               action = request.POST['action']
               if action == 'add':
                    form = self.get_form()
                    if form.is_valid():
                         form.save()
                    else:
                         data['error']= form.errors
               else:
                    data['error'] = 'No se ha elegido una opcion'
          except Exception as e:
               data['error'] = str(e)
          return JsonResponse(data)   
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'REGISTRAR  CLIENTE'
        context['action'] = 'add'
        context['url_list'] = self.success_url
        return context
             
class DeleteClienteView(DeleteView):
    model = Clientes
    template_name = 'delete.html'
    success_url = reverse_lazy('lst03_personal_cliente')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ELIMINA CLIENTE DE LA BASE DE DATOS'
        context['entity'] = 'Clientes'
        context['list_url'] = self.success_url
        return context    