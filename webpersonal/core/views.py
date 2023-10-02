from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    htlm = "<h1>Es una prueba</h1><h2>Portada</h2>";
    #bucle for
    for i in range(10):
        htlm+="<h3>Prueba</h3>";
    return HttpResponse(htlm);