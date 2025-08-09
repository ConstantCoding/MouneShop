from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('hommes/', views.hommes, name="hommes"),
    path('femmes/', views.femmes, name = "femmes"),
    path('enfants/', views.enfants, name = "enfants"),
    path('boutique/', views.boutique, name = "boutique"),
    path('nouveautés/', views.nouveautes, name = "nouveautes"),
    path('contact/', views.contact, name = "contact"),
    path('login/', views.login_store, name = "login_store"),
    path('register/', views.register_store, name = "register_store"),
    path('details/<int:id_produit>/', views.detail_produit, name = "detail_produit"),
    path('panier/', views.voir_panier, name = "voir_panier"),
    path('ajouter_panier/<int:id_produit>/', views.ajouter_panier, name = "ajouter_panier"),
    path("supprimer-du-panier/<int:id_produit>/", views.supprimer_du_panier, name = "supprimer_du_panier"),
    path('vider-panier/', views.vider_panier, name = "vider_panier"),
    path('commander/', views.passer_commande, name = 'passer_commande'),
    path("boutique-ajax/", views.boutique_ajax, name = "boutique_ajax"),
    path("recherche/", views.recherche_boutique, name = "recherche_boutique"),
    path("utilisateur/", views.detail_utilisateur, name = "detail_utilisateur")
]