from django.shortcuts import render, HttpResponse
html_base ="""
<h1> Mi Web personal </h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
<ul>
"""
# Create your views here.
def home(request):
    htlm = "<h2>Portada</h2>";
    #bucle for
    for i in range(10):
        htlm+="<h5>Prueba</h5>";
    return HttpResponse(html_base+htlm);

def about(request):
    nombre = "Saul";
    return HttpResponse(html_base+"<h2>Acerca de</h2><p>"+nombre+"</p>");