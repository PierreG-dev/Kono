#La seule Variable ici est la variable "grille" qui definit la place de chacun des pions dans le tableau ()
import random # on importe la fonction  random pour le tirage au sort




################################### Grille Vanilla ############################

#on initialise la liste des positions de chaque pions au debut de la partie
def Vanilla():
	plateau = [['x' , 'x' , 'x' , 'x'] , ['x' , 'x' , 'x' , 'x'] , ['o' , 'o' , 'o' , 'o'] , ['o' , 'o' , 'o' , 'o']]
	return plateau

###############################################################################



##################################### Affichage ###############################

def Affichage_Grille(grille): #Fonction permettant l'affichage de l'interface de jeu de maniere combinee avec la grille actuelle, cet affichage est utilisable avec n'importe quelle version de la grille
    print("\x1b[31m     1    2    3    4\x1b[0m") #affichage des differentes coordonnees de maniere horyzontale
    print("   ╔═══╦╦═══╦╦═══╦╦═══╗    Joueur 1 => 'o'") #affichage du haut du tableau, plus une indication concernant
    for i in range(4): #n parcours la liste grille
        print("\x1b[31m",i+1,"\x1b[0m" , end = "") #affichage des differentes coordonnees de maniere verticale
        for j in range(4): #on parcours le tuple
            print("║\x1b[31m",grille[i][j],"\x1b[0m║", end="") #affichage du contenu des cases et finalisation des cases
        print("") #saut de ligne
        if i != 3: #pour ne pas avoir d'intercases a la place du bas du tableau
            print("   ╠═══╬╬═══╬╬═══╬╬═══╣")# affichage des intercases
    print("   ╚═══╩╩═══╩╩═══╩╩═══╝    Joueur 2 => 'x'") #affichage du bas du tableau
    score_x , score_o = Score(grille)
    print("score Joueur 1 = \x1b[31m" , score_o , "\x1b[0m")
    print("score Joueur 2 = \x1b[31m" , score_x , "\x1b[0m")
    print("")
    print("")
    print("          ---------------          ")

#Affichage_Grille() #affichage de la grille selon la variable grille (modifier la liste grille pour obtenir des cases differentes)

###############################################################################



################## Verification de l'existance d'un point #####################
######## /!\ Fonction Inutile dans le programme final /!\ #####################
#Fonction permettant de savoir si un pion est bel et bien present dans la grille grace a  ses coordonnees
#la variable y represente la position verticale et la variable x represente la postion horyzontale
#def Grille_Coordonnees(x , y):
#	if (0 < x <= 4 and 0 < y <= 4): #on verifie que les coordonnees entrees sont plausibles compte tenu de la taille de la grille
#		print("la position existe et elle est de : " ,grille[y-1][x-1]) #on affiche la valeur comprise dans la case correspondante aux coordonnees
#	else:
#		print("Il n'y a pas de telles coordonnees dans la grille (Rappel: la grille est de forme 4x4)")

#Grille_Coordonnees(2 , 2)#test positif
#Grille_Coordonnees(3 , 5)#test negatif

###############################################################################



############################Fonctions de controle des joueurs #################

def Tirage_au_sort(): #decider quel joueur commence a  l'aide de la fonction random.randint importee plus haut
    premier = random.randint(1,2)
    if premier == 1:
        print("Le Joueur 1 (pions o) commence")
    else:
        print("Le Joueur 2 (pions x) commence")
    return premier , premier

#Joueur = Tirage_au_sort()

def J_Courant(Joueur , Premier): #Affiche le nom du joueur courant
	print("C'est le tour du joueur " , Joueur , "!")

def Changement_de_Joueur(Joueur , Tour , Premier):
	if Tour % 2 != 0 and Premier == 1 :
		Joueur += 1
		Tour += 1
	if Tour % 2 != 0 and Premier == 2 :
		Joueur -= 1
		Tour += 1
	if Tour % 2 == 0 and Premier == 1 :
		Joueur -= 1
		Tour += 1
	if Tour % 2 == 0 and premier == 2 :
		Joueur += 1
		Tour += 1
	return Joueur , Tour

###############################################################################




#######################Saisie de coordonnees du pion a bouger##################

