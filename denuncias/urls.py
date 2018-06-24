from .views import *
from django.conf.urls import url

urlspattern = [
    url(r'quemados/', obtener_quemados, name='denuncias_quemados'),
    url(r'denuncia/', cargar_denuncia, name='denuncias_denuncia'),
    url(r'contactos/', cargar_contactos, name='denuncias_contactos'),
    url(r'mensajes/', cargar_mensajes, name='denuncias_mensajes'),
    url(r'posicion/', cargar_posicion, name='denuncias_posicion'),
]