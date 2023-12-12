from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MedioDiario, Medio,  AnalisisDiario, AnalisisGeneral, Noticia, DeterminacionIa
from datetime import datetime, timedelta
import json

# Create your views here.

#me redirije a la fecha actual
def index(request):
    fecha_str = str(datetime.today())
    fecha, marca_tiempo = fecha_str.split(' ')
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
    url = reverse('analisis_medios', args=[fecha])
    return redirect(url)

#muetra todos los analisis diario en una fecha 
def analisis_medios(request,fecha=None):
    if request.method == 'POST':
        fecha = request.POST.get('fecha_date')
        return redirect(f'/medios_diario/{fecha}/')
    else:

        fecha_actual = datetime.today()
        fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
        medios = Medio.objects.all()
        analisis_diarios = AnalisisDiario.objects.filter(fecha=fecha_obj)
        medios_diarios= MedioDiario.objects.filter(fecha=fecha_obj)
        analisis_general = AnalisisGeneral.objects.filter(fecha=fecha_obj)
        lista_porcentajes = list()
        lista_general_porcentajes = list()
        for e in analisis_diarios:
            if(e.total>0):
                per_buenas=round((e.buenas/e.total)*100 )
                per_malas= round((e.malas/e.total)*100 )
                per_neutra=round((e.neutra/e.total)*100)
            else:
                per_buenas=0
                per_malas= 0
                per_neutra=0
            medio=e.medio
            diccionario_porcentajes = {'medio':medio, 'per_buenas':per_buenas, 'per_malas':per_malas, 'per_neutra':per_neutra  }
            lista_porcentajes.append(diccionario_porcentajes)

        for e in analisis_general:
            buenas=round((e.buenas/e.total)*100 )
            malas= round((e.malas/e.total)*100 )
            neutra=round((e.neutra/e.total)*100)
            diccionario_porcentajes = {'buenas':buenas, 'malas':malas, 'neutra':neutra  }
            lista_general_porcentajes.append(diccionario_porcentajes)
        context = {'medios':medios, 'medios_diarios':medios_diarios , 'fecha':fecha, 'analisis_diarios':analisis_diarios, 'analisis_general':analisis_general, 'lista_porcentajes':lista_porcentajes ,'lista_general_porcentajes':lista_general_porcentajes ,'fecha_actual':fecha_actual}
        return render(request, 'mediaReview_app/medios_diario.html',context)

#mostrar datos de un medio para un periodo de tiempo 
def medio_periodo(request,medio):
    fecha_actual = datetime.now().date()
    fechas_periodo = [fecha_actual - timedelta(days=dia) for dia in range(10)]
    fechas_ultimos_10_dias = [str(fecha_actual - timedelta(days=dia)) for dia in range(10)]
    fechas_ultimos_10_dias.reverse()
    fecha_str = str(datetime.today())
    fecha, marca_tiempo = fecha_str.split(' ')
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
    #crear un objeto que 
    lista_positivo=list()
    lista_negativo=list()
    lista_scraping= list()
    medio = Medio.objects.get(id=medio)
    for f in fechas_ultimos_10_dias:
        try:
            fecha_obj = datetime.strptime(f, '%Y-%m-%d').date()
            analisis_diario_obj = AnalisisDiario.objects.get(medio=medio,fecha=fecha_obj)
            positivas= round((analisis_diario_obj.buenas/analisis_diario_obj.total)*100)
            lista_positivo.append(positivas)
            negativas= round((analisis_diario_obj.malas/analisis_diario_obj.total)*100)
            lista_negativo.append(negativas)
            lista_scraping.append(analisis_diario_obj.data_scraping)
        except:
            lista_positivo.append(0)
            lista_negativo.append(0)
            lista_scraping.append(0)
    
    context={'fechas_periodo':fechas_periodo, 'fechas_ultimos_10_dias_json': json.dumps(fechas_ultimos_10_dias)  ,'lista_positivas_json':json.dumps(lista_positivo) , 'lista_negativas_json':json.dumps(lista_negativo), 'lista_scraping_json':json.dumps(lista_scraping) ,'medio':medio }
    return render(request, 'mediaReview_app/medio_periodo.html',context)

#mostrar analisis general en un periodo
def general_periodo(request):
    fecha_actual = datetime.now().date()
    fechas_periodo = [fecha_actual - timedelta(days=dia) for dia in range(10)]
    fechas_ultimos_10_dias = [str(fecha_actual - timedelta(days=dia)) for dia in range(10)]
    fechas_ultimos_10_dias.reverse()
    fecha_str = str(datetime.today())
    fecha, marca_tiempo = fecha_str.split(' ')
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
    #crear un objeto que 
    lista_positivo=list()
    lista_negativo=list()
    for f in fechas_ultimos_10_dias:
        try:
            fecha_obj = datetime.strptime(f, '%Y-%m-%d').date()
            analisis_general_obj = AnalisisGeneral.objects.get(fecha=fecha_obj)
            positivas= round((analisis_general_obj.buenas/analisis_general_obj.total)*100)
            lista_positivo.append(positivas)
            negativas= round((analisis_general_obj.malas/analisis_general_obj.total)*100)
            lista_negativo.append(negativas)
        except:
            lista_positivo.append(0)
            lista_negativo.append(0)
    
    context={'fechas_periodo':fechas_periodo, 'fechas_ultimos_10_dias_json': json.dumps(fechas_ultimos_10_dias)  ,'lista_positivas_json':json.dumps(lista_positivo) , 'lista_negativas_json':json.dumps(lista_negativo) }
    return render(request, 'mediaReview_app/general_periodo.html',context)

#mostrar detalle de noticias para un dia - medio
def detalle_diario(request,fecha,medio):
    medio_obj = Medio.objects.get(id=medio)
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
    medio_diario_obj = MedioDiario.objects.get(fecha=fecha_obj,medio=medio)
    noticias = Noticia.objects.filter(medio_diario=medio_diario_obj)
    lista_noticias_completa = list()
    for n in noticias:
        try:
            respuesta = DeterminacionIa.objects.filter(noticia = n)
            if(len(respuesta)> 0):
                respuesta = respuesta[0]
            else:
                respuesta = ""
            dic = {'noticia':n , 'respuesta':respuesta }
            lista_noticias_completa.append(dic)
        except:
            True
    context = {'noticias':noticias, 'medio':medio, 'fecha':fecha , 'medio_obj':medio_obj, 'lista_noticias_completa':lista_noticias_completa }
    return render(request, 'mediaReview_app/detalle_diario.html',context)


def proyecto(request):
    return render(request, 'mediaReview_app/proyecto.html')
