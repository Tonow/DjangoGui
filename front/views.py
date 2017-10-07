from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect
from .forms import ContacteForm

# Create your views here.

def acceuil(request):
    """
    Renvoie a l'acceui
    """
    return render(request, 'front/acceuil.html', locals())


def coordonnees(request):
    """
    Renvoie au coordonder
    """
    return render(request, 'front/coordonnees.html', locals())


def contact(request):
    """
    Traite un formulaire de contacte
    """
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContacteForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        post = form.save(commit=False)
        post.save()
        return redirect(formsOk)

    else:
        form = ContacteForm(request.POST or None)

    return render(request, 'front/contact.html', {'form': form})


def formsOk(request):
    """
    Renvoie un message de validation du formulaire
    """
    return render(request, 'front/formsOk.html', locals())


def view_404(request):
    """
    Doit rediriger toute les 404 vers l'acceuil
    """

    return redirect('home')
