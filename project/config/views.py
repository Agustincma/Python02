from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola")

def saludoDos(request):
    nombre = input("Ingrese su nombre: ")
    return HttpResponse(f"Hola, su nombre es: {nombre}")

def dados(request):
    import random

    numero = random.randint(1, 6);

    if numero == 6:
        return HttpResponse(f"Felicidades ha salido el N.° {numero}.")
    else:
        return HttpResponse(f"lo siento ha salido el N.° {numero}, vuelve a intentarlo")
        