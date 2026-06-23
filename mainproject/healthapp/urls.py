from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import MyLoginView

app_name = 'healthapp'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('healthapp/', views.index, name='index'),
    path('healthapp/predict/', views.predict, name='predict'),
    path('healthapp/predict2/', views.predict2, name='predict2'),
    path('healthapp/BMIc/', views.BMIc, name='BMIc'),
    path('healthapp/survey/', views.survey, name='survey'),
    path('healthapp/survey2/', views.survey2, name='survey2'),
    path('healthapp/contact/', views.contact_view, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
