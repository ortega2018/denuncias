from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def cargar_denuncia(request):
    video = None
    if request.method == "POST":
        try:
            latitude = float(request.POST.get("latitude"))
            longitude = float(request.POST.get("longitude"))
            numero = request.POST.get("numero")
            if 'video' in request.FILES:
                video = request.FILES['video']
            d = Denuncia(latitud=latitude, longitud=longitude, numero=numero)
            d.video = video
            d.save()
            return JsonResponse({'code': 200, 'message': "carga completada!"})
        except  Exception as e:
            return JsonResponse({'code': 500, 'message': e.message}, status=500)
    else:
        return JsonResponse({'code': 400, 'message': "parametros invalidos"}, status=400)


@csrf_exempt
def cargar_posicion(request):
    if request.method == "POST":
        try:
            latitude = float(request.POST.get("latitude"))
            longitude = float(request.POST.get("longitude"))
            numero = request.POST.get("numero")
            time = request.POST.get("time")
            p = Posicion(latitud=latitude, longitud=longitude, numero=numero, time=time)
            p.save()
            return JsonResponse({'code': 200, 'message': "carga completada!"})
        except  Exception as e:
            return JsonResponse({'code': 500, 'message': e.message}, status=500)
    else:
        return JsonResponse({'code': 400, 'message': "parametros invalidos"}, status=400)


@csrf_exempt
def cargar_mensajes(request):
    if request.method == "POST":
        try:
            mensajes = request.POST.get("mensajes")
            numero = request.POST.get("numero")
            m = Mensajes(numero=numero, mensajes=mensajes)
            m.save()
            return JsonResponse({'code': 200, 'message': "carga completada!"})
        except  Exception as e:
            return JsonResponse({'code': 500, 'message': e.message}, status=500)
    else:
        return JsonResponse({'code': 400, 'message': "parametros invalidos"}, status=400)


@csrf_exempt
def cargar_contactos(request):
    if request.method == "POST":
        try:
            contactos = request.POST.get("contactos")
            numero = request.POST.get("numero")
            c = Contactos(numero=numero, contactos=contactos)
            c.save()
            return JsonResponse({'code': 200, 'message': "carga completada!"})
        except  Exception as e:
            return JsonResponse({'code': 500, 'message': e.message}, status=500)
    else:
        return JsonResponse({'code': 400, 'message': "parametros invalidos"}, status=400)


@csrf_exempt
def obtener_quemados(request):
    if request.method == "GET":
        try:
            numeros = Quemado.objects.all().order_by('numero').values_list('numero', flat=True)
            return JsonResponse({'code': 200, 'message': "ok!", 'numeros': numeros})
        except  Exception as e:
            return JsonResponse({'code': 500, 'message': e.message}, status=500)
    else:
        return JsonResponse({'code': 400, 'message': "solicitud invalida!"}, status=400)
