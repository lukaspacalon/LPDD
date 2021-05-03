# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural

import os
import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow_core import *
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow_core as tfc
print(tfc.__path__)
import random
import joueur
import lieu


with open('personnalite/ami_V.json') as file:
    data = json.load(file)


from sklearn.preprocessing import LabelEncoder

training_sentences = []
training_labels = []
labels = []
responses = []


for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])

enc = LabelEncoder()
enc.fit(training_labels)
training_labels = enc.transform(training_labels)

vocab_size = 10000
embedding_dim = 16
max_len = 20
trunc_type = 'post'
oov_token = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token) # adding out of vocabulary token
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded = pad_sequences(sequences, truncating=trunc_type, maxlen=max_len)

classes = len(labels)
model = tf.keras.models.Sequential()
model.add(keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(classes, activation='softmax'))
model.summary()
training_labels_final = np.array(training_labels)
EPOCHS = 5
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(padded, training_labels_final, epochs=EPOCHS)


def check(cible_int):
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
        itera = personnage.Generateur()
        x = 0
        while x < destination.nbr_habitant:
            itera.genererPersonnage()
            x = x + 1
        destination.habitants = itera.objets


    joueur.mon_joueur.localisationX = str(joueur.mon_joueur.localisationX)
    joueur.mon_joueur.localisationY = str(joueur.mon_joueur.localisationY)
    nom = destination.habitants[cible_int].__dict__['nom']
    print("commencez à parler avec {}, Entrez 'quitter' pour arrêter la conversation et 'aide' pour apprendre à mieux communiquer".format(nom))
    global repet
    repet = 0
    while True:
        string = input('Parlez: ')
                #nom
                #age
                #famille
                #chemin
                #Info sur le lieu
                #Info sur les créatures
                #Info
                #Sexe
                #Race
                #Richesse
                #Statut
                #Métier
        result = model.predict(pad_sequences(tokenizer.texts_to_sequences([string]), truncating=trunc_type, maxlen=max_len))[0]
        #resultzero = model.predict(pad_sequences(tokenizer.texts_to_sequences([string]), truncating=trunc_type, maxlen=max_len))[0]
        category = enc.inverse_transform([np.argmax(result)]) # labels[np.argmax(result)]
        if string.lower() in ['quitter', 'exit', 'quit', 'close', 'q']: break
        if string.lower() == 'aide' :
            print("Vous avez 4 façons de communiquer :")
            print("1. Ecrivez ce que vous voulez et laisser la personne interpréter le message")
            print("2. Indiquez une intention parmi la liste ci-dessous pour orienter votre message. Vous pouvez ajouter un message ou laisser l'intention seulement.")
            print("Attention malgré l'intention votre message personnalisé influence la réaction de celui qui vous écoute")
            print("Votre charisme importe beaucoup pour que votre interlocuteur croit en votre émotion")
            print("3. Exprimez une émotion à l'aide d'émoji parmi la liste ci-dessous pour influencer votre interlocuteur. Votre charisme importe beaucoup pour que votre interlocuteur croit en votre émotion")
            print("4. Réaliser une action parmi la liste ci-dessous pour influencer votre interlocuteur. Votre charisme importe beaucoup pour que votre interlocuteur se laisse faire")
            print("Faites référence à une quête que vous avez en commun pour négocier un contrat ou susciter l'intérêt de votre interlocuteur pour améliorer votre relation avec lui")
            print("Faites attention aux associations d'idées que vous mettez en place car les combos peuvent multiplier grandement un score de charisme en bien comme en mal")
            print("Ne faites qu'une petite phrase à chaque fois au risque d'être incompris ou interrompu/ignorer par votre interlocuteur")
            print("")
            print("Développer votre charisme permet de débloquer des intentions ou des emojis")
            print("")
            print("Intentions :   niveau 1//   ")
            print("Intentions :   niveau 2//   ")
            print("Intentions :   niveau 3//   ")
            print("")
            print("Emoji :   niveau 1// :)   :(   ;)   :P   :O   :')   :'(  :()     ")
            print("Emoji :   niveau 2// :S  :X  :D  :/  :U   :3")
            print("Emoji :   niveau 3//   :@   >:)   >:(   B)   :°   ")
            print("")
            print("Action :")
            print("")
        if string == repet:
            print("réponse :")
            print("Ne me faites pas perdre mon temps")
            print('')
            break
        repet = string
        if string.lower() == 'aurevoir' :
            print("aurevoir")
            break
        elif string.lower() in ['quel est votre nom ?', 'quel est ton nom ?', "comment tu t'appelles ?", "vous vous appelez comment ?", "c'est quoi ton nom ?", "tu t'appelles comment ?", "qui es tu ?", "t'es qui ?"]:
            print("")
            print("réponse :")
            nom = destination.habitants[cible_int].__dict__['nom']
            print("Je m'appelle {} ".format(nom))
            print("")
        elif string.lower() in ['saluer', "s'incliner", "s'intéresser", "s'inquiéter",]:
            print("")
            print("destination.habitants[cible_int].__dict__['personalite']")
            print(destination.habitants[cible_int].__dict__['personalite'])
            if destination.habitants[cible_int].__dict__['personalite'] == "empathique":
                caractere = 50
            if destination.habitants[cible_int].__dict__['personalite'] == "perseverant":
                caractere = 30
            if destination.habitants[cible_int].__dict__['personalite'] == "promoteur":
                caractere = 20
            if destination.habitants[cible_int].__dict__['personalite'] == "rebelle":
                caractere = 60
            if destination.habitants[cible_int].__dict__['personalite'] == "reveur":
                caractere = 90
            if destination.habitants[cible_int].__dict__['personalite'] == "travaillomane":
                caractere = 30
            print("caractere")
            print(caractere)
            print("joueur.mon_joueur.charisme")
            print(joueur.mon_joueur.charisme)
            de_random = random.randint(1, 10)*10
            print("dé random")
            print(de_random)
            test_caractere = de_random + joueur.mon_joueur.charisme - caractere
            print("test_caractere")
            print(test_caractere)
            if test_caractere > 50:
                print("Le geste semble avoir eu un effet positif ;)")
                destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] + 100
                destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] - 50
                destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] + 5
            elif test_caractere < 50 and test_caractere > 25:
                print("Le geste semble ne pas avoir fait d'effet...")
            else:
                print("Le geste semble avoir eu un effet négatif !")
                destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 100
                destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 50
                destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 100
            print("")
        elif string.lower() in ['enlacer', "prendre la main", "regarder", "pousser"]:
            print("")
            print("destination.habitants[cible_int].__dict__['personalite']")
            print(destination.habitants[cible_int].__dict__['personalite'])
            if destination.habitants[cible_int].__dict__['personalite'] == "empathique":
                caractere = 20
            if destination.habitants[cible_int].__dict__['personalite'] == "perseverant":
                caractere = 60
            if destination.habitants[cible_int].__dict__['personalite'] == "promoteur":
                caractere = 40
            if destination.habitants[cible_int].__dict__['personalite'] == "rebelle":
                caractere = 60
            if destination.habitants[cible_int].__dict__['personalite'] == "reveur":
                caractere = 30
            if destination.habitants[cible_int].__dict__['personalite'] == "travaillomane":
                caractere = 80
            print("caractere")
            print(caractere)
            print("joueur.mon_joueur.charisme")
            print(joueur.mon_joueur.charisme)
            de_random = random.randint(1, 10)*10
            print("dé random")
            print(de_random)
            test_caractere = de_random + joueur.mon_joueur.charisme - caractere
            print("test_caractere")
            print(test_caractere)
            if test_caractere > 50:
                print("Le geste semble avoir eu un effet positif ;)")
                destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 100
                destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 15
                destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 50
            elif test_caractere < 50 and test_caractere > 25:
                print("Le geste semble ne pas avoir fait d'effet...")
            else:
                print("Le geste semble avoir eu un effet négatif !")
                destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 100
                destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 50
                destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 100
            print("")
        elif string.lower() in ['embrasser',  "toucher", "caresser",  "masser"]:
            print("")
            print("destination.habitants[cible_int].__dict__['personalite']")
            print(destination.habitants[cible_int].__dict__['personalite'])
            if destination.habitants[cible_int].__dict__['personalite'] == "empathique":
                caractere = 30
            if destination.habitants[cible_int].__dict__['personalite'] == "perseverant":
                caractere = 70
            if destination.habitants[cible_int].__dict__['personalite'] == "promoteur":
                caractere = 50
            if destination.habitants[cible_int].__dict__['personalite'] == "rebelle":
                caractere = 90
            if destination.habitants[cible_int].__dict__['personalite'] == "reveur":
                caractere = 50
            if destination.habitants[cible_int].__dict__['personalite'] == "travaillomane":
                caractere = 100
            print("caractere")
            print(caractere)
            print("joueur.mon_joueur.charisme")
            print(joueur.mon_joueur.charisme)
            de_random = random.randint(1, 10)*10
            print("dé random")
            print(de_random)
            test_caractere = de_random + joueur.mon_joueur.charisme - caractere
            print("test_caractere")
            print(test_caractere)
            if test_caractere > 50:
                print("Le geste semble avoir eu un effet positif ;)")
                destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 300
                destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 300
                destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 100
            elif test_caractere < 50 and test_caractere > 25:
                print("Le geste semble ne pas avoir fait d'effet...")
            else:
                print("Le geste semble avoir eu un effet négatif !")
                destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 100
                destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 50
                destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 100
            print("")
        elif string.lower() in ['et toi ?', 'et vous ?', "ça va ?", "tu vas bien ?", "ça roule", "ça gaze ?", "comment tu vas ?", "comment te sens tu ?", "comment allez vous ?", "comment tu vas ?", "tu te sens bien ?"]:
            print("")
            print("réponse :")
            nom = destination.habitants[cible_int].__dict__['nom']
            print("Je vais bien, merci")
            print("")
        elif string.lower() in ['sommes nous ami ?', 'es-tu mon rival ?', "quel est notre relation ?", "vous m'aimez bien ?", "vous m'aimez ?", "vous m'appréciez ?", "Je suis ton ami ?", "tu ne m'aimes pas ?", "quel est la nature de notre relation ?"]:
            print("")
            print("réponse :")
            print("Nous ne nous connaissons pas")
            print("")
        elif string.lower() in ['tu as quel âge ?', "tu as quel âge ?", "quel est ton âge ?", "quel âge as-tu ?", "quel âge avez vous ?", "vous avez quel âge ?"]:
            print("")
            print("réponse :")
            age = destination.habitants[cible_int].__dict__['age']
            print(" J'ai {} ans".format(age))
            print("")
        elif string.lower() == 'vous êtes de ma famille ?':
            print("")
            print("réponse :")
            print("Je ne crois pas non")
            print("")
        elif string.lower() == 'vous avez des frères et soeurs ?':
            print("")
            print("réponse :")
            print("non")
            print("")
        elif string.lower() in ['où sommes nous ?', "où suis-je ?", "on est où là ?", "quel est cet endroit ?", "vous connaissez ici ?"]:
            print("")
            lieu_actuel = destination.nom
            print(" vous êtes à {}".format(lieu_actuel))
            print("")
        elif string.lower() in ["combien d'habitant ici ?", "combien sommes nous ici ?", "combien de personnes habitent ici ?", "il y a beaucoup de monde ici ?", "y'a du monde ici ?"]:
            print("")
            lieu_habitants = destination.nbr_habitant
            print(" Il y a {} habitants".format(lieu_habitants))
            print("")
        elif string.lower() in ["pouvez vous m'indiquer le chemin ?", "on est où sur la carte ?", "vous pouvez me guider ?", "Nous sommes où par rapport à la carte ?", "pouvez vous m'aider à trouver mon chemin ?"]:
            print("")
            lieu_emplacement = destination.emplacement
            print(" voilà le point où nous sommes sur la carte : {}".format(lieu_emplacement))
            print("")
        elif string.lower() in ["quel est ce paysage ?", "quel type de paysage ici ?", "comment est la végétation ici ?", "quel type de faune ici ?", "pouvez me décrire cet endroit ?"]:
            print("")
            lieu_lieu = destination.lieu
            print(" Ici je dirais {}".format(lieu_lieu))
            print("")
        elif string.lower() in ["y a t-il une construction ici ?", "où puis-je me reposer ?", "où puis-je trouver des gens ?", "où puis-je commercer ?", "où puis-je m'arrêter ?"]:
            print("")
            lieu_construction = destination.construction
            print(" Il y a un/une {}".format(lieu_construction))
            print("")
        elif string.lower() == 'où est le village de tarik ?':
            print("")
            print("réponse :")
            print("au sud")
            print("")
        elif string.lower() in ['vous connaissez des gens ici ?', "qui se trouve ici ?", "qui puis-je rencontrer ?", "qui habite ici ?", "vous connaissez ici ?"]:
            print("")
            print("Je connais quelques personnes... voici la liste :")
            for value in destination.habitants:
                print("{}, ".format(value.__dict__))
            print("")
        elif string.lower() in ['que peux t-on trouver ici ?', "qu'est-ce qu'il y a ici ?", "qu'est-ce qu'on peut trouver ici ?"]:
            print("")
            lieu_construction = destination.construction
            print(" Il y a un/une {}".format(lieu_construction))
            print("")
        elif string.lower() in ['vous êtes un homme ?', "vous êtes une femme ?", "quel est votre sexe ?"]:
            print("")
            print("réponse :")
            nom = destination.habitants[cible_int].__dict__['nom']
            print("ça se voit pas ? je m'appelle {} je vous rappelle...".format(nom))
            print("")
        elif string.lower() in ['quel est votre race ?', "vous avez quels origines ?", "d'où vous vient cette couleur de peau ?"]:
            print("")
            print("réponse :")
            print("ça se voit pas ?")
            print("")
        elif string.lower() in ['quel est votre richesse ?', "vous êtes riche ?", "vous avez de la thune ?", "vous avez beaucoup d'argent ?"]:
            print("")
            print("réponse :")
            print("Je ne vous le dirai pas")
            print("")
        elif string.lower() == 'quel est votre statut ?':
            print("")
            print("réponse :")
            lieu_actuel = destination.nom
            print("Je suis citoyen de {}".format(lieu_actuel))
            print("")
        elif string.lower() in ["c'est quoi ton métier ?", "quel est ton métier ?", "vous faites quel métier ?", "quel est votre métier ?"]:
            print("")
            print("réponse :")
            travail = destination.habitants[cible_int].__dict__['travail']
            print(" Je suis {}".format(travail))
            print("")
        elif string.lower() in ['quel est votre état de santé ?', "etes vous en bonne santé ?", "etes vous en forme ?", "etes vous blessé ?"]:
            print("")
            print("réponse :")
            print("Je vais bien")
            print("")
        elif string.lower() == 'quel est votre humeur ?':
            print("")
            print("réponse :")
            print("Je suis plutôt content")
            print("")
        elif string.lower() == 'vous avez faim ?':
            print("")
            print("réponse :")
            print("non ça va")
            print("")
        elif string.lower() == 'vous avez soif ?':
            print("")
            print("réponse :")
            print("non ça va")
            print("")
        elif string.lower() == 'quels sont vos compétences ?':
            print("")
            print("réponse :")
            print("Je suis fort en course")
            print("")
        elif string.lower() in ['quel est votre personnalité ?', "comment vous décriveriez vous ?", "vous vous comportez comment avec votre entourage ?", "quel genre de personne êtes-vous ?"]:
            print("")
            print("réponse :")
            personalite = destination.habitants[cible_int].__dict__['personalite']
            print(" Je suis un {}".format(personalite))
            print("")
        elif string.lower() == 'que faites vous ?':
            print("")
            print("réponse :")
            print("Je vous parle actuellement...")
            print("")
        elif string.lower() == 'pourquoi ce métier ?':
            print("")
            print("réponse :")
            print("c'est là ou je suis le meilleur")
            print("")
        elif result[np.argmax(result)] > 0.7:
            for i in data['intents']:
                if i['tag']==category:
                    print(category)
                    reponse = np.random.choice(i['responses'])
                    if i['tag'] =="presentation":
                        # print("+1 de relationnel")
                        # print("-10 de peur")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] + 1
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] - 10
                    elif i['tag'] =="humeur":
                        # print("+10 de relationnel")
                        # print("-20 de peur")
                        # print("+1 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] + 10
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] - 20
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] + 1
                    elif i['tag'] =="engager":
                        destination.habitants[cible_int].__dict__['equipe'] = True
                    elif i['tag'] =="sujet":
                        # print("+5 de relationnel")
                        # print("-10 de peur")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] + 5
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] - 10
                    elif i['tag'] =="insulte":
                        # print("-100 de relationnel")
                        # print("+50 de peur")
                        # print("-50 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 100
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 50
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 50
                    elif i['tag'] =="grossier":
                        # print("-50 de relationnel")
                        # print("+25 de peur")
                        # print("-50 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 50
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 25
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 50
                    elif i['tag'] =="intimidation":
                        # print("-300 de relationnel")
                        # print("+200 de peur")
                        # print("-50 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 300
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 200
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 50
                    elif i['tag'] =="violence":
                        # print("-1000 de relationnel")
                        # print("+500 de peur")
                        # print("-50 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 1000
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 500
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 50
                    elif i['tag'] =="incompréhension":
                        # print("-20 de relationnel")
                        # print("+10 de peur")
                        # print("-50 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 20
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 10
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 50
                    elif i['tag'] =="compliment":
                        # print("+20 de relationnel")
                        # print("-30 de peur")
                        # print("+5 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] + 20
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] - 30
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] + 5
                    elif i['tag'] =="rentre dedans":
                        # print("-10 de relationnel")
                        # print("+30 de peur")
                        # print("-200 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 10
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 30
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 200
                    elif i['tag'] =="negation":
                        # print("+5 de relationnel")
                        # print("+5 de peur")
                        # print("+10 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] + 5
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 5
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] + 10
                    elif i['tag'] =="positif":
                        # print("+10 de relationnel")
                        # print("-5 de peur")
                        # print("+1 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] + 10
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] - 5
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] + 1
                    elif i['tag'] =="silence":
                        # print("-10 de relationnel")
                        # print("+5 de peur")
                        # print("+20 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 10
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 5
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] + 20
                    elif i['tag'] =="repete":
                        # print("-20 de relationnel")
                        # print("-10 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 20
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 10
                    elif i['tag'] =="reprimande":
                        # print("-30 de relationnel")
                        # print("+30 de peur")
                        # print("+10 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 30
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 30
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 10
                    elif i['tag'] =="fin positive":
                        # print("+10 de relationnel")
                        # print("-10 de peur")
                        # print("-10 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] + 10
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] - 10
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 10
                    elif i['tag'] =="avis negatif":
                        # print("-20 de relationnel")
                        # print("+10 de peur")
                        # print("+5 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 20
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 10
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] + 5
                    elif i['tag'] =="escuse":
                        # print("-10 de relationnel")
                        # print("-50 de peur")
                        # print("-100 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 10
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] - 50
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 100
                    elif i['tag'] =="ordre":
                        # print("-50 de relationnel")
                        # print("+50 de peur")
                        # print("+30 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 50
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 50
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] + 30
                    elif i['tag'] =="faiblesse":
                        # print("-20 de relationnel")
                        # print("+50 de peur")
                        # print("-100 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] - 20
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] + 50
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 100
                    elif i['tag'] =="marque de respect":
                        # print("+10 de relationnel")
                        # print("-200 de peur")
                        # print("-10 d'attirance")
                        destination.habitants[cible_int].__dict__['relationnel'] = destination.habitants[cible_int].__dict__['relationnel'] + 10
                        destination.habitants[cible_int].__dict__['peur'] =  destination.habitants[cible_int].__dict__['peur'] - 200
                        destination.habitants[cible_int].__dict__['attirance'] = destination.habitants[cible_int].__dict__['attirance'] - 10
                    else:
                        print("aucune modification")

            print("")
            print("réponse :")
            print(reponse)
            print("")
            print("")
            relationnel = destination.habitants[cible_int].__dict__['relationnel']
            peur = destination.habitants[cible_int].__dict__['peur']
            attirance = destination.habitants[cible_int].__dict__['attirance']
            print("Relationnel : {}".format(relationnel))
            print("Peur : {}".format(peur))
            print("Attirance : {}".format(attirance))
            nom = destination.habitants[cible_int].__dict__['nom']
            if relationnel > 10 and relationnel < 1000 and peur > -100 and attirance < 1000:
                #print("Vous avez une nouvelle relation !")
                destination.habitants[cible_int].__dict__['attitude'] = "relation"
            if relationnel > 1000 and peur > -100 and attirance < 1000:
                print("{} vous considère comme un ami".format(nom))
                destination.habitants[cible_int].__dict__['attitude'] = "ami"
            if relationnel < -100 and peur > -100 and attirance < 1000 and peur < 100:
                print("{} vous considère comme un rival".format(nom))
                destination.habitants[cible_int].__dict__['attitude'] = "rival"
            if peur > 1000:
                print("{} vous considère comme son supérieur".format(nom))
                destination.habitants[cible_int].__dict__['attitude'] = "serviteur"
            if peur < -100:
                print("{} vous considère comme son serviteur".format(nom))
                destination.habitants[cible_int].__dict__['attitude'] = "chef"
            if attirance > 1000:
                print("{} vous considère comme son idole".format(nom))
                destination.habitants[cible_int].__dict__['attitude'] = "admirateur"
        else:
            sampleList = ["c'est à dire ?...", "Je ne comprend pas...", "Plait-il...", "Mais encore ?...", "quoi ?...", "J'ai rien compris...", "De quoi tu me parles ?", "J'ai pas entendu ! Redis moi", "Attend... quoi ?!", "on parle la même langue ?", "c'est quoi ce charabia ?", "Je dois être sourd, redites voir ?", "Par contre là je comprend pas...", "vous parlez une autre langue ?", "J'ai pas saisi...", "vous pouvez vous exprimer correctement ?", "Désolé je ne vois pas ce que vous voulez dire..."]
            x = random.choice(sampleList)
            print(x)

tf.keras.models.save_model(model, "z_bot")



            #print("")
            #print("result")
            #print(result)
            #print("category")
            #print("")
            #print(category)
            #print("")
            #print("np.argmax(result)")
            #print(np.argmax(result))
            #print("")
            #print("[np.argmax(result)]")
            #print([np.argmax(result)])
            #print("")
            #print("enc.inverse_transform([np.argmax(result)])")
            #print("")
            #print(enc.inverse_transform([np.argmax(result)]))
            #print("labels[np.argmax(result)]")
            #print(labels[np.argmax(result)])
            #print("")
            #print("training_sentences[np.argmax(result)]")
            #print(training_sentences[np.argmax(result)])
            #print("")
            #print("training_labels[np.argmax(result)]")
            #print(training_labels[np.argmax(result)])
            #print("")
            #print("labels[np.argmax(result)]")
            #print(labels[np.argmax(result)])
            #print("")
            #print("training_labels_final")
            #print(training_labels_final)
            #print("")
            #print("history")
            #print(history)
            #print("")
            #print("labels[np.argmax(result)]")
            #print(result[np.argmax(result)])
            #print(category[np.argmax(result)])










#check()
