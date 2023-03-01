from django.urls import path
from . import views

app_name = 'ali'

urlpatterns = [
    path('', views.link),
    path('sunday', views.index, name='iman'),
    path('<int:id>', views.dynamic, name='dynamic'),
    path('monday', views.test_redirect)
]
