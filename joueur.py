# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural

from threading import Thread
import time
import sched
import sys
import datetime
from datetime import timedelta
import random
import quete

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
# sec = pygame.mixer.Sound("bande_sonore/atmosphere/campagne.ogg")
# pluie = pygame.mixer.Sound("bande_sonore/atmosphere/pluie.ogg")
# orage = pygame.mixer.Sound("bande_sonore/atmosphere/orage.ogg")
# vent = pygame.mixer.Sound("bande_sonore/atmosphere/campagne_vent.ogg")
# grele = pygame.mixer.Sound("bande_sonore/atmosphere/vent_foret.ogg")
# neige = pygame.mixer.Sound("bande_sonore/atmosphere/vent_moyen.ogg")
# nuit3 = pygame.mixer.Sound("bande_sonore/atmosphere/nuit3.ogg")
# nuit2 = pygame.mixer.Sound("bande_sonore/atmosphere/nuit2.ogg")
# nuit1 = pygame.mixer.Sound("bande_sonore/atmosphere/nuit.ogg")
# hibou = pygame.mixer.Sound("bande_sonore/creature/hibou.ogg")
# loup = pygame.mixer.Sound("bande_sonore/creature/loup.ogg")
# vent_faible = pygame.mixer.Sound("bande_sonore/atmosphere/vent_faible.ogg")
# chouette = pygame.mixer.Sound("bande_sonore/creature/chouette.ogg")



#inventaire_initial = [objet.h1.__dict__, objet.h2.__dict__, objet.d1.__dict__, objet.n1.__dict__, objet.n2.__dict__]
niveau = 0
#inventaire_initial = [objet.h1_habit_de_lin.__dict__, objet.h2_chaussure_de_cuir.__dict__, objet.l1_carte_tarik.__dict__, objet.n1_bout_de_pain.__dict__, objet.n2_pomme.__dict__]
# inventaire_initial = 1
livre_datetime = datetime.datetime(1426, 1, 31, 8, 27, 0)


