from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#------------------>modelos y formularios
from APP.admins.models import *
from APP.admins.forms import ProductForm

#------->LISTA DE PRODUCTOS
class ProductListView(ListView):
    model = Productos
    template_name = 'product/list.html'
    success_url = reverse_lazy('lst01_inventario')
    form_url = reverse_lazy('form01_inventarios')

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
                for i in Productos.objects.all():
                    data.append(i.toJSON())
            elif action == "edit":
                instance = get_object_or_404(Productos, pk=request.POST.get('id'))
                form = ProductForm(request.POST, request.FILES, instance=instance)
                if form.is_valid():
                    product = form.save()
                    # Aquí simplemente podrías devolver un mensaje de éxito
                    data = {'message': "Producto actualizado con éxito"}
                else:
                    data['error'] = form.errors.as_json()
            elif action == "delete":
                cli = Productos.objects.get(pk=request.POST['id'])
                cli.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'INVENTARIO INSUMEDIC'
        context['url_list'] = self.success_url
        context['url_form'] = self.form_url
        context['form'] = ProductForm()
        return context

#------->FORMULARIO DE PRODUCTOS CON OPCION A ELIMINAR    
class FormProduct(CreateView):
    model = Productos
    form_class = ProductForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('lst01_inventario') 

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.get_form()
            if form.is_valid():
                self.object = form.save()
                return JsonResponse({'success': True, 'redirect_url': self.get_success_url()})
            else:
                return JsonResponse({'success': False, 'errors': form.errors.as_json()})
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'REGISTRAR PRODUCTOS EN INVENTARIO'
        context['entity'] = 'Productos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context