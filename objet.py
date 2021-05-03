# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural

import inspect
import joueur
import bibliotheque
import time, sched

class Objet:
    def __init__(self, nom, poid, valeur, usure, proprietaire=0, quantite=1):
        self.nom = nom
        self.poid = poid
        self.brut = nom.strip().lower()
        self.valeur = valeur
        self.usure = usure
        self.proprietaire = proprietaire
        self.quantite = quantite
        self.valeurTotal = quantite * valeur


    def recalc(self):
        self.valeurTotal = self.quantite * self.valeur

    def examiner(self):
        print(self.__dict__)

    def jeter(self, jeter_quantite):
        print("vous jetez : {} {}".format(jeter_quantite, self.nom))
        sac_joueur.retirer(self, jeter_quantite)

class Contenant:
    def __init__(self, nom):
        self.nom = nom
        self.inside = {}

    def __iter__(self):
        return iter(self.inside.objets())

    def __len__(self, objet):
        return len(self.inside)

    def __contains__(self, objet):
        return objet.brut in self.inside

    def __getitem__(self, objet):
        try:
            return self.inside[objet.brut]
        except KeyError:
            print("Key Error")

    def __setitem__(self, objet, valeur):
        self.inside[objet.brut] = valeur
        return self[objet]

    def ajouter(self, objet, quantite=1):
        quantite_int_ajouter = int(quantite)
        for loop in range(quantite_int_ajouter):
            if quantite_int_ajouter < 0:
                raise ValueError("Quantite negative, utilisez retirer() plutot")
            elif objet in self:
                self[objet].append(objet)
            else:
                self[objet] = [objet]

    def retirer(self, objet, quantite=1):
        quantite_int = int(quantite)
        if objet not in self:
            raise KeyError("L'objet n'est pas dans le contenant")
        elif quantite_int < 0:
            raise ValueError("Quantite negative, utilisez ajouter() plutot")
        else:
            for loop in range(quantite_int):
                del self.inside[objet.brut][0]
            if len(self.inside[objet.brut]) == 0:
                del self.inside[objet.brut]

    def acheter(self, objet, quantite=1):
        if objet.valeur * quantite > len(self[o1_denier]):
            print("")
            print("Vous n'avez pas assez d'argent !")
        else:
            self.retirer(o1_denier, objet.valeur * quantite)
            self.ajouter(objet, quantite)
            print("Vous avez acheté : {0} '{1}'".format(quantite, objet.nom))


    def vendre(self, objet, quantite=1):
        self.ajouter(o1_denier, objet.valeur * quantite)
        self.retirer(objet, quantite)
        print("Vous avez vendu : {0} '{1}'".format(quantite, objet.nom))


    def voler(self, objet, quantite=1):
        self.ajouter(objet, quantite)
        print("Vous avez volé : {0} '{1}'".format(quantite, objet.nom))


