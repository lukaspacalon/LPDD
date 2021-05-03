from faker import Factory
fake = Factory.create('fr_FR')
from random import choice
import random
from collections import Counter
import personnage



#
# class GenerateurLieu:
#     def __init__(self):
#         self.objets = []
#         # self.gen = []
#
#     def genererLieu(self):
#         self.objets += [Lieu()]


#1x1 billiard de galaxy
class Univers:
    def __init__(self, emplacement):
        self.emplacement = emplacement
        self.nom = fake.city()

#200x200 milliards - 800x800 milliards de Systemes
class Galaxy:
    def __init__(self, emplacement):
        self.emplacement = emplacement
        self.nom = fake.city()

#1x1 - 10x10 Planete
class Systemes:
    def __init__(self, emplacement):
        self.emplacement = emplacement
        self.nom = fake.city()

#2x2 - 10x10 Continent
class Planete:
    def __init__(self, emplacement):
        self.emplacement = emplacement
        self.nom = fake.city()

#1x1 - 100x100 (4)Pays
class Continent:
    def __init__(self, emplacement):
        self.emplacement = emplacement
        self.nom = fake.city()

#1x1 (Seigneur) 2x2 (Vassal) 3x3 (Noble) 4x4 (Baron) 5x5 (Marquis) 6x6 (Comte) 7x7 (Duc)  8x8 (Archiduc)  9x9 (Roi)  10x10 (Empereur) Region
##
##
class Pays:
    def __init__(self, emplacement):
        self.emplacement = emplacement
        self.nom = fake.city()

#2x2 (4)Departement
##
##
class Region:
    def __init__(self, emplacement):
        self.emplacement = emplacement
        self.nom = fake.city()

#4x4 (16)Lieu
####
####
####
####
class Departement:
    def __init__(self, emplacement):
        self.emplacement = emplacement
        self.nom = fake.city()



