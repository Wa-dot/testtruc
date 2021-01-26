#!/usr/bin/env python

# exemple boutons.py

import pygtk
pygtk.require('2.0')
import gtk

# On crée une boite verticale, on y place une image 
# et une étiquette, et on renvoie la boite.

def boite_xpm_etiquette(parent, fichier_xpm, texte_etiquette):
    # On crée une boite pour la pixmap et l'étiquette
    boite1 = gtk.HBox(False, 0)
    boite1.set_border_width(2)

    # A présent l'image.
    image = gtk.Image()
    image.set_from_file(fichier_xpm)

    # On crée une étiquette pour le bouton.
    etiquette = gtk.Label(texte_etiquette)

    # On place la pixmap et l'étiquette dans la boite.
    boite1.pack_start(image, False, False, 3)
    boite1.pack_start(etiquette, False, False, 3)

    image.show()
    etiquette.show()
    return boite1

class Bouton:
    # Notre méthode de rappel habituelle.
    def salut(self, widget, donnees=None):
        print "Salut ! - Clic sur le %s." % donnees

    def __init__(self):
        # Création d'une nouvelle fenêtre.
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.fenetre.set_title("Bouton et image")

        # C'est une bonne idée de faire ceci pour chaque fenêtre.
        self.fenetre.connect("destroy", lambda wid: gtk.main_quit())
        self.fenetre.connect("delete_event", lambda a1,a2: gtk.main_quit())

        # On fixe la largeur des bordures de la fenêtre.
        self.fenetre.set_border_width(10)

        # Création d'un nouveau bouton.
        bouton = gtk.Button()

        # On connecte le signal "clicked" du bouton à la fonction de rappel
        bouton.connect("clicked", self.salut, "bouton cool")

        # Ceci appelle notre fonction de création de boites.
        boite1= boite_xpm_etiquette(self.fenetre, "info.xpm", "bouton cool")

        # On place et on affiche tous nos widgets.
        bouton.add(boite1)

        boite1.show()
        bouton.show()

        self.fenetre.add(bouton)
        self.fenetre.show()

def main():
    gtk.main()
    return 0     

if __name__ == "__main__":
    Bouton()
    main()