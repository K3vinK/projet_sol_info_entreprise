from django.urls import path 
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('machines/', views.machine_list_view, name='machines'),
    path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
    path('add-machine/', views.machine_add_form, name='add-machine'),

    path('', views.index, name='index'),
    path('personnes/', views.personne_list_view, name='personnes'),
    path('personne/<pk>', views.personne_detail_view, name='personne-detail'),
    path('add-personne/', views.person_add_form, name='add-personne'),


    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
]