class Habit:
    def __init__(self, nom, poid, valeur, matiere, emplacement, port, protection, temperature, usure, proprietaire=0, quantite=1):
        self.nom = nom
        self.poid = poid
        self.brut = nom.strip().lower()
        self.valeur = valeur
        self.matiere = matiere
        self.emplacement = emplacement
        self.port = port
        self.protection = protection
        self.temperature = temperature
        self.usure = usure
        self.quantite = quantite
        self.valeurTotal = quantite * valeur

    def recalc(self):
        self.valeurTotal = self.quantite * self.valeur

    def examiner(self):
        print(self.__dict__)

    def jeter(self, jeter_quantite):
        print("vous jetez : {} {}".format(jeter_quantite, self.nom))
        sac_joueur.retirer(self, jeter_quantite)

    def porter(self):
        if self.emplacement == "tete":
            if joueur.mon_joueur.tete == 0:
                joueur.mon_joueur.tete = joueur.mon_joueur.tete + 1
                joueur.mon_joueur.protection = joueur.mon_joueur.protection + self.protection
                joueur.mon_joueur.temperature = joueur.mon_joueur.temperature + self.temperature
                print("Vous portez : {}".format(self.nom))
                self.port = True
            else:
                print("Vous portez déjà quelque chose sur la tête")
        elif self.emplacement == "torse":
                if joueur.mon_joueur.torse == 0:
                    joueur.mon_joueur.torse = joueur.mon_joueur.torse + 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection + self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature + self.temperature
                    print("Vous portez : {}".format(self.nom))
                    self.port = True
                else:
                    print("Vous portez déjà quelque chose")
        elif self.emplacement == "jambes":
                if joueur.mon_joueur.jambes == 0:
                    joueur.mon_joueur.jambes = joueur.mon_joueur.jambes + 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection + self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature + self.temperature
                    print("Vous portez : {}".format(self.nom))
                    self.port = True
                else:
                    print("Vous portez déjà quelque chose")
        elif self.emplacement == "bras":
                if joueur.mon_joueur.bras == 0:
                    joueur.mon_joueur.bras = joueur.mon_joueur.bras + 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection + self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature + self.temperature
                    print("Vous portez : {}".format(self.nom))
                    self.port = True
                else:
                    print("Vous portez déjà quelque chose")
        elif self.emplacement == "pieds":
                if joueur.mon_joueur.pieds == 0:
                    joueur.mon_joueur.pieds = joueur.mon_joueur.pieds + 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection + self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature + self.temperature
                    print("Vous portez : {}".format(self.nom))
                    self.port = True
                else:
                    print("Vous portez déjà quelque chose")
        elif self.emplacement == "mains":
                if joueur.mon_joueur.mains == 0:
                    joueur.mon_joueur.mains = joueur.mon_joueur.mains + 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection + self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature + self.temperature
                    print("Vous portez : {}".format(self.nom))
                    self.port = True
                else:
                    print("Vous portez déjà quelque chose")
        elif self.emplacement == "doigts":
                if joueur.mon_joueur.doigts < 10:
                    joueur.mon_joueur.doigts = joueur.mon_joueur.doigts + 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection + self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature + self.temperature
                    print("Vous portez : {}".format(self.nom))
                    self.port = True
                else:
                    print("Vous portez trop de bagues")
        elif self.emplacement == "cou":
                if joueur.mon_joueur.cou < 5:
                    joueur.mon_joueur.cou = joueur.mon_joueur.cou + 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection + self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature + self.temperature
                    print("Vous portez : {}".format(self.nom))
                    self.port = True
                else:
                    print("Vous portez trop de choses autour du cou ")

    def enlever(self):
        if self.emplacement == "tete":
            if joueur.mon_joueur.tete == 1:
                joueur.mon_joueur.tete = joueur.mon_joueur.tete - 1
                joueur.mon_joueur.protection = joueur.mon_joueur.protection - self.protection
                joueur.mon_joueur.temperature = joueur.mon_joueur.temperature - self.temperature
                print("Vous enlevez : {}".format(self.nom))
                self.port = False
            else:
                print("Vous ne portez rien sur la tete")
        elif self.emplacement == "torse":
                if joueur.mon_joueur.torse == 1:
                    joueur.mon_joueur.torse = joueur.mon_joueur.torse - 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection - self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature - self.temperature
                    print("Vous enlevez : {}".format(self.nom))
                    self.port = False
                else:
                    print("Vous ne portez rien")
        elif self.emplacement == "jambes":
                if joueur.mon_joueur.jambes == 1:
                    joueur.mon_joueur.jambes = joueur.mon_joueur.jambes - 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection - self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature - self.temperature
                    print("Vous enlevez : {}".format(self.nom))
                    self.port = False
                else:
                    print("Vous ne portez rien")
        elif self.emplacement == "bras":
                if joueur.mon_joueur.bras == 1:
                    joueur.mon_joueur.bras = joueur.mon_joueur.bras - 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection - self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature - self.temperature
                    print("Vous enlevez : {}".format(self.nom))
                    self.port = False
                else:
                    print("Vous ne portez rien")
        elif self.emplacement == "pieds":
                if joueur.mon_joueur.pieds == 1:
                    joueur.mon_joueur.pieds = joueur.mon_joueur.pieds - 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection - self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature - self.temperature
                    print("Vous enlevez : {}".format(self.nom))
                    self.port = False
                else:
                    print("Vous ne portez rien")
        elif self.emplacement == "mains":
                if joueur.mon_joueur.mains == 1:
                    joueur.mon_joueur.mains = joueur.mon_joueur.mains - 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection - self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature - self.temperature
                    print("Vous enlevez : {}".format(self.nom))
                    self.port = False
                else:
                    print("Vous ne portez rien")
        elif self.emplacement == "doigts":
                if joueur.mon_joueur.doigts > 0:
                    joueur.mon_joueur.doigts = joueur.mon_joueur.doigts - 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection - self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature - self.temperature
                    print("Vous enlevez : {}".format(self.nom))
                    self.port = False
                else:
                    print("Vous ne portez rien")
        elif self.emplacement == "cou":
                if joueur.mon_joueur.cou > 0:
                    joueur.mon_joueur.cou = joueur.mon_joueur.cou - 1
                    joueur.mon_joueur.protection = joueur.mon_joueur.protection - self.protection
                    joueur.mon_joueur.temperature = joueur.mon_joueur.temperature - self.temperature
                    print("Vous enlevez : {}".format(self.nom))
                    self.port = False
                else:
                    print("Vous ne portez rien")





class Nourriture:
    def __init__(self, nom, poid, valeur, calorie, effet, usure, proprietaire=0, quantite=1):
        self.nom = nom
        self.poid = poid
        self.brut = nom.strip().lower()
        self.valeur = valeur
        self.calorie = calorie
        self.effet = effet
        self.usure = usure
        self.quantite = quantite
        self.valeurTotal = quantite * valeur

    def manger(self):
        print("vous mangez : {}".format(self.nom))
        joueur.mon_joueur.faim = joueur.mon_joueur.faim + self.calorie/20
        joueur.mon_joueur.soif = joueur.mon_joueur.soif + self.calorie/40
        sac_joueur.retirer(self, 1)

    def recalc(self):
        self.valeurTotal = self.quantite * self.valeur

    def examiner(self):
        print(self.__dict__)

    def jeter(self, jeter_quantite):
        print("vous jetez : {} {}".format(jeter_quantite, self.nom))
        sac_joueur.retirer(self, jeter_quantite)

