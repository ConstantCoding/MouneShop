from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q

@login_required(login_url='login_store')
def ajouter_panier(request, id_produit):
    produit = get_object_or_404(Produits, id_produit = id_produit)
    quantite = int(request.POST.get('quantite', 1))

    image_obj = produit.images.first()
    image_url = image_obj.image_produit.url

    panier = request.session.get('panier', {})
    if str(id_produit) in panier:
        panier[str(id_produit)]['quantite'] += quantite
    else:
        panier[str(id_produit)] = {
            'nom':produit.nom_produit,
            'prix': float(produit.prix_produit),
            'image': image_url,
            'quantite': quantite
        }
    request.session['panier'] = panier
    request.session.modified = True
    return redirect('voir_panier')

def index(request):
    context_index = {
        #Sections
        "landing": Sections.objects.get(section_id = 1),
        "landing_items":Sectionitems.objects.get(sections_items_id = 1),
        "img_accueil_1": Sectionitems.objects.filter(section_id = 2).order_by('item_position'),
        "img_accueil_2": Sections.objects.get(section_id = 3),
        "img_accueil_2_item": Sectionitems.objects.get(section_id = 3),
        #Carrousels
        "car_classique":Carrousels.objects.get(carrousel_id =1),
        "car_classique_items": Carrouselsitems.objects.filter(carrousel_id = 1),
        "panier" : request.session.get('panier', {})
    }

    return render(request, "Store/index.html", context_index)

def hommes(request):
    context_homme = {
        #Sections
        "landing_homme": Sections.objects.get(section_id=4),
        "landing_item_homme": Sectionitems.objects.filter(section_id=4).order_by('item_position'),
        "ldg_homme_text": Sectionitems.objects.filter(section_id=4).order_by('item_position').first(),
        "sportifs_choice": Sections.objects.get(section_id = 5),
        "sportifs_choice_item": Sectionitems.objects.filter(section_id=5).order_by('item_position'),
        "incontournable_sport_homme":Sections.objects.get(section_id = 6),
        "incontournable_item": Sectionitems.objects.filter(section_id=6).order_by('item_position'),
        "pop_homme": Sections.objects.get(section_id=7),
        "pop_homme_item":Sectionitems.objects.filter(section_id = 7).order_by('item_position'),
        #Carrousels
        "car_classique":Carrousels.objects.get(carrousel_id =1),
        "car_classique_items": Carrouselsitems.objects.filter(carrousel_id = 1),
        "car_homme": Carrousels.objects.get(carrousel_id = 2),
        "car_homme_item": Carrouselsitems.objects.filter(carrousel_id=2),
        "panier" : request.session.get('panier', {})
    }
    return render(request, "Store/hommes.html", context_homme)

def femmes(request):
    context_femme = {
        #Sections
        "landing_femme": Sections.objects.get(section_id=8),
        "landing_femme_item": Sectionitems.objects.filter(section_id=8).order_by('item_position'),
        "mode_femmes": Sections.objects.get(section_id=9),
        "mode_femmes_item":Sectionitems.objects.raw("SELECT * FROM Sectionitems WHERE section_id = %s LIMIT 2", [9]),
        "mode_femmes_item2":Sectionitems.objects.raw("SELECT * FROM Sectionitems WHERE section_id = %s AND item_position > %s",[9,2]),
        "explore_femmes": Sections.objects.get(section_id = 10),
        "explore_femmes_items":Sectionitems.objects.filter(section_id=10).order_by('item_position'),
        #Carrousels
        "car_classique":Carrousels.objects.get(carrousel_id =1),
        "car_classique_items": Carrouselsitems.objects.filter(carrousel_id = 1),
        "car_femme1": Carrousels.objects.get(carrousel_id = 3),
        "car_femme1_item": Carrouselsitems.objects.filter(carrousel_id=3),
        "car_femme2": Carrousels.objects.get(carrousel_id=4),
        "car_femme2_item": Carrouselsitems.objects.filter(carrousel_id=4),
        "panier" : request.session.get('panier', {})
    }
    return render(request, "Store/femmes.html", context_femme)

def enfants(request):
    context_enfants = {
        #sections
        "landing_enfants": Sections.objects.get(section_id=11),
        "landing_enfants_items": Sectionitems.objects.filter(section_id=11).order_by('item_position'),
        "a_la_une":Sections.objects.get(section_id=12),
        "a_la_une_item":Sectionitems.objects.filter(section_id=12).order_by('item_position'),
        #carrousels
        "car_classique": Carrousels.objects.get(carrousel_id =1),
        "car_classique_items": Carrouselsitems.objects.filter(carrousel_id = 1),
        "per_age": Carrousels.objects.get(carrousel_id=5),
        "per_age_item": Carrouselsitems.objects.filter(carrousel_id=5),
        "car_pop": Carrousels.objects.get(carrousel_id = 6),
        "car_pop_item": Carrouselsitems.objects.filter(carrousel_id=6),
        "panier" : request.session.get('panier', {})
    }
    return render(request, "Store/enfants.html", context_enfants)

