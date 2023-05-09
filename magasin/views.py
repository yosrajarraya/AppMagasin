from django.shortcuts import redirect, render
from .models import Produit
from django.shortcuts import render, redirect, get_object_or_404
from .models import Fournisseur
from .forms import ProduitForm, FournisseurForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def index(request):
       if request.method == "POST" :
         form = ProduitForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              list=Produit.objects.all()
              return render(request,'magasin/vitrine.html',{'list':list})
       else : 
            form = ProduitForm()
            list=Produit.objects.all()
            return render(request,'magasin/majProduits.html',{'form':form,'list':list})

def indexA(request):
     return render(request,'magasin/acceuil.html' )


def indexF(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'magasin/mesFournisseurs.html', context)

def nouveauFournisseur(request):
    if request.method == "POST" :
         form = FournisseurForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              nouvFournisseur=Fournisseur.objects.all()
              return render(request,'magasin/vitrineF.html',{'nouvFournisseur':nouvFournisseur})
    else : 
            form = FournisseurForm() #créer formulaire vide 
            nouvFournisseur=Fournisseur.objects.all()
            return render(request,'magasin/fournisseur.html',{'form':form,'nouvFournisseur':nouvFournisseur})
    

def update_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'magasin/update_fournisseur.html', {'form': form})

def Catalogue(request):
        products= Produit.objects.all()
        context={'products':products}
        return render( request,'magasin/mesProduits.html',context )


def update_produit(request, id):
    # Récupérer le produit existant à modifier
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        # Créer un formulaire avec les données du produit existant
        form = ProduitForm(request.POST or None, request.FILES or None, instance=produit)
        if form.is_valid():
            # Enregistrer les modifications dans la base de données
            form.save()
            return redirect('Catalogue')
    else:
        # Pré-remplir le formulaire avec les données du produit existant
        form = ProduitForm(instance=produit)
    return render(request, 'magasin/update_produit.html', {'form': form})


def delete_produit(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Catalogue')
    return render(request, 'magasin/delete_produit.html', {'product': product})


def delete_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('fournisseurs')
    return render(request, 'magasin/delete_fournisseur.html', {'fournisseur': fournisseur})

def register(request):
     if request.method == 'POST' :
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = authenticate(username=username, password=password)
               login(request,user)
               messages.success(request, f'Coucou {username}')
               return redirect('home')
     else :
          form = UserCreationForm()
     return render(request,'registration/register.html',{'form' : form})