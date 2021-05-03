import objet
import random


class Meuble:

    def __init__(self, nom):
        self.nom = nom
        self.propriete = ''
        self.contenant = []


#Mobilier
table = Meuble("table")
random_objet = random.randint(0,1)
if random_objet == 0:
    table.contenant.append(objet.n7_tarte)
else:
    table.contenant.append(objet.d1_bougie)
random_objet2 = random.randint(0,2)
if random_objet2 == 0:
    table.contenant.append(objet.d1_verre)
    table.contenant.append(objet.d1_verre)
    table.contenant.append(objet.d1_fourchette)
    table.contenant.append(objet.d1_fourchette)
    table.contenant.append(objet.d1_assiette)
    table.contenant.append(objet.d1_assiette)
    table.contenant.append(objet.n1_bout_de_pain)
    table.contenant.append(objet.o2_choppe_de_bois)
elif random_objet2 == 1:
    table.contenant.append(objet.d1_bougie)
    table.contenant.append(objet.d1_verre)
    table.contenant.append(objet.d1_fourchette)
    table.contenant.append(objet.d1_fourchette)
    table.contenant.append(objet.d1_assiette)
    table.contenant.append(objet.d1_encens)
    table.contenant.append(objet.n1_bout_de_pain)
    table.contenant.append(objet.o2_choppe_de_bois)
else:
    table.contenant.append(objet.o2_choppe_de_bois)

random_objet3 = random.randint(0,1)
if random_objet3 == 0:
    table.contenant.append(objet.b1_bouteille_biere)
else:
    table.contenant.append(objet.n6_fromage)
    table.contenant.append(objet.n6_fromage)
    table.contenant.append(objet.n2_pomme)
    table.contenant.append(objet.n2_raisin)
    table.contenant.append(objet.b1_bouteille_hydromel)
random_objet4 = random.randint(0,1)
if random_objet4 == 0:
    pass
else:
    table.contenant.append(objet.o1_denier)
    table.contenant.append(objet.n3_ail)
random_objet5 = random.randint(0,1)
if random_objet5 == 0:
    table.contenant.append(objet.n8_fenouille)
    table.contenant.append(objet.n8_muguet)
    table.contenant.append(objet.b1_bouteille_vin_blanc)
else:
    table.contenant.append(objet.n3_endive)
    table.contenant.append(objet.n3_radis)
    table.contenant.append(objet.n3_radis)
    table.contenant.append(objet.n5_porc)
    table.contenant.append(objet.b1_bouteille_huile)

chaise = Meuble("chaise")

armoire = Meuble("armoire")
random_objet = random.randint(0,1)
if random_objet == 0:
    armoire.contenant.append(objet.n7_miel)
    armoire.contenant.append(objet.n5_lapin)
    armoire.contenant.append(objet.n3_poireau)
    armoire.contenant.append(objet.n3_poireau)
    armoire.contenant.append(objet.n3_poireau)
    armoire.contenant.append(objet.n3_oignon)
    armoire.contenant.append(objet.n3_oignon)
    armoire.contenant.append(objet.n3_oignon)
    armoire.contenant.append(objet.n4_pomme_de_terre)
    armoire.contenant.append(objet.n4_pomme_de_terre)
    armoire.contenant.append(objet.n4_pomme_de_terre)
    armoire.contenant.append(objet.n4_pomme_de_terre)
    armoire.contenant.append(objet.n3_laitue)
    armoire.contenant.append(objet.n3_laitue)
    armoire.contenant.append(objet.n3_laitue)
else:
    armoire.contenant.append(objet.a14_dague)
random_objet2 = random.randint(0,1)
if random_objet2 == 0:
    armoire.contenant.append(objet.d1_verre)
    armoire.contenant.append(objet.d1_verre)
    armoire.contenant.append(objet.d1_verre)
    armoire.contenant.append(objet.d1_verre)
    armoire.contenant.append(objet.d1_verre)
    armoire.contenant.append(objet.d1_fourchette)
    armoire.contenant.append(objet.d1_fourchette)
    armoire.contenant.append(objet.d1_fourchette)
    armoire.contenant.append(objet.d1_fourchette)
    armoire.contenant.append(objet.d1_assiette)
    armoire.contenant.append(objet.d1_assiette)
    armoire.contenant.append(objet.d1_assiette)
    armoire.contenant.append(objet.d1_assiette)
    armoire.contenant.append(objet.n1_bout_de_pain)
