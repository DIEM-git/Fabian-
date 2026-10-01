"""  ____                    _____     _     _
    |  _ \ ___  _   _ _ __  |  ___|_ _| |__ (_) __ _ _ __
    | |_) / _ \| | | | '__| | |_ / _` | '_ \| |/ _` | '_ \
    |  __/ (_) | |_| | |    |  _| (_| | |_) | | (_| | | | |
    |_|   \___/ \__,_|_|    |_|  \__,_|_.__/|_|\__,_|_| |_|
"""

import os

import sys

import time

fabian = """
d88888b  .d8b.  d8888b. d888888b  .d8b.  d8b   db
88'     d8' `8b 88  `8D   `88'   d8' `8b 888o  88
88ooo   88ooo88 88oooY'    88    88ooo88 88V8o 88
88~~~   88~~~88 88~~~b.    88    88~~~88 88 V8o88
88      88   88 88   8D   .88.   88   88 88  V888
YP      YP   YP Y8888P' Y888888P YP   YP VP   V8P
"""

gentil = """
  .oooooo.                              .    o8o  oooo
 d8P'  `Y8b                           .o8    `"'  `888
888            .ooooo.  ooo. .oo.   .o888oo oooo   888
888           d88' `88b `888P"Y88b    888   `888   888
888     ooooo 888ooo888  888   888    888    888   888
`88.    .88'  888    .o  888   888    888 .  888   888
 `Y8bood8P'   `Y8bod8P' o888o o888o   "888" o888o o888o
"""

doux = """
'||''|.    ..|''||   '||'  '|' '||' '|'
 ||   ||  .|'    ||   ||    |    || |
 ||    || ||      ||  ||    |     ||
 ||    || '|.     ||  ||    |    | ||
.||...|'   ''|...|'    '|..'   .|   ||.
"""

doux2 = """
    _/_/_/      _/_/    _/    _/  _/      _/
   _/    _/  _/    _/  _/    _/    _/  _/
  _/    _/  _/    _/  _/    _/      _/
 _/    _/  _/    _/  _/    _/    _/  _/
_/_/_/      _/_/      _/_/    _/      _/
"""
score = 0
life = 3

def clear():

    os.system("cls" if os.name == "nt" else "clear")

def lifecounter():

    if life == 3:
        print("\t[💛 - 💛 - 💛]")
    elif life == 2:
        print("\t[🧡 - 🧡]")
    elif life == 1:
        print("\t[❤️]")
    elif life == 0:
        clear()
        print("\t💥")
        print("Vous avez perdu !")
        input("<ENTER> to quit...")
        sys.exit()
    
def name_analyse():


    pseudo = input("Veyez entrer votre Pseudo: ")

    if pseudo == "Fabian" or pseudo == "fabian":

        clear()
        print("Voyons voir si tu es bien celui que tu prétends 😈")
        print(" ")
    
    elif pseudo == "Enricobaros9" or pseudo == "enricobaros9":

        clear()
        print("Il n'y a qu'une personne qui peux encore esperer porter ce pseudo et le mériter !")
        print(" ")
    
    elif pseudo == "KonailKo" or pseudo == "konailko":

        clear()
        print("Voyons voir si tu peux encore esperer porter ce pseudo légitimement")
        print(" ")
    
    else:

        clear()
        print("Alors commençons chère", pseudo,"!")
        print(" ")

def quizz(bonne_reponse):
    global score, life
    while True:
        lifecounter()
        print(" ")
        reponse = input("votre réponse: ").strip().upper()    
        if reponse in ("A", "B", "C", "D"):
            if reponse == bonne_reponse:
                score += 1
                print("🎊 Bonne Réponse !!!")
                print(" ")
                if score == 1:
                    print("\t👉|niv|👈")
                elif score == 2:
                    print("\t👉|nniver|👈")
                elif score == 3:
                    print("\t👉|ux annivers|👈")
                elif score == 4:
                    print("\t👉|eux anniversai|👈")
                elif score == 5:
                    print("\t👉|Joyeux Anniversaire|👈")
                print(" ")
                input("<ENTER> to continue...")
                break
            else:
                life -= 1
                print("Mauvaise Réponse. <❌>")
                input("<ENTER> to retry...")
        else:
            life -= 1 
            print("Error : Ceci n'est pas une réponse valide")
            input("<ENTER> to retry...")