##### joueur config #####
class joueur:
    def __init__(self):
        #identite
        self.nom = ''
        self.race = ''
        self.alignement = ''
        self.personnalite = ''
        self.statut = []
        self.noblesse = ""
        self.reputation = 0
        self.renomee = 0
        self.quetes_principales = []
        self.quetes_secondaires = []
        self.quetes_meta = [quete.survivre]
        self.desir = ''
        self.peur = ''

        #etat
        self.mort = False
        self.niveau = niveau
        self.travail = "joueur"
        self.faim = 1000
        self.soif = 1000
        self.energie = 1000
        self.pv = 200
        self.mp = 100
        self.cc = 20
        self.ct = 20
        self.force = 20
        self.endurance = 10
        self.agilite = 20
        self.dexterite = 20
        self.intelligence = 20
        self.force_mentale = 20
        self.socialibilite = 20
        self.furtif = False

        #aptitudes
        self.charisme = 10
        self.equivoque = 10
        self.eloquence = 10
        self.vitalite = 10
        self.visibile = 0
        self.bruit = 0
        self.vitesse = 0

        #lieu
        self.localisationX = 0
        self.localisationY = 0

        #temps
        self.journuit = "jour"
        self.saisontemps = "hiver"
        self.meteotemps = "pluie"
        self.jourtemps = "Mardi"
        self.livre_datetime = livre_datetime

        #possession
        self.inventaire_joueur = {}
        self.domaine = []
        self.infrastructure = []
        self.equipe = ''
        self.citoyen = ''
        self.armee = ''

        #armure
        self.tete = 0
        self.torse = 0
        self.jambes = 0
        self.bras = 0
        self.pieds = 0
        self.mains = 0
        self.main_droite = 0
        self.main_gauche = 0
        self.doigts = 0
        self.cou = 0
        self.protection_tete = 0
        self.protection_torse = 0
        self.protection_bras = 0
        self.protection_jambes = 0
        self.protection = 0
        self.temperature = 36

        #competences
        self.chasse = 0
        self.peche = 0
        self.relationnel = 0
        self.alchimie = 0
        self.crochetage = 0
        self.entretien = 0
        self.equitation = 0
        self.herboristerie = 0
        self.furtivite = 0
        self.vol_a_la_tire = 0
        self.alcool = 0
        self.maitre_chien = 0
        self.soin = 0
        self.marchandage = 0
        self.forgeage = 0
        self.armure_lourde = 0
        self.armure_legere = 0
        self.mental = 0
        self.musique = 0
        self.tannerie = 0
        self.autorite = 0
        self.telepathie = 0

        #combat
        self.combat = 0
        self.deux_mains = 0
        self.mains_nues = 0
        self.defense = 0
        self.arc = 0
        self.arbalete = 0
        self.pistolet = 0
        self.epee = 0
        self.massue = 0
        self.hache = 0
        self.parade = 0
        self.bottes = []
        self.technique = "defenseur"

        #magie
        self.alteration = 0
        self.destruction = 0
        self.conjuration = 0
        self.mysticisme = 0
        self.illusion = 0
        self.enchantement = 0



        #stats
        # Matplotlib



        print("Création du Joueur", self)


    def quisuisje(self):
        print("#INFO PERSONNAGE#")
        print('')
        print('#identite')
        print("nom : ".format(self.nom))
        print("race : {}".format(self.race))
        print("alignement : {}".format(self.alignement))
        print("personnalite : {}".format(self.personnalite))
        print("statut : {}".format(self.statut))
        print("noblesse : {}".format(self.noblesse))
        print("reputation : {}".format(self.reputation))
        print("renomee : {}".format(self.renomee))

        print("quetes_principales : {}".format(self.quetes_principales))
        print("quetes_secondaires : {}".format(self.quetes_secondaires))
        print("quetes_meta : {}".format(self.quetes_meta))

        print('')
        print('#etat')
        print("mort : {}".format(self.mort))
        print("niveau : {}".format(self.niveau))
        print("travail : {}".format(self.travail))
        print("faim : {}".format(self.faim))
        print("soif : {}".format(self.soif))
        print("energie : {}".format(self.energie))
        print("pv : {}".format(self.pv))
        print("mp : {}".format(self.mp))
        print("force : {}".format(self.force))
        print("endurance : {}".format(self.endurance))

        print('')
        print('#aptitudes')
        print("intelligence : {}".format(self.intelligence))
        print("agilite : {}".format(self.agilite))
        print("charisme : {}".format(self.charisme))
        print("equivoque : {}".format(self.equivoque))
        print("eloquence : {}".format(self.eloquence))
        print("vitalite : {}".format(self.vitalite))
        print("visibile : {}".format(self.visibile))
        print("bruit : {}".format(self.bruit))
        print("vitesse : {}".format(self.vitesse))

        print('')
        print('#possession')
        #possession
        print("inventaire_joueur : {}".format(self.inventaire_joueur))
        print("domaine : {}".format(self.domaine))
        print("infrastructure : {}".format(self.infrastructure))
        print("equipe : {}".format(self.equipe))
        print("citoyen : {}".format(self.citoyen))
        print("armee : {}".format(self.armee))

        print('')
        print('#armure')
        #armure
        print("tete : {}".format(self.tete))
        print("torse : {}".format(self.torse))
        print("jambes : {}".format(self.jambes))
        print("bras : {}".format(self.bras))
        print("pieds : {}".format(self.pieds))
        print("mains : {}".format(self.mains))
        print("doigts : {}".format(self.doigts))
        print("cou : {}".format(self.cou))
        print("protection : {}".format(self.protection))
        print("temperature : {}".format(self.temperature))


        # print("#INFO LIEU#")
        # print("localisationX : ({}) localisationY : ({})".format(self.localisationX, self.localisationY))
        # print("")
        # print("#INFO TEMPS#")
        # print("{} {}".format(self.livre_datetime, self.saisontemps))
        # print("({}) {}".format(self.meteotemps, self.jourtemps))
        # print("{}".format(self.journuit))

    def parler(self, message):
        print("{} a dit : {}".format(self.nom, message))

    def Regarder_inventaire(self):
        print("{}".format(self.inventaire_joueur))

    def lire(ouvrage):
        print(ouvrage)

    # TEMPS ET EVENEMENTS

    def travail_heure(self, heure):
        if heure == 1:
            print("{} heure est passée ".format(heure))
        else:
            print("{} heures sont passées ".format(heure))
        global livre_datetime
        livre_datetime = livre_datetime + timedelta(hours=heure)
        if heure > 2:
            meteo_changement()

    def heure(self, heure):
        self.energie = self.energie  - (heure * (3600 * 0.0002))
        self.faim = self.faim - (heure * (3600 * 0.00004))
        self.soif = self.soif - (heure * (3600 * 0.0004))
        if heure == 1:
            print("{} heure est passée ".format(heure))
        else:
            print("{} heures sont passées ".format(heure))
        global livre_datetime
        livre_datetime = livre_datetime + timedelta(hours=heure)
        if heure > 2:
            meteo_changement()

    def dormir(self):
        print("Combien de temps souhaitez vous dormir ?")
        temps_sommeil = input("temps de sommeil en heure : >")
        try:
            temps_sommeil = int(temps_sommeil)
            self.energie = self.energie + (temps_sommeil * 10)
            self.faim = self.faim - (temps_sommeil * (3600 * 0.00004))
            self.soif = self.soif - (temps_sommeil * (3600 * 0.0004))
            global livre_datetime
            livre_datetime = livre_datetime + timedelta(hours=temps_sommeil)
            meteo_changement()
            temps_sommeil = str(temps_sommeil)
            print("Vous dormez à même le sol pendant " + temps_sommeil + " heures")
        except ValueError:
            print("Vous devez rentrer un chiffre !")


    def attendre(self):
        print("Combien de temps souhaitez vous attendre ?")
        temps_attente = input("temps d'attente en heure : >")
        try:
            temps_attente = int(temps_attente)
            self.energie = self.energie  - (temps_attente * (3600 * 0.0002))
            self.faim = self.faim - (temps_attente * (3600 * 0.00004))
            self.soif = self.soif - (temps_attente * (3600 * 0.0004))
            global livre_datetime
            livre_datetime = livre_datetime + timedelta(hours=temps_attente)
            meteo_changement()
            temps_attente = str(temps_attente)
            print("Vous attendez pendant " + temps_attente + " heures")
        except ValueError:
            print("Vous devez rentrer un chiffre !")


    def mediter(self):
        print("Combien de temps souhaitez vous méditer ?")
        temps_meditation = input("temps de méditation en heure : >")
        try:
            temps_meditation = int(temps_meditation)
            self.energie = self.energie  - (temps_meditation * (3600 * 0.00002))
            self.faim = self.faim - (temps_meditation * (3600 * 0.00004))
            self.soif = self.soif - (temps_meditation * (3600 * 0.0004))
            global livre_datetime
            livre_datetime = livre_datetime + timedelta(hours=temps_meditation)
            meteo_changement()
            temps_meditation = str(temps_meditation)
            print("Vous méditez pendant " + temps_meditation + " heures")
        except ValueError:
            print("Vous devez rentrer un chiffre !")




