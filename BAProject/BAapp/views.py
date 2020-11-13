from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from django.views import View

from .forms import *
from .models import *


def landing_page(request):
	return render(request, 'Principal.html')

def admin(request):
    return render(request,'admin.html')


class ListArticuloView(View):
    def get(self, request, *args, **kwargs):
        all_articulos = Articulo.objects.all()
        return render(request, 'consultar_articulo.html', {'articulos':all_articulos})    

class ArticuloView(View):
    def get(self, request, *args, **kwargs):
        context = {
        "form": ArticuloForm()}
        if ("pk" in kwargs):
            context["articulo"] = Articulo.objects.get(pk=kwargs["pk"])
            context["form"] = ArticuloForm(instance=context["articulo"])
        return render(request, 'articulo.html', context)

    def post(self, request, *args, **kwargs):
        articulo = None
        if ("pk" in kwargs):
            articulo = Articulo.objects.get(pk=kwargs["pk"])
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            articulo = form.save()
            return redirect('articulo', pk=articulo.pk)
        return render(request, 'articulo.html', context={"form":form})

    def delete(self, request, *args, **kwargs):
        articulo = Articulo.objects.get(pk=kwargs["pk"])
        articulo.delete()
        return HttpResponse(code=200)



class ListProveedorView(View):
    def get(self, request, *args, **kwargs):
        all_proveedores = Proveedor.objects.all()
        return render(request, 'consultar_proveedor.html', {'proveedores':all_proveedores})    


class ProveedorView(View):
    def get(self, request, *args, **kwargs):
        context = {
        "form": ProveedorForm()}
        if ("pk" in kwargs):
            context["proveedor"] = Proveedor.objects.get(pk=kwargs["pk"])
            context["form"] = ProveedorForm(instance=context["proveedor"])
        return render(request, 'proveedor.html', context)

    def post(self, request, *args, **kwargs):
        proveedor = None
        if ("pk" in kwargs):
            proveedor = Proveedor.objects.get(pk=kwargs["pk"])
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            proveedor = form.save()
            return redirect('proveedor', pk=proveedor.pk)
        return render(request, 'proveedor.html', context={"form":form})

    def delete(self, request, *args, **kwargs):
        proveedor = Proveedor.objects.get(pk=kwargs["pk"])
        proveedor.delete()
        return HttpResponse(code=200)



class ListClienteView(View):
    def get(self, request, *args, **kwargs):
        all_clientes = Cliente.objects.all()
        return render(request, 'consultar_cliente.html', {'clientes':all_clientes})    


class ClienteView(View):
    def get(self, request, *args, **kwargs):
        context = {
        "form": ClienteForm()}
        if ("pk" in kwargs):
            context["cliente"] = Cliente.objects.get(pk=kwargs["pk"])
            context["form"] = ClienteForm(instance=context["cliente"])
        return render(request, 'cliente.html', context)

    def post(self, request, *args, **kwargs):
        cliente = None
        if ("pk" in kwargs):
            cliente = Cliente.objects.get(pk=kwargs["pk"])
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            return redirect("cliente", pk=cliente.pk)
        return render(request, 'cliente.html', context={"form":form})

    def delete(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(pk=kwargs["pk"])
        cliente.delete()
        return HttpResponse(status=200)