def Coordonnees_Depart(Joueur): #fonction pour entrer les coordonnees du pion a jouer
	print ("entrez les coordonnees du pion a deplacer (x/y)")
	x = int(input()) #coordonnees x
	y = int(input()) #coordonnees y
	if x>4 or y>4 :
		print("Ces coordonnees n'existent pas")
		return Coordonnees_Depart(Joueur)
	if Joueur == 1 and y < 3:
		print("ce pion ne vous appartient pas ! ressaisissez coordonnees :")
		return Coordonnees_Depart(Joueur)
	if Joueur == 2 and y > 3:
		print("ce pion ne vous appartient pas ! ressaisissez coordonnees :")
		return Coordonnees_Depart(Joueur)
	return x , y
#Joueur = 1
#x , y = Coordonnees_Depart()
#print(x , y)
#print (x,y)

###############################################################################




################################ Mouvement simple #############################

def Verif_Mouvement_Simple(x , y , x1 , y1 , grille): # fonction permettant de verifier si le mouvement de pion simple est possible
	compt = 0
	if (0 < x1 <= 4) and (0 < y1 <= 4):
		compt += 1
	if (grille[y1-1][x1-1] == ' '):
		compt += 1
	if (x1 == (x - 1) or (x + 1) or x):
		compt += 1
	if (y1 == (y-1) or (y + 1) or y):
		compt += 1
	if compt == 4:
		return 1
	else:
		return 0

def Mouvement_Simple(Joueur , grille) :#fonction pour effectuer le mouvement simpel d'un pion, utilisant les variables Joueur et grille
	x , y = Coordonnees_Depart(Joueur)
	print("ou voulez vous deplacer ce pion ?")
	x1 = int(input()) #coordonnees x de la case d'arrivee du pion a deplacer
	y1 = int(input()) #coordonnees y de la case d'arrivee du pion a deplacer
	if Verif_Mouvement_Simple(x , y , x1 , y1 , grille) == 1:
		grille[y1-1][x1-1] = grille[x-1][y-1]
		grille[y-1][x-1] = ' '
		print("Mouvement effectue")
	else:
		print("Mouvement impossible")
		return Mouvement_Simple(Joueur , grille)
	return grille

#grille = Mouvement_Simple()
#Affichage_Grille()

###############################################################################



########################## Capture de pions ###################################

def Verif_Capture(x , y , x1 , y1 , Joueur , grille): #fonction pour verifier si le mouvement de capture est possible selont les variables x,y,x1,y1, joueur et grille
	compt = 0
	if ((Joueur == 1 and grille[y1-1][x1-1] == 'x') or (Joueur == 2 and grille[y1-1][x1-1] == 'o')) :
		compt += 1
	if (0 < x1 <= 4) and (0 < y1 <= 4) :
		compt += 1
	if (x1 == x + 2 or x - 2 or x) :
		compt += 1
	if (y1 == y + 2 or y - 2 or y) :
		compt += 1
	if (x1 !=  x and grille[y-1][x-1] == grille[y1-1][x1] or grille[y1-1][x1-2]) or (y1 != y and grille[y-1][x-1] == grille[y1][x1-1] or grille[y1-2][x1-1]) :
		compt += 1
	if compt == 5 :
		return 1
	else:
		return 0

def Capture(grille , Joueur) : #fonction pour le mouvement de capture de pion, utilisant grille et Joueur
	x , y = Coordonnees_Depart(Joueur)
	print("ou voulez vous deplacer ce pion ?")
	x1 = int(input()) #coordonnees x de la case d'arrivee du pion a deplacer
	y1 = int(input()) #coordonnees y de la case d'arrivee du pion a deplacer
	if Verif_Capture(x , y , x1 , y1 , Joueur , grille) == 1:
		grille[y1-1][x1-1] = grille[y-1][x-1]
		grille[y-1][x-1] = ' '
		print("Mouvement effectue")
	else:
		print("Mouvement impossible")
		return Capture(grille , Joueur)
	return grille
#grille = Mouvement_Capture()
#Affichage_Grille

###############################################################################



######################## Fonction Principale ##################################

def Tour_de_jeu(Joueur , grille): #fonction pour effectuer un tour de jeu selon le joeur actuel utilisant les variables joueur et grille
	J_Courant(Joueur)
	Affichage_Grille(grille)
	print("Quel mouvement souhaitez vous effectuer ? (Mouvement / Capture)")
	mouv = input()
	if mouv == 'Mouvement' :
		grille = Mouvement_Simple(Joueur , grille)
		Affichage_Grille(grille)
	if mouv == 'Capture' :
		grille = Capture(grille , Joueur)
		Affichage_Grille(grille)
 		return grille