else:
    pass
random_objet3 = random.randint(0,1)
if random_objet3 == 0:
    pass
else:
    armoire.contenant.append(objet.b1_bouteille_vin_rouge)
    armoire.contenant.append(objet.b1_bouteille_vin_rouge)
    armoire.contenant.append(objet.b1_bouteille_vin_rouge)
    armoire.contenant.append(objet.n8_cytise)
    armoire.contenant.append(objet.b1_bouteille_vin_rouge)
    armoire.contenant.append(objet.b1_bouteille_vin_rouge)
random_objet4 = random.randint(0,1)
if random_objet4 == 0:
    armoire.contenant.append(objet.n6_fromage)
    armoire.contenant.append(objet.n6_fromage)
    armoire.contenant.append(objet.n6_fromage)
    armoire.contenant.append(objet.n7_biscuit)
    armoire.contenant.append(objet.n7_biscuit)
    armoire.contenant.append(objet.n7_biscuit)
    armoire.contenant.append(objet.n7_viande_seche)
else:
    armoire.contenant.append(objet.o1_denier)
    armoire.contenant.append(objet.o1_denier)
    armoire.contenant.append(objet.o1_denier)
    armoire.contenant.append(objet.o1_denier)
    armoire.contenant.append(objet.b1_bouteille_hydromel)
random_objet5 = random.randint(0,1)
if random_objet5 == 0:
    pass
else:
    armoire.contenant.append(objet.b1_bouteille_biere)
    armoire.contenant.append(objet.n3_endive)
    armoire.contenant.append(objet.n3_endive)
    armoire.contenant.append(objet.n8_menthe)
    armoire.contenant.append(objet.b1_bouteille_vinaigre)
    armoire.contenant.append(objet.b1_bouteille_vinaigre)


lit = Meuble("lit")

table_de_chevet = Meuble("table_de_chevet")
random_objet = random.randint(0,1)
if random_objet == 0:
    table_de_chevet.contenant.append(objet.b1_bracelet)
    table_de_chevet.contenant.append(objet.d1_bougie)
    table_de_chevet.contenant.append(objet.d1_encens)
    table_de_chevet.contenant.append(objet.m1_cire)
    table_de_chevet.contenant.append(objet.d1_allumette)
    table_de_chevet.contenant.append(objet.d1_bandage)
    table_de_chevet.contenant.append(objet.o1_denier)
    table_de_chevet.contenant.append(objet.o1_denier)
else:
    table_de_chevet.contenant.append(objet.b1_bague)
random_objet2 = random.randint(0,1)
if random_objet2 == 0:
    table_de_chevet.contenant.append(objet.d1_verre)
else:
    pass
random_objet3 = random.randint(0,1)
if random_objet3 == 0:
    pass
else:
    table_de_chevet.contenant.append(objet.d1_bandage)
random_objet4 = random.randint(0,1)
if random_objet4 == 0:
    table_de_chevet.contenant.append(objet.o1_denier)
    table_de_chevet.contenant.append(objet.o1_denier)
    table_de_chevet.contenant.append(objet.o1_denier)
    table_de_chevet.contenant.append(objet.n7_biscuit)
    table_de_chevet.contenant.append(objet.n7_biscuit)
else:
    armoire.contenant.append(objet.h4_couverture)
random_objet5 = random.randint(0,1)
if random_objet5 == 0:
    pass
else:
    armoire.contenant.append(objet.b1_bouteille_biere)

buanderie = Meuble("buanderie")
random_objet = random.randint(0,1)
if random_objet == 0:
    buanderie.contenant.append(objet.h2_chaussons)
    buanderie.contenant.append(objet.b1_bracelet)
    buanderie.contenant.append(objet.b1_collier)
    buanderie.contenant.append(objet.h3_pantalon_cuir)
    buanderie.contenant.append(objet.h3_pantalon_cuir)
    buanderie.contenant.append(objet.h2_souliers)
    buanderie.contenant.append(objet.h4_couverture)
    buanderie.contenant.append(objet.h4_couverture)
    buanderie.contenant.append(objet.h2_bottes)
    buanderie.contenant.append(objet.h5_chemise_de_laine)
    buanderie.contenant.append(objet.h5_chemise_de_laine)
    buanderie.contenant.append(objet.h5_chemise_de_laine)
    buanderie.contenant.append(objet.h8_ceinture)
    buanderie.contenant.append(objet.h7_tunique_de_cuir)