class Boisson:
    def __init__(self, nom, poid, valeur, effet, centilitres, contenu, usure, proprietaire=0, quantite=1):
        self.nom = nom
        self.poid = poid
        self.brut = nom.strip().lower()
        self.valeur = valeur
        self.effet = effet
        self.centilitres = centilitres
        self.contenu = contenu
        self.usure = usure
        self.quantite = quantite
        self.valeurTotal = quantite * valeur

    def examiner(self, centilitres):
        print(self.__dict__)
        print(self.centilitres + " centilitres")

    def boire(self):
        if self.centilitres > 0:
            print("vous buvez 10 centilitres de : {}".format(self.nom))
            joueur.mon_joueur.soif = joueur.mon_joueur.soif + 10
            self.centilitres = self.centilitres - 10
        else:
            print("La boisson est vide !")

    def recalc(self):
        self.valeurTotal = self.quantite * self.valeur

    def examiner(self):
        print(self.__dict__)

    def jeter(self, jeter_quantite):
        print("vous jetez : {} {}".format(jeter_quantite, self.nom))
        sac_joueur.retirer(self, jeter_quantite)


class Livre:

    def __init__(self, nom, poid, valeur, c_chapitre, c_page, c_contenu, usure, proprietaire=0, quantite=1):
        print("")
        self.nom = nom
        self.poid = poid
        self.brut = nom.strip().lower()
        self.valeur = valeur
        self.chapitre = c_chapitre
        self.page = c_page
        self.contenu = c_contenu
        self.usure = usure
        self.quantite = quantite
        self.valeurTotal = quantite * valeur

    def lire(self):
        print(self.__dict__["contenu"])

    def ecrire(cls, nouveau_paragraphe):
        Livre.contenu = Livre.contenu + nouveau_paragraphe

    def recalc(self):
        self.valeurTotal = self.quantite * self.valeur

    def examiner(self):
        print(self.__dict__)

    def jeter(self, jeter_quantite):
        print("vous jetez : {} {}".format(jeter_quantite, self.nom))
        sac_joueur.retirer(self, jeter_quantite)

    ecrire = classmethod(ecrire)

class Divers_utilisable:
        def __init__(self, nom, poid, effet, valeur, usure, proprietaire=0, quantite=1):
            self.nom = nom
            self.poid = poid
            self.effet = effet
            self.valeur = valeur
            self.brut = nom.strip().lower()
            self.usure = usure
            self.quantite = quantite
            self.valeurTotal = quantite * valeur

        def utiliser():
            print("vous utilisez : {}".format(self.nom))
            sac_joueur.retirer(self, 1)

        def recalc(self):
            self.valeurTotal = self.quantite * self.valeur

        def examiner(self):
            print(self.__dict__)

        def jeter(self, jeter_quantite):
            print("vous jetez : {} {}".format(jeter_quantite, self.nom))
            sac_joueur.retirer(self, jeter_quantite)

class Arme:
        def __init__(self, nom, poid, effet, valeur, degat, parade, usure, proprietaire=0, quantite=1):
            self.nom = nom
            self.port = False
            self.poid = poid
            self.effet = effet
            self.valeur = valeur
            self.brut = nom.strip().lower()
            self.degat = degat
            self.parade = parade
            self.usure = usure
            self.quantite = quantite
            self.valeurTotal = quantite * valeur

        def recalc(self):
            self.valeurTotal = self.quantite * self.valeur

        def examiner(self):
            print(self.__dict__)

        def jeter(self, jeter_quantite):
            print("vous jetez : {} {}".format(jeter_quantite, self.nom))
            sac_joueur.retirer(self, jeter_quantite)

        def armer(self, emplacement):
            if emplacement == "main_droite":
                if joueur.mon_joueur.main_droite == 0 and self.port == False:
                    joueur.mon_joueur.main_droite = joueur.mon_joueur.main_droite + 1
                    joueur.mon_joueur.force = joueur.mon_joueur.force + self.degat
                    joueur.mon_joueur.endurance = joueur.mon_joueur.endurance + self.parade
                    print("Vous armez : {} dans la main droite".format(self.nom))
                    self.port = True
                else:
                    print("Vous avez déjà quelque chose dans la main droite ou cette arme est déjà utilisée")
            elif emplacement == "main_gauche":
                    if joueur.mon_joueur.main_gauche == 0 and self.port == False:
                        joueur.mon_joueur.main_gauche = joueur.mon_joueur.main_droite + 1
                        joueur.mon_joueur.force = joueur.mon_joueur.force + self.degat
                        joueur.mon_joueur.endurance = joueur.mon_joueur.endurance + self.parade
                        print("Vous armez : {} dans la main gauche".format(self.nom))
                        self.port = True
                    else:
                        print("Vous avez déjà quelque chose dans la main gauche ou cette arme est déjà utilisée")

        def desarmer(self, emplacement):
            if emplacement == "main_droite":
                if joueur.mon_joueur.main_droite == 1 and self.port == True:
                    joueur.mon_joueur.main_droite = joueur.mon_joueur.main_droite - 1
                    joueur.mon_joueur.force = joueur.mon_joueur.force - self.degat
                    joueur.mon_joueur.endurance = joueur.mon_joueur.endurance - self.parade
                    print("Vous desarmez : {} de la main droite".format(self.nom))
                    self.port = False
                else:
                    print("Vous n'avez rien dans la main droite ou cette arme est déjà utilisée")
            elif emplacement == "main_gauche":
                    if joueur.mon_joueur.main_gauche == 1 and self.port == True:
                        joueur.mon_joueur.main_gauche = joueur.mon_joueur.main_droite - 1
                        joueur.mon_joueur.force = joueur.mon_joueur.force - self.degat
                        joueur.mon_joueur.endurance = joueur.mon_joueur.endurance - self.parade
                        print("Vous desarmez : {} de la main gauche".format(self.nom))
                        self.port = False
                    else:
                        print("Vous n'avez rien dans la main gauche ou cette arme est déjà utilisée")