def DBG():
    clear()
    print("----🎉 Bienvenue! 🎉----")
    print("Dans le DEUX BARRES GAME - DBG")
    print(" ")
    print("Ce programme est la pour tester si vous étes bien celui que vous prétendez être...")
    print(" ")
    input("Press <ENTER> to continue...")
    clear()
    print("Votre but sera d'écarter les deux barres le plus possible pour découvrir le message caché.")
    print(" ")
    print("\t👉||👈")
    print(" ")
    print("Seule une personne peux y arriver!")
    print(" ")
    print("Et ce programme est là pour le vérifier !!!")
    print(" ")
    input("Press <ENTER> to continue...")
    clear()
    name_analyse()
    print("Avant de commencer: ")
    print("Ce jeu se déroulera sous la forme d'un QCM avec différent niveaux de difficulté: \n[🟢(vert) - 🟡(jaune) - 🟠(non je rigole) - 🔴(c'est pas drôle et j'en suis désolé)]")
    print(" ")
    print("Vous disposerez de 3 Vies: ")
    print(" ")
    lifecounter()
    print(" ")
    print("Si vous perdez toutes vos vies, vous devrez recommencer le programme.")
    print(" ")
    while True:
        ready = input("Are you Ready? (Y/n): ")
        if ready in ("Y", "y", "N", "n"):
            if ready == "Y" or ready == "y":
                break
            else:
                print("Non, je sais que tu es prêt.")
    clear()
    while True:
        print("1.")
        print("[🟠] - Premiere Question: ")
        print(" ")
        print("[🎮] - Quel est le Skin le plus rare et iconique du casier Fortnite de FABIAN ?")
        print("(A) - Galaxy 🌌")
        print("(B) - Travis scott 🎤")
        print("(C) - Artilleur Royal 😎🛩️")
        print("(D) - Apple 🍎")
        print(" ")
        quizz("C")
        break
    clear()
    while True:
        print("2.")
        print("[🟡] - Deuxieme Question: ")
        print(" ")
        print("[💸] - Combien doit Fabian à la famille Scohier pour tous les trajets en voiture?")
        print("<HINT> 👉 Pour les amis c'est gratuit")
        print("(A) - €25.49")
        print("(B) - €65 pour quand mon père s'est fait flacher sur la route pour nous emmener à la salle.")
        print("(C) - ~€80 (€2.43/L (diesel actuellement) avec une voiture 5L/100, pour un total de 658km...)")
        print("(D) - €0")
        quizz("D")
        break
    clear()
    while True:
        print("3.")
        print("[🟢] - Troisieme Question: ")
        print("")
        print("[🎒] - Quel emplacement Fabian choisirait pour y placer son sac lors d'un rdv sur la place des Wallons ? 🧐")
        print("(A) - Il le garde sur son dos, tant pis si c'est inconfortable.")
        print("(B) - Il le pose dans une fraiche flaque de Vomit, au moins ça fait un prétexte pour que son ami lui touche les fesses 😶‍🌫️")
        print("(C) - Il se force à le garder en mains pour s'empecher de faire des 🫲 67🫴 🤪")
        print("(D) - Il a voulu faire TOP 1 🎶, Sans l'aide d'aucun copain 🎵, (sorry j'avais plus d'inspi 🥀...)")
        quizz("B")
        break
    clear()
    while True:
        print("4.")
        print("[🔴] - Quatrième Question: ")
        print(" ")
        print("[🤸] - Contexte: Resto Sushi, t'as bien mangé, tu payes,.... (complete cette situation)")
        print("(A) - Tu laisses un Pourboire de 500€ car ils étaient vachement bon ces sushi. Miammm...😋")
        print("(B) - Tu lâches ton meilleur 🫲 67🫴 car après tout, pourquoi pas?(on sait tous que tu en es acro, et c'est bien, on t'en veux pas...)")
        print("(C) - Tu remarques une tâche de sauce soja (t'es maudit, qu'est ce que tu veux que je te dise)")
        print("(D) - Tu te retournes et tu tombes à cause d'une chaise pour bébé (va savoir comment j'ai eu cette information)")
        quizz("D")
        break
    clear()
    while True:
        print("5.")
        print("")
        print("\t[❔] - L̴̡̧̡̩͎͍͙͕̝̫͙̖̣͉̉̅̀̈́̉͋͝A̸̝̓̽̿̾͐͐̎̿̍̆̐͆̕͘Ş̶̜͓̞̗̝̲̯̼̞̔̊̾̓̍̈́̈́̈́̄̇͘͠T̴̛̻̹͎͖̱̮̣͔͚̻͖̅̑́̈̂ͅͅ ̸̨̧̛̠͇̺̥̯̟͕̌͐̀̀̋̊̎͂̿̎̔͘̕͜͜͠ͅQ̸̛͕̘̽͑͆Ǘ̴̡̧̻̠̖͉̬̠̖͉̎̈E̸͕͂͂̎͘S̶̹̦̭̼͎͈͚̹͍̽̿̓̃͝T̵̛̯̗̲̿̂̽Ī̴̢̦̰̎́̌̂͆͆̔̓̒͑̍̋̕Ò̵̺̻̞̤͐Ṉ̶̡̣̬͔̫̗̮͍̥̯͓̊͗̔̚̕ : ")
        print(" ")
        input("Révéler <ENTER> ...")
        clear()
        print("\tComment...")
        print(" ")
        print(" ")
        input("\t<ENTER>")
        clear()
        print("\têtre...")
        print(" ")
        print(" ")
        input("\t<ENTER>")
        clear()
        time.sleep(2)
        print(fabian)
        print(" ")
        print(" ")
        time.sleep(1.5)
        input("\t<ENTER> Savoir Comment ???")
        clear()
        time.sleep(0.5)
        print("Il faut d'abord être...")
        time.sleep(1)
        print(gentil)
        print(" ")
        time.sleep(1.5)
        input("<ENTER>...")
        clear()
        print("\tET Surtout...")
        print(" ")
        print(" ")
        time.sleep(1)
        input("<ENTER>...")
        for i in range(16):
            print(doux)
            time.sleep(0.1)
            print(doux2)
            time.sleep(0.1)
        input("<ENTER>...")
        clear()
        print("\tET...")
        print(" ")
        print(" ")
        time.sleep(1)
        input("<ENTER>...")
        clear()
        for i in range(1, 40):
            print("Bienveillant "*i)
            time.sleep(0.01)
        print(" ")
        print(" ")
        time.sleep(1)
        input("<ENTER>...")
        clear()
        time.sleep(2)
        print("👉| Joyeux Anniversaire |👈")
        print(" ")
        print(" ")
        time.sleep(1)
        print("🫶  Damian (feat. Elsa)")
        time.sleep(2)
        input("<ENTER> to finish DBG...")
        clear()
        sys.exit()


        
DBG()