else:
    buanderie.contenant.append(objet.a14_dague)
random_objet2 = random.randint(0,1)
if random_objet2 == 0:
    buanderie.contenant.append(objet.h11_tunique_velours)
    buanderie.contenant.append(objet.h12_braies_velours)
    buanderie.contenant.append(objet.d1_verre)
else:
    pass
random_objet3 = random.randint(0,1)
if random_objet3 == 0:
    pass
else:
    buanderie.contenant.append(objet.h13_chemise_de_toile)
    buanderie.contenant.append(objet.h13_chemise_de_toile)
    buanderie.contenant.append(objet.h13_chemise_de_toile)
    buanderie.contenant.append(objet.h4_capuchon)
    buanderie.contenant.append(objet.h4_couverture)
    buanderie.contenant.append(objet.h4_manteau)
random_objet4 = random.randint(0,1)
if random_objet4 == 0:
    buanderie.contenant.append(objet.h2_houseaux)
    buanderie.contenant.append(objet.h2_houseaux)
    buanderie.contenant.append(objet.h2_houseaux)
    buanderie.contenant.append(objet.h2_houseaux)
    buanderie.contenant.append(objet.h2_chaussure_de_cuir)
    buanderie.contenant.append(objet.h1_chemise_de_lin)
    buanderie.contenant.append(objet.n7_viande_seche)
else:
    buanderie.contenant.append(objet.h9_collant_noble)
    buanderie.contenant.append(objet.h12_braies_velours)
    buanderie.contenant.append(objet.h13_chemise_de_toile)
    buanderie.contenant.append(objet.h13_chemise_de_toile)
    buanderie.contenant.append(objet.h17_jambiere)
random_objet5 = random.randint(0,1)
if random_objet5 == 0:
    pass
else:
    buanderie.contenant.append(objet.d1_bandage)
    buanderie.contenant.append(objet.d1_bandage)
    buanderie.contenant.append(objet.d1_bandage)
    buanderie.contenant.append(objet.d1_bougie)
    buanderie.contenant.append(objet.m1_laine)
    buanderie.contenant.append(objet.m1_tissu)

coffre = Meuble("coffre")
random_objet = random.randint(0,1)
if random_objet == 0:
    coffre.contenant.append(objet.h3_braies_de_lin)
    coffre.contenant.append(objet.h3_braies_de_lin)
    coffre.contenant.append(objet.b1_couronne)
    coffre.contenant.append(objet.b1_bague)
    coffre.contenant.append(objet.n3_oignon)
    coffre.contenant.append(objet.h2_souliers)
    coffre.contenant.append(objet.h4_couverture)
    coffre.contenant.append(objet.h4_couverture)
    coffre.contenant.append(objet.h2_bottes)
    coffre.contenant.append(objet.h5_chemise_de_laine)
    coffre.contenant.append(objet.h5_chemise_de_laine)
    coffre.contenant.append(objet.h5_chemise_de_laine)
    coffre.contenant.append(objet.h8_ceinture)
    coffre.contenant.append(objet.h7_tunique_de_cuir)
else:
    coffre.contenant.append(objet.h3_braies_de_lin)
random_objet2 = random.randint(0,1)
if random_objet2 == 0:
    coffre.contenant.append(objet.h3_braies_de_lin)
    coffre.contenant.append(objet.h3_braies_de_lin)
    coffre.contenant.append(objet.h3_braies_de_lin)
    coffre.contenant.append(objet.h3_braies_de_lin)
    coffre.contenant.append(objet.h2_houseaux)
    coffre.contenant.append(objet.h2_chaussons)
    coffre.contenant.append(objet.h2_houseaux)
    coffre.contenant.append(objet.h4_cape)
    coffre.contenant.append(objet.d1_clou)
    coffre.contenant.append(objet.d1_clou)
    coffre.contenant.append(objet.d1_clou)
    coffre.contenant.append(objet.d1_clou)
    coffre.contenant.append(objet.d1_clou)
    coffre.contenant.append(objet.d1_clou)
else:
    pass
random_objet3 = random.randint(0,1)
if random_objet3 == 0:
    pass
