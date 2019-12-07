from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webpage-home'),
    path('globals/', views.globals, name='webpage-globals'),
    path('finance/', views.finance, name='webpage-finance'),
    path('sales/', views.sales, name='webpage-sales'),
    path('hr/', views.hr, name='webpage-hr'),
    path('engineering/', views.engineering, name='webpage-engineering'),
]
