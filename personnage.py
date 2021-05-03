# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural
#import lieu
from faker import Factory
fake = Factory.create('fr_FR')
import random
from random import choice
import objet


# class IterationA:
#     def __init__(self):
#         self.n = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         result = 2 ** self.n
#         self.n += 1
#         return result

# class Generateur:
#     def __init__(self):
#         self.objets = []
#
#     def genererPersonnage(self):
#         self.objets += [Personnage()]


class GenerateurPersonnage:
    def __init__(self):
        self.objets = []
        # self.gen = []

    def genererPersonnage(self, niveau):
        self.objets += [Personnage(niveau)]


class Personnage:
    personnages_crees = 0
    def __init__(self, niveau):
        self.nom = fake.name()
        self.age = random.randint(10,50)
        self.vivant = ""
        self.pv = 100
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
        self.inventaire_personnage = []
        self.porte = []

        #armure
        self.tete = 0
        self.torse = 0
        self.jambes = 0
        self.bras = 0
        self.pieds = 0
        self.mains = 0
        self.doigts = 0
        self.cou = 0
        self.protection_tete = 0
        self.protection_torse = 0
        self.protection_bras = 0
        self.protection_jambes = 0
        self.protection = 0
        self.temperature = 36
        # print("print(livre.destination.construction)")
        # print(livre.destination.construction)
        if niveau == 0:
            travail_choix = ["pillard", "bandit", "vagabond", "criminel", "hors-la-loi", "braconnier"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h7_tunique_de_cuir)
            self.inventaire_personnage.append(objet.a1_epee_courte)
            self.inventaire_personnage.append(objet.a14_dague)
            self.inventaire_personnage.append(objet.b1_bouteille_biere)

        elif niveau == 1:
            travail_choix = ["paysan", "sans emploi", "marchand", "vagabond", "mendiant", "soldat", "moine", "roturier", "fille de joie", "aventurier", "artisan", 'voyageur', "chasseur", "pecheur", "pisteur", "trappeur"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 2:
            travail_choix = ["paysan", "sans emploi", "apprenti", "roturier", "cuisinier", "barde", "marchand", "vagabond", "jardinier", "mendiant", "soldat", "moine", "forgeron", "berger", "voyageur", "trappeur", "paysan", "tisserand", "meunier", "boulanger", "charpentier", "fille de joie", "aubergiste", "aventurier", "herboriste"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 3:
            travail_choix = ["paysan", "sans emploi", "bailli", "tresorier", "receleur", "inquisiteur", "laboureur", "jardinier", "dramaturge","tenancier", "citoyen", "milicien", "geolier", "apprenti", "curé", "medecin", "avocat", "bourgeois", "noble", "cuisinier", "marchand", "vagabond", "mendiant", "soldat", "moine", "forgeron", "berger", "chevalier", "ecuyer", "page", "tisserand", "meunier", "boulanger", "charpentier", "fille de joie", "aubergiste", "aventurier", "herboriste"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 4:
            travail_choix = ["paysan", "scribe", "officier", "delegue", "artisan_compagnon", "tresorier", "artisan_expert", "bouffon", "jardinier", "barde", "dramaturge", "comedien", "courtisan", "ingenieur", "pretre", "abbe" ,"bourgeois","noble", "conseiller", "sans emploi", "bailli", "inquisiteur", "laboureur", "tenancier", "citoyen", "milicien", "geolier", "apprenti", "curé", "medecin", "avocat", "bourgeois", "noble", "cuisinier", "marchand", "vagabond", "mendiant", "soldat", "moine", "forgeron", "berger", "chevalier", "ecuyer", "page", "tisserand", "meunier", "boulanger", "charpentier", "fille de joie", "aubergiste", "aventurier", "herboriste", "contrebandier"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 5:
            travail_choix = ["paysan", "scribe", "officier", "delegue", "artisan_compagnon", "tresorier", "artisan_expert", "bouffon", "jardinier", "barde", "dramaturge", "comedien", "courtisan", "ingenieur", "pretre", "abbe" ,"bourgeois","noble", "conseiller", "intendant", "sans emploi", "bailli", "inquisiteur", "laboureur", "tenancier", "citoyen", "milicien", "geolier", "apprenti", "curé", "medecin", "avocat", "bourgeois", "noble", "cuisinier", "marchand", "vagabond", "mendiant", "soldat", "moine", "forgeron", "berger", "chevalier", "ecuyer", "page", "tisserand", "meunier", "boulanger", "charpentier", "fille de joie", "aubergiste", "aventurier", "herboriste", "contrebandier", "vicaire", "baron", "eveque"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 1.5:
            travail_choix = ["roi", "intendant", "prince", "archiduc", "archeveque", "comte", "patriarch", "cardinal", "grand seigneur", "duc"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 1.4:
            travail_choix = ["comte", "baron", "duc", "marquis", "vassal", "seigneur", "bailli", "grand seigneur", "primat", "cardinal"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 1.3:
            travail_choix = ["maire", "seigneur", "abbe", "noble", "vicomte", "bailli", "delegue", "doyen", "vicaire", "pretre", "chef", "sergent", "capitaine"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 1.2:
            travail_choix = ["chef", "doyen", "abbe", "capitaine", "delegue", "sergent", "officier", "seigneur", "pretre", "maire"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 3.1:
            travail_choix = ["paysan", "sans emploi", "laboureur", "domestique", "tenancier", "serf", "ouvrier", "maitre", "cueilleur", "laitier", "tanneur", "bucheron", "artisan"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 1.1:
            travail_choix = ["moine", "moine", "moine", "moine guerrisseur", "moine guerrier", "moine herboriste", "moine erudit", "moine du chapitre", "moine paysan", "moine brasseur"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 1.21:
            travail_choix = ["mage", "thaumaturge", "illusioniste", "apprenti mage", "adepte", "conjurateur", "enchanteur", "alternateur", "mysticiste", "guerisseur", "invocateur", "devin", "haut mage", "sorcier"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 2.1:
            travail_choix = ["pretre", "diacre", "vicaire", "seminariste"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 2.2:
            travail_choix = ["abbe", "vicaire", "doyen", "curé"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 2.3:
            travail_choix = ["mage", "thaumaturge", "illusioniste", "apprenti mage", "adepte", "conjurateur", "enchanteur", "alternateur", "mysticiste", "guerisseur", "invocateur", "devin", "haut mage", "archimage", "necromancier", "liche", "demoniste", "chaman", "medium", "oracle", "gardien du savoir"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 2.4:
            travail_choix = ["haut mage", "archimage", "maitre sorcier", "haut archimage", "gardien du savoir", "theurge", "haut conjurateur", "haut alternateur", "haut mysticiste", "haut enchanteur", "haut invocateur", "haut devin", "haut mage", 'prince mage']
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 0.1:
            travail_choix = ['prince dechu', 'dragon', 'liche', "prince vampire", "prince démon", "séraphin"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        elif niveau == 0.2:
            travail_choix = ["fossoyeur", "croque-mort"]
            self.porte.append(objet.h2_houseaux)
            self.porte.append(objet.h2_chaussons)
            self.porte.append(objet.h1_chemise_de_lin)
            self.inventaire_personnage.append(objet.n2_pomme)

        travail = choice(travail_choix)
        #self.race = race
        self.travail = travail
        personalite_choix = ["empathique", "perseverant", "promoteur", "rebelle", "reveur", "travaillomane"]
        personalite = choice(personalite_choix)
        self.personalite = personalite
        attitude_choix = ["chef", "inconnu", "rival", "inconnu", "inconnu"]
        attitude = choice(attitude_choix)
        self.attitude = attitude
        inventaire_personnage = objet.Contenant("inventaire_personnage")
        etalage = objet.Contenant("etalage")
        self.etalage = etalage
        self.relationnel = 0
        self.peur = 0
        self.attirance = 0
        self.surveillance = 10
        self.equipe = False
        technique_choix = ["defenseur", "gardien", "conquerant", "provocateur"]
        technique = choice(technique_choix)
        self.technique = technique

        Personnage.personnages_crees +=1
        #print("Decouverte d'un personnage", self)
        #print("Decouverte d'un personnage :")
        #print(self.__dict__)

        self.quete = []
        self.propriete = []

    def se_deplacer(self, vitesse):
        print("{} se déplace {}".format(self.prenom, vitesse))

    def parler(self, message):
        print("{} a dit : {}".format(self.prenom, message))
#





# g1 = Generateur()

#g1.genererPersonnage()
