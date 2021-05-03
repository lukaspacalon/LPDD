
# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
#Created by Lukas Pacalon
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques

import source
import personnage
import bibliotheque
import joueur
import objet
import lieu
import quete
import infrastructure

import cmd
import textwrap
import sys
import os
import sched, time
import random
from random import choice
import pickle
import inspect
import datetime
from datetime import timedelta
from pathlib import Path
import smtplib, ssl
import json
# import discussion_amant
# import discussion_ami
# import discussion_base
# import discussion_chef
# import discussion_inconnu
# import discussion_relation
# import discussion_rival
# import discussion_serviteur
from collections import defaultdict
from operator import itemgetter

import pygame
window_resolution = (500, 500)
launched = True
white = (255, 255, 255)
pygame.init()
pygame.display.set_caption("Python #42 : jouer du son")
window_surface = pygame.display.set_mode(window_resolution)
arial_font = pygame.font.SysFont("arial", 18)
hello_text_surface = arial_font.render("Bienvenue dans La Plume du Dev", False, white)
window_surface.blit(hello_text_surface, [10, 10])
pygame.mixer.init()
# orage = pygame.mixer.Sound("bande_sonore/atmosphere/orage.ogg")
# voyager = pygame.mixer.Sound("bande_sonore/action/voyager.ogg")
# page = pygame.mixer.Sound("bande_sonore/action/page.ogg")
# inventaire = pygame.mixer.Sound("bande_sonore/action/inventaire.ogg")
# dormir = pygame.mixer.Sound("bande_sonore/action/dormir.ogg")
# mediter = pygame.mixer.Sound("bande_sonore/action/mediter.ogg")
# pecher = pygame.mixer.Sound("bande_sonore/action/pecher.ogg")
# pecher_plouf = pygame.mixer.Sound("bande_sonore/action/pecher_plouf.ogg")
# chasser = pygame.mixer.Sound("bande_sonore/action/chasser.ogg")
# manger_pomme = pygame.mixer.Sound("bande_sonore/action/manger_pomme.ogg")
# jeter = pygame.mixer.Sound("bande_sonore/action/jeter.ogg")
# boire = pygame.mixer.Sound("bande_sonore/action/boire.ogg")
# attaquer = pygame.mixer.Sound("bande_sonore/action/attaquer.ogg")
# mort = pygame.mixer.Sound("bande_sonore/action/mort.ogg")
# peter = pygame.mixer.Sound("bande_sonore/action/peter.ogg")
# uriner = pygame.mixer.Sound("bande_sonore/action/uriner.ogg")
# vomir = pygame.mixer.Sound("bande_sonore/action/vomir.ogg")
# hurler = pygame.mixer.Sound("bande_sonore/action/hurler.ogg")
# chanter = pygame.mixer.Sound("bande_sonore/action/chanter.ogg")
#
# marecage = pygame.mixer.Sound("bande_sonore/creature/grenouilles.ogg")
# serpent = pygame.mixer.Sound("bande_sonore/creature/sifflement-serpent.ogg")
# aigle = pygame.mixer.Sound("bande_sonore/creature/aigle.ogg")
# volcan = pygame.mixer.Sound("bande_sonore/atmosphere/volcan.ogg")
# cerf = pygame.mixer.Sound("bande_sonore/creature/grenouilles.ogg")
# mer = pygame.mixer.Sound("bande_sonore/atmosphere/mer.ogg")
# jungle = pygame.mixer.Sound("bande_sonore/creature/grenouilles.ogg")
# ville = pygame.mixer.Sound("bande_sonore/atmosphere/ville.ogg")
# cariole = pygame.mixer.Sound("bande_sonore/situation/cariole.ogg")
# village = pygame.mixer.Sound("bande_sonore/dialogue/discussion1.ogg")
# feu = pygame.mixer.Sound("bande_sonore/creature/grenouilles.ogg")
# poulailler = pygame.mixer.Sound("bande_sonore/creature/poulailler.ogg")
# vaches = pygame.mixer.Sound("bande_sonore/creature/vaches.ogg")
# feu = pygame.mixer.Sound("bande_sonore/atmosphere/feu.ogg")
# allumage = pygame.mixer.Sound("bande_sonore/atmosphere/allumage.ogg")
# pluie_tente = pygame.mixer.Sound("bande_sonore/atmosphere/pluie_tente.ogg")

# montagne = pygame.mixer.Sound("bande_sonore/action/chanter.ogg")
# desert = pygame.mixer.Sound("bande_sonore/action/chanter.ogg")
# foret = pygame.mixer.Sound("bande_sonore/action/chanter.ogg")
# plaine = pygame.mixer.Sound("bande_sonore/action/chanter.ogg")
# volcan = pygame.mixer.Sound("bande_sonore/action/chanter.ogg")
# foretprofonde = pygame.mixer.Sound("bande_sonore/action/chanter.ogg")
# mer = pygame.mixer.Sound("bande_sonore/action/chanter.ogg")
# jungle = pygame.mixer.Sound("bande_sonore/action/chanter.ogg")

    # foret.play()
    # marecage.play()
    # montagne.play()
    # desert.play()
    # plaine.play()
    # volcan.play()
    # foretprofonde.play()
    # mer
    # jungle
# alchimie = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# crochetage = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# entretien = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# equitation = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# herboristerie = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# furtivite = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# vol_a_la_tire = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# alcool = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# maitre_chien = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# soin = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# marchandage = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# forgeage = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# armure_lourde= pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# armure_legere = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# mental = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# musique = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# tannerie = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# autorite = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# telepathie = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
#
# # Combat
#
# combat = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# deux_mains = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# mains_nues = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# defense = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# arc = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# arbalete = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# pistolet = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# epee = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# massue = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# hache = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# parade = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# bottes = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
#
# Magie
#
# alteration = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# destruction = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# conjuration = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# mysticisme = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# illusion = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
# enchantement = pygame.mixer.Sound("bande_sonore/action/alchimie.ogg")
pygame.display.flip()

vente = False
equipe = []

class Iteration:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = 2 ** self.n
        self.n += 1
        return result

n1 = Iteration()

#Created by Lukas Pacalon

my = None

#print(joueur.sac_joueur[denier].__dict__)



page1 = source.LivreSource(1, 1, "Il était une fois...")
print ("Chapitre {}".format(page1.chapitre))
print ("Page {} :".format(page1.page))
print ("\n   {}".format(source.LivreSource.contenu_page))

#### Title Screen ####
def title_screen_selection():
    option = input("> ")
    if option.lower() in ['jouer', 'nouvelle partie']:
        config_jeu()
    elif option.lower() == "":
        title_screen_selection()
    elif option.lower() == ("charger"):
        charger_jeu()
        for liste_inventaire in joueur.mon_joueur.inventaire_joueur:
                print(liste_inventaire)
    elif option.lower() == ("aide"):
        aide_menu()
    elif option.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
        sys.exit(0)
    while option.lower() not in ['', 'quit', 'exit', 'close', 'nouvelle partie','charger', 'aide', 'quitter', 'jouer']:
        print("Cette commande n'est pas valide.")
        option = input("> ")
        if option.lower() in ['jouer', 'nouvelle partie']:
            config_jeu()
        elif option.lower() == "":
            title_screen_selection()
        elif option.lower() == ("charger"):
            charger_jeu()
        elif option.lower() == ("aide"):
            aide_menu()
        elif option.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
            sys.exit(0)

def title_screen():
    os.system('cls')
    print("####################################")
    print('utilisez ces commandes : jouer (nouvelle partie), charger, aide, quitter')
    print("Created by Lukas Pacalon")
    print("####################################")
    title_screen_selection()

def aide_menu():
    print("####################################")
    print('Tapez bouger puis utilisez haut, bas, gauche, droite pour vous deplacer dans le jeu')
    print("vous pouvez utiliser les commandes suivantes : c, clear, temps, attendre, mediter, dormir, q, quit, exit, close, inventaire, sauvegarder, bouger, travel, walk, quitter, examiner, interact, look, moi, quisuisje")
    print("####################################")
    title_screen_selection()


def joueur_sauvegarder(action):
    destination = generer_monde()
    joueur.mon_joueur.quisuisje()
    #print(joueur.livre_datetime)
    #print(joueur.MyThread.temps(my))
    print("Comment voulez-les vous nommer votre sauvegarde ?")
    sauvegarde_nom = input("> ")
    if sauvegarde_nom.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
        sys.exit(0)
    sauvegarde_nom = sauvegarde_nom + ".data"
    with open("sauvegardes/"+ sauvegarde_nom, "wb") as fic_sauvegarde:
        record = pickle.Pickler(fic_sauvegarde)
        record.dump(joueur.mon_joueur)
        #record.dump(my)

def charger_jeu():
    afficher_sauvegarde()
    print("Quel partie voulez-vous charger ?")
    sauvegarde_charger = input("> ")
    if sauvegarde_charger.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
        sys.exit(0)
    with open("sauvegardes/"+ sauvegarde_charger, "rb") as fic_sauvegarde:
        get_record = pickle.Unpickler(fic_sauvegarde)
        joueur.mon_joueur = get_record.load()
        #my = get_record.load()
    joueur.mon_joueur.quisuisje()
    #print(joueur.livre_datetime)
    #print(joueur.MyThread.temps(my))
    main_jeu_loop()

def afficher_sauvegarde():
    chemin = Path(r'sauvegardes')
    contenu_dossier = os.listdir(chemin)
    print(contenu_dossier)

#### MAP ####

#Created by Lukas Pacalon
#-----------------
#|a1F|a2F|a3F|a4F|
#-----------------
#|b1F|b2F|b3T|b4F|
#-----------------
#|c1P|c2V|c3P|c4P|
#-----------------
#|d1P|d2P|d3P|d4V|
#-----------------
map = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]





def print_localisation():
    print("\n" + "Vous avez bouger en " + joueur.mon_joueur.localisationX  + "/" + joueur.mon_joueur.localisationY )
    print("")
    print('\n' + ('#' * (4 + len(joueur.mon_joueur.localisationX))))
    print('#' + joueur.mon_joueur.localisationX.upper() + '#')
    print('#' + lieu.carte[joueur.mon_joueur.localisationX][lieu.description] + '#')
    print('\n' + ('#' * (4 + len(joueur.mon_joueur.localisationX))))

#Created by Lukas Pacalon

def prompt():
    my = None
    while True and joueur.mon_joueur.mort is False:
        action = input("> ")
        if my == None:
            my = joueur.MyThread()
        #else:
        #    print("Thread is already started.")
        acceptable_actions = ['discours','guide','maison', 'cambrioler', 'marche', 'marcher', 'base', 'tente', 'feu', 'meteo','sonoff', 'sonon', 'quête', 'quetes', 'quete', 'quêtes', 'oreille', 'ecouter', 'sentir', 'furtif', 'imiter', 'danser', 'chanter', 'vomir', 'uriner', 'peter', 'hurler', 'voler','attaquer', 'map', 'voyager',' attaquer','travail','travailler','competence', 'competences', 'ennemi', 'ennemis', 'equipe', 'equipiers', 'habitant', 'habitants', 'engager', 'chasser', 'pecher', 'lieu','test', 'ami', 'amis', 'relation', 'relations', 'serviteur', 'serviteurs', 'commercer', 'parler','aide', 'c', 'clear','temps', 'attendre', 'mediter', 'dormir', 'q', 'quit', 'exit', 'close', 'inventaire', '', 'sauvegarder', 'bouger', 'travel', 'walk', 'quitter', 'examiner', 'interact', 'look', 'moi', 'quisuisje']
        while action.lower() not in acceptable_actions:
            print("Action inconnue, tape 'aide' pour savoir ce que tu peux faire ! \n")
            action = input("> ")
        if action.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
            sys.exit(0)
        elif action.lower() in ['bouger', 'travel', 'walk','voyager', 'marche', 'marcher']:
            joueur_bouger(action.lower())
        elif action.lower() == '':
            prompt()
        elif action.lower() in ['examiner', 'interact', 'look']:
            joueur_examiner(action.lower())
        elif action.lower() in ['quisuisje', 'moi']:
            joueur_quisuisje(action.lower())
        elif action.lower() in ['sauvegarder']:
            joueur_sauvegarder(action.lower())
        elif action.lower() in ['inventaire']:
            # inventaire.play()
            joueur_inventaire(action.lower())
        elif action.lower() in ['dormir']:
            # dormir.play()
            joueur_dormir(action.lower())
        elif action.lower() in ['attendre']:
            joueur_attendre(action.lower())
        elif action.lower() in ['mediter']:
            # mediter.play()
            joueur_mediter(action.lower())
        elif action.lower() in ['temps']:
            joueur_temps(action.lower())
        elif action.lower() in ['aide']:
            joueur_aide(action.lower())
        elif action.lower() in ['parler']:
            joueur_parler(action.lower())
        elif action.lower() in ['commercer']:
            joueur_commercer(action.lower())
        elif action.lower() in ['lieu']:
            joueur_infolieu(action.lower())
        elif action.lower() in ['test']:
            joueur_test(action.lower())
        elif action.lower() in ['engager']:
            joueur_engager(action.lower())
        elif action.lower() in ['chasser']:
            # chasser.play()
            joueur_chasser(action.lower())
        elif action.lower() in ['pecher']:
            pecher_plouf.play()
            # pecher.play()
            joueur_pecher(action.lower())
        elif action.lower() in ['competence', 'competences']:
            joueur_competence(action.lower())
        elif action.lower() in ['habitants', 'habitant']:
            joueur_habitants(action.lower())
        elif action.lower() in ['ami', 'amis']:
            joueur_amis(action.lower())
        elif action.lower() in ['serviteur', 'serviteurs']:
            joueur_serviteurs(action.lower())
        elif action.lower() in ['ennemis', 'ennemi']:
            joueur_ennemis(action.lower())
        elif action.lower() in ['equipe', 'equipiers']:
            joueur_equipe(action.lower())
        elif action.lower() in ['travail', 'travailler']:
            joueur_travailler(action.lower())
        elif action.lower() in ['clean', 'c']:
            joueur_clear(action.lower())
        elif action.lower() in ['attaquer']:
            joueur_attaquer(action.lower())
        elif action.lower() in ['map']:
            joueur_map(action.lower())
        elif action.lower() in ['voler', 'cambrioler']:
            joueur_voler(action.lower())
        elif action.lower() in ['hurler']:
            joueur_hurler(action.lower())
        elif action.lower() in ['peter']:
            joueur_peter(action.lower())
        elif action.lower() in ['uriner']:
            joueur_uriner(action.lower())
        elif action.lower() in ['vomir']:
            joueur_vomir(action.lower())
        elif action.lower() in ['chanter']:
            joueur_chanter(action.lower())
        elif action.lower() in ['danser']:
            joueur_danser(action.lower())
        elif action.lower() in ['imiter']:
            joueur_imiter(action.lower())
        elif action.lower() in ['furtif']:
            joueur_furtif(action.lower())
        elif action.lower() in ['ecouter']:
            joueur_ecouter(action.lower())
        elif action.lower() in ['sentir']:
            joueur_sentir(action.lower())
        elif action.lower() in ['quete', 'quetes', 'quêtes', "quête"]:
            joueur_quete(action.lower())
        elif action.lower() in ["oreille"]:
            joueur_oreille(action.lower())
        elif action.lower() in ["sonoff"]:
            joueur_son_off(action.lower())
        elif action.lower() in ["sonon"]:
            joueur_son_on(action.lower())
        elif action.lower() in ["meteo"]:
            joueur_meteo(action.lower())
        elif action.lower() in ["feu"]:
            joueur_feu(action.lower())
        elif action.lower() in ["tente"]:
            joueur_tente(action.lower())
        elif action.lower() in ["base"]:
            joueur_aide_base(action.lower())
        elif action.lower() in ["maison"]:
            joueur_propriete(action.lower())
        elif action.lower() in ["guide"]:
            joueur_guide(action.lower())
        elif action.lower() in ["discours"]:
            joueur_discours(action.lower())

