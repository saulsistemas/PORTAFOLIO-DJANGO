from django.shortcuts import render, HttpResponse
html_base ="""

"""
# Create your views here.
def home(request):
    #return request;
    return render(request,"core/home.html");

def about(request):
    nombre = "Saul";
    return HttpResponse(html_base+"<h2>Acerca de</h2><p>"+nombre+"</p>");

def porfolio(request):
    nombre = "Saul";
    return HttpResponse(html_base+"<h2>Portafolio</h2><p>"+nombre+"</p>");

def contact(request):
    nombre = "Saul";
    return HttpResponse(html_base+"<h2>Contacto</h2><p>"+nombre+"</p>");