def fin_de_partie_1(grille): #fonction pour verifier si la partie est finie
	x , o = Score(grille)
	if x > 6 or o > 6 :
		return 0
	else:
		return 1



def partie(): #fonction creant une partie a 2 joueurs
	grille = Vanilla()
	Tour = 1
	Joueur , Premier = Tirage_au_sort()
	while fin_de_partie(grille) != 0 and Mouvement_Possible(grille) != 0 :
		grille = Tour_de_jeu(Joueur , grille)
		Joueur , Tour = Changement_de_Joueur(Joueur , Tour , Premier)

def Score(grille) : #fonction calculant le score , utilise la variable grille
	pions_x = 0 #compteur de pions x
	pions_o = 0 #compteur de pions o
	score_x = 0 #score des x
	score_o = 0 #score des o
	for i in range(len(grille)) :
		for j in range(len(grille[i])) :
			if grille[i][j] == 'x':
				pions_x += 1
			if grille[i][j] == 'o':
				pions_o +=1
	score_x = 8 - pions_o
	score_o = 8 - pions_x
	return score_x , score_o

def Mouvement_Possible(grille):
	Mouvement_x = 0
	Mouvement_o = 0
	for y in range(len(grille)) :
		for x in range(len(grille[y])) :
			if grille[y][x] != ' ' :
				for y1 in range(len(grille)) :
					for x1 in range(len(grille[y1])) :
						if Verif_Mouvement_Simple(x , y , x1 , y1 , grille) == 1 :
							if grille[y][x] == 'x' :
								Mouvement_x += 1
							if grille[y][x] == 'o' :
								Mouvement_o += 1
	if Mouvement_o == 0 or Mouvement_x == 0 :
		return 0
	else:
		return 1

#partie()
###############################################################################



################################## IA #########################################

def IA_Guidee(grille , Joueur) : #fonction permettant la mise en marche de l'IA Guidee , usant les variables grille et Joueur
	liste_simple = []
	liste_coup_choisit = []
	liste_indice = []
	indice = 0
	for y in range(len(grille)) :
		for x in range(len(grille[y])) :
			for y1 in range(len(grille)) :
				for x1 in range(len(grille[y1])) :
					if Verif_Mouvement_Simple(x , y , x1 , y1 , grille) == 1 :
						liste_simple.append([x1 , y1 , x , y])
						liste_indice.append(indice)
						indice += 1
					if Verif_Capture(x , y , x1 , y1 , Joueur , grille) == 1 :
						grille = Capture_IA(Joueur , grille , x1 , y1 , x , y)
						return grille
	Elu = random.randint(0 , len(liste_indice) - 1)
	liste_coup_choisit = liste_simple[Elu]
	grille = Mouvement_Simple_IA(Joueur , grille , liste_coup_choisit[0] , liste_coup_choisit[1] , liste_coup_choisit[2] , liste_coup_choisit[3])
	return grille







def IA_Naive(grille , Joueur) : #fonction permettant la mise en marche de l'IA Naive, usant les variables grille et Joueur
	liste_coups = []
	liste_coup_choisit = []
	liste_indice = []
	indice = 0
	for y in range(len(grille)) :
		for x in range(len(grille[y])) :
			for y1 in range(len(grille)) :
				for x1 in range(len(grille[y1])) :
					if Verif_Mouvement_Simple(x , y , x1 , y1 , grille) == 1 :
						liste_coups.append([x1 , y1 , x , y])
						liste_indice.append(indice)
						indice += 1
					if Verif_Capture(x , y , x1 , y1 , Joueur , grille) == 1 :
						liste_coups.append([x1 , y1 , x , y])
						liste_indice.append(indice)
						indice += 1
	Elu = random.randint(0 , len(liste_indice) - 1)
	liste_coup_choisit = liste_coups[Elu]
	if Verif_Capture(liste_coup_choisit[2] , liste_coup_choisit[3] , liste_coup_choisit[0] , liste_coup_choisit[1] , Joueur , grille) == 1 :
		grille = Capture_IA(Joueur , grille , liste_coup_choisit[0] , liste_coup_choisit[1] , liste_coup_choisit[2] , liste_coup_choisit[3])
	if Verif_Mouvement_Simple(liste_coup_choisit[2] , liste_coup_choisit[3] , liste_coup_choisit[0] , liste_coup_choisit[1] , grille) == 1 :
		grille = Mouvement_Simple_IA(Joueur , grille , liste_coup_choisit[0] , liste_coup_choisit[1] , liste_coup_choisit[2] , liste_coup_choisit[3])
	return grille