def joueur_guide(action):
    print("Bonjour, vous êtes sur l'assistant du jeu")
    print("Vous allez être guidé pour une meilleure expérience de jeu !")
    print("")
    print("")
    print("(1) Essayez de tapez les commandes suivantes (une par une) pour comprendre votre situation dans le jeu : ")
    print("a) moi")
    print("b) lieu")
    print("c) temps")
    print("d) inventaire")
    print("")
    print("")
    print("(2) Puis essayez d'interagir avec le monde autour de vous avec les commandes suivantes : ")
    print("a) bouger (puis tapez sud / est / ouest ou nord)")
    print("b) commercer")
    print("c) quete")
    print("d) maison")
    print("e) parler (Verifiez que vous avez installé la version avec le deep learning)")
    print("")
    print("")
    print("(3) Si vous n'avez pas peur d'être un méchant n'hésitez pas à utiliser ces commandes :")
    print("a) voler")
    print("b) attaquer")
    print("")
    print("")
    print("(4) D'autres commandes existent ! S'il n'y a pas d'étoile à côté vous pouvez les utiliser.")
    print("L'étoile signifie que ces fonctionnalités seront actives dans une prochaine version !")
    print("a) Tapez la commande 'base' pour les découvrir !")
    print("b) N'hésitez pas à envoyer un mail à lkcoredo@gmail.com pour suggérer de nouvelles commandes ou actions")



def joueur_aide_base(action):
    print("""

COMMANDE MENU
c clear
q quit exit close quitter
sauvegarder
guide

COMMANDE INFO
temps
lieu
carte*
personnage moi quisuije
inventaire
quete
equipe
ami
ennemi
serviteur
propriete*
royaume*
diplomatie*
(identite, etat, attribut, propriete/possession,*
armure, alignement, competence)*

COMMANDE ACTION BASE
parler
attendre méditer dormir
bouger travel walk
examiner interact look
discours
attaquer*
gifler*
assassiner*
voler*
embrasser*
serrer dans les bras*
serrer la main*
commercer
engager
provoquer*
hurler*
chanter*
danser*
imiter*
murmurer*

CUSTOM
custom : suggerer une nouvelle action*

""")

def joueur_discours(action):
    print("Vous vous placez au point centrale pour être le mieux entendu et vous déclarez de vive voix : ")
    discours = input("> ")

    print("Personne ne vous écoute...")

def joueur_propriete(action):
    destination = generer_monde()
    print("Voici la liste de vos propriétés dans ce lieu :")
    x = 0
    for value in destination.propriete_joueur:
        print("{} : ".format(x), end='')
        print(value.__dict__['nom'], end=' ')
        print(value.__dict__['localisationX'], end=' ')
        print(value.__dict__['localisationY'], end=' ')
        print(value.__dict__['emplacementX'], end=' ')
        print(value.__dict__['emplacementY'])
        x = x + 1

    print("")
    print("")
    print("Voici la liste de vos propriétés :")
    x = 0
    for value in joueur.mon_joueur.infrastructure:
        print("{} : ".format(x), end='')
        print(value.__dict__['nom'], end=' ')
        print(value.__dict__['localisationX'], end=' ')
        print(value.__dict__['localisationY'], end=' ')
        print(value.__dict__['emplacementX'], end=' ')
        print(value.__dict__['emplacementY'])
        x = x + 1

    cible = input("Souhaitez-vous rentrer dans une de vos propriété dans ce lieu ? (numero_propriete/non)")
    if cible == "non":
        pass
    else:
        cible_int = int(cible)
        print(destination.propriete_joueur[cible_int].__dict__['nom'])
        fouiller = True
        while fouiller == True:
            x = 0
            for value in destination.propriete_joueur[cible_int].meuble:
                print("{} : ".format(x), end='')

                print(value.nom)
                x = x + 1
            chercher_maison = input("Souhaitez vous regarder dans un de vos meubles ? (numero_meuble/non)")
            if chercher_maison == "non":
                fouiller = False
            else:
                fouiller_meuble = True
                while fouiller_meuble == True:
                    x = 0
                    chercher_maison_int = int(chercher_maison)
                    for value in destination.propriete_joueur[cible_int].meuble[chercher_maison_int].contenant:
                        print("{} : ".format(x), end='')
                        print(value.nom)
                        x = x + 1
                    chercher_meuble = input("Souhaitez vous prendre un objet ? (numero_objet/non)")
                    if chercher_meuble == "non":
                        fouiller_meuble = False
                        deposer_objet = True
                        while deposer_objet == True:
                            x = 0
                            for i, k in enumerate(objet.sac_joueur.inside):
                                print(i, k, end=' ')
                                quantite_objet = len(tuple(objet.sac_joueur.inside.items())[x][1])
                                print("({})".format(quantite_objet))
                                x = x + 1
                            deposer_meuble = input("Souhaitez vous deposer un objet ? (numero_objet/non)")
                            if deposer_meuble == "non":
                                deposer_objet = False
                            else:
                                deposer_meuble_int = int(deposer_meuble)
                                objet_a_lindice = tuple(objet.sac_joueur.inside.items())[deposer_meuble_int][1]
                                print(tuple(objet.sac_joueur.inside.items())[deposer_meuble_int][1][0])
                                destination.propriete_joueur[cible_int].meuble[chercher_maison_int].contenant.append(objet_a_lindice)
                                objet.sac_joueur.retirer(objet_a_lindice[0])
                    else:
                        chercher_meuble_int = int(chercher_meuble)
                        objet.sac_joueur.voler(destination.propriete_joueur[cible_int].meuble[chercher_maison_int].contenant[chercher_meuble_int])
                        destination.propriete_joueur[cible_int].meuble[chercher_maison_int].contenant.remove(destination.propriete_joueur[cible_int].meuble[chercher_maison_int].contenant[chercher_meuble_int])

    acheter_maison = input("Souhaitez-vous acheter une propriété ? maison = 500000 deniers (oui/non)")
    if acheter_maison == "oui":
        if len(tuple(objet.sac_joueur.inside.items())[0][1]) > 500000:
            # len(objet.sac_joueur[objet.o1_denier]
            print(objet.sac_joueur.inside.items())
            objet.sac_joueur.retirer(objet.o1_denier, 5)
            maison = infrastructure.Infrastructure("maison", joueur.mon_joueur.localisationX, joueur.mon_joueur.localisationY)
            destination.propriete_joueur.append(maison)
            joueur.mon_joueur.infrastructure.append(maison)
        else:
            print("Vous n'avez pas assez d'argent")
    else:
        print("test")

def joueur_tente(action):
    print("vous montez la tente");
    joueur.stop_meteo_sound()
    if joueur.mon_joueur.meteotemps[0] == "pluie" or joueur.mon_joueur.meteotemps[0] == "orage":
        pass
        # pluie_tente.play()

def joueur_feu(action):
    print("vous lancez un feu...");
    # allumage.play()

def joueur_meteo(action):
    print(joueur.mon_joueur.meteotemps[0]);

def joueur_son_off(action):
    pygame.mixer.pause()

def joueur_son_on(action):
    pygame.mixer.unpause()

def joueur_quete(action):
    print("Voici la liste des quetes dans le lieu (à faire)")
    print("")
    print("")
    print("QUETES METAS")
    # print(joueur.mon_joueur.quetes_meta)
    for i in joueur.mon_joueur.quetes_meta:
        print("- " + i.nom)
        print(" score : " + str(i.score))


    print("")
    print("")
    print("QUETES PRINCIPALES")
    print("")
    print("Voici la liste des quetes découvertes")
    # print(joueur.mon_joueur.quetes_principales)
    x = 0
    for i in joueur.mon_joueur.quetes_principales:
        print("{} : ".format(x), end=' ')
        print("" + i.quoi + " / " + i.nom)
        print(" etat : " + str(i.etat))
        x = x + 1
    print("")
    print("Voici la liste des quetes en cours")


    print("")
    print("Voici la liste des quetes en validées")

    print("")
    print("Voici la liste des quetes en échouées")

    print("")

    print("")
    print("")
    print("QUETES SECONDAIRES")
    print("")
    print("Voici la liste des quetes découvertes")
    # print(joueur.mon_joueur.quetes_secondaires)
    x = 0
    for i in joueur.mon_joueur.quetes_secondaires:
        print("{} : ".format(x), end=' ')
        print("" + i.quoi + " / " + i.nom)
        print(" etat : " + str(i.etat))
        x = x + 1
    print("")
    print("Voici la liste des quetes en cours")

    print("")
    print("Voici la liste des quetes en validées")

    print("")
    print("Voici la liste des quetes en échouées")

    print("")
    print("Souhaitez vous réaliser une quête ou dénicher de nouvelles quêtes ? réaliser une quête (1) dénicher une nouvelle quête (2) s'ajouter une quête méta (3)")
    quete_recherche = input("> ")
    if quete_recherche == "2":
        print("c'est parti !")
        generer_quete()
    elif quete_recherche == "1":
        print("c'est parti !")
        x = 0
        for i in joueur.mon_joueur.quetes_secondaires:
            print("{} : ".format(x), end=' ')
            print("" + i.quoi + " / " + i.nom)
            print(" etat : " + str(i.etat))
            x = x + 1
        print("Indiquez le numero de la quête que vous souhaitez réaliser")
        quete_a_terminer = input("> ")
        print(joueur.mon_joueur.quetes_secondaires[int(quete_a_terminer)].__dict__)
        print("Voulez vous chercher")

    elif quete_recherche == "3":
        # joueur.mon_joueur.quetes_meta.append(quete.origine)
        liste_nom_quetes = []
        # for k, uneQuete in enumerate(joueur.mon_joueur.quetes_meta):
        #     print(k, ":", uneQuete)
        #     liste_nom_quetes.append(uneQuete)

        print(liste_nom_quetes)
        print(""" Voici la liste des quetes meta disponibles :
        (Vous pouvez en ajouter ou en retirer dès que vous le souhaitez depuis n'importe ou)


        1. survivre : """ + str(quete.survivre.description) +  """
        2. origine : """ + str(quete.origine.description) +  """
        3. gloire : """ + str(quete.gloire.description) +  """
        4. amour : """ + str(quete.amour.description) +  """
        5. statut : """ + str(quete.statut.description) +  """
        6. vengeance : """ + str(quete.vengeance.description) +  """
        7. terres : """ + str(quete.terres.description) +  """
        8. noblesse : """ + str(quete.noblesse.description) +  """
        9. argent : """ + str(quete.argent.description) +  """
        10. armee : """ + str(quete.armee.description) +  """
        11. bien : """ + str(quete.bien.description) +  """
        12. mal : """ + str(quete.mal.description) +  """
        13. neutralite : """ + str(quete.neutralite.description) +  """
        14. ordre : """ + str(quete.ordre.description) +  """
        15. equilibre : """ + str(quete.equilibre.description) +  """
        16. chaos : """ + str(quete.chaos.description) +  """
        17. famille : """ + str(quete.famille.description) +  """
        18. sexualite : """ + str(quete.sexualite.description) +  """
        19. science : """ + str(quete.science.description) +  """
        """)

        liste_quete_meta_existante = [quete.science, quete.sexualite, quete.famille, quete.chaos, quete.equilibre, quete.ordre, quete.neutralite, quete.mal, quete.bien, quete.armee, quete.argent, quete.noblesse, quete.terres, quete.vengeance, quete.statut, quete.amour, quete.gloire, quete.origine, quete.survivre]

        for i in joueur.mon_joueur.quetes_meta:
            # print(i.nom)
            liste_nom_quetes.append(i.nom)
        quete_meta = input("Indiquez le nom de la quête que vous souhaitez ajouter ou supprimer de vos quêtes en cours : ")

# for elt in (elt for elt in lst if getattr(elt, "bar", None) == foo):
    # ...
        if quete_meta in liste_nom_quetes:
            print("La quête existe")
            for i in liste_quete_meta_existante:
                if i.nom == quete_meta:
                    joueur.mon_joueur.quetes_meta.remove(i)
                    print("La quete " + quete_meta + " a été supprimé")
        else:
            for i in liste_quete_meta_existante:
                if i.nom == quete_meta:
                    joueur.mon_joueur.quetes_meta.append(i)
                    print("La quete " + quete_meta + " a été ajouté")
    else:
        pass