else:
    coffre.contenant.append(objet.h7_tunique_de_cuir)
    coffre.contenant.append(objet.h7_tunique_de_cuir)
    coffre.contenant.append(objet.h7_tunique_de_cuir)
    coffre.contenant.append(objet.h4_cape)
    coffre.contenant.append(objet.h7_tunique_de_cuir)
    coffre.contenant.append(objet.b1_bouteille_vin_rouge)
    coffre.contenant.append(objet.h3_braies_de_lin)
    coffre.contenant.append(objet.h3_braies_de_lin)
    coffre.contenant.append(objet.h3_braies_de_lin)
    coffre.contenant.append(objet.n7_biscuit)
    coffre.contenant.append(objet.n7_biscuit)
    coffre.contenant.append(objet.n7_biscuit)
    coffre.contenant.append(objet.n7_viande_seche)
random_objet4 = random.randint(0,2)
if random_objet4 == 0:
    random_deniers = random.randint(0,10)
    for loop in range(random_deniers):
        coffre.contenant.append(objet.o1_denier)
elif random_objet4 == 1:
    random_deniers = random.randint(0,50)
    for loop in range(random_deniers):
        coffre.contenant.append(objet.o1_denier)
else:
    random_deniers = random.randint(0,100)
    for loop in range(random_deniers):
        coffre.contenant.append(objet.o1_denier)
    coffre.contenant.append(objet.b1_bouteille_hydromel)
random_objet5 = random.randint(0,1)
if random_objet5 == 0:
    pass
else:
    coffre.contenant.append(objet.m1_or)
    coffre.contenant.append(objet.n3_endive)
    coffre.contenant.append(objet.d1_coupole)
    coffre.contenant.append(objet.d1_cierge)
    coffre.contenant.append(objet.b1_bouteille_vinaigre)
    coffre.contenant.append(objet.b1_bouteille_vinaigre)

banc = Meuble("banc")
etagere = Meuble("etagere")
random_objet = random.randint(0,1)
if random_objet == 0:
    etagere.contenant.append(objet.n7_miel)
    etagere.contenant.append(objet.n5_lapin)
    etagere.contenant.append(objet.n3_poireau)
    etagere.contenant.append(objet.n3_poireau)
    etagere.contenant.append(objet.n3_poireau)
    etagere.contenant.append(objet.n3_oignon)
    etagere.contenant.append(objet.n3_oignon)
    etagere.contenant.append(objet.n5_sanglier)
    etagere.contenant.append(objet.n2_poire)
    etagere.contenant.append(objet.n2_poire)
    etagere.contenant.append(objet.n4_pomme_de_terre)
    etagere.contenant.append(objet.n4_pomme_de_terre)
    etagere.contenant.append(objet.n2_poire)
    etagere.contenant.append(objet.n3_laitue)
    etagere.contenant.append(objet.n3_laitue)
else:
    etagere.contenant.append(objet.a14_dague)
random_objet2 = random.randint(0,1)
if random_objet2 == 0:
    etagere.contenant.append(objet.n7_gateau)
    etagere.contenant.append(objet.n7_gateau)
    etagere.contenant.append(objet.n7_gateau)
    etagere.contenant.append(objet.n7_gateau)
    etagere.contenant.append(objet.d1_verre)
    etagere.contenant.append(objet.b1_bouteille_biere)
    etagere.contenant.append(objet.b1_bouteille_biere)
    etagere.contenant.append(objet.b1_bouteille_biere)
    etagere.contenant.append(objet.d1_fourchette)
    etagere.contenant.append(objet.d1_assiette)
    etagere.contenant.append(objet.d1_assiette)
    etagere.contenant.append(objet.d1_assiette)
    etagere.contenant.append(objet.d1_assiette)
    etagere.contenant.append(objet.n1_bout_de_pain)
else:
    pass
random_objet3 = random.randint(0,1)
if random_objet3 == 0:
    pass
else:
    etagere.contenant.append(objet.b1_bouteille_vin_rouge)
    etagere.contenant.append(objet.b1_bouteille_vin_rouge)
    etagere.contenant.append(objet.b1_bouteille_vin_rouge)
    etagere.contenant.append(objet.n8_cytise)
    etagere.contenant.append(objet.b1_bouteille_vin_rouge)
    etagere.contenant.append(objet.b1_bouteille_vin_rouge)
