from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Carrousels(models.Model):
    carrousel_id = models.AutoField(primary_key=True)
    carrousel_title = models.CharField(max_length=150, blank=True, null=True)
    carrousel_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.carrousel_name

class Carrouselsitems(models.Model):
    carrousel_item_id = models.AutoField(primary_key=True)
    car_item_name = models.CharField(max_length=60, blank=True, null=True)
    car_item_description = models.CharField(max_length=300, blank=True, null=True)
    car_item_image = models.ImageField(upload_to='carrousels_images/')
    carrousel = models.ForeignKey(Carrousels, models.DO_NOTHING)
    car_item_categorie = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.car_item_name != None:
            return self.car_item_name
        else:
            return self.car_item_description


class Produits(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom_produit = models.CharField(max_length=80)
    description_produit = models.CharField(max_length=1000, blank=True, null=True)
    categorie = models.CharField(max_length=50, blank=True, null=True)
    prix_produit = models.IntegerField()
    texte_optionnel = models.CharField(max_length=200, blank=True, null=True)
    quantite_produit = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nom_produit
    def get_absolute_url(self):
        return reverse('produit_detail', args=[self.id_produit])

class ImagesProduits(models.Model):
    id_image_produit = models.AutoField(primary_key=True)
    image_produit = models.ImageField(upload_to='produits_images/')
    id_produit = models.ForeignKey('Produits', models.CASCADE, db_column='id_produit', related_name='images')


class Sections(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_title = models.CharField(max_length=255, blank=True, null=True)
    section_slogan = models.CharField(max_length=1000, blank=True, null=True)
    section_name = models.CharField(max_length=100)

    def __str__(self):
        return self.section_name

class Sectionitems(models.Model):
    sections_items_id = models.AutoField(primary_key=True)
    optional_text = models.CharField(max_length=1000, blank=True, null=True)
    item_position = models.IntegerField(blank=True, null=True)
    item_image = models.ImageField(upload_to='sections_images/')
    section = models.ForeignKey('Sections', models.CASCADE)
    item_name = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        if self.item_name != None:
            return self.item_name
        else:
            return "Pas de nom"

class Categories(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=50)
    id_produit = models.ForeignKey('Produits', models.DO_NOTHING, db_column='id_produit', blank=True, null=True)
    carrousel_item = models.ForeignKey(Carrouselsitems, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nom_categorie

class Commandes(models.Model):
    id_commande = models.AutoField(primary_key=True)
    produit = models.ForeignKey(Produits, models.CASCADE, db_column='produit')
    utilisateur = models.ForeignKey(User, models.DO_NOTHING, db_column='utilisateur')
    date_commande = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveIntegerField()
    total = models.FloatField()
    statut_commande = models.CharField(max_length=50)

    def __str__(self):
        return f"commande de {self.utilisateur.username} - {self.produit.nom_produit}"
