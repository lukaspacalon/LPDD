from random import choice

#/ Novice / Apprenti  / Compagnon / Professionnel / Expert / Maître /

class Quete:

    def __init__(self, nom, etat, description, qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description
        self.qui = qui
        self.quand = quand
        self.quoi = quoi
        self.comment = comment
        self.ou = ou
        self.pourquoi = pourquoi
        self.objectif = objectif
        self.recompense = recompense
        self.experience = experience
        self.score = score
        self.type = type



    def accepter(self):
        self.etat = "acceptée"

    def refuser(self):
        self.etat = "refusée"

class QueteSecondaireRecherche:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un livre", "mon repas", "un médaillon", "mes lunettes", "ma bourse", "mon fils", "mes affaires", "une amulette", "un objet précieux", "un parchemin", "un outil", "un écrit", "un manuscrit", "un cigario", "une arme", "mon épée", "mon arc", "mon manteau", "ma canne à pêche", "mon animal de compagnie", "mon chat", "mon chien", "mes amis", "ma bouteille", "mon sac"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["perdu", "égaré", "laissé", "entendu parlé", "l'envie", "fait tombé"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["c'est important pour moi", "c'est essentiel pour moi", "c'est toute ma vie", "c'est ma vie", "j'en ai besoin", "cela appartient à ma soeur", "cela appartient à ma mère qui le tient elle même de ma mère", "je suis perdu sans", "c'est essentiel pour moi", "j'en ai besoin demain", "sans ça je suis paumé", "ultra important", "ça serait sympa de le récupérer", "j'en ai peut être besoin"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["récupérer", "détruire", "trouvé", "faire disparaitre", "m'apporté l'objet", "que je l'ai"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type

class QueteSecondaireMonstre:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "son repaire", "son tresor"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type

class QueteSecondaireRumeur:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence", "le voisin", "une femme du village", "le prêtre", "le chef du village", "le chasseur", "le curée", "ma voisine", "mon voisin", "ma mère", "mon fils", "la mère du chef du village", "le père du petit grigory", "le boucher", "le fils du boulanger", "le boulanger", "la boulangère", "le tavernier", "un soldat de la garde", "un pêcheur", 'une prostitué', "une fille de petite vertu", "un chat", "un chien", "un lapin", "un druide", "un moine", "l'herboriste", "un espion", "le diacre", "un médecin", "un astrologue", "le bailli", "l'homme le plus riche du village", "tresorier", "le marquis", "le seigneur", "le baron", "le vicomte", "le vicaire", "le doyen", "le comte", "l'eveque", "l'abbe", "l'intendant", "le roi", "le prince", "le fils de l'empereur", "l'élu de la prophétie", "un elfe", "un nain", "un humain", "une fée", "une demi-homme", "un demi-elfe", "un aventurier", "un voyageur", "un type pas net", "un drôle de voyageur", "un lutin", "un homme arbre", "un centaure", "un minotaure", "un cheval", "un étrange marchand", "un musicien"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["hier", "il y a une semaine", "il y a un mois de cela", "avant hier", "", "hier soir soir", "hier à minuit", "il y a quelques jours"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["a prié le diable", "a perdu toute sa richesse", "est devenu riche", "a été tué", "a été violé", "a été assassiné", "est amoureux", "est devenu fou", "a pété les plombs", "a tué toute sa famille", "a massacré tout une ville", "a perdu son dentier", "a été excommunié", "s'est promené nu", "a mangé une pomme empoisonnée", "a danser sous la lune", "dort pied nu", "a été banni", "a gagné le grand prix", " a découvert un dragon", "a inventé la poudre", "a découvert le feu", "a changé tout un village en pierre", "a mis feu à la grange", "a fait tomber tous les criminelles de la région", "garde une pierre très précieuse", "a invoqué un démon !", "a annoncé la fin du monde", "a vu un nain sans barbe !", "a révolutionné la science", "a perdu ses clefs", "a vendu sa maison", "est à la rue", "est devenu sans domicile fixe", "était bourré", "a vomi dans l'église", "a déféquer dans la mairie", "sent mauvais", "pu le fromage pourri", "a trouvé un trésor", "a déterré un manuscrit qui date de 50 ans", "court tous les soirs", "ne mange jamais de légumes !", "ne mange jamais de viande", "se nourrit exclusivement de poisson"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["j'ai entendu dire que", "j'ai ouïe dire que", "il parait que", "vous savez ce qui se dit ?", "Approchez j'ai un secret pour vous !", " Vous ne connaissez pas la nouvelle ?", "Vous allez halluciner de ce que je vais vous dire !", "Préparez vous au pire", "Ecoutez moi bien", "J'ai entendu des rumeurs...", "Il court des bruits..", "Tout le monde en parle !", "C'est la nouvelle du moment !", "Vous n'allez pas me croire", "C'était sur toutes les bouches."]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["il parait !", "L'information n'est pas sur", "Je tiens ça de source sur !", "Il n'y a pas de doute !", "C'est une info exclusive !", "Je t'assure que c'est vrai", "Je ne mens pas", "C'est ce que j'ai entendu dire", "apparament !", "Après tout pourquoi pas !", "Moi vous savez ça m'en touche une sans toucher l'autre", "ça me parait bizarre mais bon", "C'est ce que j'ai entendu dire", "c'est ce qu'on m'a dit", "c'est ce que j'ai entendu dire mais c'est peut être faux", "je pense que c'est n'importe quoi !", "C'est plausible", "L'info n'est pas sur mais ça me parait cohérent", "il y a des chances pour que ce soit vrai", "tout ça me fait peur", "c'est pathétique !", "c'est surprenant !", "ça m'étonne mais bon..."]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["c'est étrange", "bref", "vous y croyez vous ?", "ça vous dit quelque chose ?", "une prière pour vous", "c'est tout", "j'ai jamais entendu quelque chose d'aussi con !", "...", "..", ".", "alors qu'est-ce que vous en dites", "c'est étrange n'est pas ?", "je ne comprend plus rien", "ça envisage rien de bon", "mauvaise augure", "c'est un présage !", "je ne suis pas superstitieux mais ça sent mauvais du cul !", "c'est quelque chose tout de même !", "ça me fait un peu peur tout ça !", "jamais entendu quelque chose d'aussi... bref", ""]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type

class QueteSecondaireTresor:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["par un ami", "par un voyageur", "par un marchand", "par mon cercle privée", "par quelqu'un", "par hasard", "sur un vieux document", "par des inconnus"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["hier", "il y a une semaine", "il y a un mois de cela", "avant hier", "", "hier soir soir", "hier à minuit", "il y a quelques jours"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["qu'un trésor", "qu'un coffre", "qu'un bouclier magique", "qu'une épée magique", "qu'une amulette", "qu'un trésor", "qu'un trésor", "qu'un trésor", "qu'un trésor", "qu'un trésor", "qu'un trésor", "qu'un trésor"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["j'ai entendu dire que", "j'ai ouïe dire que", "il parait que", "vous savez ce qui se dit ?", "Approchez j'ai un secret pour vous !", " Vous ne connaissez pas la nouvelle ?", "Vous allez halluciner de ce que je vais vous dire !", "Préparez vous au pire", "Ecoutez moi bien", "J'ai entendu des rumeurs...", "Il court des bruits..", "Tout le monde en parle !", "C'est la nouvelle du moment !", "Vous n'allez pas me croire", "C'était sur toutes les bouches."]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["qu'il est gardé par un orque", "qu'il est abandonné", "qu'il est vieux de 5000 ans", "qu'il est gardé par un troll", "qu'il est gardé par un dragon", "qu'il n'a jamais été découvert", "qu'il a été enterré par de riches commerçants", "qu'il a été enterré par de riches princes", "qu'il a été enterré par de riches rois sorciers", "qu'il a été enterré par des mages puissants", "qu'il a été enterré par un étrange peuple du nord", "qu'il a été enterré par de riches commerçants et des voleurs", "qu'il a été enterré par des brigants", "qu'il a été caché par des sorcières", "que c'est l'héritage d'un noble", "que c'est l'héritage d'un empereur", "que c'est l'héritage de notre empereur", "que c'est l'héritage d'un chef orc", "qu'il contient des pierres précieuses", "qu'il est vide !", "qu'il contient des armes forgées par des nains", "qu'il contient des armes magiques", "qu'il contient des talismans elfiques"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["vous devriez y jeter un coup d'oeil", "tout le monde le cherche, personne ne l'a trouvé", "il a été trop prondément enfoncé dans la terre", "trop bien gardé pour vous peut être", "vous devriez essayer de le trouver", "un coffre bien défendu", "beaucoup d'argent à la clef", "des objets elfiques surement dedans", "des pierres précieuses", "un objet magique peut être trouvé", "", "", "", ""]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireChasse:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le garde chasse", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["du lapin", "du daim", "du sanglier", "du loup", "de l'ours", "du chien", "du rat", "du cerf", "du gibier", "de la viande", "de la barbak", "du brigand", "du poulet", "de la volaille", "du moineau", "de la viande", "de la viande", "de la viande", "du cerf", "du lapin"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["50 grammes", "1 kg", "500 grammes", "2 kg", "5 kg", "10 kg", "20 kg", "25 kg", "40 kg", "100 kg", "200 grammes",]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["les villageois ont faim", "nous n'avons plus de vivres", "nous avons faim", "il y a trop de peu de réserves", "l'hiver sera rude !", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "apporter", "faire cuire", "dépecer", "manger"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireNettoyage:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["ma maison", "l'auberge", "l'église", "la grange", "la ferme", "le village", "la route", "la cave", "mon grenier", "mes affaires", "l'auberge", "la taverne"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["ça pue", "les villageois ont vomi partout", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de la saleté", "ça shlingue", "c'est sale", "ce n'est pas présentable", "c'est moche", "la saleté s'est infiltré partout !",  "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette saleté", "j'ai l'impression que je vais mourrir tellement ça pue", "la saleté me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "ça rend les gens malades", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireIdentite:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence", "le voisin", "une femme du village", "le prêtre", "le chef du village", "le chasseur", "le curée", "ma voisine", "mon voisin", "ma mère", "mon fils", "la mère du chef du village", "le père du petit grigory", "le boucher", "le fils du boulanger", "le boulanger", "la boulangère", "le tavernier", "un soldat de la garde", "un pêcheur", 'une prostitué', "une fille de petite vertu", "un chat", "un chien", "un lapin", "un druide", "un moine", "l'herboriste", "un espion", "le diacre", "un médecin", "un astrologue", "le bailli", "l'homme le plus riche du village", "tresorier", "le marquis", "le seigneur", "le baron", "le vicomte", "le vicaire", "le doyen", "le comte", "l'eveque", "l'abbe", "l'intendant", "le roi", "le prince", "le fils de l'empereur", "l'élu de la prophétie", "un elfe", "un nain", "un humain", "une fée", "une demi-homme", "un demi-elfe", "un aventurier", "un voyageur", "un type pas net", "un drôle de voyageur", "un lutin", "un homme arbre", "un centaure", "un minotaure", "un cheval", "un étrange marchand", "un musicien"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["de la discipline", "votre compétence", "quelqu'un comme vous", "des gens comme vous"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["nous en avons vraiment besoin", "c'est très important pour le chef du village"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["faire de l'argent", "apprendre votre langue", "des cours de chasse"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireSpiritualite:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le grand prêtre", "l'église'"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["d'adeptes", "de vous", "de serviteurs", "d'adorateurs", "de gens bien", "de gens pieux", "de gens comme vous", "de personnes saines", "de personnes bienveillantes comme vous", "de gens qui ont de la foi", "de foi", "de courage", "de gens érudit", "de prêtre", "de prier pour nous", "de beaucoup de foi", "de croire", "d'intelligence", "de gens cultivé", "de concentration"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["excommunier", "prier", "lire les écrits sacrées", "s'agenouiller", "croire", "retrouver la foi", "exorciser", "repousser le démon", "faire revivre notre déesse", "avoir la foi", "retrouver la vrai foi", "du courage", "des gens érudit", "un prêtre", "prier pour nous", "beaucoup de foi", "croire en notre seigneur", "de l'intelligence", "des gens cultivé", "de la concentration"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["des temps terribles s'annoncent", "nous avons eu des victimes", "j'ai perdu la foi", "j'ai foi en vous", "je crois en vous", "les villageois ont perdu la foi", "notre déesse se meurt", "notre ordre est menacé", "des payens sont arrivé ici", "la guerre va éclater", "quelque chose de grave se prépare", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours, les gens ont perdu la foi", "nous avons besoin d'aide", "j'ai vu mon destin funeste approcher à grands pas...", "c'est important", "nous avons eu peu de récolte cette année", "c'est ce qu'il faut faire !", "notre prêtre l'a décidé ainsi", "les paysans sont sans foi ni loi", "c'est la décadence", "les valeurs se perdent", "il a assombri le ciel ! Le mage noir !", "les sorciers sont de retour", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "l'argent de notre dieu disparait !", "j'ai perdu un objet sacré !", "un objet sacré a été profané", "nous avons presque trouvé la relique sacrée", "la tombe de notre prophète à été profané", "un homme a blasphémé", "un homme a péché", "vous avez péché", "j'ai péché", "dieu le demande", "dieu le veut !", "nous avons tous péché !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["prier", "notre déesse", "notre dieu", "louer notre seigneur", "notre ordre", "s'occuper de nos adeptes", "aider notre ordre", "notre seigneur", "le bien de tous", "le bien de notre église", "notre église", "sauver les pêcheurs", "excommunier les pêcheurs", "repousser le malin", "pour lutter contre Lucifer", "pour ne pas sombrer dans la folie", "continuer à avoir la foi", "regagner la foi", "que les habitants retrouvent la foi", "que notre prêtre retrouve la foi", "redonner confiance aux paysans", "les récoltes de cette année", "lutter contre la guerre", "sauver nos âmes", "pardonner nos péchés", "pour retrouver la foi en nous"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireCourse:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["grammes de farine", "litre de bière"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["récupérer", "demander", "en trouver", "en acheter", ""]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["j'ai envie aha !", "vous serez récompensé !", "j'en ai besoin", "c'est nécessaire", "c'est urgent", "je risque d'être ruiné !", "j'en ai besoin urgemment", "c'est nécessaire pour mes affaires", "mon business risque de couler", "c'est important pour moi"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["m'amener", "livrer", "emmener", "faire disparaitre", "détruire", "apporter", "emporter", "me donner", "m'amener", "me livrer", "me donner rapidemment"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        combien_choix = [0, 10, 100]
        combien = choice(combien_choix)
        self.combien = combien
        experience_choix = [5, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireCommercial:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["un ami", "un voyageur", "un marchand", "mon cercle privée", "quelqu'un", "par hasard", "le vicomte", "le maire", "le bailli "]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un marché", "une livraison", "une marchandise", "une charette", "un commerce", "une affaire", "un échange", "un troc", "un décret", "une restriction", "un chemin commercial", "un engagement", "une route commercial"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["du parchemin pour le contrat", "trouver le bailli", "demander au bailli", "faire une demande au près de la mairie", ""]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["j'ai envie aha !", "vous serez récompensé !", "j'en ai besoin", "c'est nécessaire", "c'est urgent", "je risque d'être ruiné !", "j'en ai besoin urgemment", "c'est nécessaire pour mes affaires", "mon business risque de couler", "c'est important pour moi"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["effectuer", "neutraliser", "mettre en place", "faire disparaitre", "détruire", "conclure", "faire", "rendre concret", "créer", "ouvrir", "livrer"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["un pourcentage", "une part de marché",  "de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        combien_choix = [0, 10, 100]
        combien = choice(combien_choix)
        self.combien = combien
        contrat_choix = ["lapins", "chou", "grammes de farine", "kg de viande"]
        contrat = choice(contrat_choix)
        self.contrat = contrat
        occurence_choix = ["tous les mardi", "1 fois par semaine", "1 fois par mois", "tous les jours", "tous les jeudis"]
        occurence = choice(occurence_choix)
        self.occurence = occurence
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireRomantique:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["Il y a cette fille que j'apprécie grandement", "Il y a cette homme que j'apprécie grandements", "je suis tombé amoureux", "j'aimerai déclarer ma flamme", "faire une faveur", "offrir un présent", "entretenir un galant", "courtiser", "courtiser un homme", "courtiser le roi", "courtiser un bandit", "courtiser une femme", "apporter des fleurs", "demander en mariage quelqu'un", "quelqu'un me plait", "je suis tombé sous le charme", "je me sens tout ému", "je suis heureux", "une sorcière", "un démon m'a jeté un sort", "je suis complétement fou d'une fille", "je suis tombé raide dingue amoureux d'une fille", "je suis géné mais j'aime une fille", "une homme m'a envouté", "je suis tombé sour le charme d'un homme"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["m'aider je vous en supplie", "me sauver de cette situation", "que vous m'aidiez, s'il vous plait", "que vous me trouver quelque chose", "que vous soyez là pour moi, je vous en prie, je meurt d'amour", "que vous me trouviez quelque chose à lui dire", "que vous me trouviez quelque chose à lui offrir", "que vous m'aidiez à la rencontrer", "que vous m'écriviez un poème", "fassiez quelque chose !", "la séduire", "que vous me trouviez un objet magique", "que vous me trouviez un cadeau qui séduit", "que vous m'aidiez à écrire une lettre d'amour"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["je n'arrive pas", "je suis trop timide", "je ne sais pas comment faire", "je ne sais pas par ou commencer", "je suis maladroit", "j'ai besoin de vous", "je ne vais pas y arriver tout seul", "vous seul pouvait m'aider", "j'ai besoin d'un prêtre", "je ne suis pas assez bien pour elle", "je ne suis pas assez riche", "je ne suis pas assez important", "je ne suis pas assez influent", "j'ai mauvaise réputation", "je sens mauvais", "je pue", "qui s'intéresserait à un crétin comme moi...", "je suis trop triste pour le faire", "ses parents ne veulent pas", "il y a quelque chose qui cloche chez moi et je n'arrive pas à dire ce que c'est", "j'ai peur"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["l'inviter à boire un verre", "lui offrir des fleurs", "le tuer", "le faire disparaitre", "lui faire l'amour", "la séduire", "qu'elle m'aime", "conquérir son coeur", "être son amant", "obtenir ses faveurs", "me marier", "que nos âmes se rencontrent", "la rencontrer", "être avec elle", "être avec lui"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireDefense:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["un ami", "un voyageur", "un marchand", "mon cercle privée", "quelqu'un", "le vicomte", "le maire", "le bailli "]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["m'accuse de lui avoir volé quelque chose", "m'accuse d'escroquerie", "veut ma peau", "a menacé ma famille", "cherche les ennuies", "m'a insulté", "m'accuse de lui avoir volé tout son argent", "me déteste", "crache derrière mon dos", "médit sur moi", "a raconté une vilaine rumeur sur moi", "veut me tuer", "veut tuer ma soeur", "veut tuer mon frère", "dit n'importe quoi sur moi", "me critique", "fait beaucoup trop de bruit", "est totalement stupide", "empiète sur mon jardin", "incante comme une sorcière", "invoque des démons", "se protitue", "inflitre des rats dans ma maison", "élève des araignées !", "fabrique des monstres affreux", "fait des choses ignobles", "est une étrange"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "je ne sais qu'elle raison", "nous nuire", "ma reconnaissance", "sa stupide religion", "un peu d'argent", "beaucoup d'argent", "me nuire", "rien", "une raison que j'ignore", "me faire tomber", "nuire à mon marché", "absolument rien", "quelque chose mais je ne sais pas pourquoi"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireRelique:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "l'église", "le grand prêtre"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["une relique", "un livre sacrée", "un parchemin sacrée", "une pierre de notre déesse", "un objet céleste", "un relicat", "un objet magique", "une épée magique", "un outil de dieu", "un fragment céleste", "une relique de notre seigneur"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["c'est un objet très important pour notre ordre","c'est un objet très important pour nous","vous serez récompensé !", "c'est une relique vraiment sacrée !", "c'est dela plus haute importance !", "il y a une malédiction à lever", "une malédiction qui empoisonne nos villageois", "une sombre magie est à l'oeuvre", "cette objet contient de la magie noire", "cette objet est maudit", "la prophétie a annoncé cette évenement", "vous êtes l'élu !", "vous seul pouvez la toucher", "cette objet est dangereux !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper", "récuperer", "protéger", "conserver", "m'amener", "m'apporter", "apporter à notre église", "apporter dans notre ordre", "à donner à notre seigneur"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireInspecteur:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie", "le grand magistrat"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un meurtre", "une sale affaire", "un crime", "un vol", "un cambriolage", "un assassinat", "un délit", "un affreuse affaire", "un blasphème", "une conspiration", "un coup d'état", "un jugement", "un tribunal", "un vol à la tire", "un vol à l'étalage", "une contrebande", "un complot", "une embuscade"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["résoudre cette affaire", "résoudre cette énigme", "retrouver le coupable", "trouver le coupable", "que vous partiez à la recherche du coupable", "que vous trouviez des indices", "gagner le procès", "faire perdre le procès", "trouver des indices", "investiguer sur cette affaire", "inspecter la région", "que le coupable soit puni !", "que vous fassiez quelque chose", "que vous aidez la garde", "de l'aide pour trouver les monstres qui ont pu commetre un tel crime"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !", "le crime augmente !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["par ordre du magistrat", "pour aider la communauté", "pour notre salut", "pour la justice", "pour nous sauver !", "important, aidez nous !", "affreux...", "nécessaire", "un mal pour un bien", "un ordre", "important vous devez nous aider", "essentiel pour la survie de notre peuple", "terrible"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type



# GUILDES

class QueteSecondaireGuildeMage:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type

class QueteSecondaireGuildeGuerrier:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type

class QueteSecondaireGuildeVoleur:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type

class QueteSecondaireGuildeAssassin:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type

class QueteSecondaireGuildePretre:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type

class QueteSecondaireGuildeBarde:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type


class QueteSecondaireGuildeMarchand:

    def __init__(self, nom, etat, description, score, type):
        self.nom = nom
        self.etat = etat #"non decouvert" #découvertes #en cours #validées #échouées
        self.description = description

        qui_choix = ["j'", "le chef du village", "le bailli", "la mairie"]
        qui = choice(qui_choix)
        self.qui = qui
        quand_choix = ["10 minutes donc très vite, dépêchez vous...", "30 minutes", "1h", "2h", "5h", "ce soir", "minuit", "demain", "après demain", "une semaine", "un mois", "deux mois", "quatre mois", "six mois", "l'année prochaine", "5 ans"]
        quand = choice(quand_choix)
        self.quand = quand
        quoi_choix = ["un troll", "des gobelins", "un vampire", "des loups", "un ours", "des orques", "un géant", "un dragon", "une vouivre", "le chef des bandits", "un bandit", "un truand", "un mendiant", "un assassin", "un spectre", "un esprit", "un homme malveillant", "un sorcier", "une sorcière", "un démon", "des rats", "des araignées", "des monstres affreux", "des choses ignobles", "une étrange présence"]
        quoi = choice(quoi_choix)
        self.quoi = quoi
        comment_choix = ["tout brûler", "égorger ce genre de montre", "apporter de l'ail", "tout tuer", "faire un rituel", "prendre par surprise", "faire quelque chose mais je ne sais pas quoi !", "trouver une solution", "déterrer la hache de guerre", "vous préparer", "neutraliser", "faire disparaître cette menace", "vous en occuper", "être bien armé", "il faut des armes magiques", "des outils sophistiqués", "beaucoup de patience", "être fort", "être nombreux", "être malin", "être perspicace et efficace !", "ne pas avoir peur", "il faut en avoir dans le slip", "il faut être sacrément couillu", "avoir du courage", "être quelqu'un de sérieux", "être quelqu'un tel que vous", "être bien armé", "attaquer pendant la nuit", "attendre la tombée du jour", "attendre la journée", "être aidé par le village", "que vous demandiez au chef", "que vous soyez attentif", "être un peu plus coriace que vous je pense mais bon...", "pas que vous soyez peureux sur ce coup là", "en vouloir", "de l'intelligence", "bien manger avant", "pas avoir le ventre vide", "être sournoix", "un prêtre", "un magicien", "rien que votre mental"]
        comment = choice(comment_choix)
        self.comment = comment
        ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs", "caché dans la ville", "dehors", "je ne sais ou !", "à l'est", "à l'ouest", "au sud", "au nord", "quelque part", "dans un trou", "dans une grotte", "dans une ruine", "dans un cimetierre", "dans les montagnes"]
        ou = choice(ou_choix)
        self.ou = ou
        pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant", "c'est effrayant", "mon frère est mort à cause de cette menace", "ma soeur est morte...", "j'ai perdu ma mère à cause de ce genre de montre", "j'ai perdu mon père à cause de ce genre de montre", "j'ai perdu ma tante hier et je soupçonne ça", "j'ai perdu mon oncle et je pense que c'est lié", "j'ai perdu ma famille, c'est terrible... ce fils de p... escusez moi je suis sous le choc vous comprenez...", "j'ai peur", "tout le monde a peur", "nous avons peur", "la menace grandit", "la menace s'est infiltré partout !", "ils sont partout !", "je suis terrifié", "ça devient problèmatique", "tout est devenu si sombre ces derniers jours à cause de cette menance", "j'ai l'impression que je vais mourrir", "j'ai vu mon destin funeste approcher à grands pas...", "ça presence me fatigue !", "j'en ai marre", "c'est ce qu'il faut faire !", "le chef l'a décidé", "les paysans en ont marre !", "j'ai cru le voir dans mes toilettes ce matin", " je l'ai trouvé dans mon bain !", "il a assombri le ciel !", "la magicienne du village m'a prédit que cette menace me tuera demain", "ma vie est en danger", "je me suis fait volé tout ce que j'avais", "mes affaires disparaissent !", "j'ai perdu un projet précieux et ce n'est pas anodin !", "Je soupçonne ces montres de me voler mes économies", "je soupçonne ce genre de malotru de piquer mes réserves...", "j'en peux plus !", "je ne veux plus les voir !", "je veux en finir avec eux", "j'ai envie aha !", "vous serez récompensé !"]
        pourquoi = choice(pourquoi_choix)
        self.pourquoi = pourquoi
        objectif_choix = ["éliminer", "neutraliser", "éloigner", "faire disparaitre", "détruire", "s'occuper"]
        objectif = choice(objectif_choix)
        self.objectif = objectif
        recompense_choix = ["de l'argent", "ce que vous voulez", "un objet précieux", "ma reconnaissance", "une prière pour vous", "un peu d'argent", "beaucoup d'argent", "tout ce que j'ai !", "des pierres précieuses", "un objet magique", "ce que vous aurez l'audace de demander", "quelque chose", "absolument rien", "peut être quelque chose"]
        recompense = choice(recompense_choix)
        self.recompense = recompense
        experience_choix = [0, 10, 100]
        experience = choice(experience_choix)
        self.experience = experience
        self.score = score
        self.type = type



#QUETES META
survivre = Quete("survivre", "en cours", "votre personnage doit garder ses 100 points de vie", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
origine = Quete("origine", "decouvert", "votre personnage doit comprendre ses origines", "moi", "maintenant", "mon origine", "retracer son passé", "ici", "pour comprendre qui vous êtes", 100, "le savoir", 100, 0, "meta")
gloire = Quete("gloire", "decouvert", "votre personnage doit obtenir la gloire", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
amour = Quete("amour", "decouvert", "votre personnage doit trouver l'amour", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
statut = Quete("statut", "decouvert", "votre personnage doit obtenir le meilleur statut", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
pouvoir = Quete("pouvoir", "decouverts", "votre personnage doit obtenir le plus de pouvoir", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
vengeance = Quete("vengeance", "decouvert", "votre personnage doit se venger", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
terres = Quete("terres", "decouvert", "votre personnage doit obtenir le plus de terres", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
noblesse = Quete("noblesse", "decouvert", "votre personnage doit obtenir le titre de noblesse le plus haut", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
argent = Quete("argent", "decouvert", "votre personnage doit obtenir le plus d'argent", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
armee = Quete("armée", "decouvert", "votre personnage doit obtenir la plus grande armée", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
foi = Quete("foi", "decouvert", "votre personnage doit trouver la foi", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
bien = Quete("bien", "decouvert", "votre personnage doit faire le bien", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
mal = Quete("mal", "decouvert", "votre personnage doit faire le mal", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
neutralite = Quete("neutralite", "decouvert", "votre personnage doit garder la neutralité", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
ordre = Quete("ordre", "decouvert", "votre personnage doit garder l'ordre", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0, "meta")
equilibre = Quete("equilibre", "decouvert", "votre personnage doit garder l'équilibre", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0,"meta")
chaos = Quete("chaos", "decouvert", "votre personnage doit répandre le chaos", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0,"meta")
famille = Quete("famille", "decouverts", "votre personnage doit protéger sa famille", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0,"meta")
sexualite = Quete("sexualite", "decouverts", "votre personnage est un chaud lapin !", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0,"meta")
science = Quete("science", "decouverts", "votre personnage doit faire des découvertes scientifiques", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0,"meta")
# democratie = Quete("democratie", "decouverts", "votre personnage doit imposer la démocratie au monde", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0,"meta")
# communisme = Quete("republique", "decouverts", "votre personnage doit imposer le communisme dans le monde", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0,"meta")
# monarchie = Quete("monarchie", "decouverts", "votre personnage doit imposer la monarchie dans le monde", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0,"meta")
# capitalisme = Quete("capitalisme", "decouverts", "votre personnage doit imposer le capitalisme dans le monde", "moi", "maintenant", "ma vie", "ne pas mourir", "ici", "pour continuer le jeu", 100, 0, 0, 0,"meta")

#QUETES PRINCIPALES

#MONSTRE
qui_choix = ["vous", "moi", "quelqu'un"]
qui = choice(qui_choix)
quand_choix = ["ce soir", "demain", "après demain"]
quand = choice(quand_choix)
quoi_choix = ["troll", "gobelin", "vampire"]
quoi = choice(quoi_choix)
comment_choix = ["le brûler", "l'égorger", "apporter de l'ail"]
comment = choice(comment_choix)
ou_choix = ["dans la forêt", "dans les égoûts", "dans le champs"]
ou = choice(ou_choix)
pourquoi_choix = ["cela terrorise les villageois", "nous avons eu des victimes", "c'est gênant"]
pourquoi = choice(pourquoi_choix)
objectif_choix = ["éliminer", "neutraliser", "éloigner"]
objectif = choice(objectif_choix)
recompense_choix = ["36 deniers", "ce que vous voulez", "un objet précieux"]
recompense = choice(recompense_choix)
experience_choix = [0, 10, 100]
experience = choice(experience_choix)



#QUETES SECONDAIRES
#Niv1 de Confiance
recherche = Quete("recherche", "cache", "votre personnage doit trouver quelque chose", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
monstre = Quete("monstre", "cache", "votre personnage doit neutraliser un monstre", qui, quand, quoi, comment, ou, pourquoi,  objectif, recompense, experience, 0, "secondaire")
rumeur = Quete("rumeur", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi,  objectif, recompense, experience, 0, "secondaire")
tresor = Quete("tresor", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
chasse = Quete("chasse", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi,  objectif, recompense, experience, 0, "secondaire")

#Niv2 de Confiance
nettoyage = Quete("nettoyage", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi,  objectif, recompense, experience, 0, "secondaire")
identite = Quete("identite", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
spiritualite = Quete("spiritualite", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
course = Quete("course", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
commercial = Quete("commercial", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")

#Niv3 de Confiance
romantique = Quete("romantique", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
defense = Quete("defense", "cache", "votre personnage doit trouver quelque chose", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
guilde = Quete("guilde", "cache", "votre personnage doit neutraliser un monstre", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
relique = Quete("relique", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
inspecteur = Quete("inspecteur", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")

#Scientifique
manuscrit = Quete("manuscrit", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif,  recompense, experience, 0, "secondaire")
paleontologie = Quete("paleontologie", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
astronomie = Quete("astronomie", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
medecine = Quete("medecine", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")

#Seigneur
siege = Quete("siege", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
attaque = Quete("attaque", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
escarmouche = Quete("escarmouche", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
paix = Quete("paix", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
guerre = Quete("guerre", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
politique = Quete("politique", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
diplomatique = Quete("diplomatique", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
evasion = Quete("evasion", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
embuscade = Quete("embuscade", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
hotage = Quete("hotage", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, recompense, objectif, experience, 0, "secondaire")
noblesse = Quete("noblesse", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
artefact = Quete("artefact", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
pelerinage = Quete("pelerinage", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")

#Guilde
guilde_mage = Quete("guilde_mage", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
guilde_guerrier = Quete("guilde_guerrier", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
guilde_voleur = Quete("guilde_voleur", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
guilde_assassin = Quete("guilde_assassin", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
guilde_pretre = Quete("guilde_pretre", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
guilde_barde = Quete("guilde_barde", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")
guilde_marchand = Quete("guilde_marchand", "cache", "votre personnage doit élucider une rumeur", qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, 0, "secondaire")

# qui, quand, quoi, comment, ou, pourquoi, objectif, recompense, experience, "secondaire")


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