def Mouvement_Simple_IA(Joueur , grille , x1 , y1 , x , y): #fonction permettant le mouvement simple sans affichage (pour IA)
    grille[y1-1][x1-1] = grille[x-1][y-1]
    grille[y-1][x-1] = ' '
    return grille

def Capture_IA(Joueur , grille , x1 , y1 , x , y) : #fonction permettant la capture sans impression(pour IA)
    grille[y1-1][x1-1] = grille[y-1][x-1]
    grille[y-1][x-1] = ' '
    return grille

###############################################################################



############################### Principal IA ##################################
def partie_IA_Guidee() : #fonction permettant le deroulement d'une partie contre une IA guidee
    grille = Vanilla()
    Joueur = Tirage_au_sort()
    while fin_de_partie(grille) != 0 :
        if Joueur == 2 :
            Joueur , grille = Tour_de_jeu_IA_Guidee(Joueur , grille)
        if Joueur == 1 :
            Joueur , grille = Tour_de_jeu(Joueur , grille)

def partie_IA_Naive() : #fonction pour jouer contre l'IA
    grille = Vanilla()
    Joueur = Tirage_au_sort()
    while fin_de_partie(grille) != 0 :
        if Joueur == 2 :
            Joueur , grille = Tour_de_jeu_IA_Guidee(Joueur , grille)
        if Joueur == 1 :
            Joueur , grille = Tour_de_jeu(Joueur , grille)

def Tour_de_jeu_IA_Naive(Joueur , grille): #fonction pour effectuer un tour de jeu selon le joeur actuel
	J_Courant(Joueur)
	Affichage_Grille(grille)
	if Joueur == 1 :
		print("Quel mouvement souhaitez vous effectuer ? (Mouvement / Capture)")
		mouv = input()
		if mouv == 'Mouvement' :
			grille = Mouvement_Simple(Joueur , grille)
			Affichage_Grille(grille)
		if mouv == 'Capture' :
			grille = Capture(grille , Joueur)
			Affichage_Grille(grille)
	if Joueur == 2 :
		grille = IA_Naive(grille , Joueur)
		Affichage_Grille()
	if Joueur == 1 :
		Joueur = 2
	if Joueur == 2 :
		Joueur = 1
	return Joueur , grille

def Tour_de_jeu_IA_Guidee(Joueur , grille): #fonction pour effectuer un tour de jeu selon le joeur actuel
	J_Courant(Joueur)
	Affichage_Grille(grille)
	if Joueur == 1 :
		print("Quel mouvement souhaitez vous effectuer ? (Mouvement / Capture)")
		mouv = input()
		if mouv == 'Mouvement' :
			grille = Mouvement_Simple(Joueur , grille)
			Affichage_Grille(grille)
		if mouv == 'Capture' :
			grille = Capture(grille , Joueur)
			Affichage_Grille(grille)
	if Joueur == 2 :
		grille = IA_Guidee(grille , Joueur)
		Affichage_Grille()
	if Joueur == 1 :
		Joueur = 2
	if Joueur == 2 :
		Joueur = 1
	return Joueur , grille


###############################################################################



################################# Menu ########################################