def generer_quete():
    destination = generer_monde()

    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    print("")
    print("personnes disponibles dans le lieu ou vous êtes :")
    x = 0
    for value in destination.habitants:
        print("{} : ".format(x), end='')

        print(value.__dict__['nom'], end=' ')
        print(value.__dict__['age'], end=' ')
        print("ans", end=' ')
        print(value.__dict__['travail'], end=" ")
        print(value.__dict__['vivant'])
        x = x + 1
    #print(destination.habitants)
    #print(destination.habitants[0].__dict__['nom'])

    try:
        cible = input("A qui souhaitez parler de votre désir d'aventure ? (indiquez le numero) > ")
        cible_int = int(cible)
        nom = destination.habitants[cible_int].__dict__['nom']
        attitude = destination.habitants[cible_int].__dict__['attitude']
        if destination.habitants[cible_int].__dict__['vivant'] == "X":
            print("La personne est morte...")
        else:
            print("")
            print("")
            print("vous > Escusez moi, avez vous un travail ou une mission pour moi ?")

            quete_hasard_choix = ["recherche", "monstre", "rumeur",
            "tresor", "chasse", "nettoyage",
            "identite",
            "spiritualite", "course",
            "commercial", "romantique", "defense", "relique", "inspecteur",
            # "guilde"
            ]
            quete_hasard_choisi = choice(quete_hasard_choix)
            print(quete_hasard_choisi)
            if quete_hasard_choisi == "recherche":
                # print("Oui, j'ai perdu mon médaillon hier. Il faudrait me le retrouver car c'est très important pour ma famille. Si vous le faites avant minuit, j'offre beaucoup d'argent")
                quete_hasard = quete.QueteSecondaireRecherche("recherche", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, j'ai " + quete_hasard.comment + " " + quete_hasard.quoi + " " + quete_hasard.ou + ". Il faudrait " + quete_hasard.objectif + " car " + quete_hasard.pourquoi + " . Si vous le faites avant " + quete_hasard.quand + ", " + quete_hasard.qui +  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "monstre":
                # print("Oui, il y a un troll qu'il faudrait tuer car nous avons eu des victimes. C'est dans le bois, il faut le surprendre, Si vous le faites avant minuit, j'offre beaucoup d'argent ")
                quete_hasard = quete.QueteSecondaireMonstre("monstre", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, il y a " + quete_hasard.quoi + " qu'il faudrait " + quete_hasard.objectif + " car " + quete_hasard.pourquoi + " . C'est " + quete_hasard.ou +  ", il faut " + quete_hasard.comment + ". Si vous le faites avant " + quete_hasard.quand + ", " + quete_hasard.qui +  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "rumeur":
                # print("Oui, j'ai entendu dire que le voisin a prier le diable hier dans les bois. Il parait qu'il essaye d'invoquer un démon. Je nous vous ai rien dit ! ")
                quete_hasard = quete.QueteSecondaireRumeur("rumeur", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, " + quete_hasard.comment + " " + quete_hasard.qui +  " " + quete_hasard.quoi + " " + quete_hasard.quand + " " + quete_hasard.ou + " . " + quete_hasard.objectif + " " + quete_hasard.recompense)
            elif quete_hasard_choisi == "tresor":
                # print("print(nom + " > Oui, j'ai entendu dire par un ami hier qu'un trésor se trouve dans les bois. Il parait qu'il est gardé par un orque mais il y a un beaucoup d'or à la clef !")
                quete_hasard = quete.QueteSecondaireTresor("tresor", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, " + quete_hasard.comment + " " + quete_hasard.qui +  " " + quete_hasard.quand + " " + quete_hasard.quoi + " se trouve " + quete_hasard.ou + " Il parait " + quete_hasard.objectif + " " + quete_hasard.recompense)
            elif quete_hasard_choisi == "chasse":
                # print(" ")
                quete_hasard = quete.QueteSecondaireChasse("chasse", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, le village a besoin d'un chasseur. Il faudrait amener " + quete_hasard.quoi + " qu'il faudrait " + quete_hasard.objectif + " car " + quete_hasard.pourquoi + " . C'est " + quete_hasard.ou +  ", il faut " + quete_hasard.comment + ". Si vous le faites avant " + quete_hasard.quand + ", " + quete_hasard.qui +  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "nettoyage":
                # print("Oui, j'ai entendu dire que le voisin a prier le diable hier. Il parait qu'il essaye d'invoquer un démon. Je nous vous ai rien dit ! ")
                quete_hasard = quete.QueteSecondaireNettoyage("nettoyage", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, il faudrait nettoyer " + quete_hasard.quoi + " car " + quete_hasard.pourquoi + " . C'est " + quete_hasard.ou +  ". Si vous le faites avant " + quete_hasard.quand + ", " + quete_hasard.qui +  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "identite":
                # print("Oui vous êtes un elfe ? Beaucoup de gens chercher des elfes pour leur apprendre la langue elfique car notre commerce a récemment ouver chez eux. SI vous allez dans les bois, vous pouvez enseigner aux gens à l'aide de nos parchemins à parler elfique. Si vous le faites avant minuit, j'offre beaucoup d'argent "")
                quete_hasard = quete.QueteSecondaireIdentite("identite", "découverte", "", 0, "secondaire")
                print(nom + " > Je vous reconnais vous êtes un *custom*. On cherche un " + quete_hasard.quoi + " pour " + quete_hasard.objectif + " car " + quete_hasard.pourquoi + " . Si vous allez" + quete_hasard.ou +  ", il faut " + quete_hasard.comment + ". Si vous le faites avant " + quete_hasard.quand + ", " + quete_hasard.qui +  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "spiritualite":
                # print("Oui, nous avons besoin d'adepte pour servir notre déesse Kraliamn car l'esprit de la forêt a déchainé sa colère récement sur nos récoltes. C'est désastreux, il faut absolument trouver du lorier pour le rituel sacré qui calmera la colère de la déesse. Si vous le faites avant....")
                quete_hasard = quete.QueteSecondaireSpiritualite("spiritualite", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, nous avons besoin de " + quete_hasard.quoi + " pour " + quete_hasard.objectif + " car " + quete_hasard.pourquoi + " . C'est " + quete_hasard.ou +  ", il faut " + quete_hasard.comment + ". Si vous le faites avant " + quete_hasard.quand + ", " + quete_hasard.qui +  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "course":
                # print("Oui, j'ai besoin de 50 sac de farines qu'il faudrait m'amener à mon moulin car la récolte de cette année a été désastreuse. C'est au marché de lacaol, il faut s'adresser a la guilde des marchands. Si vous le faites avant minuit, j'offre beaucoup d'argent")
                quete_hasard = quete.QueteSecondaireCourse("course", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, j'ai besoin de " + str(quete_hasard.combien) + " " + quete_hasard.quoi + " qu'il faudrait " + quete_hasard.objectif + " car " + quete_hasard.pourquoi + " . C'est " + quete_hasard.ou +  ", il faut " + quete_hasard.comment + ". Si vous le faites avant " + quete_hasard.quand + ", " + quete_hasard.qui +  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "commercial":
                # print("Oui, j'ai perdu mon médaillon hier. Il faudrait me le retrouver car c'est très important pour ma famille. Si vous le faites avant minuit, j'offre beaucoup d'argent")
                quete_hasard = quete.QueteSecondaireCommercial("commercial", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, il y a " + quete_hasard.quoi + " qu'il faudrait " + quete_hasard.objectif + " avec " + quete_hasard.qui +  "  car " + quete_hasard.pourquoi + " . C'est " + quete_hasard.ou +  ", il faut " + quete_hasard.comment + ". Les termes du contrat seraient : " + str(quete_hasard.combien) + " de " + quete_hasard.contrat + " " + quete_hasard.occurence + ". Si vous le faites avant " + quete_hasard.quand + ", j'offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "romantique":
                # print("Oui, Il y a cette fille que j'apprécie grandement.  J'aimerais l'inviter à diner un soir mais je n'ose pas lui demander... Vous pouvez trouver ma bien aimé dans l'église, il faut lui apporter les fleurs. Si vous le faites avant minuit j'offre beaucoup d'argent")
                quete_hasard = quete.QueteSecondaireRomantique("romantique", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, " + quete_hasard.quoi + ". J'aimerais " + quete_hasard.objectif + " mais " + quete_hasard.pourquoi + " . Vous pouvez trouver cette personne " + quete_hasard.ou +  ", il faut " + quete_hasard.comment + ". Si vous le faites avant " + quete_hasard.quand + ", " + quete_hasard.qui +  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "defense":
                # print("Oui, il y a cette homme qui m'accuse de lui avoir volé 3 pommes pour nourrir ces enfants.. Il faudrait me le retrouver car c'est très important pour ma famille. Si vous le faites avant minuit, j'offre beaucoup d'argent")
                quete_hasard = quete.QueteSecondaireDefense("defense", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, il y a  " + quete_hasard.qui + " qui " + quete_hasard.quoi + " pour " + quete_hasard.objectif + "  . C'est " + quete_hasard.ou +  ", il faut " + quete_hasard.comment + ". Si vous le faites avant " + quete_hasard.quand + ", "  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "relique":
                # print("Oui, un livre sacré a été égaré et c'est un objet très important pour notre ordre. Il a été perdu dans les bois, il faut suivre son intuition divine. Si vous le faites avant minuit, j'offre beaucoup d'argent")
                quete_hasard = quete.QueteSecondaireRelique("relique", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, il y a " + quete_hasard.quoi + " à " + quete_hasard.objectif + " et " + quete_hasard.pourquoi + " . " + quete_hasard.ou +  ", il faut " + quete_hasard.comment + ". Si vous le faites avant " + quete_hasard.quand + ", " + quete_hasard.qui +  " offre " + quete_hasard.recompense)
            elif quete_hasard_choisi == "inspecteur":
                # print("Oui, il y a eu un meutre à l'église cette nuit. Il faut retrouver l'assassin car il est encore en liberté. C'est par ordre du magistrat Si vous le faites avant minuit, il y a une grande récompense")
                quete_hasard = quete.QueteSecondaireInspecteur("inspecteur", "découverte", "", 0, "secondaire")
                print(nom + " > Oui, il y a eu " + quete_hasard.quoi + " " + quete_hasard.ou +  " " + quete_hasard.quand + ", il faut " + quete_hasard.comment + " "" car " + quete_hasard.pourquoi + " . C'est  " + quete_hasard.objectif + ". Si vous le faites " + quete_hasard.qui +  " offre " + quete_hasard.recompense)

            print("")
            print(quete_hasard.nom)
            print("")

            print("")
            print("")
            print(quete_hasard.__dict__)
            joueur.mon_joueur.quetes_secondaires.append(quete_hasard)

    except ValueError:
        print("Vous ne pouvez qu'entrer des chiffres")
    except IndexError:
        print("Il n'y a pas ce nombre dans la liste")



def joueur_oreille(action):
    print("Vous vous bouchez les oreilles")

def joueur_sentir(action):
    print("L'air autour de vous sent l'herbe mouillée...")

def joueur_ecouter(action):
    print("Que souhaitez vous écouter ?")
    print("le sol ?")
    print("une conversation ?")
    print("au loin ?")
    print("un objet ?")

def joueur_furtif(action):
    if joueur.mon_joueur.furtif == False:
        joueur.mon_joueur.furtif = True
        print("Vous entrez en mode furtif")
    else:
        joueur.mon_joueur.furtif = False
        print("Vous sortez du mode furtif")


def joueur_voler(action):
    destination = generer_monde()
    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    print("Comment souhaitez vous voler ?")
    print("vol à la tire ? : 1")
    print("cambriolage ? : 2")
    choix_vol = input(" > ")
    if choix_vol == "1":
        print("Qui souhaitez vous voler ?")
        print("personnes disponibles dans le lieu ou vous êtes :")
        x = 0
        for value in destination.habitants:
            print("{} : ".format(x), end='')

            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
            x = x + 1
        #print(destination.habitants)
        #print(destination.habitants[0].__dict__['nom'])
        cible = input("voler > ")
        try:
            cible_int = int(cible)
            nom = destination.habitants[cible_int].__dict__['nom']
            pv = destination.habitants[cible_int].__dict__['pv']
            inventaire_perso = destination.habitants[cible_int].__dict__['inventaire_personnage']
            attitude = destination.habitants[cible_int].__dict__['attitude']
            surveillance = destination.habitants[cible_int].__dict__['surveillance']
            if destination.habitants[cible_int].__dict__['vivant'] == "X":
                print("La personne est morte, vous allez donc profaner sa tombe...")
            print(inventaire_perso[0].nom)
            print(surveillance)
            voler_objet_boucle = True
            while voler_objet_boucle == True:
                x = 0
                for value in inventaire_perso:
                    print("{} : ".format(x), end='')
                    print(value.__dict__['nom'])
                    x = x + 1
                voler_objet = input("Souhaitez vous voler un objet ? (numero_de_l'objet/non)")
                if voler_objet == "non":
                    voler_objet = False
                else:
                    voler_objet_int = int(voler_objet)
                    objet.sac_joueur.voler(destination.habitants[cible_int].inventaire_personnage[voler_objet_int])
                    destination.habitants[cible_int].inventaire_personnage.remove(destination.habitants[cible_int].inventaire_personnage[voler_objet_int])
        except ValueError:
            print("Vous ne pouvez qu'entrer des chiffres")
        except IndexError:
            print("Il n'y a pas ce nombre dans la liste")

    elif choix_vol == "2":
        print("Qui souhaitez vous cambrioler ?")
        print("personnes disponibles dans le lieu ou vous êtes :")
        x = 0
        for value in destination.habitants:
            print("{} : ".format(x), end='')

            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
            x = x + 1
        #print(destination.habitants)
        #print(destination.habitants[0].__dict__['nom'])
        cible = input("cambrioler > ")
        try:
            cible_int = int(cible)
            nom = destination.habitants[cible_int].__dict__['nom']
            pv = destination.habitants[cible_int].__dict__['pv']
            force = destination.habitants[cible_int].__dict__['force']
            attitude = destination.habitants[cible_int].__dict__['attitude']
            surveillance = destination.habitants[cible_int].__dict__['surveillance']
            if not destination.habitants[cible_int].propriete:
                print ("La personne n'a pas de propriété")
            else:
                x = 0
                for value in destination.habitants[cible_int].propriete:
                    print("{} : ".format(x), end='')

                    print(value.nom)
                    x = x + 1
                methode_infiltration = input("vous localisez la maison de cette personne, souhaitez vous 1) forcer la porte ou 2) brisez une fenêtre ou 3) crocheter la serrure pour rentrer ? (1/2/3)")
                if methode_infiltration == "1":
                    print("la porte est trop solide")
                elif methode_infiltration == "2":
                    print("vous brisez la fenêtre et entrer à l'intérieur")
                    fouiller = True
                    while fouiller == True:
                        x = 0
                        for value in destination.habitants[cible_int].propriete[0].meuble:
                            print("{} : ".format(x), end='')

                            print(value.nom)
                            x = x + 1
                        fouille_infrastructure = input("Souhaitez vous fouiller un meuble ? (numero_meuble/non)")
                        if fouille_infrastructure == "non":
                            fouiller = False
                        else:
                            fouiller_meuble = True
                            while fouiller_meuble == True:
                                x = 0
                                fouille_infrastructure_int = int(fouille_infrastructure)
                                for value in destination.habitants[cible_int].propriete[0].meuble[fouille_infrastructure_int].contenant:
                                    print("{} : ".format(x), end='')

                                    print(value.nom)
                                    x = x + 1
                                if not destination.habitants[cible_int].propriete[0].meuble[fouille_infrastructure_int].contenant:
                                    print ("Le meuble est vide")
                                    fouiller_meuble = False
                                else:
                                    fouille_infrastructure_meuble = input("Souhaitez vous prendre un objet dans ce meuble ? (numero_objet/non)")
                                    if fouille_infrastructure_meuble == "non":
                                        fouiller_meuble = False
                                    else:
                                        fouille_infrastructure_meuble_int = int(fouille_infrastructure_meuble)
                                        objet.sac_joueur.voler(destination.habitants[cible_int].propriete[0].meuble[fouille_infrastructure_int].contenant[fouille_infrastructure_meuble_int])
                                        destination.habitants[cible_int].propriete[0].meuble[fouille_infrastructure_int].contenant.remove(destination.habitants[cible_int].propriete[0].meuble[fouille_infrastructure_int].contenant[fouille_infrastructure_meuble_int])
                elif methode_infiltration == "3":
                    print("vous n'avez pas assez de compétence en crochetage de serrure")
        except ValueError:
            print("Vous ne pouvez qu'entrer des chiffres")
        except IndexError:
            print("Il n'y a pas ce nombre dans la liste")

def joueur_hurler(action):
    print("vous vous mettez à hurler")
    # hurler.play()

def joueur_peter(action):
    print("vous vous mettez à... hum hum")
    # peter.play()

def joueur_uriner(action):
    print("vous vous mettez à faire vos besoins...")
    # uriner.play()

def joueur_vomir(action):
    print("vous tentez de vous faire vomir..")

def joueur_chanter(action):
    print("vous vous mettez à chanter")
    # chanter.play()

def joueur_danser(action):
    print("vous vous mettez à danser")

def joueur_imiter(action):
    print("Que souhaitez vous imiter ?")
    print("chant des oiseaux ?")
    print("quelqu'un ?")

def joueur_map(action):
    destination = generer_monde()
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end=' ')
        print()

def joueur_attaquer(action):
    destination = generer_monde()

    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    print("Qui souhaitez vous attaquer ? (indiquez le numero)")
    print("")
    print("personnes disponibles dans le lieu ou vous êtes :")
    x = 0
    for value in destination.habitants:
        print("{} : ".format(x), end='')

        print(value.__dict__['nom'], end=' ')
        print(value.__dict__['age'], end=' ')
        print("ans", end=' ')
        print(value.__dict__['travail'], end=' ')
        print(value.__dict__['vivant'])
        x = x + 1
    #print(destination.habitants)
    #print(destination.habitants[0].__dict__['nom'])
    try:
        cible = input("attaquer > ")
        cible_int = int(cible)
        print()
        nom = destination.habitants[cible_int].__dict__['nom']
        pv = destination.habitants[cible_int].__dict__['pv']
        force = destination.habitants[cible_int].__dict__['force']
        attitude = destination.habitants[cible_int].__dict__['attitude']
        if destination.habitants[cible_int].__dict__['vivant'] == "X":
            print("La personne est morte...")
        else:
            combat = True
            while combat == True:

                technique_opposant_choice = ["defenseur", "provocateur", "conquerant", "gardien", "fuite"]
                technique_opposant = choice(technique_opposant_choice)


                print("Quel technique de combat choisissez vous ? (1) conquerant (2) defenseur (3) provocateur (4) gardien")
                votre_technique_de_combat = input("> ")
                print("La technique de combat de l'adversaire est : " + str(technique_opposant))
                print("")
                print(nom + " a " + str(destination.habitants[cible_int].__dict__['pv']) + " points de vie")
                print("et " + str(destination.habitants[cible_int].__dict__['force']) + " points d'attaque")

                print("")

                print("vous avez " + str(joueur.mon_joueur.pv) + " points de vie")
                print("et " + str(joueur.mon_joueur.force) + " points d'attaque")

                print("")
                bonus_technique_personnage = 1
                votre_bonus_technique = 1
                if votre_technique_de_combat != technique_opposant:
                    if votre_technique_de_combat == "1" and technique_opposant == "provocateur":
                        bonus_technique_personnage = 4
                        print("Votre technique vous apporte x4 de malus...")
                    if votre_technique_de_combat == "1" and technique_opposant == "gardien":
                        votre_bonus_technique = 6
                        print("Votre technique vous apporte x6 de bonus !")
                    if votre_technique_de_combat == "1" and technique_opposant == "defenseur":
                        bonus_technique_personnage = 2
                        print("Votre technique vous apporte x2 de malus...")
                    if votre_technique_de_combat == "1" and technique_opposant == "fuite":
                        votre_bonus_technique = 4
                        print("Votre technique vous apporte x4 de bonus !")

                    if votre_technique_de_combat == "2" and technique_opposant == "conquerant":
                        votre_bonus_technique = 2
                        print("Votre technique vous apporte x2 de bonus !")
                    if votre_technique_de_combat == "2" and technique_opposant == "gardien":
                        votre_bonus_technique = 2
                        print("Votre technique vous apporte x2 de bonus !")
                    if votre_technique_de_combat == "2" and technique_opposant == "provocateur":
                        bonus_technique_personnage = 4
                        print("Votre technique vous apporte x4 de malus...")

                    if votre_technique_de_combat == "3" and technique_opposant == "conquerant":
                        votre_bonus_technique = 4
                        print("Votre technique vous apporte x4 de bonus !")
                    if votre_technique_de_combat == "3" and technique_opposant == "gardien":
                        bonus_technique_personnage = 2
                        print("Votre technique vous apporte x2 de malus...")
                    if votre_technique_de_combat == "3" and technique_opposant == "defenseur":
                        bonus_technique_personnage = 2
                        print("Votre technique vous apporte x2 de malus...")

                    if votre_technique_de_combat == "4" and technique_opposant == "provocateur":
                        votre_bonus_technique = 2
                        print("Votre technique vous apporte x2 de bonus !")
                    if votre_technique_de_combat == "4" and technique_opposant == "conquerant":
                        bonus_technique_personnage = 6
                        print("Votre technique vous apporte x6 de malus...")
                    if votre_technique_de_combat == "4" and technique_opposant == "defenseur":
                        votre_bonus_technique = 4
                        print("Votre technique vous apporte x4 de bonus !")

                    #     	         conquerant	 defenseur	provocateur	  gardien
                    # conquerant	       0	    x2#	         x4#     	x6
                    # defenseur            x2  	    0         	 x2      	x4#
                    # provocateur	       x4	    x2#	         0	        x2#
                    # gardien             x6#	   x4	         x2	        0

                print("le combat commence...")
                force_de_votre_attaque = random.randint(0,10)
                print("force_de_votre_attaque : " + str(force_de_votre_attaque))
                efficacite_de_votre_attaque = random.randint(0,1)
                print("efficacite_de_votre_attaque : " + str(efficacite_de_votre_attaque))
                de6_votre_attaque = random.randint(0,6)
                print("de6_votre_attaque : " + str(de6_votre_attaque))
                print("votre force avec votre arme actuelle : " + str(joueur.mon_joueur.force))
                print("Endurance de l'adversaire avec son armure : " + str(destination.habitants[cible_int].__dict__['endurance']))
                effet_attaque_joueur = (joueur.mon_joueur.force - destination.habitants[cible_int].__dict__['endurance'] - destination.habitants[cible_int].__dict__['protection']) * ((force_de_votre_attaque/10) + efficacite_de_votre_attaque) * votre_bonus_technique
                print("effet_de_votre_attaque : " + str(effet_attaque_joueur))

                if de6_votre_attaque == 1:
                    print("Vous avez touché votre cible à la tête x3")
                    effet_attaque_joueur = effet_attaque_joueur - destination.habitants[cible_int].__dict__['protection_tete'] - destination.habitants[cible_int].__dict__['protection']
                    if effet_attaque_joueur < 0:
                        effet_attaque_joueur = 0
                    destination.habitants[cible_int].__dict__['pv'] = destination.habitants[cible_int].__dict__['pv'] - (effet_attaque_joueur * 3)
                    if destination.habitants[cible_int].__dict__['pv'] < 0 and destination.habitants[cible_int].__dict__['pv'] > - 10:
                        print("Votre arme assome votre adversaire sur le coup qui s'effrondre sur le sol...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -10 and destination.habitants[cible_int].__dict__['pv'] > - 100:
                        print("Vous plantez votre arme dans la tête de votre adversaire le laissant tomber sur les genoux puis à terre sans connaissance...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -100:
                        print("Vous coupez la tête de votre adversaire avec votre coup... son corps s'effondre sur le sol sans vie et sans tête")
                elif de6_votre_attaque == 2:
                    print("Vous avez touché votre cible au bras droit")
                    effet_attaque_joueur = effet_attaque_joueur - destination.habitants[cible_int].__dict__['protection_bras'] - destination.habitants[cible_int].__dict__['protection']
                    if effet_attaque_joueur < 0:
                        effet_attaque_joueur = 0
                    destination.habitants[cible_int].__dict__['pv'] = destination.habitants[cible_int].__dict__['pv'] - effet_attaque_joueur
                    if destination.habitants[cible_int].__dict__['pv'] < 0 and destination.habitants[cible_int].__dict__['pv'] > - 10:
                        print("Votre arme blesse profondément votre adversaire qui s'effrondre sur le sol en tenant son bras droit meurtris...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -10 and destination.habitants[cible_int].__dict__['pv'] > - 100:
                        print("Vous plantez votre arme dans le bras droit de votre adversaire qui se laisse tomber sur les genoux puis à terre sans connaissance...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -100:
                        print("Vous coupez le bras droit de votre adversaire avec votre coup... son corps s'effondre sur le sol sans vie")
                elif de6_votre_attaque == 3:
                    print("Vous avez touché votre cible au bras gauche")
                    effet_attaque_joueur = effet_attaque_joueur - destination.habitants[cible_int].__dict__['protection_bras'] - destination.habitants[cible_int].__dict__['protection']
                    if effet_attaque_joueur < 0:
                        effet_attaque_joueur = 0
                    destination.habitants[cible_int].__dict__['pv'] = destination.habitants[cible_int].__dict__['pv'] - effet_attaque_joueur
                    if destination.habitants[cible_int].__dict__['pv'] < 0 and destination.habitants[cible_int].__dict__['pv'] > - 10:
                        print("Votre arme blesse profondément votre adversaire qui s'effrondre sur le sol en tenant son bras gauche meurtris...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -10 and destination.habitants[cible_int].__dict__['pv'] > - 100:
                        print("Vous plantez votre arme dans le bras gauche de votre adversaire qui se laisse tomber sur les genoux puis à terre sans connaissance...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -100:
                        print("Vous coupez le bras gauche de votre adversaire avec votre coup... son corps s'effondre sur le sol sans vie")
                elif de6_votre_attaque == 4:
                    print("Vous avez touché votre cible au torse x2")
                    effet_attaque_joueur = effet_attaque_joueur - destination.habitants[cible_int].__dict__['protection_torse'] - destination.habitants[cible_int].__dict__['protection']
                    if effet_attaque_joueur < 0:
                        effet_attaque_joueur = 0
                    destination.habitants[cible_int].__dict__['pv'] = destination.habitants[cible_int].__dict__['pv'] - (effet_attaque_joueur * 2)
                    if destination.habitants[cible_int].__dict__['pv'] < 0 and destination.habitants[cible_int].__dict__['pv'] > - 10:
                        print("Votre arme blesse profondément votre adversaire à l'épaule. Il s'effrondre sur le sol...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -10 and destination.habitants[cible_int].__dict__['pv'] > - 100:
                        print("Vous plantez votre arme dans le ventre de votre adversaire qui se laisse tomber sur les genoux puis à terre sans connaissance...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -100 and destination.habitants[cible_int].__dict__['pv'] > - 500:
                        print("Vous plantez votre arme dans le coeur de votre adversaire, avec votre coup son corps s'effondre sur le sol sans vie")
                    elif destination.habitants[cible_int].__dict__['pv'] < -500:
                        print("Vous coupez votre adversaire en deux, le haut de son corps tombe sur le sol lorsque ses jambes restent en suspend quelques secondes avant de tomber à leur tour...")
                elif de6_votre_attaque == 5:
                    print("Vous avez touché votre cible à la jambe droite")
                    effet_attaque_joueur = effet_attaque_joueur - destination.habitants[cible_int].__dict__['protection_jambes'] - destination.habitants[cible_int].__dict__['protection']
                    if effet_attaque_joueur < 0:
                        effet_attaque_joueur = 0
                    destination.habitants[cible_int].__dict__['pv'] = destination.habitants[cible_int].__dict__['pv'] - effet_attaque_joueur
                    if destination.habitants[cible_int].__dict__['pv'] < 0 and destination.habitants[cible_int].__dict__['pv'] > - 10:
                        print("Votre arme blesse profondément votre adversaire à la jambe droite. Il s'effrondre sur le sol en se tenant la jambe...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -10 and destination.habitants[cible_int].__dict__['pv'] > - 100:
                        print("Vous plantez votre arme dans la jambe droite de votre adversaire qui se laisse tomber sur les genoux puis à terre sans connaissance...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -100 and destination.habitants[cible_int].__dict__['pv'] > - 500:
                        print("Vous plantez votre arme dans l'aine de votre adversaire, il tombe sans connaissance par terre...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -500:
                        print("Vous coupez la jambe droite de votre adversaire, il s'effondre aussitôt...")
                elif de6_votre_attaque == 6:
                    print("Vous avez touché votre cible à la jambe gauche")
                    effet_attaque_joueur = effet_attaque_joueur - destination.habitants[cible_int].__dict__['protection_jambes'] - destination.habitants[cible_int].__dict__['protection']
                    if effet_attaque_joueur < 0:
                        effet_attaque_joueur = 0
                    destination.habitants[cible_int].__dict__['pv'] = destination.habitants[cible_int].__dict__['pv'] - effet_attaque_joueur
                    if destination.habitants[cible_int].__dict__['pv'] < 0 and destination.habitants[cible_int].__dict__['pv'] > - 10:
                        print("Votre arme blesse profondément votre adversaire à la jambe gauche. Il s'effrondre sur le sol en se tenant la jambe...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -10 and destination.habitants[cible_int].__dict__['pv'] > - 100:
                        print("Vous plantez votre arme dans la jambe gauche de votre adversaire qui se laisse tomber sur les genoux puis à terre sans connaissance...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -100 and destination.habitants[cible_int].__dict__['pv'] > - 500:
                        print("Vous plantez votre arme dans l'aine de votre adversaire, il tombe sans connaissance par terre...")
                    elif destination.habitants[cible_int].__dict__['pv'] < -500:
                        print("Vous coupez la jambe gauche de votre adversaire, il s'effondre aussitôt...")
                else:
                    print("Vous avez manqué votre cible")

                if technique_opposant == "fuite" and destination.habitants[cible_int].__dict__['pv'] > 10:
                    print("Votre opposant prend la fuite")
                    break

                print("")
                force_attaque_personnage = random.randint(0,10)
                print("force_attaque_personnage : " + str(force_attaque_personnage))
                efficacite_attaque_personnage = random.randint(0,1)
                print("efficacite_attaque_personnage : " + str(efficacite_attaque_personnage))
                de6_attaque_personnage = random.randint(0,6)
                print("de6_attaque_personnage : " + str(de6_attaque_personnage))
                print("Force de l'adversaire avec son arme : " + str(destination.habitants[cible_int].__dict__['force']))
                print("votre endurance avec votre armure actuelle : " + str(joueur.mon_joueur.endurance))
                effet_attaque_personnage = (destination.habitants[cible_int].__dict__['force'] - joueur.mon_joueur.endurance) * ((force_attaque_personnage/10) + efficacite_attaque_personnage) * bonus_technique_personnage
                print("effet_attaque_personnage : " + str(effet_attaque_personnage))
                if de6_attaque_personnage == 1:
                    print("Vous avez été touché à la tête x3")
                    effet_attaque_personnage = effet_attaque_personnage - joueur.mon_joueur.protection_tete - joueur.mon_joueur.protection
                    if effet_attaque_personnage < 0:
                        effet_attaque_personnage = 0
                    joueur.mon_joueur.pv = joueur.mon_joueur.pv - (effet_attaque_personnage * 3)
                    if joueur.mon_joueur.pv < 0 and joueur.mon_joueur.pv > - 10:
                        print("L'arme de votre adversaire vous assome sur le coup et vous tombez sur le sol sans connaissance...")
                    elif joueur.mon_joueur.pv < -10 and joueur.mon_joueur.pv > - 100:
                        print("Votre adversaire plante son arme dans votre tête et vous tombez sur les genoux puis à terre sans connaissance...")
                    elif joueur.mon_joueur.pv < -100:
                        print("Votre adversaire vous coupe la tête, votre corps s'effondre sur le sol sans vie et sans tête")
                elif de6_attaque_personnage == 2:
                    print("Vous avez été touché au bras droit")
                    effet_attaque_personnage = effet_attaque_personnage - joueur.mon_joueur.protection_bras - joueur.mon_joueur.protection
                    if effet_attaque_personnage < 0:
                        effet_attaque_personnage = 0
                    joueur.mon_joueur.pv = joueur.mon_joueur.pv - effet_attaque_personnage
                    if joueur.mon_joueur.pv < 0 and joueur.mon_joueur.pv > - 10:
                        print("l'arme de votre adversaire vous blesse profondément et vous vous effrondrez sur le sol en tenant votre bras droit meurtris...")
                    elif joueur.mon_joueur.pv < -10 and joueur.mon_joueur.pv > - 100:
                        print("L'arme de votre adversaire se plante dans votre bras droit et vous vous laissez tomber sur les genoux puis à terre sans connaissance...")
                    elif joueur.mon_joueur.pv < -100:
                        print("L'arme de votre adversaire vous coupe le bras droit... votre corps s'effondre sur le sol sans vie")
                elif de6_attaque_personnage == 3:
                    print("Vous avez été touché au bras gauche")
                    effet_attaque_personnage = effet_attaque_personnage - joueur.mon_joueur.protection_bras - joueur.mon_joueur.protection
                    if effet_attaque_personnage < 0:
                        effet_attaque_personnage = 0
                    joueur.mon_joueur.pv = joueur.mon_joueur.pv - effet_attaque_personnage
                    if joueur.mon_joueur.pv < 0 and joueur.mon_joueur.pv > - 10:
                        print("L'arme de votre adversaire vous blesse profondément et vous vous effrondrez sur le sol en tenant votre bras gauche meurtris...")
                    elif joueur.mon_joueur.pv < -10 and joueur.mon_joueur.pv > - 100:
                        print("L'arme de votre adversaire se plante dans votre bras gauche et vous vous laissez tomber sur les genoux puis à terre sans connaissance...")
                    elif joueur.mon_joueur.pv < -100:
                        print("L'arme de votre adversaire vous coupe, votre corps s'effondre sur le sol sans vie")
                elif de6_attaque_personnage == 4:
                    print("Vous avez été touché au torse x2")
                    effet_attaque_personnage = effet_attaque_personnage - joueur.mon_joueur.protection_torse - joueur.mon_joueur.protection
                    if effet_attaque_personnage < 0:
                        effet_attaque_personnage = 0
                    joueur.mon_joueur.pv = joueur.mon_joueur.pv - (effet_attaque_personnage * 2)
                    if joueur.mon_joueur.pv < 0 and joueur.mon_joueur.pv > - 10:
                        print("L'arme de votre adversaire vous blesse profondément à l'épaule. Vous vous effrondrez sur le sol...")
                    elif joueur.mon_joueur.pv < -10 and joueur.mon_joueur.pv > - 100:
                        print("L'arme de votre adversaire se plante dans votre ventre. Vous vous laissez tomber sur les genoux puis à terre sans connaissance...")
                    elif joueur.mon_joueur.pv < -100 and joueur.mon_joueur.pv > - 500:
                        print("L'arme de votre adversaire se plante dans votre coeur, avec ce coup votre corps s'effondre sur le sol sans vie")
                    elif joueur.mon_joueur.pv < -500:
                        print("Votre adversaire vous coupe en deux, le haut de votre corps tombe sur le sol lorsque vos jambes restent en suspend quelques secondes avant de tomber à leur tour...")
                elif de6_attaque_personnage == 5:
                    print("Vous avez été touché à la jambe droite")
                    effet_attaque_personnage = effet_attaque_personnage - joueur.mon_joueur.protection_jambes - joueur.mon_joueur.protection
                    if effet_attaque_personnage < 0:
                        effet_attaque_personnage = 0
                    joueur.mon_joueur.pv = joueur.mon_joueur.pv - effet_attaque_personnage
                    if joueur.mon_joueur.pv < 0 and joueur.mon_joueur.pv > - 10:
                        print("L'arme de votre adversaire vous blesse profondément à la jambe droite. Vous vous effrondrez sur le sol en se tenant votre jambe...")
                    elif joueur.mon_joueur.pv < -10 and joueur.mon_joueur.pv > - 100:
                        print("L'arme de votre adversaire se plante dans votre jambe droite. Vous vous laissez tomber sur les genoux puis à terre sans connaissance...")
                    elif joueur.mon_joueur.pv < -100 and joueur.mon_joueur.pv > - 500:
                        print("L'arme de votre adversaire se plante dans votre aine, Vous tombez sans connaissance par terre...")
                    elif joueur.mon_joueur.pv < -500:
                        print("Vous adversaire vous coupe la jambe droite, vous vous effondrez aussitôt...")
                elif de6_attaque_personnage == 6:
                    print("Vous avez été touché à la jambe gauche")
                    effet_attaque_personnage = effet_attaque_personnage - joueur.mon_joueur.protection_jambes - joueur.mon_joueur.protection
                    if effet_attaque_personnage < 0:
                        effet_attaque_personnage = 0
                    joueur.mon_joueur.pv = joueur.mon_joueur.pv - effet_attaque_personnage
                    if joueur.mon_joueur.pv < 0 and joueur.mon_joueur.pv > - 10:
                        print("Votre adversaire vous blesse profondément à la jambe gauche. Vous tombez sur le sol en vous tenant la jambe...")
                    elif joueur.mon_joueur.pv < -10 and joueur.mon_joueur.pv > - 100:
                        print("L'arme de votre adversaire se plante dans votre jambe gauche. Vous vous laissez tomber sur les genoux puis à terre sans connaissance...")
                    elif joueur.mon_joueur.pv < -100 and joueur.mon_joueur.pv > - 500:
                        print("L'arme de votre adversaire se plante dans votre l'aine, après un douloureux moment vous tombez dans les pommes...")
                    elif joueur.mon_joueur.pv < -500:
                        print("Vous adversaire vous coupe la jambe gauche, vous vous effondrez aussitôt...")
                else:
                    print("Vous avez été manqué par votre cible")


                print("")

                print(nom + " a " + str(destination.habitants[cible_int].__dict__['pv']) + " points de vie")
                print("et " + str(destination.habitants[cible_int].__dict__['force']) + " points d'attaque")

                print("")

                print("vous avez " + str(joueur.mon_joueur.pv) + " points de vie")
                print("et " + str(joueur.mon_joueur.force) + " points d'attaque")

                print("")
                combat_decision = input("souhaitez vous continuer ? (oui/non)")
                if combat_decision == "non":
                    break
                elif joueur.mon_joueur.pv < 0:
                    print("vous êtes vaincu...")
                    break
                elif destination.habitants[cible_int].__dict__['pv'] < 0:
                    combat_final = input("Vous avez vaincu " + nom + ", souhaitez vous l'achever ? (oui/non)")
                    if combat_final == "oui":
                        print("vous avez tué " + nom)
                        destination.habitants[cible_int].__dict__['vivant'] = "X"
                        fouille = input("Souhaitez vous le fouiller ? (oui/non)")
                        if fouille == "oui":
                            prendre_objet_boucle = True
                            while prendre_objet_boucle == True:
                                x = 0
                                for value in destination.habitants[cible_int].inventaire_personnage:
                                    print("{} : ".format(x), end='')
                                    print(value.nom)
                                    x = x + 1
                                prendre_objet = input("Souhaitez vous prendre un objet ? (numero_de_l'objet/non)")
                                if prendre_objet == "non":
                                    prendre_objet_boucle = False
                                else:
                                    prendre_objet_int = int(prendre_objet)
                                    nom = destination.habitants[cible_int].inventaire_personnage[prendre_objet_int].nom
                                    objet.sac_joueur.voler(destination.habitants[cible_int].inventaire_personnage[prendre_objet_int])
                                    destination.habitants[cible_int].inventaire_personnage.remove(destination.habitants[cible_int].inventaire_personnage[prendre_objet_int])
                            x = 0
                            prendre_habit_boucle = True
                            while prendre_habit_boucle == True:
                                x = 0
                                for value in destination.habitants[cible_int].porte:
                                    print("{} : ".format(x), end='')
                                    print(value.nom)
                                    x = x + 1
                                prendre_habit = input("Souhaitez vous prendre un habit ? (numero_de_l'habit/non)")
                                if prendre_habit == "non":
                                    prendre_habit_boucle = False
                                else:
                                    prendre_habit_int = int(prendre_habit)
                                    nom = destination.habitants[cible_int].porte[prendre_habit_int].nom
                                    objet.sac_joueur.voler(destination.habitants[cible_int].porte[prendre_habit_int])
                                    destination.habitants[cible_int].porte.remove(destination.habitants[cible_int].porte[prendre_objet_int])
                            x = 0
                            for value in destination.habitants[cible_int].__dict__['porte']:
                                print("{} : ".format(x), end='')
                                print(value.nom)
                                x = x + 1
                        else:
                            break
                    if combat_final == "non":
                        break
                    break



        # if attitude == "amant":
        #     intro = ["Oh... " + joueur.mon_joueur.nom + " comment tu vas ?", "Mon très chere " + joueur.mon_joueur.nom + ", comment te sens tu ?", "Ah ! " + joueur.mon_joueur.nom + "! Qu'est-ce que j'apprécie ta compagnie ?", "Salut " + joueur.mon_joueur.nom + " comment te sens tu ?", "Bonjour " + joueur.mon_joueur.nom + " ça va ?", "Vous m'avez fait attendre " + joueur.mon_joueur.nom + ", comment tu vas ?"]
        #     intro = choice(intro)
        #     print(intro)
        #     discussion_amant.check(cible_int)

    except ValueError:
        print("Vous ne pouvez qu'entrer des chiffres")
    except IndexError:
        print("Il n'y a pas ce nombre dans la liste")

def joueur_travailler(action):
    destination = generer_monde()
    if destination.construction[0] in ["village", "commune", "bourgade", "fermes"]:
        print("vous pouvez travailler en tant que serf (2 deniers par jour -1 reput)")
        choix_labeur = input("> ")
        if choix_labeur == "serf":
            joueur.mon_joueur.travail_heure(8)
            destination.reputation = destination.reputation - 1
            for loop in range(2):
                objet.sac_joueur.ajouter(objet.o1_denier)
    elif destination.construction[0] in ["bourg", "ville", "cité", "bastion", "château", "cité", "forteresse", "krak", "zone agricole", "zone industriel", "bourg", "bastion", "fort"]:
        print("vous pouvez travailler en tant que serf (3 deniers par jour -1 reput) ou veilleur (4 deniers par jour -4 reput)")
        choix_labeur = input("> ")
        if choix_labeur == "serf":
            joueur.mon_joueur.travail_heure(8)
            destination.reputation = destination.reputation - 1
            for loop in range(3):
                objet.sac_joueur.ajouter(objet.o1_denier)
        elif choix_labeur == "veilleur":
            joueur.mon_joueur.travail_heure(8)
            destination.reputation = destination.reputation - 4
            for loop in range(4):
                objet.sac_joueur.ajouter(objet.o1_denier)
    elif destination.construction[0] in ["citadelle"]:
        print("vous pouvez travailler en tant que serf (4 deniers par jour -1 reput), domestique (16 deniers par jour -12 reput) ou veilleur (6 deniers par jour -4 reput)")
        choix_labeur = input("> ")
        if choix_labeur == "serf":
            joueur.mon_joueur.travail_heure(8)
            destination.reputation = destination.reputation - 1
            for loop in range(4):
                objet.sac_joueur.ajouter(objet.o1_denier)
        elif choix_labeur == "veilleur":
            joueur.mon_joueur.travail_heure(8)
            destination.reputation = destination.reputation - 4
            for loop in range(6):
                objet.sac_joueur.ajouter(objet.o1_denier)
        elif choix_labeur == "domestique":
            joueur.mon_joueur.travail_heure(8)
            destination.reputation = destination.reputation - 12
            for loop in range(16):
                objet.sac_joueur.ajouter(objet.o1_denier)
    else:
        print("il n'y a pas de travail pour vous ici")


    # print(destination.__dict__["habitants"])


def joueur_competence(action):
    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    destination = generer_monde()
    print("#INFO COMPETENCE#")
    print('')
    print('Principale')
    print('')
    print("chasse : {} ".format(joueur.mon_joueur.chasse))
    print("pêche : {} ".format(joueur.mon_joueur.peche))
    print("alchimie : {} ".format(joueur.mon_joueur.alchimie))
    print("crochetage : {} ".format(joueur.mon_joueur.crochetage))
    print("entretien : {} ".format(joueur.mon_joueur.entretien))
    print("equitation : {} ".format(joueur.mon_joueur.equitation))
    print("herboristerie : {} ".format(joueur.mon_joueur.herboristerie))
    print("furtivite : {} ".format(joueur.mon_joueur.furtivite))
    print("vol_a_la_tire : {} ".format(joueur.mon_joueur.vol_a_la_tire))
    print("alcool : {} ".format(joueur.mon_joueur.alcool))
    print("maitre_chien : {} ".format(joueur.mon_joueur.maitre_chien))
    print("soin : {} ".format(joueur.mon_joueur.soin))
    print("marchandage : {} ".format(joueur.mon_joueur.marchandage))
    print("forgeage : {} ".format(joueur.mon_joueur.forgeage))
    print("armure_lourde : {} ".format(joueur.mon_joueur.armure_lourde))
    print("armure_legere : {} ".format(joueur.mon_joueur.armure_legere))
    print("mental : {} ".format(joueur.mon_joueur.mental))
    print("musique : {} ".format(joueur.mon_joueur.musique))
    print("tannerie : {} ".format(joueur.mon_joueur.tannerie))
    print("autorite : {} ".format(joueur.mon_joueur.autorite))
    print("telepathie : {} ".format(joueur.mon_joueur.telepathie))

    print('')
    print('Combat')
    print('')
    print("combat : {} ".format(joueur.mon_joueur.combat))
    print("deux_mains : {} ".format(joueur.mon_joueur.deux_mains))
    print("mains_nues : {} ".format(joueur.mon_joueur.mains_nues))
    print("defense : {} ".format(joueur.mon_joueur.defense))
    print("arc : {} ".format(joueur.mon_joueur.arc))
    print("arbalete : {} ".format(joueur.mon_joueur.arbalete))
    print("pistolet : {} ".format(joueur.mon_joueur.pistolet))
    print("epee : {} ".format(joueur.mon_joueur.epee))
    print("massue : {} ".format(joueur.mon_joueur.massue))
    print("hache : {} ".format(joueur.mon_joueur.hache))
    print("parade : {} ".format(joueur.mon_joueur.parade))
    print("bottes : {} ".format(joueur.mon_joueur.bottes))

    print('')
    print('Magie')
    print('')
    print("alteration : {} ".format(joueur.mon_joueur.alteration))
    print("destruction : {} ".format(joueur.mon_joueur.destruction))
    print("conjuration : {} ".format(joueur.mon_joueur.conjuration))
    print("mysticisme : {} ".format(joueur.mon_joueur.mysticisme))
    print("illusion : {} ".format(joueur.mon_joueur.illusion))
    print("enchantement : {} ".format(joueur.mon_joueur.enchantement))

def joueur_chasser(action):
    if objet.a3_arc_simple and objet.a7_fleche_simple not in objet.sac_joueur:
        print("vous n'avez pas de quoi chasser, il vous faut un arc et des flèches.")
    else:
        joueur.mon_joueur.heure(2)
        chasse = random.randint(0,100)
        if chasse < joueur.mon_joueur.chasse:
            print("vous tentez de chasser dans le lieu ou vous êtes...")
            print("vous trouvez un lapin et vous le tuez")
            objet.sac_joueur.ajouter(objet.n5_lapin)
        else:
            print("C'est un échec mais vous avez acquis de l'expérience !")
        joueur.mon_joueur.chasse = joueur.mon_joueur.chasse + 0.1


def joueur_pecher(action):
    if objet.o1_canne_a_peche not in objet.sac_joueur:
        print("vous n'avez pas de quoi pecher, il vous faut une canne à pêche.")
    else:
        joueur.mon_joueur.heure(2)
        peche = random.randint(0,100)
        if peche < joueur.mon_joueur.peche:
            print("vous trouvez un point d'eau dans le lieu ou vous êtes...")
            print("Un poisson mord à l'hameçon...")
            objet.sac_joueur.ajouter(objet.n5_poisson)
        else:
            print("C'est un échec mais vous avez acquis de l'expérience !")
        joueur.mon_joueur.peche = joueur.mon_joueur.peche + 0.1


def joueur_bouger(monAction):
    ask = "Ou veux tu aller ?\n"
    dest = input(ask)
    # voyager.play()
    if dest in ['haut', 'nord', 'Nord']:
        joueur.mon_joueur.localisationX = int(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = int(joueur.mon_joueur.localisationY)
        joueur.mon_joueur.localisationY = joueur.mon_joueur.localisationY + 1
        joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
        destination = generer_monde()



        for value in destination.__dict__.values():
            print(value)
        #print(destination.__dict__)
        print("")
        print("Liste d'habitants du lieu actuel")
        xo = 0
        for value in destination.habitants:
            print("{} : ".format(xo), end='')
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
            xo = xo + 1
        x = int(joueur.mon_joueur.localisationX)
        y = int(joueur.mon_joueur.localisationY)
        x = x*(-1)
        y = y*(-1)
        gestion_mouvement(destination)
        map[y][x] = 1
        for i in range(len(map)):
            for j in range(len(map[i])):
                print(map[i][j], end=' ')
            print()



    elif dest in ['gauche', 'Ouest', 'ouest']:
        joueur.mon_joueur.localisationX = int(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = int(joueur.mon_joueur.localisationY)
        joueur.mon_joueur.localisationX = joueur.mon_joueur.localisationX + 1
        joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
        destination = generer_monde()


        for value in destination.__dict__.values():
            print(value)
        #print(destination.__dict__)
        print("")
        print("Liste d'habitants du lieu actuel")
        xo = 0
        for value in destination.habitants:
            print("{} : ".format(xo), end='')
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
            xo = xo + 1
        x = int(joueur.mon_joueur.localisationX)
        y = int(joueur.mon_joueur.localisationY)
        x = x*(-1)
        y = y*(-1)
        gestion_mouvement(destination)
        map[y][x] = 1
        for i in range(len(map)):
            for j in range(len(map[i])):
                print(map[i][j], end=' ')
            print()


    elif dest in ['Est', 'droite', 'est']:
        joueur.mon_joueur.localisationX = int(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = int(joueur.mon_joueur.localisationY)
        joueur.mon_joueur.localisationX = joueur.mon_joueur.localisationX - 1
        joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
        destination = generer_monde()


        for value in destination.__dict__.values():
            print(value)
        #print(destination.__dict__)
        print("")
        print("Liste d'habitants du lieu actuel")
        xo = 0
        for value in destination.habitants:
            print("{} : ".format(xo), end='')
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
            xo = xo + 1
        x = int(joueur.mon_joueur.localisationX)
        y = int(joueur.mon_joueur.localisationY)
        x = x*(-1)
        y = y*(-1)
        gestion_mouvement(destination)

        map[y][x] = 1
        for i in range(len(map)):
            for j in range(len(map[i])):
                print(map[i][j], end=' ')
            print()


    elif dest in ['sud', 'bas', 'Sud']:
        joueur.mon_joueur.localisationX = int(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = int(joueur.mon_joueur.localisationY)
        joueur.mon_joueur.localisationY = joueur.mon_joueur.localisationY - 1
        joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
        destination = generer_monde()


        for value in destination.__dict__.values():
            print(value)
        #print(destination.__dict__)
        print("")
        print("Liste d'habitants du lieu actuel")
        xo = 0
        for value in destination.habitants:
            print("{} : ".format(xo), end='')
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
            xo = xo + 1
        x = int(joueur.mon_joueur.localisationX)
        y = int(joueur.mon_joueur.localisationY)
        x = x*(-1)
        y = y*(-1)
        gestion_mouvement(destination)
        map[y][x] = 1
        for i in range(len(map)):
            for j in range(len(map[i])):
                print(map[i][j], end=' ')
            print()


def gestion_mouvement(destination):
    print("\n" + "Vous avez bouger en " + joueur.mon_joueur.localisationX  + "/" + joueur.mon_joueur.localisationY )
    print("Vous avez mis 2h pour un trajet de 10 km")
    joueur.meteo_changement()
    play_sound_lieu(destination)
    joueur.mon_joueur.energie = joueur.mon_joueur.energie - (2 * 10)
    joueur.mon_joueur.faim = joueur.mon_joueur.faim - (2 * (3600 * 0.00004))
    joueur.mon_joueur.soif = joueur.mon_joueur.soif - (2 * (3600 * 0.0004))
    global livre_datetime
    joueur.livre_datetime = joueur.livre_datetime + timedelta(hours=2)

def play_sound_lieu(destination):
    print(destination.lieu[0])
    if destination.lieu[0] == "forêt":
        stop_sound_lieu()
    elif destination.lieu[0] == "marécage":
        stop_sound_lieu()
        # marecage.play(100)
    elif destination.lieu[0] == "montagne":
        # aigle.play(100)
        stop_sound_lieu()
    elif destination.lieu[0] == "désert":
        # serpent.play()
        stop_sound_lieu()
    elif destination.lieu[0] == "plaine":
        # aigle.play(100)
        stop_sound_lieu()
    elif destination.lieu[0] == "volcan":
        # volcan.play()
        stop_sound_lieu()
    elif destination.lieu[0] == "forêt profonde":
        # cerf.play(100)
        stop_sound_lieu()
    elif destination.lieu[0] == "mer":
        # mer.play(100)
        stop_sound_lieu()
    elif destination.lieu[0] == "jungle":
        # jungle.play(100)
        stop_sound_lieu()

    if destination.construction[0] == ["bourg", "ville", "cité", "bastion", "château", "ville", "cité", "citadelle", "forteresse", "krak","bourg", "bastion", "fort"]:
        stop_sound_lieu()
        # ville.play(100)
        # cariole.play(100)
    elif destination.construction[0] == ["village", "commune", "bourgade", "repaire", "clôcher","village"]:
        stop_sound_lieu()
        # village.play(100)
    elif destination.construction[0] == ["feu de camps", "campement"]:
        stop_sound_lieu()
        # feu.play(100)
        # allumage.play()
    elif destination.construction[0] == ["zone agricole", "zone industriel", "fermes"]:
        stop_sound_lieu()
        # poulailler.play(100)
        # vaches.play(100)

def stop_sound_lieu():
    pass
    # marecage.stop()
    # vaches.stop()
    # poulailler.stop()
    # allumage.stop()
    # feu.stop()
    # village.stop()
    # ville.stop()
    # cariole.stop()
    # jungle.stop()
    # mer.stop()
    # cerf.stop()
    # aigle.stop()
    # serpent.stop()
    # foret.play()
    # marecage.play()
    # montagne.play()
    # desert.play()
    # plaine.play()
    # volcan.play()
    # foretprofonde.play()
    # mer
    # jungle

def joueur_habitants(action):
    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    destination = generer_monde()

    joueur.mon_joueur.localisationX = int(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = int(joueur.mon_joueur.localisationY)

    print("Liste d'habitants du lieu actuel")
    xo = 0
    for value in destination.habitants:
        print("{} : ".format(xo), end='')
        print(value.__dict__['nom'], end=' ')
        print(value.__dict__['age'], end=' ')
        print("ans", end=' ')
        print(value.__dict__['travail'], end=' ')
        print(value.__dict__['vivant'])
        xo = xo + 1

    print("")
    print("Mes amis")
    i = 0
    for value in destination.habitants:
        attitude = destination.habitants[i].__dict__['attitude']
        if attitude == "ami":
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
        i = i + 1

    print("")
    print("Mes serviteurs")
    i = 0
    for value in destination.habitants:
        attitude = destination.habitants[i].__dict__['attitude']
        if attitude == "serviteur":
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
        i = i + 1

    print("")
    print("Mes ennemis")
    i = 0
    for value in destination.habitants:
        attitude = destination.habitants[i].__dict__['attitude']
        if attitude == "rival":
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
        i = i + 1

    print("")
    print("Mon équipe")
    i = 0
    for value in equipe:
        print(equipe[i].__dict__)
        print("")
        i = i + 1

def joueur_amis(action):
    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    destination = generer_monde()

    print("Mes amis")
    i = 0
    for value in destination.habitants:
        attitude = destination.habitants[i].__dict__['attitude']
        if attitude == "ami":
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
        i = i + 1

def joueur_serviteurs(action):
    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    destination = generer_monde()

    print("")
    print("Mes serviteurs")
    i = 0
    for value in destination.habitants:
        attitude = destination.habitants[i].__dict__['attitude']
        if attitude == "serviteur":
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
        i = i + 1

def joueur_ennemis(action):
    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    destination = generer_monde()

    print("")
    print("Mes ennemis")
    i = 0
    for value in destination.habitants:
        attitude = destination.habitants[i].__dict__['attitude']
        if attitude == "rival":
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
        i = i + 1

def joueur_equipe(action):
    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    destination = generer_monde()

    print("")
    print("Mon équipe")
    i = 0
    for value in equipe:
        print(equipe[i].__dict__)
        print("")
        i = i + 1




    #joueur.mon_joueur.localisationX = destination
    #print_localisation()

def joueur_quisuisje(action):
    joueur.mon_joueur.quisuisje()
    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    destination = generer_monde()


def joueur_infolieu(action):
    destination = generer_monde()

    print("")
    print("#INFO LIEU#")
    for value in destination.__dict__.values():
        print(value)
    joueur.mon_joueur.localisationX = int(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = int(joueur.mon_joueur.localisationY)
    print("")
    print("Reputation dans le lieu : {}".format(destination.reputation))





def joueur_examiner(action):
    destination = generer_monde()

    print("")
    print("#INFO LIEU#")
    for value in destination.__dict__.values():
        print(value)
    joueur.mon_joueur.localisationX = int(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = int(joueur.mon_joueur.localisationY)
    #joueur.mon_joueur.localisationX = int(joueur.mon_joueur.localisationX)
    #joueur.mon_joueur.localisationY = int(joueur.mon_joueur.localisationY)
    #if lieu.carte[joueur.mon_joueur.localisationX][lieu.resolution]:
    #    print("Vous avez déjà examiner l'endroit")
    #else:
    #    print("you can trigger a puzzle here")



def joueur_dormir(action):
    joueur.mon_joueur.dormir()

def joueur_attendre(action):
    joueur.mon_joueur.attendre()

def joueur_mediter(action):
    joueur.mon_joueur.mediter()

def joueur_temps(action):
    print(joueur.MyThread.temps(my))
    #print("")
    #print("FAUX")

def joueur_parler(action):
    destination = generer_monde()

    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    print("Avec qui voulez vous parler ? (indiquez le numero)")
    print("")
    print("personne disponible dans le lieu ou vous êtes :")
    x = 0
    for value in destination.habitants:
        print("{} : ".format(x), end='')
        print(value.__dict__['nom'], end=' ')
        print(value.__dict__['age'], end=' ')
        print("ans", end=' ')
        print(value.__dict__['travail'], end=' ')
        print(value.__dict__['vivant'])
        x = x + 1
    #print(destination.habitants)
    #print(destination.habitants[0].__dict__['nom'])
    try:
        cible = input("parler à > ")
        cible_int = int(cible)
        print()
        attitude = destination.habitants[cible_int].__dict__['attitude']
        nom = destination.habitants[cible_int].__dict__['nom']
        if destination.habitants[cible_int].__dict__['vivant'] == "X":
            print("La personne est morte...")
        else:
            print(nom + " dit : ")
            if attitude == "amant":
                intro = ["Oh... " + joueur.mon_joueur.nom + " comment tu vas ?", "Mon très chere " + joueur.mon_joueur.nom + ", comment te sens tu ?", "Ah ! " + joueur.mon_joueur.nom + "! Qu'est-ce que j'apprécie ta compagnie ?", "Salut " + joueur.mon_joueur.nom + " comment te sens tu ?", "Bonjour " + joueur.mon_joueur.nom + " ça va ?", "Vous m'avez fait attendre " + joueur.mon_joueur.nom + ", comment tu vas ?"]
                intro = choice(intro)
                print(intro)
                discussion_amant.check(cible_int)
            elif attitude == "ami":
                intro = ["Salut " + joueur.mon_joueur.nom + " comment tu vas ?", "Bonjour " + joueur.mon_joueur.nom + ", alors la forme ?", "Ah ! " + joueur.mon_joueur.nom + "! Qu'est-ce que tu racontes ?", "Salut " + joueur.mon_joueur.nom + " comment te sens tu ?", "Bonjour " + joueur.mon_joueur.nom + " ça va ?", "Ah tiens " + joueur.mon_joueur.nom + ", comment tu vas ?"]
                intro = choice(intro)
                print(intro)
                discussion_ami.check(cible_int)
            elif attitude == "base":
                intro = ["Salut " + joueur.mon_joueur.nom + " comment tu vas ?", "Bonjour " + joueur.mon_joueur.nom + ", alors la forme ?", "Ah ! " + joueur.mon_joueur.nom + "! Qu'est-ce que tu racontes ?", "Salut " + joueur.mon_joueur.nom + " comment te sens tu ?", "Bonjour " + joueur.mon_joueur.nom + " ça va ?", "Ah tiens " + joueur.mon_joueur.nom + ", comment tu vas ?"]
                intro = choice(intro)
                print(intro)
                discussion_base.check(cible_int)
            elif attitude == "chef":
                intro = ["Salut " + joueur.mon_joueur.nom + " comment tu vas ?", "Bonjour " + joueur.mon_joueur.nom + ", alors la forme ?", "Ah ! " + joueur.mon_joueur.nom + "! Qu'est-ce que tu racontes ?", "Salut " + joueur.mon_joueur.nom + " comment te sens tu ?", "Bonjour " + joueur.mon_joueur.nom + " ça va ?", "Ah tiens " + joueur.mon_joueur.nom + ", comment tu vas ?"]
                intro = choice(intro)
                print(intro)
                discussion_chef.check(cible_int)
            elif attitude == "inconnu":
                intro = ["Salut ", "Bonjour ", "Qui êtes-vous ?", "Oui ? ", "Je peux vous aider ?", "Plait-t-il ? ", "Bonjour à vous", "Ah tiens "]
                intro = choice(intro)
                print(intro)
                discussion_inconnu.check(cible_int)
            elif attitude == "relation":
                intro = ["Salut " + joueur.mon_joueur.nom + " comment tu vas ?", "Bonjour " + joueur.mon_joueur.nom + ", alors la forme ?", "Ah ! " + joueur.mon_joueur.nom + "! Qu'est-ce que tu racontes ?", "Salut " + joueur.mon_joueur.nom + " comment te sens tu ?", "Bonjour " + joueur.mon_joueur.nom + " ça va ?", "Ah tiens " + joueur.mon_joueur.nom + ", comment tu vas ?"]
                intro = choice(intro)
                print(intro)
                discussion_relation.check(cible_int)
            elif attitude == "rival":
                intro = ["C'est pas vrai " + joueur.mon_joueur.nom + " est de retour...", "Encore toi...", "Ah ! " + joueur.mon_joueur.nom + "! ... Qu'est-ce que tu racontes ?", "oh non pas lui", "Bonjour " + joueur.mon_joueur.nom + "", "Ah tiens " + joueur.mon_joueur.nom + " qu'est que tu peux bien faire ici ?"]
                intro = choice(intro)
                print(intro)
                discussion_rival.check(cible_int)
            elif attitude == "serviteur":
                intro = ["Monseigneur " + joueur.mon_joueur.nom + " comment allez vous ?", "Monseigneur, vous avez toute ma considération", "Bonjour monsieur " + joueur.mon_joueur.nom + " comment vous sentez vous ?", "Bonjour seigneur " + joueur.mon_joueur.nom + "", "Ah tiens monseigneur " + joueur.mon_joueur.nom + ", que me vaut ce plaisir ?"]
                intro = choice(intro)
                print(intro)
                discussion_serviteur.check(cible_int)
    except ValueError:
        print("Vous ne pouvez qu'entrer des chiffres")

def joueur_commercer(action):
    destination = generer_monde()

    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    print("Avec qui voulez vous commercer ? (indiquez le numero)")
    print("")
    print("marchands disponibles dans le lieu ou vous êtes :")
    x = 0
    for value in destination.habitants:
        print("{} : ".format(x), end=' ')
        print(value.__dict__['nom'], end=' ')
        print(value.__dict__['age'], end=' ')
        print("ans", end=' ')
        print(value.__dict__['travail'], end=' ')
        print(value.__dict__['vivant'])
        x = x + 1
    #print(destination.habitants)
    #print(destination.habitants[0].__dict__['nom'])
    try:
        cible = input("commercer avec > ")
        cible_int = int(cible)
        travail = destination.habitants[cible_int].__dict__['travail']
        etalage = destination.habitants[cible_int].__dict__['etalage']
        if destination.habitants[cible_int].__dict__['vivant'] == "X":
            print("La personne est morte...")
        else:

            if travail in ["marchand", "forgeron", "tisserand", "boulanger", "aubergiste", "herboriste", "vagabond", "berger", "aventurier"] and destination.habitants[cible_int].__dict__['attitude'] != "rival":
                choix_commerce = input("Souhaitez-vous vendre ou acheter ?")
                if choix_commerce == "vendre":
                    print(objet.poid_sac_joueur)
                    inventaire_ouvert = True
                    while inventaire_ouvert:
                        print("\n")
                        print("###################")
                        # x = 0
                        # for value in tuple(joueur.sac_joueur.inside.items()):
                        #     print("{} : ".format(x), end='')
                        #     print(value.__dict__['nom'], end=' ')
                        #     print("(" + value.__dict__['quantite'] + ")")
                        #     x = x + 1
                        x = 0
                        for i, k in enumerate(objet.sac_joueur.inside):
                            print(i, k, end=' ')
                            quantite_objet = len(tuple(objet.sac_joueur.inside.items())[x][1])
                            print("({})".format(quantite_objet))
                            x = x + 1
                        # objet.Objet.examiner(objettest1)
                        print("Quel objet de votre inventaire voulez-vous vendre ?")
                        try:
                            indice_inventaire = int(input("choisissez le numero (inventaire) > "))
                            if indice_inventaire in ['quitter', 'exit', 'quit', 'close', 'q']:
                                inventaire_ouvert = False
                            elif indice_inventaire == "":
                                continue
                            result = isinstance(indice_inventaire, int)
                            indice_inventaire = int(indice_inventaire)
                            objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]
                            # objet.Boisson.boire(objet_a_lindice)
                            nombre_quantite = input("Combien souhaitez vous en vendre ?")
                            nombre_quantite = int(nombre_quantite)
                            #print("vous mangez : " + tuple(objet.joueur.sac_joueur.inside.items())[indice_inventaire][0])
                            if objet.o1_denier not in etalage:
                                print("le commerçant n'a plus d'argent")
                            elif objet_a_lindice[0].valeur * nombre_quantite > len(etalage[objet.o1_denier]):
                                print("le commerçant n'a pas assez d'argent")
                            elif len(objet_a_lindice) < nombre_quantite:
                                print("Il n'y a pas assez de quantité disponible")
                            else:
                                etalage.ajouter(objet_a_lindice[0], nombre_quantite)
                                etalage.ajouter(objet.o1_denier, objet_a_lindice[0].valeur * nombre_quantite)
                                objet.sac_joueur.vendre(objet_a_lindice[0], nombre_quantite) #modif : cette ligne a été mis en dernier pour ne pas que l'objet se supprime avant detre ajoute à l'étalage
                                # etalage.retirer(objet_id)
                                inventaire_ouvert = False
                        except IndexError:
                            print("Vous n'avez pas plus d'objet à examiner")
                        except ValueError:
                            print("Vous ne pouvez qu'entrer des chiffres")
                            inventaire_ouvert = False
                else:
                    print("Quel objet souhaitez-vous examiner et éventuellement acheter ?")
                    print("voici l'étalage :")
                    etalage_ouvert = True
                    while etalage_ouvert:
                        x = 0
                        for i, k in enumerate(etalage.inside):
                            print(i, k, end=' ')
                            quantite_objet = len(tuple(etalage.inside.items())[x][1])
                            print("({})".format(quantite_objet))
                            x = x + 1
                        try:
                            indice_etalage = int(input("choisissez le numero (étalage) > "))
                            if indice_etalage in ['quitter', 'exit', 'quit', 'close', 'q']:
                                etalage_ouvert = False
                            result = isinstance(indice_etalage, int)
                            indice_etalage = int(indice_etalage)

                            try:
                                #joueur.sac_joueur.inside[0].items()
                                print("\n")
                                print(tuple(etalage.inside.items())[indice_etalage][0])
                                print(tuple(etalage.inside.items())[indice_etalage])
                                nom_id, objet_id = tuple(etalage.inside.items())[indice_etalage]
                                print(nom_id)
                                print(objet_id)
                                print("\n")
                                # for i, k in enumerate(tuple((etalage.inside.items())[indice_etalage][1]):
                                #     print(i, k)
                                objet_examen = True
                                while objet_examen:
                                    print("Actions possibles : examiner, negocier, voler, acheter")
                                    action_objet = input("" + tuple(etalage.inside.items())[indice_etalage][0] + " >")
                                    if action_objet == "acheter":
                                        nombre_quantite = input("Combien souhaitez vous en acheter ?")
                                        nombre_quantite = int(nombre_quantite)
                                        #print("vous mangez : " + tuple(objet.joueur.sac_joueur.inside.items())[indice_inventaire][0])
                                        if objet.o1_denier not in objet.sac_joueur:
                                            print("vous n'avez plus d'argent")
                                        elif objet_id[0].valeur * nombre_quantite > len(objet.sac_joueur[objet.o1_denier]):
                                            print("Pas assez d'argent")
                                        elif len(tuple(etalage.inside.items())[indice_etalage][1]) < nombre_quantite:
                                            print("Il n'y a pas assez de quantité disponible")
                                        else:
                                            # print(objet.__dict__['inside'])
                                            # print(objet_id)
                                            # print(objet_id[0])
                                            # print(objet_id[0].brut)
                                            # print(objet_id['inside'][1])
                                            # etalage.retirer(objet_id)
                                            etalage.retirer(objet_id[0], nombre_quantite)
                                            etalage.ajouter(objet.o1_denier, nombre_quantite * objet_id[0].valeur)
                                            objet.sac_joueur.acheter(objet_id[0], nombre_quantite)
                                            objet_examen = False
                                    elif action_objet == "negocier":
                                        # objet_a_lindice = tuple(etalage.inside.items())[indice_etalage][1]
                                        # objet.Objet.examiner(objet_a_lindice)
                                        prix_negociation = input("proposez un nouveau prix > ")
                                        print("le commerçant refuse la proposition")
                                    elif action_objet == "examiner":
                                        objet_a_lindice = tuple(etalage.inside.items())[indice_etalage][1]
                                        objet.Objet.examiner(objet_a_lindice[0])
                                    elif action_objet == "voler":
                                        vol_a_la_tire = random.randint(0,100)
                                        if vol_a_la_tire < joueur.mon_joueur.vol_a_la_tire:
                                            print("vous réussissez à subtiliser l'objet sans que le commerçant ne vous prenne !")
                                            objet.sac_joueur.voler(objet_id[0])
                                            # etalage.retirer(objet_id)
                                            etalage.retirer(objet_id[0])
                                            joueur.mon_joueur.vol_a_la_tire = joueur.mon_joueur.vol_a_la_tire + 0.1
                                            objet_examen = False
                                            #print(objet_a_lindice.__dict__["contenu"])
                                            #print(bibliotheque.carte_tarik["plan"]["plan"])
                                        else:
                                            print("C'est un échec mais vous avez acquis de l'expérience !")
                                            print("Le marchand veut votre peau !")
                                            joueur.mon_joueur.vol_a_la_tire = joueur.mon_joueur.vol_a_la_tire + 0.1
                                            decision = input("Vous fuyez ou vous tentez de raisonner le marchand ? (raisonner) = 1 (fuir) = 2 > ")
                                            if decision == "1":
                                                print("Vous arrivez à le raisonner et l'incident s'arrête ici")
                                                destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 100
                                                destination.reputation = destination.reputation - 10
                                            else:
                                                print("vous vous échappez avec succès mais votre réputation en a pris un coup !")
                                                destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 1000
                                                destination.reputation = destination.reputation - 100
                                            relationnel = destination.habitants[cible_int].__dict__['relationnel']
                                            peur = destination.habitants[cible_int].__dict__['peur']
                                            attirance = destination.habitants[cible_int].__dict__['attirance']
                                            if relationnel < -100 and peur > -100 and attirance < 1000 and peur < 100:
                                                print("{} vous considère comme un rival".format(destination.habitants[cible_int].__dict__['nom']))
                                                destination.habitants[cible_int].__dict__['attitude'] = "rival"
                                            objet_examen = False
                                            etalage_ouvert = False






                                    else:
                                        objet_examen = False
                            except IndexError:
                                print("Vous n'avez pas plus d'objet à examiner")
                            #except TypeError:
                            #    print("Vous ne pouvez qu'entrer des chiffres")
                        except ValueError:
                            print("Vous ne pouvez qu'entrer des chiffres")
                            etalage_ouvert = False
            else:
                print("La personne refuse de marchander avec vous")
    except ValueError:
        print("Vous ne pouvez qu'entrer des chiffres")
    except IndexError:
        print("Cette index n'existe pas")

def joueur_aide(action):

    print("""

COMMANDE MENU
c clear
q quit exit close quitter
sauvegarder

COMMANDE INFO
moi
temps
lieu
inventaire
carte*
personnage moi quisuije
(identite, etat, attribut, propriete/possession,*
armure, alignement, competence)*
equipe
ami
ennemi
serviteur
maison
propriete*
royaume*
diplomatie*

COMMANDE ACTION BASE
parler
attendre méditer dormir
bouger travel walk
examiner interact look
attaquer*
gifler*
assassiner*
voler*
embrasser*
serrer dans les bras*
serrer la main*
commercer
engager
provoquer*
hurler*
chanter*
danser*
imiter*
murmurer*

CUSTOM
suggerer une nouvelle action*

COMMANDE COMPETENCE
chasser
pecher
alchimie *
crochetage *
entretien*
equitation *
herboristerie*
furtivite*
vol_a_la_tire*
alcool*
maitre_chien*
soin*
marchandage *
forgeage *
armure_lourde *
armure_legere *
mental *
musique *
tannerie *
autorite *
telepathie *

Combat

combat *
deux_mains *
mains_nues *
defense*
arc *
arbalete *
pistolet *
epee*
massue*
hache*
parade*
bottes*

Magie

alteration*
destruction *
conjuration*
mysticisme*
illusion*
enchantement*
""")

# A FAIRE : voler, se cacher, ami, enemi, serviteur, infrastructure, equipe, declamer(discours, héraut, agitateur), vendre, politique, attaquer, prier

def joueur_clear(action):
    os.system('cls')


def joueur_inventaire(action):
    generer_monde()
    print(objet.poid_sac_joueur)
    inventaire_ouvert = True
    while inventaire_ouvert:
        print("\n")
        print("###################")
        x = 0
        for i, k in enumerate(objet.sac_joueur.inside):
            print(i, k, end=' ')
            quantite_objet = len(tuple(objet.sac_joueur.inside.items())[x][1])
            print("({})".format(quantite_objet))
            x = x + 1
        print("Quel objet de votre inventaire voulez-vous examiner ?")
        try:
            indice_inventaire = int(input("choisissez le numero (inventaire) > "))
            if indice_inventaire in ['quitter', 'exit', 'quit', 'close', 'q']:
                inventaire_ouvert = False
            elif indice_inventaire == "":
                continue
            result = isinstance(indice_inventaire, int)
            indice_inventaire = int(indice_inventaire)
            try:
                #joueur.sac_joueur.inside[0].items()
                print("\n")
                print(tuple(objet.sac_joueur.inside.items())[indice_inventaire][0])
                print("\n")
                for i, k in enumerate(inspect.getmembers(tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0], predicate=inspect.ismethod)):
                    print(i, k)
                objet_examen = True
                while objet_examen:
                    action_objet = input("" + tuple(objet.sac_joueur.inside.items())[indice_inventaire][0] + " >")
                    if action_objet == "manger":
                        # manger_pomme.play()
                        #print("vous mangez : " + tuple(joueur.sac_joueur.inside.items())[indice_inventaire][0])
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0]
                        objet.Nourriture.manger(objet_a_lindice)
                    elif action_objet == "jeter":
                        # jeter.play()
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0]
                        jeter_quantite = input("Combien souhaitez-vous en jeter ? > ")
                        jeter_quantite_int = int(jeter_quantite)
                        if jeter_quantite_int > len(tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]) :
                            print("Vous ne pouvez pas jeter autant d'objet")
                        else:
                            objet.Objet.jeter(objet_a_lindice, jeter_quantite)
                            # if len(tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]) == 0: #traduire ça directement dans la fonction retirer()
                            #     print(tuple(objet.sac_joueur.inside.items())[indice_inventaire][1])
                    elif action_objet == "examiner":
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0]
                        objet.Objet.examiner(objet_a_lindice)
                    elif action_objet == "lire":
                        # page.play()
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0]
                        objet.Livre.lire(objet_a_lindice)
                    elif action_objet == "porter":
                        # inventaire.play()
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0]
                        objet.Habit.porter(objet_a_lindice)
                    elif action_objet == "armer":
                        # inventaire.play()
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0]
                        print("main droite (1) ou main gauche (2) ?")
                        quelmain = input("> ")
                        if quelmain == "1":
                            emplacement = "main_droite"
                        elif quelmain == "2":
                            emplacement = "main_gauche"
                        objet.Arme.armer(objet_a_lindice, emplacement)
                    elif action_objet == "desarmer":
                        # inventaire.play()
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0]
                        print("main droite (1) ou main gauche (2) ?")
                        quelmain = input("> ")
                        if quelmain == "1":
                            emplacement = "main_droite"
                        elif quelmain == "2":
                            emplacement = "main_gauche"
                        objet.Arme.desarmer(objet_a_lindice, emplacement)
                    elif action_objet == "enlever":
                        # inventaire.play()
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0]
                        objet.Habit.enlever(objet_a_lindice)
                    elif action_objet == "boire":
                        # boire.play()
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1][0]
                        objet.Boisson.boire(objet_a_lindice)



                        #print(objet_a_lindice.__dict__["contenu"])
                        #print(bibliotheque.carte_tarik["plan"]["plan"])
                    else:
                        objet_examen = False
                #print(joueur.mon_joueur.inventaire_joueur[indice_inventaire])
                #objet.Habit.porter(objet.h1_habit_de_lin, joueur.mon_joueur.nom)
                #print(getattr(objet.h1_habit_de_lin, "nom"))
                #inspect.getmembers(objet.Habit, predicate=inspect.ismethod)
            except IndexError:
                print("Vous n'avez pas plus d'objet à examiner")
            #except TypeError:
            #    print("Vous ne pouvez qu'entrer des chiffres")

            if indice_inventaire in ['carte', 'map']:
                print(bibliotheque.carte_tarik["plan"]["plan"])
        except ValueError:
            print("Vous ne pouvez qu'entrer des chiffres")
            inventaire_ouvert = False


def joueur_engager(action):
    destination = generer_monde()
    print("Souhaitez-vous engager une personne ou desengager ?")
    # print(destination.__dict__["habitants"])
    choix_engager = input("> ")
    if choix_engager == "engager":
        habitants = destination.__dict__["habitants"]

        joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
        print("Qui souhaitez vous engager ? (indiquez le numero)")
        print("")
        print("personne disponible dans le lieu ou vous êtes :")
        x = 0
        for value in destination.habitants:
            attitude = destination.habitants[x].__dict__['attitude']
            print("{} : ".format(x), end='')
            print(value.__dict__['nom'], end=' ')
            print(value.__dict__['age'], end=' ')
            print("ans", end=' ')
            print(value.__dict__['travail'], end=' ')
            print(value.__dict__['vivant'])
            x = x + 1
        #print(destination.habitants)
        #print(destination.habitants[0].__dict__['nom'])
        try:
            cible = input("engager > ")
            cible_int = int(cible)
            habitant_cible = destination.__dict__["habitants"][cible_int]
            attitude = destination.habitants[cible_int].__dict__['attitude']
            nom = destination.habitants[cible_int].__dict__['nom']
            if destination.habitants[cible_int].__dict__['vivant'] == "X":
                print("La personne est morte...")
            else:
                if attitude == "ami" or attitude == "serviteur":
                    equipe.append(habitant_cible)
                    habitants.remove(habitant_cible)
                    print("Vous avez un nouveau membre dans votre équipe !")
                else:
                    print("la personne refuse de vous suivre, essayez d'en faire un ami ou un serviteur avant de l'engager")
        except ValueError:
            print("Vous ne pouvez qu'entrer des chiffres")
        except IndexError:
            print("L'index n'existe pas")
    else:
        print("Qui souhaitez-vous désengager ?")
        print("")
        print("Mon équipe")
        i = 0
        for value in equipe:
            print(i, end=" : ")
            print(equipe[i].__dict__)
            print("")
            i = i + 1
        try:
            cible = input("desengager > ")
            cible_int = int(cible)
            equipier_cible = equipe[cible_int]
            attitude = destination.habitants[cible_int].__dict__['attitude']
            nom = destination.habitants[cible_int].__dict__['nom']
            if destination.habitants[cible_int].__dict__['vivant'] == "X":
                print("La personne est morte...")
            else:
                if attitude != "amant":
                    equipe.remove(equipier_cible)
                    destination.__dict__["habitants"].append(equipier_cible)
                else:
                    print("la personne vous aime et refuse de vous quitter, essayez d'en faire un enemi ou un serviteur")
        except ValueError:
            print("Vous ne pouvez qu'entrer des chiffres")
        except IndexError:
            print("L'index n'existe pas")






#Created by Lukas Pacalon
#### jeu FUNCIONALITY ####

def generer_monde():
    # print("Generateur de monde en marche...")
    # sac_joueur = objet.Contenant("sac joueur")
    try:
        joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
        joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
        destination = lieu.carte[joueur.mon_joueur.localisationX + "/" + joueur.mon_joueur.localisationY]
        itera = destination
    except KeyError:
        d = n1.__dict__
        for key, value in d.items():
            print("")
            print("#######################")
            print("Nouveau lieu découvert!")
            print(d[key])
            iter = d[key]

        n1.__next__()
        iter = lieu.Lieu(iter)
        lieu.carte[joueur.mon_joueur.localisationX + "/" + joueur.mon_joueur.localisationY] = iter
        destination = lieu.carte[joueur.mon_joueur.localisationX + "/" + joueur.mon_joueur.localisationY]
        itera = destination
        # itera = personnage.Generateur(itera)
        itera = personnage.GenerateurPersonnage()
        x = 0
        destination.habitants = itera.objets
        if destination.construction[0] in ["citadelle", "acropole", "palais", "archiduchet"]:
            niveau = 5
            chef = 1.5
            itera.genererPersonnage(chef)
        elif destination.construction[0] in ["cité", "baronnerie", "forteresse", "duchet", "comté", "bastille", "grand fort"]:
            niveau = 4
            chef = 1.4
            itera.genererPersonnage(chef)
        elif destination.construction[0] in ["bourg", "ville", "bastion", "château", "krak", "zone agricole", "zone industriel", "fort", "manoir"]:
            niveau = 3
            chef = 1.3
            itera.genererPersonnage(chef)
        elif destination.construction[0] in ["zone agricole", "fermes", "zone industriel"]:
            niveau = 3.1
        elif destination.construction[0] in ["village", "commune", "bourgade", "feu de camps", "campement"]:
            niveau = 2
            chef = 1.2
            itera.genererPersonnage(chef)
        elif destination.construction[0] in ["cabane", "pavillon", "caravane", "maison isolé"]:
            niveau = 1
        elif destination.construction[0] in ["sanctuaire", "monastere"]:
            niveau = 1.1
        elif destination.construction[0] in ['chapelle', 'eglise', "clôcher"]:
            niveau = 0
            chef = 2.1
            itera.genererPersonnage(chef)
        elif destination.construction[0] in ['abbaye', 'basilique']:
            niveau = 0
            chef = 2.2
            itera.genererPersonnage(chef)
        elif destination.construction[0] in ['tour isolé']:
            niveau = 0
            chef = 2.3
            itera.genererPersonnage(chef)
        elif destination.construction[0] in ['temple', 'sanctuaire']:
            chef = 2.4
            niveau = 1.21
            itera.genererPersonnage(chef)
        elif destination.construction[0] in ["vide", "ruines", "repaire"]:
            niveau = 0
        elif destination.construction[0] in ["donjon"]:
            niveau = 0.1
        elif destination.construction[0] in ["mausolee", "crypte", "sepulcre", "tombeau"]:
            niveau = 0.2



        while x < destination.nbr_habitant:
            itera.genererPersonnage(niveau)
            # y = itera.genererPersonnage()
            travail = destination.habitants[x].__dict__['travail']
            etalage = destination.habitants[x].__dict__['etalage']
            # print(travail)
            if travail in ["boulanger"]:
                boulangerie = infrastructure.Infrastructure("boulangerie", joueur.mon_joueur.localisationX, joueur.mon_joueur.localisationY)
                destination.habitants[x].propriete.append(boulangerie)
                for loop in range(600):
                    etalage.ajouter(objet.o1_denier)
                for loop in range(20):
                    etalage.ajouter(objet.n4_pain)
                for loop in range(10):
                    etalage.ajouter(objet.n4_farine)
                for loop in range(10):
                    etalage.ajouter(objet.n4_avoine)
                for loop in range(10):
                    etalage.ajouter(objet.n4_ble)
                for loop in range(10):
                    etalage.ajouter(objet.n4_seigle)

            elif travail in ["marchand"]:
                maison = infrastructure.Infrastructure("maison", joueur.mon_joueur.localisationX, joueur.mon_joueur.localisationY)
                destination.habitants[x].propriete.append(maison)
                for loop in range(1250):
                    etalage.ajouter(objet.o1_denier)
                for loop in range(10):
                    etalage.ajouter(objet.h1_chemise_de_lin)
                for loop in range(5):
                    etalage.ajouter(objet.h2_chaussure_de_cuir)
                for loop in range(10):
                    etalage.ajouter(objet.h3_braies_de_lin)
                for loop in range(50):
                    etalage.ajouter(objet.d1_allumette)
                for loop in range(200):
                    etalage.ajouter(objet.d1_clou)
                for loop in range(10):
                    etalage.ajouter(objet.d1_bandage)
                for loop in range(2):
                    etalage.ajouter(objet.d1_louche)
                for loop in range(10):
                    etalage.ajouter(objet.d1_assiette)
                for loop in range(2):
                    etalage.ajouter(objet.h2_chaussons)
                for loop in range(10):
                    etalage.ajouter(objet.h2_houseaux)
                for loop in range(5):
                    etalage.ajouter(objet.h4_manteau)
                for loop in range(10):
                    etalage.ajouter(objet.h4_couverture)
                for loop in range(2):
                    etalage.ajouter(objet.h10_tunique_noble)
                for loop in range(10):
                    etalage.ajouter(objet.b1_bouteille_vin_rouge)
                etalage.ajouter(objet.o1_canne_a_peche)


            elif travail in ["forgeron"]:
                forge = infrastructure.Infrastructure("forge", joueur.mon_joueur.localisationX, joueur.mon_joueur.localisationY)
                destination.habitants[x].propriete.append(forge)
                for loop in range(950):
                    etalage.ajouter(objet.o1_denier)
                for loop in range(10):
                    etalage.ajouter(objet.a1_epee_fer)
                for loop in range(2):
                    etalage.ajouter(objet.a1_epee_batarde)
                for loop in range(5):
                    etalage.ajouter(objet.a2_bouclier_fer)
                for loop in range(2):
                    etalage.ajouter(objet.a2_grand_bouclier)
                for loop in range(5):
                    etalage.ajouter(objet.a5_hache_courte)
                for loop in range(5):
                    etalage.ajouter(objet.a3_arc_simple)
                for loop in range(10):
                    etalage.ajouter(objet.a13_hallebarde)
                for loop in range(5):
                    etalage.ajouter(objet.a1_epee_acier)
                for loop in range(5):
                    etalage.ajouter(objet.a16_marteau)
                for loop in range(10):
                    etalage.ajouter(objet.a17_pique)
                for loop in range(10):
                    etalage.ajouter(objet.a19_fourche)
                for loop in range(10):
                    etalage.ajouter(objet.a19_faucille)
                for loop in range(100):
                    etalage.ajouter(objet.a7_fleche_fer)
                for loop in range(20):
                    etalage.ajouter(objet.a14_dague)

            elif travail in ["berger"]:
                bergerie = infrastructure.Infrastructure("bergerie", joueur.mon_joueur.localisationX, joueur.mon_joueur.localisationY)
                destination.habitants[x].propriete.append(bergerie)
                etalage.ajouter(objet.a19_fourche)


            elif travail in ["tisserand"]:
                atelier_de_tisserand = infrastructure.Infrastructure("atelier_de_tisserand", joueur.mon_joueur.localisationX, joueur.mon_joueur.localisationY)
                destination.habitants[x].propriete.append(atelier_de_tisserand)
                for loop in range(350):
                    etalage.ajouter(objet.o1_denier)
                for loop in range(40):
                    etalage.ajouter(objet.h1_chemise_de_lin)
                for loop in range(5):
                    etalage.ajouter(objet.h2_chaussure_de_cuir)

            elif travail in ["herboriste"]:
                apothicaire = infrastructure.Infrastructure("apothicaire", joueur.mon_joueur.localisationX, joueur.mon_joueur.localisationY)
                destination.habitants[x].propriete.append(apothicaire)
                for loop in range(750):
                    etalage.ajouter(objet.o1_denier)
                for loop in range(10):
                    etalage.ajouter(objet.n8_menthe)
                for loop in range(10):
                    etalage.ajouter(objet.n8_acerola)
                for loop in range(10):
                    etalage.ajouter(objet.n7_miel)
                for loop in range(2):
                    etalage.ajouter(objet.n8_cytise)
                for loop in range(2):
                    etalage.ajouter(objet.n8_melisse)
                for loop in range(2):
                    etalage.ajouter(objet.n8_fenouille)
                for loop in range(2):
                    etalage.ajouter(objet.n8_cassis)
                for loop in range(5):
                    etalage.ajouter(objet.n8_valeriane)
                for loop in range(5):
                    etalage.ajouter(objet.n8_artichaud)
                for loop in range(20):
                    etalage.ajouter(objet.d1_bandage)

            elif travail in ["aubergiste"]:
                auberge = infrastructure.Infrastructure("auberge", joueur.mon_joueur.localisationX, joueur.mon_joueur.localisationY)
                destination.habitants[x].propriete.append(auberge)
                for loop in range(500):
                    etalage.ajouter(objet.o1_denier)
                for loop in range(2):
                    etalage.ajouter(objet.n7_miel)
                for loop in range(2):
                    etalage.ajouter(objet.n5_boeuf)
                for loop in range(10):
                    etalage.ajouter(objet.n2_pomme)
                for loop in range(10):
                    etalage.ajouter(objet.n5_sardine)
                for loop in range(2):
                    etalage.ajouter(objet.n7_tarte)
                for loop in range(20):
                    etalage.ajouter(objet.n7_viande_seche)
                for loop in range(10):
                    etalage.ajouter(objet.n7_soupe)
                for loop in range(5):
                    etalage.ajouter(objet.n6_fromage)
                for loop in range(20):
                    etalage.ajouter(objet.n7_biscuit)
                for loop in range(20):
                    etalage.ajouter(objet.b1_bouteille_biere)
            elif travail in ["vagabond", "mendiant", "voyageur", "aventurier"]:
                for loop in range(2):
                    etalage.ajouter(objet.o1_denier)
            else:
                maison = infrastructure.Infrastructure("maison", joueur.mon_joueur.localisationX, joueur.mon_joueur.localisationY)
                destination.habitants[x].propriete.append(maison)
                etalage.ajouter(objet.d1_bandage)
            x = x + 1
        # destination.habitants = itera.objets
    return destination

def joueur_test(action):
    destination = generer_monde()


    #ajouter
    #retirer
    #acheter
    #vendre
    # vendre tout son stock ne l'affiche pas dans l'inventaire du marchand
    #voler

    # chasser/pecher
    # travailler
    # cambrioler
    # vol à la tir
    # reputation dans chaque ville
    # prison
    # combat seul temps reel
    # se faire accoster dans les deplacements
    # afficher la carte (vert foncé = foret) (gris = montagne) (marron = village) (jaune/vert = plaine) (bleu = lac/mer) (autrecouleur X = ville appartenant à un seigneur X)
    # equipe => armee
    # infrastructure (en lien avec les métiers des habitants)
    # village et ville plus espacé (traverser des forets et des des fortes avant de trouver une ville)
    # gérer la diplomatie et les royaumes ainsi que les empires + alliances et races
    # sauvegarde de plusieurs classes
    # quetes qui apparaissent selon la date du jour
    # ( 2 evenements par jour) / ( 3 quetes secondaires par semaine ) / ( 4 evements principales par mois ) / ( 5 longues quetes par an )
    # etre seigneur en mode stronghold
    # Naturalisé l'apparition de la nature et de la vie humaine (determiner la taille des empires)
    # stats selon le temps (ex : l'argent) (force) (nombre de transactions) (nombre de population/ville/foret croisé)
    # niveau de noblesse

    # objectifs ? ===> survivre ? statut ? guilde ? assassinat ? argent ? noblesse ? pouvoir ? terres ? quetes ? gloire ? armée ? bienfait ? malfait ? demoniaque ? equilibre ? nature ?
    # objectifs 2 ? redorer le blason de sa famille ? retrouver ses ancetres, connaitre son histoire ? elever ses enfants pour perdurer la famille
    # score

    # statut et type de quete (principale, secondaire, annexe)
    # statut : vagabond, aventurier, citoyen, hero, noble, seigneur, roi, empereur,

    # interface , graphisme
    # réaliste apprentissage réalité virtuelle #reflexe #habilité
    # Apprentissage pour moi de la BI de l'IA big data machine learning Procédural etc...

    #     Quetes : ressources
    # Quetes : recherche
    # Quetes : monstre
    # Quetes : rumeur
    # Quetes : trésor
    # Quetes : chasse
    # Quetes : nettoyage
    # Quetes : identité
    # Quetes : spiritualité
    # Quetes :
    #
    # Quetes : défense
    # Quetes : guilde
    # Quetes : relique
    # Quetes : romantique
    # Quetes : course
    # Quetes : commercial
    # Quetes : inspecteur
    # Quetes : manuscrit
    # Quetes : paléontologie
    # Quetes : astronomie
    # Quetes : médecine
    #
    # Quetes : siège
    # Quetes : attaque
    # Quetes : escarmouche
    # Quetes : paix/guerre
    # Quetes : politique
    # Quetes : diplomatique
    # Quetes : évasion
    # Quetes : embuscade
    # Quetes : hotage
    # Quetes :
    #
    # Quetes : noblesse
    # Quetes : artefact
    # Quetes : pèlerinage
    # Quetes :
    #
    # Guildes :
    # - Guerrier
    # - Mage
    # - Voleur
    # - Assassin
    # - Prêtre
    # - Barde
    # - Marchand
    # -
    #
    #
    # GESTION royaume seigneur(stronghold)
    # Ressources
    # Réputation
    # Joie du peuple
    # Vivres +
    # Aubergiste +
    # Religion cierge +
    # Décoration +
    # Aménagements +
    # Medecin +
    # Magicien -
    # Impôts -
    # Crimes -
    # Gestion déchets -
    # Maladie / rats -
    # Immigration -
    # Incendie -
    # Sécheresse -
    # Hérésie -
    #
    #
    # Naissances et début de l'histoire (prise d'une famille random sans nom)
    # si tu meurt tu joue le frère ou un autre membre de la famille
    # jusqu'à la mort de la famille et le passage à une nouvelle famille
    # Armée
    # Bon / mauvais / neutre
    # Paix / guerre
    # Flaneur / travail acharné
    #
    # Famille
    # Chômeur
    #
    # Objectifs
    # Dépend de l'alignement :
    # Bon
    # Neutre
    # Mauvais
    #
    # Chaotique
    # Neutre
    # Loyal

    # multijoueur :
    # le jeu est comme un monde parallèle qui ne sarrête jamais
    # on commence le jeu dans la peau d'un personnage déjà agé aléatoire dont on joura la Famille, on peux tomber sur la famille d'un autre joueur
    # si on met pause, le personnage agit comme un png et peut très bien mourir car le jeu continue même si on ne joue pas
    # si le joueur meurt on joue un autre personnage de la famille
    # on peut paraméter les actions d'un joueur pour qu'il fasse des actions spécifiques en l'absence du joueur
    # on peut mettre des alertes en cas d'attaque mais il faut accepter de changer de personnage de la famille souvent

    # afficher la carte générée







def main_jeu_loop():
    while joueur.mon_joueur.mort is False:
        prompt()
    # Here handle if puzzle resolution, boss defeated, explored everything, etc...

def config_jeu():
    os.system('cls')
    joueur.meteo_changement()
    # joueur_son_off("action")
    #nom
    qqq = ""
    question1 = "Fermier de Tarik dit : Hey! Reveille toi ! Tu peux pas rester ici ! C'est mon champs, je dois défricher avant l'arrivee du maire de Tarik ! C'est quoi ton nom au juste ? \n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.0000001)
    joueur_nom = input("> ")
    joueur.mon_joueur.nom = joueur_nom

    #race HANDLING
    qqq2 = ""
    question2 = "par contre dis moi... tu as une drôle de tête.. D'ou viens-tu ? ( Elfe des Bois (1), Nain des Montagnes (2), Homme du Sud (3), Homme d'Asie (4), Homme d'Afrique (5), Homme du Caucase (6), Homme du Nord (7), Nain des Collines (8), Hallefling des Collines (9), Petite Personne (10), Haut-Elfe des Steppes (11), Elfe Noir (12), Orc (13), Demi-Orc (14), Demi-Elfe (15)). "
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00000001)
    joueur_race = input("> ")
    joueur.mon_joueur.race = joueur_race

    #joueur STAT
    if joueur.mon_joueur.race == '1':
        joueur.mon_joueur.pv = 120
        joueur.mon_joueur.mp = 20
    elif joueur.mon_joueur.race == '2':
        joueur.mon_joueur.pv = 40
        joueur.mon_joueur.mp = 120
    elif joueur.mon_joueur.race == '3':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '4':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '5':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '6':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '7':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '8':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '9':
        joueur.mon_joueur.pv = 40
        joueur.mon_joueur.mp = 120
    elif joueur.mon_joueur.race == '10':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '11':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '12':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '13':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '14':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    elif joueur.mon_joueur.race == '15':
        joueur.mon_joueur.pv = 60
        joueur.mon_joueur.mp = 60
    #INTRO
    qqq3 = ""
    question3 = "Fermier de Tarik dit : Hum... Je n'aime pas les gens de votre race dans le coin. " + joueur.mon_joueur.nom + " le... " + joueur_race + " je vous conseille de déguerpir au plus vite avant l'arrivé des chevaliers.\n Fermier de Tarik s'en va... "
    reponsehumain = "Fermier de Tarik dit : Ok bon... " + joueur.mon_joueur.nom + ", je vous conseille de déguerpir au plus vite avant l'arrivé des chevaliers.\n Fermier de Tarik s'en va... "
    if joueur_race == "humain":
        for character in reponsehumain:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.00000001)
    else:
        for character in question3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.0000001)

    speech1 = "L'aventure commence !"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00000001)

    print("")
    print("Tu es prêt pour l'aventure mais premièrement répond à deux questions...")
    print("Entre le bon numéro :")
    print("")
    print("Quel est ton plus grand désir ?")
    print("L'Or (1) L'Amour (2) Le Bonheur (3) La Gloire (4) La Sagesse (5) Le Plaisir (6) Le Voyage (7) L'Immortalité (8)")
    desir = input("> ")
    joueur.mon_joueur.desir = desir
    print("")
    print("Quel est ta plus grande peur ?")
    print("La Mort (1) La Vieillesse (2) L'Inconnu (3) L'Infini (4) La Perte (5) La Fin Du Monde (6) La Maladie (7) Dieu (8) ")
    peur = input("> ")
    joueur.mon_joueur.peur = peur

    sys.stdout.flush()
    print(" C'est parti !")
    print(" tape le mot 'guide' si tu sais pas quoi faire !")
    main_jeu_loop()

title_screen()

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
#Created by Lukas Pacalon




    # inventaire_exemple.acheter(objet.b1_bouteille_biere)

#Created by Lukas Pacalon