mon_joueur = joueur()

def meteo_changement():
    if mon_joueur.saisontemps == "printemps":
        meteo_printemps()
    elif mon_joueur.saisontemps == "été":
        meteo_ete()
    elif mon_joueur.saisontemps == "automne":
        meteo_automne()
    else:
        meteo_hiver()


def meteo_printemps():
    meteo = ["sec", "pluie", "orage", "vent", "neige", "grêle"]
    meteo = random.choices(meteo, weights=(50, 40, 10, 30, 1, 0.1), k=1)
    mon_joueur.meteotemps = meteo
    play_meteo_sound()
def meteo_ete():
    meteo = ["sec", "pluie", "orage", "vent", "neige", "grêle"]
    meteo = random.choices(meteo, weights=(60, 20, 20, 10, 1, 0.1), k=1)
    mon_joueur.meteotemps = meteo
    play_meteo_sound()
def meteo_automne():
    meteo = ["sec", "pluie", "orage", "vent", "neige", "grêle"]
    meteo = random.choices(meteo, weights=(10, 40, 40, 40, 10, 1), k=1)
    mon_joueur.meteotemps = meteo
    play_meteo_sound()
def meteo_hiver():
    meteo = ["sec", "pluie", "orage", "vent", "neige", "grêle"]
    meteo = random.choices(meteo, weights=(10, 40, 10, 60, 40, 1), k=1)
    mon_joueur.meteotemps = meteo
    play_meteo_sound()

def play_meteo_sound():
    print(mon_joueur.journuit)
    if mon_joueur.journuit == "nuit":
        stop_meteo_sound()
        randnocturne = random.randint(1, 6)
        if randnocturne == 1:
            pass
            # hibou.play(100)
        elif randnocturne == 2:
            pass
            # nuit3.play(100)
        elif randnocturne == 3:
            pass
            # nuit2.play(100)
        elif randnocturne == 4:
            pass
            # nuit1.play(100)
            # chouette.play(100)
        elif randnocturne == 5:
            pass
            # vent_faible.play(100)
        elif randnocturne == 6:
            pass
            # loup.play(100)

    if mon_joueur.meteotemps[0] == "sec" and mon_joueur.journuit == "jour":
        stop_meteo_sound()
        # sec.play(100)
    elif mon_joueur.meteotemps[0] == "pluie":
        stop_meteo_sound()
        # pluie.play(100)
    elif mon_joueur.meteotemps[0] == "orage":
        stop_meteo_sound()
        # orage.play(100)
    elif mon_joueur.meteotemps[0] == "vent":
        stop_meteo_sound()
        # vent.play(100)
    elif mon_joueur.meteotemps[0] == "neige":
        stop_meteo_sound()
        # neige.play(100)
    else:
        stop_meteo_sound()
        # grele.play(100)