def Menu_Principal() : #programme du menu principal
	print("          \x1b[31m          -- Kono --\x1b[0m                      ")
	print(" ")
	print("          \x1b[31m             고노\x1b[0m")
	print(" ")
	print(" ")
	print("         Choisissez ce que vous voulez faire")
	print(" ")
	print(" 1 ----> Jeu a deux Joueurs")
	print(" 2 ----> Jeu contre IA")
	print(" 3 ----> Tests du programme")
	choix_1 = int(input())
	if 0 > choix_1 or 3 < choix_1 :
		print(" /!\ choisissez une des trois rubriques")
		return Menu_Principal()
	if choix_1 == 1 :
		return partie()
	if choix_1 == 2 :
		print("Contre quelle IA souhaitez vous jouer ?")
		print(" ")
		print(" 1 ----> IA Naive")
		print(" 2 ----> IA Guidee")
		choix_2 = int(input())
		if 0 > choix_2 or 2 < choix_2 :
			print(" /!\ choisissez une des deux rubriques")
			return Menu_Principal()
		if choix_2 == 1 :
			return partie_IA_Naive()
		if choix_2 == 2 :
			return partie_IA_Guidee()
	if choix_1 == 3 :
		print("Quels test voulez vous effectuer ?")
		print(" ")
		print(" 1 ----> test Capture")
		print(" 2 ----> test IA Naive")
		print(" 3 ----> test Mouvement simple")
		print(" 4 ----> test IA Guidee")
		choix_3 = int(input())
		if 0 > choix_3 or 4 < choix_3 :
			print("/!\ choisissez une des quatres rubriques")
			return Menu_Principal()
		if choix_3 == 1 :
			return Test_Capture()
		if choix_3 == 2 :
			return Test_IA_Naive()
		if choix_3 == 3 :
			return Test_Mouvement()
		if choix_3 == 4 :
			return Test_IA_Guidee()

###############################################################################



################################## Tests ######################################

def Test_Mouvement() : #programme du test de mouvement
	Joueur = 1
	grille = [['x' , 'x' , 'x' , 'x'] , ['x' , 'x' , 'x' , 'x'] , ['o' , ' ' , 'o' , ' '] , [' ' , 'o' , 'o' , 'o']]
	Affichage_Grille(grille)
	print("Au tour du Joueur 1")
	grille = Mouvement_Simple(Joueur , grille)
	Affichage_Grille(grille)
	print("\x1b[31m고노  Tapez 'exit' pour retourner au menu principal // Pour refaire ce test tapez n'importe quoi\x1b[0m")
	sortie = input()
	if sortie != 'exit' :
		return Test_Mouvement()
	else:
		return Menu_Principal()

def Test_Capture() : #Programme du test de capture
	Joueur = 1
	grille = [['x' , 'x' , 'x' , 'x'] , ['x' , 'x' , 'x' , 'x'] , ['o' , 'o' , 'o' , 'o'] , ['o' , 'o' , 'o' , 'o']]
	Affichage_Grille(grille)
	print("Au tour du Joueur 1")
	grille = Capture(grille , Joueur)
	Affichage_Grille(grille)
	Joueur = 2
	print("Au tour du Joueur 2")
	grille = Capture(grille , Joueur)
	Affichage_Grille(grille)
	print("\x1b[31m고노  Tapez 'exit' pour retourner au menu principal // Pour refaire ce test tapez n'importe quoi\x1b[0m")
	sortie = input()
	if sortie != 'exit' :
		return Test_Capture()
	else:
		return Menu_Principal()

def Test_IA_Naive() : #programme du test de l'IA naive
	Joueur = 2
	grille = [['x' , ' ' , 'x' , 'x'] , ['x' , ' ' , 'x' , 'x'] , ['o' , ' ' , 'o' , ' '] , [' ' , 'o' , 'o' , 'o']]
	Affichage_Grille(grille)
	print("Au tour de L'IA")
	grille = IA_Naive(grille , Joueur)
	Affichage_Grille(grille)
	print("\x1b[31m고노  Tapez 'exit' pour retourner au menu principal // Pour refaire ce test tapez n'importe quoi\x1b[0m")
	sortie = input()
	if sortie != 'exit' :
		return Test_IA_Naive()
	else:
		return Menu_Principal()

def Test_IA_Guidee() : #programme du test de l'IA guidee
	Joueur = 2
	grille = [['x' , 'x' , 'x' , 'x'] , ['x' , ' ' , ' ' , 'x'] , ['o' , 'o' , 'o' , 'o'] , ['o' , 'o' , 'o' , 'o']]
	Affichage_Grille(grille)
	print("Au tour de l'IA")
	grille = IA_Guidee(grille , Joueur)
	Affichage_Grille(grille)
	print("\x1b[31m고노  Tapez 'exit' pour retourner au menu principal // Pour refaire ce test tapez n'importe quoi\x1b[0m")
	sortie = input()
	if sortie != 'exit' :
		return Test_IA_Naive()
	else:
		return Menu_Principal()

##############################################################################

Menu_Principal()