random_objet4 = random.randint(0,1)
if random_objet4 == 0:
    etagere.contenant.append(objet.n6_fromage)
    etagere.contenant.append(objet.n6_fromage)
    etagere.contenant.append(objet.n6_fromage)
    etagere.contenant.append(objet.n7_biscuit)
    etagere.contenant.append(objet.n7_biscuit)
    etagere.contenant.append(objet.n7_biscuit)
    etagere.contenant.append(objet.n7_viande_seche)
else:
    etagere.contenant.append(objet.o1_denier)
    etagere.contenant.append(objet.o1_denier)
    etagere.contenant.append(objet.o1_denier)
    etagere.contenant.append(objet.o1_denier)
    etagere.contenant.append(objet.b1_bouteille_hydromel)
random_objet5 = random.randint(0,1)
if random_objet5 == 0:
    pass
else:
    etagere.contenant.append(objet.b1_bouteille_biere)
    etagere.contenant.append(objet.n3_endive)
    etagere.contenant.append(objet.n3_endive)
    etagere.contenant.append(objet.n8_menthe)
    etagere.contenant.append(objet.b1_bouteille_vinaigre)
    etagere.contenant.append(objet.b1_bouteille_vinaigre)

atelier_boulangerie = Meuble("atelier_boulangerie")
random_objet = random.randint(0,1)
if random_objet == 0:
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n7_gateau)
    atelier_boulangerie.contenant.append(objet.n7_gateau)
    atelier_boulangerie.contenant.append(objet.n7_gateau)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n7_biscuit)
    atelier_boulangerie.contenant.append(objet.n7_biscuit)
    atelier_boulangerie.contenant.append(objet.n7_biscuit)
    atelier_boulangerie.contenant.append(objet.n7_tarte)
    atelier_boulangerie.contenant.append(objet.n7_tarte)
    atelier_boulangerie.contenant.append(objet.n7_tarte)
    atelier_boulangerie.contenant.append(objet.n7_tarte)
else:
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_pain)
    atelier_boulangerie.contenant.append(objet.n4_farine)
    atelier_boulangerie.contenant.append(objet.n4_farine)
    atelier_boulangerie.contenant.append(objet.n4_farine)
    atelier_boulangerie.contenant.append(objet.n4_seigle)

atelier_forge = Meuble("atelier_forge")
random_objet = random.randint(0,1)
if random_objet == 0:
    atelier_forge.contenant.append(objet.a1_epee_acier)
    atelier_forge.contenant.append(objet.a1_epee_acier)
    atelier_forge.contenant.append(objet.a2_bouclier_acier)
    atelier_forge.contenant.append(objet.a2_bouclier_fer)
    atelier_forge.contenant.append(objet.a1_epee_bersek)
    atelier_forge.contenant.append(objet.a3_arc_chasseur)
    atelier_forge.contenant.append(objet.h4_couverture)
    atelier_forge.contenant.append(objet.a13_hallebarde)
    atelier_forge.contenant.append(objet.h2_bottes)
    atelier_forge.contenant.append(objet.a1_epee_batarde)
    atelier_forge.contenant.append(objet.a1_epee_batarde)
    atelier_forge.contenant.append(objet.a1_epee_batarde)
    atelier_forge.contenant.append(objet.a1_epee_acier)
    atelier_forge.contenant.append(objet.h7_tunique_de_cuir)
else:
    atelier_forge.contenant.append(objet.a14_dague)
    atelier_forge.contenant.append(objet.a14_dague)
    atelier_forge.contenant.append(objet.a5_hache_courte)
    atelier_forge.contenant.append(objet.a5_hache_courte)
    atelier_forge.contenant.append(objet.a5_hache_de_lancer)
    atelier_forge.contenant.append(objet.a7_fleche_fer)
    atelier_forge.contenant.append(objet.a7_fleche_fer)
    atelier_forge.contenant.append(objet.a14_dague)

atelier_tisserie = Meuble("atelier_tisserie")
random_objet = random.randint(0,1)
if random_objet == 0:
    atelier_tisserie.contenant.append(objet.h2_chaussons)
    atelier_tisserie.contenant.append(objet.b1_bracelet)
    atelier_tisserie.contenant.append(objet.b1_collier)
    atelier_tisserie.contenant.append(objet.h3_pantalon_cuir)
    atelier_tisserie.contenant.append(objet.h3_pantalon_cuir)
    atelier_tisserie.contenant.append(objet.h2_souliers)
    atelier_tisserie.contenant.append(objet.h4_couverture)
    atelier_tisserie.contenant.append(objet.h4_couverture)
    atelier_tisserie.contenant.append(objet.h2_bottes)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h8_ceinture)
    atelier_tisserie.contenant.append(objet.h7_tunique_de_cuir)
