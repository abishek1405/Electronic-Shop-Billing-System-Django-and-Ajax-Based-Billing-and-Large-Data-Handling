"""bill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from billapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('proo/',views.seldail),
    path('de/<id>/',views.delete_view),
    path('hardup/<id>/',views.hardup),
    path('elecup/<id>/',views.elecup),
    path('plumup/<id>/',views.plumup),
    path('hardde/<id>/',views.hardde),
    path('elecde/<id>/',views.elecde),
    path('plumde/<id>/',views.plumde),
    path('deq/<id>/',views.delete_v),
    path('upq/<id>/',views.upd),
    path('bdeq/<id>/',views.delete_b),
    path('bupq/<id>/',views.upb),
    path('ade/',views.dall),
    path('bade/',views.bdall),
    path('cout/',views.cout),
    path('bcout/',views.bcout),
    path('pri/',views.pri),
    path('bpri/',views.bpri),
    path('perdet/',views.perdet),
    path('bperdet/',views.bperdet),
    path('det/<id>',views.det),
    path('overdel/<id>',views.overdel),
    path('bill2/',views.bill2),
    path('bill2ed/<id>',views.billed),
    path('bhis/<id>',views.bhis),
    path('htotd/<id>',views.htotd),
    path('overalldel/<id>',views.overalldel),
    path('eror/',views.eror),
    path('prolis/',views.prolis),
    path('predictclear/',views.predictclear),
    path('bpredictclear/',views.bpredictclear),
    path('elec/',views.elec),
    path('plum/',views.plum),
    path('hard/',views.hard),
    path('newbill/',views.newbil),
    path('get-product-details/', views.get_product_details, name='get_product_details'),
    path('bget-product-details/', views.bget_product_details, name='bget_product_details'),
    path('bget-product-details/', views.bget_product_details ),
    path('stock/',views.billing_form),
    path('list/', views.billing_list, name='billing_list'),
    path('totout/',views.out),
    # path('filter-by-amount/',views.filter_by_amount_view, name='filter_by_amount_view'),
    # path('filter-by-date/', views.filter_by_date_view, name='filter_by_date_view'),
    path('stockout/',views.stockout),
    path('tigall/',views.tigall),
    path('rowpage/<id>',views.rowpage),
    path('row/<id>', views.rodel),
    path('maap/',views.cusmap),
    path('bmaap/',views.bcusmap),

]
