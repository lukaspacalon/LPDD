import meuble
import random
import joueur

class Infrastructure:
    #
    # localisationX = joueur.mon_joueur.localisationX
    # localisationY = joueur.mon_joueur.localisationY

    def __init__(self, nom, localisationX, localisationY):
        self.nom = nom
        self.localisationX = localisationX
        self.localisationY = localisationY
        self.emplacementX = random.randint(0,100000)
        self.emplacementY = random.randint(0,100000)
        self.proprietaire = ''
        self.cout = ''
        self.employe = ''
        self.piece = ''
        self.meuble = []
        self.meuble.append(meuble.table)
        self.meuble.append(meuble.chaise)
        self.meuble.append(meuble.chaise)
        self.meuble.append(meuble.armoire)
        self.meuble.append(meuble.coffre)
        self.meuble.append(meuble.etagere)
        self.meuble.append(meuble.lit)
        random_objet = random.randint(0,1)
        if random_objet == 0:
            self.meuble.append(meuble.etagere)
            self.meuble.append(meuble.chaise)
            self.meuble.append(meuble.chaise)
        else:
            self.meuble.append(meuble.coffre)
            self.meuble.append(meuble.buanderie)
            self.meuble.append(meuble.banc)
        random_objet = random.randint(0,1)
        if random_objet == 0:
            self.meuble.append(meuble.table)
            self.meuble.append(meuble.chaise)
            self.meuble.append(meuble.chaise)
        else:
            self.meuble.append(meuble.banc)
            self.meuble.append(meuble.coffre)
            self.meuble.append(meuble.table_de_chevet)
        if nom == "boulangerie":
            self.meuble.append(meuble.atelier_boulangerie)
        if nom == "forge":
            self.meuble.append(meuble.atelier_forge)
        if nom == "tisserand":
            self.meuble.append(meuble.atelier_tisserie)
        if nom == "herboriste":
            self.meuble.append(meuble.atelier_herboristerie)
        if nom == "aubergiste":
            self.meuble.append(meuble.atelier_auberge)
        # self.meuble = [armoire, coffre, table, etagere]

#Batiment du chateau
# donjon = Infrastructure("donjon")
# tour = Infrastructure("tour")
# chateau = Infrastructure("chateau")
# refuge = Infrastructure("refuge")
# lice = Infrastructure("lice")
# cuisine_royal = Infrastructure("cuisine_royal")
# grenier = Infrastructure("grenier")
# palais_de_justice = Infrastructure("palais_de_justice")
# theatre = Infrastructure("theatre")
# amphitheatre = Infrastructure("amphitheatre")
# joutes = Infrastructure("joutes")
# statue = Infrastructure("statue")
# champ_de_foire = Infrastructure("champ_de_foire")
# auberge = Infrastructure("auberge")
# eglise = Infrastructure("eglise")
# monastere = Infrastructure("monastère")
# reserve = Infrastructure("reserve")
# marche = Infrastructure("marche")
# poste_de_charretier = Infrastructure("poste_de_charretier")
# tresorerie = Infrastructure("tresorerie")
# bibliotheque = Infrastructure("bibliotheque")
# port = Infrastructure("port")
# universite = Infrastructure("universite")
# merveille = Infrastructure("merveille")
# temple = Infrastructure("temple")
# academie = Infrastructure("academie")
# forum = Infrastructure("forum")
# jardin = Infrastructure("jardin")
# ministere = Infrastructure("jardin")
#
# #Batiment militaire
# caserne = Infrastructure("caserne")
# armurerie = Infrastructure("armurerie")
# guilde_des_ingénieurs = Infrastructure("guilde_des_ingénieurs")
# guilde_des_bourreaux = Infrastructure("guilde_des_bourreaux")
# guilde_des_bardes = Infrastructure("guilde_des_bardes")
# guilde_des_assassins = Infrastructure("guilde_des_assassins")
# guilde_des_mages = Infrastructure("guilde_des_mages")
# guilde_des_voleurs = Infrastructure("guilde_des_voleurs")
# guilde_des_guerriers = Infrastructure("guilde_des_guerriers")
# camp_des_mercenaires = Infrastructure("camp_des_mercenaires")
# camp_de_siege = Infrastructure("camp_de_siege")
#
# #Edifice manufacturier
# forge = Infrastructure("forge")
# tannerie = Infrastructure("tannerie")
# atelier_darcherie = Infrastructure("atelier_darcherie")
# ecurie = Infrastructure("ecurie")
# brasserie = Infrastructure("brasserie")
# houblonniere = Infrastructure("houblonniere")
# ruche = Infrastructure("ruche")
# cirier = Infrastructure("cirier")
# atelier_de_tisserand = Infrastructure("atelier_de_tisserand")
#
# #Batiment de ferme
# ferme = Infrastructure("ferme")
# pommeraie = Infrastructure("pommeraie")
# abri_de_chasse = Infrastructure("abri_de_chasse")
# laiterie = Infrastructure("laiterie")
# moulin = Infrastructure("moulin")
# boulangerie = Infrastructure("boulangerie")
# potager = Infrastructure("potager")
# vivier = Infrastructure("vivier")
# porcherie = Infrastructure("porcherie")
# vignoble = Infrastructure("vignoble")
# chai = Infrastructure("chai")
# bergerie = Infrastructure("bergerie")
#
# #Batiment urbain
# etalage = Infrastructure("etalage")
# maison = Infrastructure("maison")
# poste_de_surveillance = Infrastructure("poste_de_surveillance")
# pilori = Infrastructure("pilori")
# puit = Infrastructure("puit")
# citerne = Infrastructure("citerne")
# apothicaire = Infrastructure("apothicaire")
# fosse_a_fange = Infrastructure("fosse_a_fange")
# fauconnerie = Infrastructure("fauconnerie")
#
# #batiment magique
# tour_de_magicien = Infrastructure("tour_de_magicien")
