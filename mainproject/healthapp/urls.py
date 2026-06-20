from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'healthapp'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('healthapp/', views.index, name='index'),
    path('healthapp/predict', views.predict, name='predict')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