class Lieu:
    #region = ["tempéré", "tropical", "froid", "ocean", "glacier", "mort", "désertique", "îles", "continental", "montagneuse", "mer"]
    #region = ["tempéré", "continental", "humide", "froid"]

    # print(personnage.g1.objets)
    # habitant = personnage.g1.objets
    # for habitants in habitant:
    #     print(habitants)


    # if type_hasard == "infranchissable":
    #     lieu = ["forêt profonde", "forêt", "marécage", "montagne", "désert", "pic", "grand lac", "crevasse", "volcan", "terre brule"]
    #     construction = ["vide", "vide", "vide", "cabane", "tour isolé", "vide", "vide", "vide", "vide", "vide", "feu de camps", "vide", "vide", "vide", "vide" ]
    #     #habitants = ["insecte", "insecte", "insecte", "insecte", "oiseau", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "brigant", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte"]
    # elif type_hasard == "naturel":
    #     lieu = ["prairie", "forêt", "marais", "montagne", "désert", "plaine", "lac", "collines", "pic", "terre brule"]
    #     construction = ["vide", "vide", "vide", "cabane", "vide", "vide", "vide", "vide", "vide", "vide", "vide", "vide", "vide", "vide", "vide" ]
    #     #habitants = ["insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "vagabond", "voyageur", "insecte", "insecte", "brigant", "insecte", "chevalier", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte", "insecte"]
    # elif type_hasard == "fréquenté":
    #     lieu = ["prairie", "forêt", "marais", "vallées", "désert", "plaine", "lac", "collines", "chemin", "cailloux"]
    #     construction = ["village", "commune", "bourgade", "cabane", "tour isolé", "ville", "donjon", "vide", "clôcher", "feu de camps", "campement", "ruines", "fermes" ,"village", "village"]
    #     #habitants = ["paysan", "enfant", "retraité", "sans emploi", "insecte", "insecte", "mendiant", "vagabond", "mendiant", "insecte", "insecte", "insecte", "insecte", "paysan", "insecte", "insecte", "insecte", "oiseau", "insecte", "insecte", "fille de joie", "insecte", "aventurier", "herboriste"]
    # else:
    #     lieu = ["prairie", "boisé", "petit lac", "vallées", "terre sêche", "plaine", "lac", "collines", "monticule", "terre"]
    #     construction = ["bourg", "ville", "cité", "bastion", "château", "ville", "cité", "citadelle", "forteresse", "krak", "zone agricole", "zone industriel", "bourg", "bastion", "fort"]
    #     #habitants = ["paysan", "enfant", "retraité", "sans emploi", "apprenti", "cuisinier", "marchand", "vagabond", "mendiant", "soldat", "moine", "forgeron", "berger", "chevalier", "ecuyer", "page", "tisserand", "meunier", "boulanger", "charpentier", "fille de joie", "aubergiste", "aventurier", "herboriste"]

    def __init__(self, emplacement):
        type = ["infranchissable", "naturel", "fréquenté", "stratégique"]
        type_hasard = random.choices(type, weights=(60, 30, 15, 10), k=1)
        self.emplacement = emplacement
        self.nom = fake.city()
        self.type = type_hasard
        #self.region = choice(Lieu.region)
        # self.lieu = random.choices(Lieu.lieu, weights=(60, 40, 1, 10, 1, 40, 10, 30, 0.5, 0.5), k=1)
        # self.construction = random.choices(Lieu.construction, weights=(30, 40, 10, 10, 10, 10, 5, 5, 10, 20, 20, 20, 10, 20, 10), k=1)


        self.infrastructure = []
        if type_hasard[0] == "infranchissable":
            lieu = ["forêt profonde", "forêt", "marécage", "montagne", "désert", "pic", "grand lac", "crevasse", "volcan", "terre brule"]
            construction = ["vide", "vide", "vide", "cabane", "tour isolé", "vide", "donjon", "vide", "vide", "crypte", "feu de camps", "vide", "vide", "vide", "vide" ]
            self.nbr_habitant = 0
            self.lieu = random.choices(lieu, weights=(60, 40, 1, 10, 1, 40, 10, 30, 0.5, 0.5), k=1)
            self.construction = random.choices(construction, weights=(30, 40, 10, 10, 10, 10, 5, 5, 10, 20, 20, 20, 10, 20, 10), k=1)
        elif type_hasard[0] == "naturel":
            lieu = ["prairie", "forêt", "marais", "montagne", "désert", "plaine", "lac", "collines", "pic", "terre brule"]
            construction = ["vide", "vide", "vide", "cabane", "vide", "vide", "vide", "vide", "vide", "mausolee", "vide", "vide", "vide", "vide", "vide" ]
            self.nbr_habitant = random.randint(0,1)
            self.lieu = random.choices(lieu, weights=(60, 40, 1, 10, 1, 40, 10, 30, 0.5, 0.5), k=1)
            self.construction = random.choices(construction, weights=(30, 40, 10, 10, 10, 10, 5, 5, 10, 20, 20, 20, 10, 20, 10), k=1)
        elif type_hasard[0] == "fréquenté":
            lieu = ["prairie", "forêt", "marais", "vallées", "désert", "plaine", "lac", "collines", "chemin", "cailloux"]
            construction = ["village", "commune", "bourgade", "cabane", "tour isolé", "ville", "repaire", "vide", "clôcher", "feu de camps", "campement", "ruines", "fermes" ,"village", "village"]
            self.nbr_habitant = random.randint(1,50)
            self.lieu = random.choices(lieu, weights=(60, 40, 1, 10, 1, 40, 10, 30, 0.5, 0.5), k=1)
            self.construction = random.choices(construction, weights=(30, 40, 10, 10, 10, 10, 5, 5, 10, 20, 20, 20, 10, 20, 10), k=1)
        else:
            lieu = ["prairie", "boisé", "petit lac", "vallées", "terre sêche", "plaine", "lac", "collines", "monticule", "terre"]
            construction = ["bourg", "ville", "cité", "bastion", "château", "ville", "cité", "citadelle", "forteresse", "krak", "zone agricole", "zone industriel", "bourg", "bastion", "fort"]
            self.nbr_habitant = random.randint(1,500)
            self.lieu = random.choices(lieu, weights=(60, 40, 1, 10, 1, 40, 10, 30, 0.5, 0.5), k=1)
            self.construction = random.choices(construction, weights=(30, 40, 10, 10, 10, 10, 5, 5, 10, 20, 20, 20, 10, 20, 10), k=1)

        self.reputation = 0
        #self.habitants = random.choices(Lieu.habitants, weights=(90, 40, 30, 40, 10, 5, 60, 20, 30, 10, 5, 5, 10, 1, 1, 1, 20, 5, 10, 10, 5, 10, 5, 1), k=self.nbr_habitant)
        # x = 0
        # while x < self.nbr_habitant:
        #     personnage.g1.genererPersonnage()
        #     x = x + 1
        # g1 = personnage.Generateur(emplacement)
        gp1 = personnage.GenerateurPersonnage()
        habitant = gp1.objets
        for habitants in habitant:
            print(habitants)
        self.habitants = habitant
        self.propriete_joueur = []





# lieu1 = Lieu("lieu1")
# print("lieu1.emplacement")
# print(lieu1.habitants)
# print(lieu1.nbr_habitant)

