from django.urls import path
from . import views

urlpatterns = [
    # Definir las rutas y asociarlas con las vistas correspondientes
    path('', views.index, name='index'),
    path('medios_diario/<str:fecha>/', views.analisis_medios, name='analisis_medios'),
    path('detalle_diario/<str:fecha>/<int:medio>', views.detalle_diario, name='detalle_diario'),
    path('medio_periodo/<int:medio>', views.medio_periodo, name='medio_periodo'),
    path('general_periodo/', views.general_periodo, name='general_periodo'),
    path('proyecto/', views.proyecto, name='proyecto'),
]