def boutique_ajax(request):
    offset = int(request.GET.get('offset', 0))
    limit = 6
    produits = Produits.objects.prefetch_related('images').all()[offset:offset+limit]
    produits_data = []
    for produit in produits:
        produits_data.append({
            "id":produit.id_produit,
            "nom": produit.nom_produit,
            "prix": produit.prix_produit,
            "description":produit.description_produit,
            "categorie":produit.categorie,
            "image":produit.images.first().images_produit.url
        })
    return JsonResponse({"produits":produits_data})

def boutique(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        offset = int(request.GET.get("offset", 0))
        limit = int(request.GET.get("limit", 6))
        produits = list(Produits.objects.prefetch_related('images').all()[offset:offset+limit])
        
        produits_data = []
        for produit in produits:
            produits_data.append({
                "id": produit.id_produit,
                "nom": produit.nom_produit,
                "description": produit.description_produit,
                "prix": produit.prix_produit,
                "categorie": str(produit.categorie),
                "image": produit.images.first().image_produit.url if produit.images.first() else None
            })
        return JsonResponse({"produits": produits_data})

    # Chargement initial
    context_boutique = {
        "produits": Produits.objects.prefetch_related('images').all()[:6],
        "categories": Categories.objects.all(),
        "panier": request.session.get('panier', {})
    }
    return render(request, "Store/boutique.html", context_boutique)

def recherche_boutique(request):
    query = request.GET.get('query', '').strip()
    if query:
        produit = Produits.objects.filter(Q(nom__icontains = query)).first()
        if produit:
            return redirect(produit.get())
        else:
            messages.error(request, "Aucun produit trouvé !")
            return redirect('boutique')
        
    return redirect('boutique')

def nouveautes(request):
    context_nouveau = {
        "produits":Produits.objects.prefetch_related('images').all,
        "categories": Categories.objects.all(),
        "panier" : request.session.get('panier', {})
    }
    return render(request, "Store/nouveau.html", context_nouveau)

def contact(request):
    panier = request.session.get('panier', {})
    return render(request, "Store/contact.html", {"panier":panier})

User = get_user_model()

def login_store(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)

            user = authenticate(request, username = user_obj.username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('index')
            else:
                messages.error(request, "email ou mot de passe incorrect")
        except User.DoesNotExist:
                messages.error(request, "Aucun utilisateur avec cet email")

    context_login = {
        "background":Sectionitems.objects.get(section_id=13),
        "panier" : request.session.get('panier', {})
    }
    return render(request, "Store/login.html", context_login)

def register_store(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('last_name')
        last_name = request.POST.get('first_name')
        username = first_name + last_name
        if User.objects.filter(username=username).exists():
            messages.error(request, "Nom d'utilisateur déja pris")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Cet email existe déjà")
        elif len(password) < 6:
            messages.error(request, "votre mot de passe est trop court")
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, "Creation de compte réussi")
            return redirect('login_store')

    context_register = {
        "background":Sectionitems.objects.get(section_id=13),
        "panier" : request.session.get('panier', {})
    }
    return render(request, "Store/register.html", context_register)

def detail_produit(request, id_produit):
    produits = get_object_or_404(Produits, id_produit = id_produit)
    images = produits.images.all()
    context = {
        "produit":produits,
        "images": images,
        "panier" : request.session.get('panier', {})
    }
    return render(request, "Store/detail_produit.html", context)



def voir_panier(request):
    panier = request.session.get('panier', {})

    total = sum(item['prix'] * item['quantite'] for item in panier.values())
    return render(request, "Store/panier.html", {'panier':panier, "total":total})

def supprimer_du_panier(request, id_produit):
    panier = request.session.get('panier', {})
    id_produit_str = str(id_produit)
    if id_produit_str in panier:
        del panier[id_produit_str]
        request.session['panier'] = panier
        request.session.modified = True
        return redirect('voir_panier')

def vider_panier(request):
    request.session['panier'] = {}
    return redirect('boutique')

@login_required(login_url='login_store')
def passer_commande(request):
    panier = request.session.get('panier', {})
    if not panier:
        messages.warning(request, "votre panier est vide")
        return redirect('boutique')
    for id_produit, details in panier.items():
        try:
            produit = Produits.objects.get(pk = id_produit)
        except Produits.DoesNotExist:
            messages.error(request, f"Produit ID {id_produit} introuvable")
            continue
        quantite_demandee = details['quantite']
        if produit.quantite_produit is None or produit.quantite_produit < quantite_demandee:
            messages.error(request, f"Stock insuffisant pour {produit.nom_produit}")
            return redirect('voir_panier')
        produit.quantite_produit -= quantite_demandee
        produit.save()
        Commandes.objects.create(produit = produit, utilisateur = request.user, quantite = quantite_demandee, total = quantite_demandee * produit.prix_produit, statut_commande = "en cours")
        request.session['panier'] = {}
        messages.success(request, "Commande passée avec succès")
        return redirect('voir_panier')
    
def detail_utilisateur(request):
    context_user = {
        "user":request.user
    }
    return render(request, "Store/detail_utilisateur.html", context_user)