# class Village(Lieu):
#     villages_decouverts = 0
#     def __init__(self, emplacement, nom_village, nombre_habitant):
#         self.emplacement = emplacement
#         self.nom = nom_village
#         self.hab = nombre_habitant
#         #print("Découverte d'un village", self)
#         Village.villages_decouverts +=1
#
# class Foret(Lieu):
#     forets_decouvertes = 0
#     def __init__(self, emplacement, nom_foret, taille_foret):
#         self.emplacement = emplacement
#         self.nom = nom_foret
#         self.taille = taille_foret
#         #print("Découverte d'une Forêt", self)
#         Foret.forets_decouvertes +=1
#
# class Prairie(Lieu):
#     prairies_decouvertes = 0
#     def __init__(self, emplacement, nom_foret, taille_foret):
#         self.emplacement = emplacement
#         self.nom = nom_foret
#         self.taille = taille_foret
#         #print("Découverte d'une Prairie", self)
#         Prairie.prairies_decouvertes +=1
#
# v1 = Village("b1", "Tarik", 500)
# #print ("nom de v1 -> {}".format(v1.nom))
# #print ("Nombre d'habitant de {} -> {} habitants".format(v1.nom, v1.taille))
#
# f1 = Foret("a1", "Forêt de Hautefeuille", 500)
# #print ("nom de v1 -> {}".format(f1.nom))
# #print ("Nombre de km² de la {} -> {} km²".format(f1.nom, f1.taille))
#
# pr1 = Prairie("b2", "Prairie de L'aude", 100)
#print ("nom de v1 -> {}".format(pr1.nom))
#print ("Nombre de km² de la {} -> {} km²".format(pr1.nom, pr1.taille))

#print("Village découvert : {}".format(Village.villages_decouverts))
#print("Foret découverte : {}".format(Foret.forets_decouvertes))
#print("Prairie découverte : {}".format(Prairie.prairies_decouvertes))

#y+5x-5 y+5x-4 y+5x-3 y+5x-2 y+5x-1   y+5x0    y+5x+1  y+5x+2  y+5x+3  y+5x+4  y+5x+5
#y+4x-5 y+4x-4 y+4x-3 y+4x-2 y+4x-1   y+4x0    y+4x+1  y+4x+2  y+4x+3  y+4x+4  y+4x+5
#y+3x-5 y+3x-4 y+3x-3 y+3x-2 y+3x-1   y+3x0    y+3x+1  y+3x+2  y+3x+3  y+3x+4  y+3x+5
#y+2x-5 y+2x-4 y+2x-3 y+2x-2 y+2x-1   y+2x0    y+2x+1  y+2x+2  y+2x+3  y+2x+4  y+2x+5
#y+1x-5 y+1x-4 y+1x-3 y+1x-2 y+1x-1   y+1x0    y+1x+1  y+1x+2  y+1x+3  y+1x+4  y+1x+5
#y0x-5  y0x-4  y0x-3  y0x-2  y0x-1    y0x0     y0x+1    y0x+2  y0x+3   y0x+4   y0x+5
#y-1x-5 y-1x-4 y-1x-3 y-1x-2 y-1x-1   y-1x0    y-1x+1   y-1x+2 y-1x+3  y-1x+4  y-1x+5
#y-2x-5 y-2x-4 y-2x-3 y-2x-2 y-2x-1   y-2x0    y-2x+1   y-2x+2 y-2x+3  y-2x+4  y-2x+5
#y-3x-5 y-3x-4 y-3x-3 y-3x-2 y-3x-1   y-3x0    y-3x+1   y-3x+2 y-3x+3  y-3x+4  y-3x+5
#y-4x-5 y-4x-4 y-4x-3 y-4x-2 y-4x-1   y-4x0    y-4x+1   y-4x+2 y-4x+3  y-4x+4  y-4x+5
#y-5x-5 y-5x-4 y-5x-3 y-5x-2 y-5x-1   y-5x0    y-5x+1   y-5x+2 y-5x+3  y-5x+4  y-5x+5

nom = "nom"
description = "description"
examination = "examiner"
resolution = False
haut = 'haut', 'nord'
bas = 'bas', 'sud'
gauche = 'gauche', 'Ouest'
droite = 'droite', 'Est'

resolution_places = {'-3/3': False, '-2/3': False, '-1/3': False, '0/3': False, '1/3': False, '2/3': False, '3/3': False,
                     '-3/2': False, '-2/2': False, '-1/2': False, '0/2': False, '1/2': False, '2/2': False, '3/2': False,
                     '-3/1': False, '-2/1': False, '-1/1': False, '0/1': False, '1/1': False, '2/1': False, '3/1': False,
                     '-3/0': False, '-2/0': False, '-1/0': False, '0/0': False, '1/0': False, '2/0': False, '3/0': False,
                     '-3/-1': False, '-2/-1': False, '-1/-1': False, '0/-1': False, '1/-1': False, '2/-1': False, '3/-1': False,
                     '-3/-2': False, '-2/-2': False, '-1/-2': False, '0/-2': False, '1/-2': False, '2/-2': False, '3/-2': False,
                     '-3/-3': False, '-2/-3': False, '-1/-3': False, '0/-3': False, '1/-3': False, '2/-3': False, '3/-3': False
                }

carte = {}
