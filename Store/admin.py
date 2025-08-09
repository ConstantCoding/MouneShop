from django.contrib import admin
from .models import *

class AdminCarrouselsItems(admin.ModelAdmin):
    list_display = ('car_item_name', 'car_item_description', 'car_item_image', 'carrousel', 'car_item_categorie', 'carrousel_id')

class AdminCarrousels(admin.ModelAdmin):
    list_display = ('carrousel_name', 'carrousel_title', 'carrousel_id')

class AdminSections(admin.ModelAdmin):
    list_display = ('section_id','section_title', 'section_name', 'section_slogan')

class AdminSectionItems(admin.ModelAdmin):
    list_display = ('sections_items_id','item_name', 'item_image', 'optional_text', 'item_position', 'section')

class AdminProduits(admin.ModelAdmin):
    list_display = ('nom_produit', 'description_produit', 'categorie', 'prix_produit', 'texte_optionnel', 'quantite_produit')

class AdminImagesProduits(admin.ModelAdmin):
    list_display = ('image_produit', 'id_produit')

class AdminCategorie(admin.ModelAdmin):
    list_display = ('nom_categorie',)

admin.site.register(Carrousels, AdminCarrousels)
admin.site.register(Carrouselsitems, AdminCarrouselsItems)
admin.site.register(Sections, AdminSections)
admin.site.register(Sectionitems, AdminSectionItems)
admin.site.register(Produits, AdminProduits)
admin.site.register(ImagesProduits, AdminImagesProduits)
admin.site.register(Categories, AdminCategorie)
admin.site.register(Commandes)