o1_denier_joueur = Objet("Denier Joueur", 1, 1, 50)
o1_denier = Objet("Denier", 1, 1, 50)
o2_choppe_de_bois = Objet("Choppe de bois", 1, 5, 100)
o3_choppe_de_fer = Objet("Choppe de fer", 1, 5, 100)
d1_bandage = Divers_utilisable("Bandage", 1, 1, 5, 100)
d1_clou = Objet("Clou", 1, 1, 100)
d1_allumette = Objet("Allumette", 1, 1, 100)
d1_fourchette = Objet("Fourchette", 5, 20, 100)
d1_cuillere = Objet("Cuillere", 5, 20, 100)
d1_coupole = Objet("coupole", 50, 20, 100)
d1_assiette = Objet("assiette", 50, 20, 100)
d1_verre = Objet("verre", 50, 100, 100)
d1_louche = Objet("louche", 5, 20, 100)
d1_cierge = Objet("cierge", 5, 20, 100)
d1_bougie = Objet("bougie", 5, 40, 100)
d1_encens = Objet("encens", 5, 80, 100)
m1_cire = Objet("cire", 5, 40, 100)
m1_laine = Objet("laine", 5, 20, 100)
m1_tissu = Objet("tissu", 5, 20, 100)
m1_bois = Objet("bois", 1000, 20, 100)
m1_fer = Objet("fer", 2000, 100, 100)
m1_cuir = Objet("cuir", 500, 30, 100)
m1_acier = Objet("acier", 4000, 400, 100)
m1_pierre = Objet("pierre", 10000, 20, 100)
m1_or = Objet("or", 1, 8000, 100)
m1_diamant = Objet("diamant", 5, 45000000, 100)
m1_emeraude = Objet("emeraude", 5, 3000000, 100)
m1_rubis = Objet("rubis", 5, 8000000, 100)
m1_opale = Objet("opale", 5, 2000000, 100)
b1_bague = Objet("baguer", 5, 230, 100)
b1_collier = Objet("collier", 5, 200, 100)
b1_bracelet = Objet("bracelet", 5, 70, 100)
b1_couronne = Objet("couronne", 5, 420, 100)
h1_chemise_de_lin = Habit("Chemise de lin", 100, 40, "lin", "torse", False, 1, 5, 100)
h2_chaussure_de_cuir = Habit("Chaussure de cuir", 200, 80, "cuir", "pieds", False, 5, 10, 100)
h2_houseaux = Habit("houseaux", 200, 30, "cuir", "pieds", False, 5, 10, 100)
h2_chaussons = Habit("chaussons", 100, 80, "cuir", "pieds", False, 5, 10, 100)
h2_souliers = Habit("souliers", 100, 50, "cuir", "pieds", False, 5, 10, 100)
h2_bottes = Habit("bottes", 200, 80, "cuir", "pieds", False, 5, 10, 100)
h3_braies_de_lin = Habit("Braies de lin", 100, 40, "lin", "jambes", False, 1, 5, 100)
h3_pantalon_cuir = Habit("h3_pantalon_cuir", 100, 80, "cuir", "jambes", False, 1, 5, 100)
h4_capuchon = Habit("Capuchon", 100, 20, "chanvre", "tete", False, 1, 5, 100)
h4_cape = Habit("cape", 300, 70, "chanvre", "tete", False, 1, 20, 100)
h4_manteau = Habit("manteau", 400, 210, "chanvre", "tete", False, 1, 50, 100)
h4_couverture = Habit("couverture", 30, 40, "chanvre", "tete", False, 1, 70, 100)
h5_chemise_de_laine = Habit("Chemise de laine", 10, 80, "laine", "torse", False, 1, 50, 100)
h6_coule_de_moine = Habit("Coule de moine", 20, 50, "lin", "torse", False, 1, 20, 100)
h7_tunique_de_cuir = Habit("Tunique de cuir", 20, 90, "lin", "torse", False, 5, 10, 100)
h8_ceinture = Habit("Ceinture", 1, 10, "lin", "torse", False, 0, 0, 100)
h9_collant_noble = Habit("Collant de noble", 10, 3200, "lin", "jambes", False, 1, 20, 100)
h10_tunique_noble = Habit("tunique_noble", 10, 4200, "lin", "torse", False, 1, 20, 100)
h11_tunique_velours = Habit("tunique_velours", 10, 6200, "velours", "torse", False, 1, 30, 100)
h12_braies_velours = Habit("braies_velours", 10, 8200, "velours", "jambes", False, 1, 30, 100)
h13_chemise_de_toile = Habit("Chemise de toile", 5, 60, "toile", "torse", False, 1, 20, 100)
h14_camail = Habit("camail", 200, 600, "toile", "torse", False, 40, 20, 100)
h14_colletin_maille = Habit("colletin_maille", 400, 420, "toile", "torse", False, 50, 20, 100)
h15_cagoule_rembourre = Habit("cagoule_rembourre", 40, 250, "toile", "torse", False, 30, 20, 100)
h16_gambison = Habit("gambison", 400, 750, "toile", "torse", False, 40, 20, 100)
h16_brigandine = Habit("brigandine", 800, 650, "toile", "torse", False, 60, 20, 100)
h16_haubergeon = Habit("haubergeon", 400, 400, "toile", "torse", False, 40, 20, 100)
h16_haubert = Habit("haubert", 300, 800, "toile", "torse", False, 90, 20, 100)
h17_jambiere = Habit("jambiere", 200, 450, "toile", "torse", False, 80, 20, 100)
h17_jambiere_cuir = Habit("jambiere_cuir", 200, 350, "toile", "torse", False, 40, 20, 100)
h17_jambiere_maille = Habit("jambiere_maille", 250, 850, "toile", "torse", False, 50, 20, 100)
h17_jambe_armure = Habit("jambe_armure", 350, 1850, "toile", "torse", False, 120, 20, 100)
h18_heaume = Habit("heaume", 200, 2850, "toile", "torse", False, 200, 20, 100)
h18_calot = Habit("calot", 20, 60, "toile", "torse", False, 20, 20, 100)
h18_casque_leger = Habit("casque_leger", 20, 90, "toile", "torse", False, 30, 20, 100)
h18_casque_lourd = Habit("casque_lourd", 200, 210, "toile", "torse", False, 60, 20, 100)
h18_casque_bourguignon = Habit("casque_bourguignon", 300, 840, "toile", "torse", False, 250, 20, 100)
h18_casque_salade = Habit("casque_salade", 200, 620, "toile", "torse", False, 80, 20, 100)
h18_bassinet = Habit("bassinet", 200, 1420, "toile", "torse", False, 120, 20, 100)
h18_casque_leger = Habit("casque_leger", 20, 80, "toile", "torse", False, 40, 20, 100)
h18_chapeau_de_paille = Habit("chapeau_de_paille", 1, 60, "toile", "torse", False, 1, 20, 100)
h19_brassard = Habit("brassard", 5, 70, "toile", "torse", False, 20, 20, 100)
h20_cotte_de_maille = Habit("cotte_de_maille", 200, 290, "toile", "torse", False, 60, 20, 100)
h21_spalière = Habit("spalière", 40, 495, "toile", "torse", False, 20, 20, 100)
h22_gorgerin = Habit("gorgerin", 40, 560, "toile", "torse", False, 20, 20, 100)
h23_gants_fer = Habit("gants_fer", 80, 420, "toile", "torse", False, 30, 20, 100)
h24_gants_acier = Habit("gants_acier", 120, 840, "toile", "torse", False, 60, 20, 100)
h25_gantelet = Habit("gantelet", 100, 700, "toile", "torse", False, 100, 20, 100)
h26_plastron = Habit("plastron", 200, 3500, "toile", "torse", False, 200, 20, 100)
h26_cuirasse = Habit("cuirasse", 400, 7000, "toile", "torse", False, 300, 20, 100)
h27_tassettes = Habit("tassettes", 50, 450, "toile", "torse", False, 50, 20, 100)
h28_armure_fer = Habit("armure_fer", 250, 2200, "toile", "torse", False, 250, 20, 100)
h28_armure_acier = Habit("armure_acier", 600, 8400, "toile", "torse", False, 500, 20, 100)
o1_canne_a_peche = Objet("canne_a_peche", 10, 250, 50)
l1_carte_tarik = Livre("Carte du village de Tarik", 1, 5, 1, 1, bibliotheque.carte_tarik["plan"]["plan"], 100)
n1_bout_de_pain = Nourriture("Bout de pain", 1, 2, 265, "nourrie", 100)
n2_pomme = Nourriture("Pomme", 2, 0.5, 52, "nourrie", 100)
n2_poire = Nourriture("Poire", 2, 1, 52, "nourrie", 100)
n2_abricot = Nourriture("abricot", 2, 3, 52, "nourrie", 100)
n2_mure = Nourriture("mure", 0.5, 4, 52, "nourrie", 100)
n2_raisin = Nourriture("raisin", 0.6, 8, 52, "nourrie", 100)
n2_framboise = Nourriture("framboise", 1, 4, 52, "nourrie", 100)
n2_fraise = Nourriture("fraise", 1, 45, 52, "nourrie", 100)
n2_orange = Nourriture("orange", 1, 12, 52, "nourrie", 100)
n2_pamplemousse = Nourriture("pamplemousse", 1, 34, 52, "nourrie", 100)
n2_citron = Nourriture("citron", 1, 20, 52, "nourrie", 100)
n2_mirtille = Nourriture("mirtille", 1, 10, 52, "nourrie", 100)
n2_pêche = Nourriture("pêche", 1, 15, 52, "nourrie", 100)
n3_laitue = Nourriture("laitue", 1, 2, 52, "nourrie", 100)
n3_ail = Nourriture("ail", 1, 8, 52, "nourrie", 100)
n3_oignon = Nourriture("oignon", 1, 6, 52, "nourrie", 100)
n3_poireau = Nourriture("poireau", 1, 4, 52, "nourrie", 100)
n3_betterave = Nourriture("betterave", 1, 10, 52, "nourrie", 100)
n3_endive = Nourriture("endive", 1, 0.1, 52, "nourrie", 100)
n3_radis = Nourriture("radis", 1, 0.2, 52, "nourrie", 100)
n3_chou = Nourriture("chou", 1, 2, 52, "nourrie", 100)
n3_epinard = Nourriture("epinard", 1, 4, 52, "nourrie", 100)
n4_pomme_de_terre = Nourriture("pomme_de_terre", 5, 0.8, 52, "nourrie", 100)
n4_pain = Nourriture("pain", 2, 4, 52, "nourrie", 100)
n4_houblon = Nourriture("houblon", 1, 50, 52, "nourrie", 100)
n4_riz = Nourriture("riz", 10, 40, 52, "nourrie", 100)
n4_avoine = Nourriture("avoine", 10, 20, 52, "nourrie", 100)
n4_ble = Nourriture("ble", 10, 10, 52, "nourrie", 100)
n4_seigle = Nourriture("seigle", 10, 5, 52, "nourrie", 100)
n4_farine = Nourriture("farine", 20, 40, 52, "nourrie", 100)
n4_levain = Nourriture("levain", 10, 90, 52, "nourrie", 100)
n5_lapin = Nourriture("lapin", 20, 50, 52, "nourrie", 100)
n5_cheval = Nourriture("cheval", 150, 250, 52, "nourrie", 100)
n5_daim = Nourriture("daim", 150, 120, 52, "nourrie", 100)
n5_chevreuil = Nourriture("chevreuil", 150, 140, 52, "nourrie", 100)
n5_porc = Nourriture("porc", 150, 100, 52, "nourrie", 100)
n5_boeuf = Nourriture("boeuf", 200, 450, 52, "nourrie", 100)
n5_sanglier = Nourriture("sanglier", 250, 350, 52, "nourrie", 100)
n5_poulet = Nourriture("poulet", 25, 80, 52, "nourrie", 100)
n5_anguille = Nourriture("anguille", 20, 300, 52, "nourrie", 100)
n5_oie = Nourriture("oie", 30, 90, 52, "nourrie", 100)
n5_poisson = Nourriture("poisson", 10, 65, 52, "nourrie", 100)
n5_saumon = Nourriture("saumon", 10, 1200, 52, "nourrie", 100)
n5_sardine = Nourriture("sardine", 2, 40, 52, "nourrie", 100)
n6_oeuf = Nourriture("oeuf", 1, 50, 52, "nourrie", 100)
n6_fromage = Nourriture("fromage", 2, 90, 52, "nourrie", 100)
n6_lait = Nourriture("lait", 10, 50, 52, "nourrie", 100)
n7_tarte = Nourriture("tarte", 5, 40, 52, "nourrie", 100)
n7_gateau = Nourriture("gateau", 1, 10, 52, "nourrie", 100)
n7_biscuit = Nourriture("biscuit", 1, 2, 52, "nourrie", 100)
n7_viande_seche = Nourriture("viande_seche", 2, 45, 52, "nourrie", 100)
n7_soupe = Nourriture("soupe", 1, 1, 52, "nourrie", 100)
n7_bouillon = Nourriture("bouillon", 1, 2, 52, "nourrie", 100)
n7_miel = Nourriture("miel", 1, 120, 52, "nourrie", 100)
n8_acerola = Nourriture("acerola", 1, 140, 52, "nourrie", 100)
n8_artichaud = Nourriture("artichaud", 1, 85, 52, "nourrie", 100)
n8_cassis = Nourriture("cassis", 1, 250, 52, "nourrie", 100)
n8_fenouille = Nourriture("fenouille", 1, 120, 52, "nourrie", 100)
n8_melisse = Nourriture("melisse", 1, 640, 52, "nourrie", 100)
n8_menthe = Nourriture("menthe", 1, 200, 52, "nourrie", 100)
n8_valeriane = Nourriture("valeriane", 1, 120, 52, "nourrie", 100)
n8_cytise = Nourriture("cytise", 1, 260, 52, "nourrie", 100)
n8_belladone = Nourriture("belladone", 1, 480, 52, "nourrie", 100)
n8_arsenic = Nourriture("arsenic", 1, 900, 52, "empoisonne", 100)
n8_cigue = Nourriture("cigue", 1, 1200, 52, "empoisonne", 100)
n8_muguet = Nourriture("muguet", 1, 150, 52, "empoisonne", 100)
n8_ricin = Nourriture("ricin", 1, 130, 52, "empoisonne", 100)
n8_cepe = Nourriture("cêpe", 1, 100, 52, "nourrie", 100)
n8_champignon_tue = Nourriture("cortinaire", 1, 450, 52, "empoisonne", 100)
n8_champignon_hallucinogene = Nourriture("psylocibe", 1, 200, 52, "hallucinogène", 100)
n8_laurier_cerise = Nourriture("laurier_cerise", 1, 120, 52, "empoisonne", 100)
b1_gourde = Boisson("Gourde", 1, 5, "hydrate", 50, "eau", 100)
b1_bouteille_vin_rouge = Boisson("bouteille_vin_rouge", 500, 40, "alcoolise", 50, "eau", 100)
b1_bouteille_vin_blanc = Boisson("bouteille_vin_blanc", 500, 45, "alcoolise", 50, "eau", 100)
b1_bouteille_vin_rose = Boisson("bouteille_vin_rose", 500, 50, "alcoolise", 50, "eau", 100)
b1_bouteille_hydromel = Boisson("bouteille_hydromel", 500, 30, "alcoolise", 50, "eau", 100)
b1_bouteille_biere = Boisson("bouteille_biere", 500, 20, "alcoolise", 50, "eau", 100)
b1_bouteille_huile = Boisson("bouteille_huile", 500, 25, "cuisson", 50, "eau", 100)
b1_bouteille_poix = Boisson("bouteille_poix", 500, 80, "s'enflamme", 50, "eau", 100)
b1_bouteille_vinaigre = Boisson("bouteille_vinaigre", 500, 35, "hydrate", 50, "eau", 100)
a1_epee_bois = Arme("Epee de bois", 100, "contondante", 10, 5, 20, 55)
a1_epee_fer = Arme("Epee de fer", 1000, "tranchante", 120, 50, 30, 85)
a1_epee_acier = Arme("Epee d'acier", 2000, "tranchante", 280, 90, 40, 100)
a1_epee_courte = Arme("Epee courte", 500, "tranchante", 100, 40, 10, 40)
a1_epee_batarde = Arme("Epee batarde", 4000, "tranchante", 950, 80, 40, 8200)
a1_epee_longue = Arme("Epee longue", 3000, "tranchante", 1400, 120, 20, 100)
a1_epee_de_croise = Arme("Epee de croise", 6000, "tranchante", 6200, 160, 80, 100)
a1_epee_a_deux_mains = Arme("Epee a_deux_mains", 8000, "tranchante", 4200, 200, 10, 100)
a1_fleuret = Arme("fleuret", 800, "tranchante", 250, 60, 40, 100)
a1_epee_bersek = Arme("Epee bersek", 5000, "tranchante", 350, 180, 5, 100)
a1_cimeterre = Arme("cimeterr", 600, "tranchante", 250, 75, 10, 100)
a2_rondin = Arme("rondin", 1000, "tranchante", 80, 5, 40, 100)
a2_bouclier_fer = Arme("bouclier_fer", 2000, "tranchante", 220, 5, 80, 100)
a2_bouclier_acier = Arme("bouclier_acier", 4000, "tranchante", 440, 5, 120, 100)
a2_grand_bouclier = Arme("grand_bouclier", 6000, "tranchante", 850, 5, 250, 100)
a2_bouclier_normand = Arme("Epee de bois", 8000, "tranchante", 1600, 5, 350, 100)
a2_targe = Arme("targe", 400, "tranchante", 40, 5, 20, 100)
a3_arc_simple = Arme("arc_simple", 200, "perforant", 70, 20, 0, 100)
a3_arc_compose = Arme("arc_composé", 400, "perforant", 290, 30, 0, 100)
a3_arc_chasseur = Arme("arc_chasseur", 600, "perforant", 200, 50, 0, 100)
a3_arc_ebene = Arme("arc_ebene", 800, "tranchante", 860, 80, 0, 100)
a4_masse_darme = Arme("masse_darme", 3000, "contondante", 90, 95, -10, 100)
a5_hache_courte = Arme("hache_courte", 1000, "tranchante", 110, 55, 5, 100)
a5_hache_bucheron = Arme("hache_bucheron", 2000, "tranchante", 180, 105, 5, 100)
a5_double_hache = Arme("double_hache", 4000, "tranchante", 350, 305, -20, 100)
a5_francisque = Arme("francisque", 8000, "tranchante", 645, 380, -5, 100)
a5_hache_de_lancer = Arme("hache_de_lancer", 200, "tranchante", 110, 50, 0, 100)
a6_gourdin = Arme("gourdin", 9000, "contondante", 55, 90, -80, 100)
a7_fleche_simple = Arme("fleche_simple", 10, "perforant", 5, 10, 0, 100)
a7_fleche_fer = Arme("fleche_fer", 20, "perforant", 20, 20, 0, 100)
a7_fleche_acier = Arme("fleche_acier", 40, "perforant", 40, 30, 0, 100)
a8_arbalete = Arme("arbalete", 2000, "perforant", 840, 80, 0, 100)
a9_carreau = Arme("carreau", 50, "perforant", 20, 50, 0, 100)
a10_baton = Arme("baton", 300, "contondante", 2, 5, 40, 100)
a11_branche = Arme("branche", 100, "contondante", 0.1, 5, 40, 100)
a12_pierre = Arme("pierre", 100, "contondante", 0.1, 5, 40, 100)
a13_hallebarde = Arme("hallebarde", 4000, "tranchante", 720, 15, 40, 100)
a14_dague = Arme("dague", 100, "tranchante", 40, 5, 40, 100)
a14_poignard = Arme("poignard", 100, "tranchante", 60, 5, 40, 100)
a14_coupe_papier = Arme("coupe_papier", 100, "tranchante", 20, 5, 40, 100)
a15_lance = Arme("lance", 800, "perforant", 120, 5, 40, 100)
a16_marteau = Arme("marteau de guerre", 4000, "contondante", 105, 5, 40, 100)
a17_pique = Arme("pique", 1000, "perforant", 230, 5, 40, 100)
a18_fleau_darme = Arme("fleau_darme", 2000, "contondante", 120, 5, 40, 100)
a18_goupillon = Arme("goupillon", 1000, "contondante", 80, 5, 40, 100)
a19_fourche = Arme("fourche", 600, "perforant", 50, 5, 40, 100)
a19_faucille = Arme("faucille", 100, "tranchante", 10, 5, 40, 100)
a19_faux = Arme("faux", 1000, "tranchante", 40, 5, 40, 100)
a19_houe = Arme("houe", 1000, "tranchante", 80, 5, 40, 100)