else:
    atelier_tisserie.contenant.append(objet.h3_pantalon_cuir)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)
    atelier_tisserie.contenant.append(objet.h5_chemise_de_laine)

atelier_herboristerie = Meuble("atelier_herboristerie")
random_objet = random.randint(0,1)
if random_objet == 0:
    atelier_herboristerie.contenant.append(objet.n3_ail)
    atelier_herboristerie.contenant.append(objet.n3_ail)
    atelier_herboristerie.contenant.append(objet.n3_epinard)
    atelier_herboristerie.contenant.append(objet.n8_cassis)
    atelier_herboristerie.contenant.append(objet.n8_acerola)
    atelier_herboristerie.contenant.append(objet.n8_artichaud)
    atelier_herboristerie.contenant.append(objet.n8_menthe)
    atelier_herboristerie.contenant.append(objet.n8_valeriane)
    atelier_herboristerie.contenant.append(objet.n8_valeriane)
    atelier_herboristerie.contenant.append(objet.n8_cytise)
    atelier_herboristerie.contenant.append(objet.n8_belladone)
    atelier_herboristerie.contenant.append(objet.n8_muguet)
    atelier_herboristerie.contenant.append(objet.n8_ricin)
    atelier_herboristerie.contenant.append(objet.n8_cepe)
else:
    atelier_herboristerie.contenant.append(objet.n3_ail)
    atelier_herboristerie.contenant.append(objet.n3_ail)
    atelier_herboristerie.contenant.append(objet.n3_epinard)
    atelier_herboristerie.contenant.append(objet.b1_bouteille_huile)
    atelier_herboristerie.contenant.append(objet.n8_acerola)
    atelier_herboristerie.contenant.append(objet.n8_artichaud)
    atelier_herboristerie.contenant.append(objet.n8_melisse)
    atelier_herboristerie.contenant.append(objet.n8_champignon_hallucinogene)
    atelier_herboristerie.contenant.append(objet.n8_laurier_cerise)
    atelier_herboristerie.contenant.append(objet.n8_cytise)
    atelier_herboristerie.contenant.append(objet.b1_bouteille_poix)
    atelier_herboristerie.contenant.append(objet.n8_muguet)
    atelier_herboristerie.contenant.append(objet.n8_ricin)
    atelier_herboristerie.contenant.append(objet.n8_cepe)

atelier_auberge = Meuble("atelier_auberge")
random_objet = random.randint(0,1)
if random_objet == 0:
    atelier_auberge.contenant.append(objet.b1_bouteille_biere)
    atelier_auberge.contenant.append(objet.b1_bouteille_biere)
    atelier_auberge.contenant.append(objet.b1_bouteille_biere)
    atelier_auberge.contenant.append(objet.b1_bouteille_biere)
    atelier_auberge.contenant.append(objet.b1_bouteille_biere)
    atelier_auberge.contenant.append(objet.b1_bouteille_biere)
    atelier_auberge.contenant.append(objet.b1_bouteille_biere)
    atelier_auberge.contenant.append(objet.b1_bouteille_hydromel)
    atelier_auberge.contenant.append(objet.b1_bouteille_hydromel)
    atelier_auberge.contenant.append(objet.b1_bouteille_hydromel)
    atelier_auberge.contenant.append(objet.b1_bouteille_hydromel)
    atelier_auberge.contenant.append(objet.b1_bouteille_vin_rouge)
    atelier_auberge.contenant.append(objet.b1_bouteille_vin_rouge)
    atelier_auberge.contenant.append(objet.b1_bouteille_vin_rouge)
else:
    atelier_auberge.contenant.append(objet.b1_bouteille_biere)
    atelier_auberge.contenant.append(objet.b1_bouteille_biere)
    atelier_auberge.contenant.append(objet.b1_bouteille_hydromel)
    atelier_auberge.contenant.append(objet.b1_bouteille_hydromel)
    atelier_auberge.contenant.append(objet.b1_bouteille_hydromel)
    atelier_auberge.contenant.append(objet.b1_bouteille_hydromel)
    atelier_auberge.contenant.append(objet.b1_bouteille_vin_rouge)
