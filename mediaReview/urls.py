from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mediaReview_app.urls')),  # Reemplaza 'miapp' con el nombre de tu aplicación
    # Otras rutas del proyecto
]
