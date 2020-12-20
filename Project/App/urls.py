from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from .views import *
urlpatterns = [
    
    path('', Home , name= 'Home'),
    path('login', loginfun ,name='login'),
    path('cregi',custregi,name='cregi'),
    path('sregi',supregi,name='sregi'),
    path('Product', product , name= 'Product'),
    path('OrderThis/<int:pid>', chart , name= 'chart'),
    path('view', viewproduct , name= 'view'),
    path('Addrese/<int:oid>',addrese,name='addrese'),
    path('payment/<int:oid>',payment,name='payment'),
    path('order/<int:oid>/<int:ad>',order,name='order'),
    path('finshed/<int:pid>',finshed,name='finshed'),
    path('logout',logoutfun,name='logout'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)