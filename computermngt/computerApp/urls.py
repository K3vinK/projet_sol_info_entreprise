from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('machines/', views.machine_list_view, name='machines'),
    path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
    path('add-machine/', views.machine_add_form, name='add-machine'),

    path('personnes/', views.personne_list_view, name='personnes'),
    path('personne/<pk>', views.personne_detail_view, name='personne-detail'),
    path('add-personne/', views.person_add_form, name='add-personne'),

    path('del-machine', views.delete_machine, name='del-machine'),
    path('del-personne', views.delete_personne, name='del-personne'),

]