def stop_meteo_sound():
    pass
    # sec.stop()
    # pluie.stop()
    # orage.stop()
    # vent.stop()
    # neige.stop()
    # grele.stop()
    # nuit3.stop()
    # nuit2.stop()
    # nuit1.stop()
    # hibou.stop()
    # loup.stop()
    # vent_faible.stop()
    # chouette.stop()

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        while (True):
            self.foo()
            self.poid()
            time.sleep(1)
            global livre_datetime
            livre_datetime = livre_datetime + timedelta(seconds=0.1)
            mon_joueur.livre_datetime = livre_datetime
            # get the current day of the year
            doy = livre_datetime.timetuple().tm_yday
            # "day of year" ranges for the northern hemisphere
            printemps = range(80, 172)
            ete = range(172, 264)
            automne = range(264, 355)
            # winter = everything else
            if doy in printemps:
              saison = 'printemps'
            elif doy in ete:
              saison = 'été'
            elif doy in automne:
              saison = 'automne'
            else:
              saison = 'hiver'

            if livre_datetime.weekday() == 0:
                jour_semaine = "Lundi"
            elif livre_datetime.weekday() == 1:
                jour_semaine = "Mardi"
            elif livre_datetime.weekday() == 2:
                jour_semaine = "Mercredi"
            elif livre_datetime.weekday() == 3:
                jour_semaine = "Jeudi"
            elif livre_datetime.weekday() == 4:
                jour_semaine = "Vendredi"
            elif livre_datetime.weekday() == 5:
                jour_semaine = "Samedi"
            elif livre_datetime.weekday() == 6:
                jour_semaine = "Dimanche"


            if livre_datetime.timetuple().tm_hour < 6 or livre_datetime.timetuple().tm_hour > 18:
                mon_joueur.journuit = "nuit"
            else:
                mon_joueur.journuit = "jour"

            mon_joueur.saisontemps = saison
            mon_joueur.jourtemps = jour_semaine


    def temps(self):
        print(livre_datetime)
        print(mon_joueur.saisontemps)
        print("({})".format(mon_joueur.meteotemps))
        print(mon_joueur.jourtemps)
        print(mon_joueur.journuit)

    def poid(self):
        poid_inventaire = 10
        if (mon_joueur.force*1000) < poid_inventaire:
            print("Votre inventaire est plein")

    def foo(self):

        if mon_joueur.faim > 0:
            mon_joueur.faim -= 0.00004
            if mon_joueur.faim == 50:
                print("Vous avez faim")
            if mon_joueur.pv == 10:
                print("Vous êtes gravement blessé")
            if mon_joueur.faim == 0:
                print("Vous êtes mort de faim")
                mon_joueur.mort = True
            if mon_joueur.pv == 0:
                print("Vous êtes mort de vos blessures")
                mon_joueur.mort = True
        if mon_joueur.soif > 0:
            mon_joueur.soif -= 0.0004
            if mon_joueur.soif == 50:
                print("Vous avez soif")
            if mon_joueur.soif == 0:
                print("Vous êtes mort de déshydratation")
                mon_joueur.mort = True
        if mon_joueur.energie > 0:
            mon_joueur.energie -= 0.0004
            if mon_joueur.energie == 50:
                print("Vous êtes fatigué !")
            if mon_joueur.energie == 20:
                print("Vous êtes épuisé !")
            if mon_joueur.energie == 0:
                print("Vous vous endormez sur place !")
        if mon_joueur.pv < 0:
            print("Vous êtes mort de vos blessures")
            mon_joueur.mort = True
            sys.exit()
        if mon_joueur.faim < 0:
            print("Vous êtes mort de faim")
            mon_joueur.mort = True
            sys.exit()
        if mon_joueur.soif < 0:
            print("Vous êtes mort de déshydratation")
            mon_joueur.mort = True
            sys.exit()
        if mon_joueur.energie < 0:
            print("Vous êtes mort à cause du manque de sommeil !")
            mon_joueur.mort = True
            sys.exit()
