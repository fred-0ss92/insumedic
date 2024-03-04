from django.shortcuts import render
from django.views import View

# Create your views here.

"""def Primera_prueba(request):

    return render(request, "H_page.html", {"algo": "algos"})"""

class Pagina_Inicio(View):

    def get(self, request):
        return render(request, 'H_page.html')