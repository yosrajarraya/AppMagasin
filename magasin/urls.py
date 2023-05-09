from django.urls import path
from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('products/', views.index, name='index'),
    path('', views.indexA, name='indexA'),
    path('fournisseurs/', views.indexF, name='fournisseurs'),
    path('Catalogue/', views.Catalogue, name='Catalogue'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouvFournisseur'),
    path('fournisseurs/<int:pk>/update/', views.update_fournisseur, name='update_fournisseur'),
    path('fournisseurs/<int:pk>/delete/', views.delete_fournisseur, name='delete_fournisseur'),
    path('produit/modifier/<int:id>/', views.update_produit, name='update_produit'),
    path('delete/<int:pk>/', views.delete_produit, name='delete_produit'),
    path('register/',views.register, name = 'register'), 
]