sac_joueur = Contenant("sac_joueur")
sac_autre = Contenant("autre")
poid_sac_joueur = d1_bandage.poid

for loop in range(2000):
    sac_joueur.ajouter(o1_denier)
for loop in range(5):
    sac_joueur.ajouter(d1_bandage)
sac_joueur.ajouter(o2_choppe_de_bois)
sac_joueur.ajouter(h1_chemise_de_lin)
sac_joueur.ajouter(h2_chaussure_de_cuir)
sac_joueur.ajouter(h3_pantalon_cuir)
sac_joueur.ajouter(l1_carte_tarik)
for loop in range(2):
    sac_joueur.ajouter(n1_bout_de_pain)
sac_joueur.ajouter(n2_pomme)
sac_joueur.ajouter(h4_capuchon)
# sac_joueur.ajouter(h4_capuchon, "joueur")
sac_joueur.ajouter(b1_gourde)
sac_joueur.ajouter(a1_epee_bois)
sac_joueur.ajouter(a2_bouclier_acier)
sac_joueur.ajouter(a1_epee_de_croise)
# for loop in range(6250):
#     sac_autre.ajouter(o1_denier)
# sac_autre.ajouter(d1_bandage)
# sac_autre.ajouter(o2_choppe_de_bois)
# sac_autre.ajouter(h1_chemise_de_lin)
# sac_autre.ajouter(h2_chaussure_de_cuir)
# sac_autre.ajouter(h3_braies_de_lin)
# sac_autre.ajouter(l1_carte_tarik)
# sac_autre.ajouter(n1_bout_de_pain)
# sac_autre.ajouter(n1_bout_de_pain)
# sac_autre.ajouter(n1_bout_de_pain)
# for loop in range(2):
#     sac_autre.ajouter(n2_pomme)
# sac_autre.ajouter(h4_capuchon)
# sac_autre.ajouter(b1_gourde)



# inventaire_initial = [h1_chemise_de_lin.__dict__, h2_chaussure_de_cuir.__dict__, l1_carte_tarik.__dict__, n1_bout_de_pain.__dict__, n2_pomme.__dict__]


#begin = time.time()
#print("Début")
#time.sleep(5)
#end = time.time()
#print("Fin")
#print(f"Temps exécuté : {end - begin}s")
tps = time.localtime()
print(tps)
