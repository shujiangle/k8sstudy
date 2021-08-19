from django.urls import path
from . import views

app_name = 'k8shost'

urlpatterns = [
    path('', views.hostinfor, name='hostinfor'),
    path('pods', views.pods, name='pods')
]
