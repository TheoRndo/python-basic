nombre1=1
for loop in range(20):
    print(nombre1, end=" ")
    nombre1 = nombre1 + 1
nombre1=1
print()
for loop in range(20):
    print(nombre1*2, end=" ")
    nombre1 = nombre1 +1
print()
nombre1 = 1


nombre1=1
nombre2=1
for loop in range(20):
    for loop in range(20):
        print(nombre1*nombre2, end=" ")
        nombre1 = nombre1 +1
    print()
    nombre1 = 1
    nombre2 = nombre2 + 1

tempMin = int(input())
tempMax = int(input())
for loop in range(tempMax - tempMin + 1):
   print(tempMin)
   tempMin = tempMin + 1

nbNombres=int(input())
number = 66
nb = 2
for loop in range(nbNombres):
   print(number)
   number = number * nb
   nb = nb + 1

positionDepart=int(input())
largeurEmplacement=int(input())
nbVendeurs=int(input())

print(positionDepart)
for loop in range(nbVendeurs):
   print(positionDepart + largeurEmplacement)
   positionDepart = positionDepart + largeurEmplacement

somme = int(input())
for loop in range(19):
    nombreajt = int(input())
    somme = somme + nombreajt
print(somme)

cotebas=int(input())
cotehaut=int(input())
volume = 0
nb = 0
for loop in range (cotehaut - cotebas + 1):
    volume = volume + (cotebas+nb)**2
    nb = nb + 1
print(volume)

nbKarvas=int(input())
for loop in range(nbKarvas):
    poids=int(input())
    age=int(input())
    cornes=int(input())
    garrot=int(input())
    note=cornes*garrot+poids
    print(note)

borne1=int(input())
borne2=int(input())
distance = borne1-borne2
if distance > 0:
   print(distance)
else :
   print(-distance)

poids=0
poids_=0
nbMembres=int(input())
for loop in range(nbMembres):
    poids= poids + int(input())
    poids_= poids_ + int(input())
if poids > poids_ :
    print("L'équipe 1 a un avantage")
else :
    print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 :",poids)
print("Poids total pour l'équipe 2 :",poids_)

total = 0
nbLieus=int(input())
for loop in range(nbLieus):
    lieu=int(input())
    if lieu > 10000:
        total = total + 1
print(total)

route=int(input())
village=int(input())
distance = 0
total = 0
for loop in range(village):
    distance=int(input())
    if abs(route-distance) <= 50:
        total = total + 1
print(total)

nbJours=int(input())
distancemax = 0
for loop in range(nbJours):
    distance=int(input())
    if distance >= distancemax :
        distancemax = distance
print(distancemax)

nbMD=int(input())
montee = 0
descente = 0
for loop in range(nbMD):
    chemin=int(input())
    if chemin > 0:
        montee = montee + chemin
    else :
        descente = descente - chemin
print(montee)
print(descente)

hauteur=int(input())
folioles=int(input())
if hauteur >= 10 and folioles >= 10 :
    print("Calaelen")
if hauteur <= 5 and folioles >= 8:
    print("Tinuviel")
if hauteur <= 8 and folioles <= 5:
    print("Falarion")
if hauteur >= 12 and folioles <= 7:
    print("Dorthonion")

age=int(input())
bagages=int(input())
prix = 0
if age == 60:
    prix = 0
else:
    if age < 10:
        prix = 5
    else :
        prix = 30
        if bagages >= 20:
            prix = prix + 10
print(prix)

maison=int(input())
abscisse = 0
ordonnee = 0
abscissemax = 0
ordonneemax = 0
abscissemin = 1000000
ordonneemin = 1000000
for loop in range(maison):
    abscisse=int(input())
    ordonnee=int(input())
    if abscisse >= abscissemax:
        abscissemax = abscisse
    if abscisse <= abscissemin:
        abscissemin = abscisse
    if ordonnee >= ordonneemax:
        ordonneemax = ordonnee
    if ordonnee <= ordonneemin:
        ordonneemin = ordonnee
print( (abscissemax-abscissemin)*2 + (ordonneemax-ordonneemin)*2 )

nbMarchands=int(input())
prixmax=1000000
position = 0
positionmax = 0
for loop in range(nbMarchands):
    prix=int(input())
    if prix < prixmax:
        prixmax = prix
    position = position + 1
    if prix == prixmax:
        positionmax = position
print(positionmax)
print(prixmax)

debut=int(input())
fin=int(input())
nbEntrees=int(input())
personnes = 0
for loop in range(nbEntrees):
    entre=int(input())
    if (entre>=debut) and (entre<=fin):
        personnes = personnes + 1
print(personnes)

abmin=int(input())
abmax=int(input())
ormin=int(input())
ormax=int(input())
maisons=int(input())
compte = 0
for loop in range(maisons):
    abscisse=int(input())
    ordonnee=int(input())
    if (abscisse <= abmax) and (abscisse >= abmin) and (ordonnee <= ormax) and (ordonnee >= ormin):
        compte = compte + 1
print(compte)

algoreen=int(input())
if (algoreen==4) or (algoreen==5) or (algoreen==6) or (algoreen==10):
    print(31)
if (algoreen==11):
    print(29)
if (algoreen==1) or (algoreen==2) or (algoreen==3) or (algoreen==7) or (algoreen==8) or (algoreen==9):
    print(30)


debutA=int(input())
finA=int(input())
debutB=int(input())
finB=int(input())
if (debutB<=finA):
    print("Amis")
else:
    print("Pas amis")


nbPersonnes=int(input())
compte = 0
comptemax = 0
for loop in range(2*nbPersonnes):
    personne=int(input())
    if personne > 0 :
        compte = compte + 1
    if personne < 0 :
        compte = compte - 1
    if comptemax <= compte:
        comptemax = compte
print(comptemax)

#RESOLU --------------------------------
nbPaires=int(input())
for loop in range(nbPaires):
    abmin=int(input())
    abmax=int(input())
    ormin=int(input())
    ormax=int(input())
    abmin2=int(input())
    abmax2=int(input())
    ormin2=int(input())
    ormax2=int(input())
    notintersection = (((abmin<abmin2 and abmax<abmin2)or(abmin>abmax2 and abmax>abmax2))or((ormin<ormin2 and ormax<ormin2)or(ormin>ormax2 and ormax>ormax2))) or (((abmin2<abmin and abmax2<abmin)or(abmin2>abmax and abmax2>abmax))or((ormin2<ormin and ormax2<ormin)or(ormin2>ormax and ormax2>ormax)))
    if not notintersection:
        print("OUI")
    else:
        print("NON")

#--------------------------------------------------

numeroPersonne = int(input())
tailleListe = int(input())
estSorti  = False
for loop in range(tailleListe):
   numero = int(input())
   if numero == numeroPersonne:
      estSorti = True
if estSorti:
   print("Sorti de la ville")
else:
   print("Encore dans la ville")


debut=int(input())
fin=int(input())
nbInvites=int(input())
compte=0
for loop in range(nbInvites):
    arrivee=int(input())
    depart=int(input())
    suspect = ((debut<=arrivee<fin) and (debut<depart<=fin)) or ((arrivee<=debut) and (depart>=fin)) or ((arrivee<=debut) and (debut<=depart<=fin)) or ((fin>=arrivee>=debut) and (depart>=fin))
    if suspect:
        compte = compte + 1
print(compte)


nombre = float(input())
print(nombre*(1/0.707))

nbPersonnes=int(input())
criteres = 0
for loop in range(nbPersonnes):
    taille=int(input())
    age=int(input())
    poids=int(input())
    cheval=int(input())
    cheveux=int(input())
    if (178<=taille<=182):
        criteres = criteres + 1
    if (age>=34):
        criteres = criteres + 1
    if (poids<70):
        criteres = criteres + 1
    if (cheval==0):
        criteres = criteres + 1
    if (cheveux==1):
        criteres = criteres + 1
    if criteres == 5:
        print("Très probable")
    elif (criteres == 3) or (criteres == 4):
        print("Probable")
    elif criteres == 0:
        print("Impossible")
    elif (criteres == 1) or (criteres == 2):
        print("Peu probable")
    criteres = 0


nbJetons=int(input())
for loop in range(nbJetons):
    X=int(input())
    Y=int(input())
    if (X>90) or (X<0) or (Y>70) or (Y<0):
        print("En dehors de la feuille")
    elif (60<Y<70) and ((10<X<45)or(60<X<85)):
        print("Dans une zone rouge")
    elif ((10<X<25)and(10<Y<55)) or ((25<X<50)and((10<Y<20)or(45<Y<55))) or ((50<X<85)and(10<Y<55)):
        print("Dans une zone bleue")
    else:
        print('Dans une zone jaune')


population=int(input())
compte = 1
jour = 1
while compte<population:
    compte = compte*3
    jour = jour + 1
print(jour)


stop = 0
somme = 0
while (stop != -1):
    stop = int(input())
    somme = somme + stop
print(somme)


nbcible=int(input())
proposition = -1
essais = 0
while (proposition != nbcible):
    proposition=int(input())
    essais = essais + 1
    if proposition < nbcible:
        print("c'est plus")
    elif proposition > nbcible:
        print("c'est moins")
print("Nombre d'essais nécessaires :")
print(essais)


maxpierres=int(input())
hauteur=1
pierres=1
if maxpierres == 0:
    print(0)
    print(0)
while (pierres <= maxpierres):
    hauteur = hauteur + 1
    pierres = pierres + hauteur**2
if maxpierres != 0:
    print(hauteur-1)
    print(pierres-hauteur**2)


mesures=int(input())
tempMin=int(input())
tempMax=int(input())
testmesure=0
while (mesures != 0):
    mesures = mesures - 1
    testmesure=int(input())
    if (tempMin<=testmesure<=tempMax):
        print("Rien à signaler")
    else:
        print("Alerte !!")
        mesures = 0



# NIVEAU 2 -------------------------------------------------

nbLegumes=int(input())
for loop in range(nbLegumes):
    poids=float(input())
    age=float(input())
    prix=float(input())
    print(prix/poids)


nbNotes=int(input())
total=0
for loop in range(nbNotes):
    note=float(input())
    total = total + note
print(total/nbNotes)

from math import *
population=int(input())
croissance=float(input())/100
print(floor(population+population*croissance))

from math import *
ciment=float(input())
prix = (45*ceil(ciment/60))
print(prix)

from math import *
temps=float(input())
distance = round((temps*340.29)/1000)
print(distance)

from math import *
taxeA=float(input())
taxeB=float(input())
prix=float(input())
prixsanstaxeA = prix - round((taxeA/100)*prix,2)
prixavectaxeB = prixsanstaxeA + round((taxeB/100)*prix,2)
print(round(prixavectaxeB,2))

from math import *

taxeActuelle = float(input())
nouvelleTaxe = float(input())
prixActuel = float(input())

nouveauPrix = round (prixActuel / (1 + taxeActuelle / 100) + prixActuel / (1 + taxeActuelle / 100) * (nouvelleTaxe /100), 2)

print(nouveauPrix)


argent=int(input())
prix=int(input())
print(argent//prix)


nbPersonnes=int(input())
nbFruits=int(input())
if (nbFruits % nbPersonnes == 0):
    print("oui")
else:
    print("non")

nbZones=int(input())
zone = nbZones%24
print(zone)

ingredients=[500, 180, 650, 25, 666, 42, 421, 1, 370, 211]
num=int(input())
print(ingredients[num])

ingredients=[9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
total = 0
for loop in range(10):
    poids=int(input())
    total = total + ingredients[loop]*poids
print(total)


produits=[0]*7
nbOperations=int(input())
for loop in range(nbOperations):
    num=int(input())
    produits[num-1]=int(input()) + produits[num-1]
for loop in range(10):
    print(produits[loop])


nbProduits=int(input())
nbPersonnes=int(input())
produits=[0]*nbProduits
for loop in range(nbPersonnes):
    num=int(input())
    produits[num] = produits[num]+1
for loop in range(nbProduits):
    print(produits[loop])


nbCharrettes=int(input())
charrettes=[0]*nbCharrettes
somme = 0
for loop in range(nbCharrettes):
    charrettes[loop]=float(input())
    somme = (charrettes[loop] + somme)
moyenne = somme/nbCharrettes
for loop in range(nbCharrettes):
    charrettes[loop] = moyenne - charrettes[loop]
    print(charrettes[loop])


nbDeplacements=int(input())
deplacements=[0]*nbDeplacements
for loop in range(nbDeplacements):
    deplacements[loop]=int(input())
    if (deplacements[loop] == 1) or (deplacements[loop] == 4):
        deplacements[loop] = deplacements[loop] + 1
    elif (deplacements[loop] == 2) or (deplacements[loop] == 5):
        deplacements[loop] = deplacements[loop] - 1
for loop in range(nbDeplacements):
    print(deplacements[nbDeplacements-loop-1])


from math import *
nbHabitants=int(input())
fortune=[0]*nbHabitants
for loop in range(nbHabitants):
    fortune[loop]=int(input())
fortune.sort()
medianne = 0
if nbHabitants % 2 == 0:
    medianne = (fortune[ceil((nbHabitants)/2)-1]+fortune[ceil((nbHabitants+2)/2)-1])/2
else:
    medianne = fortune[ceil(nbHabitants/2)-1]
print(medianne)

from math import *
nbParticipants=int(input())
liste=[0]*nbParticipants
for loop in range(nbParticipants):
    liste[loop]=int(input())
liste.sort()
for loop in range(ceil(nbParticipants/2)):
    print(liste[loop],liste[nbParticipants-loop-1])


nbPositions=int(input())
chPositions=int(input())
positions=[0]*nbPositions
for loop in range(nbPositions):
    positions[loop]=int(input())
for loop in range(chPositions):
    position1=int(input())
    position2=int(input())
    positions[position2],positions[position1] = positions[position1],positions[position2]
for loop in range(nbPositions):
    print(positions[loop])


nbEmplacements=int(input())
liste=[0]*nbEmplacements
for loop in range(nbEmplacements):
    liste[loop]=int(input())
for loop in range(nbEmplacements):
    print(liste.index(loop))


livres=[0]*6
auteurs=[0]*6
for loop in range(6):
    auteurs[loop]=input()
    livres[loop]=input()
for loop in range(6):
    print(livres[loop])
    print(auteurs[loop])

nom1=input()
nom2=input()
if nom1 > nom2:
    print(nom2)
if nom1 < nom2:
    print(nom1)

nbLignes=int(input())
lignes=[0]*nbLignes
for loop in range(nbLignes):
    lignes[loop]=input()
for loop in range(nbLignes):
    if loop % 2 == 1:
    print(lignes[loop])


nbLivres=int(input())
longueurMinimale=int(input())
for loop in range(2 * nbLivres):
    titre=input()
    resume=input()
    if len(resume) < longueurMinimale:
        print(titre)


nbLivres=int(input())
livres=[0]*nbLivres
for loop in range(nbLivres):
    livre[loop]=input()
print(livre[0])
for loop in range(nbLivres + 1):
    if len(livre[loop+1]) > len(livre[loop]):
        print(livre[loop])


nbPersonnes=int(input())
for loop in range(nbPersonnes):
    name=input().split(" ")
    print(name[1], name[0])


nbLignes, nbMots = map(int, input().split(" "))
nbLettres = [0]*100
for loop in range(nbLignes):
    ligne = input().split(" ")
    for loop in range(nbMots):
        nbLettres[len(ligne[loop])+1] = nbLettres[len(ligne[loop])+1] + 1
        for loop in range(len(nbLettres)+1):
            if nbLettres[loop] != 0:
                print(len(ligne[loop]), ":", nbLettres[loop])


nbLignes, nbMots = map(int, input().split(" "))
apparition = [0] * 101

for loop in range(nbLignes):
   texte = input().split(" ")

   for loop in range(nbMots):
      texte[loop] = len(texte[loop])

      for fois in range(101):
         if texte[loop] == fois:
            apparition[fois] = apparition[fois] + 1

for loop in range(101):
   if apparition[loop] > 0:
      print("{} : {}".format(loop, apparition[loop]))

#CORRECTION :
nbLignes, nbMots = map(int, input().split(" "))
histogramme = [0] * 101
for loop in range(nbLignes):
   mots = input().split(" ")
   for idMot in range(nbMots):
      longueur = len(mots[idMot])
      histogramme[longueur] = histogramme[longueur] + 1
for longueur in range(101):
   if histogramme[longueur] > 0:
      print("{} : {}".format(longueur, histogramme[longueur]))


texte=input()
for loop in range(len(texte)):
    print(texte[loop])


nbLignes=int(input())
for loop in range(nbLignes):
    ligne=input()
    for idLettre in range(len(ligne)):
        print(ligne[len(ligne)-idLettre-1], end="")
    print()


nometudiant=input()
if ("A"<=nometudiant[0]<="F"):
    print(1)
if ("G"<=nometudiant[0]<="P"):
    print(2)
if ("Q"<=nometudiant[0]<="Z"):
    print(3)


livre=input()
auteur=input()
voyelles=["A","E","I","O","U","Y"," "]
for loop in range(len(livre)):
    if livre[loop] not in voyelles:
        print(livre[loop], end="")
print()
for loop in range(len(auteur)):
    if auteur[loop] not in voyelles:
        print(auteur[loop], end="")


joueur1=input()
joueur2=input()
egalites = 0
minimum=min(len(joueur1),len(joueur2))
if joueur1 == joueur2:
    print("=")
for loop in range(minimum):
    if joueur1[loop] == joueur2[loop]:
        egalites = egalites + 1
    if joueur1[loop] < joueur2[loop]:
        print(1)
        break
    if joueur1[loop] > joueur2[loop]:
        print(2)
        break
print(egalites)

#AUTRE TEST
jeu1=input()
jeu2=input()
length1=len(jeu1)
length2=len(jeu2)
nbEgalites=0

while length1>0 and length2>0:
   if jeu1[nbEgalites]==jeu2[nbEgalites]:
      length1=length1-1
      length2=length2-1
      nbEgalites=nbEgalites+1

   elif jeu1[nbEgalites]>jeu2[nbEgalites]:
      print("2")
      print(nbEgalites)
      break

   else:
      print("1")
      print(nbEgalites)
      break

if length1==0 and length2==0:
    print("=")
    print(nbEgalites)
elif length1==0:
    print("2")
    print(nbEgalites)
elif length2==0:
    print("1")
    print(nbEgalites)

#CORRECTION
main1 = input()
main2 = input()
tour = 0
while tour < len(main1) and tour < len(main2) and main1[tour] == main2[tour]:
   tour = tour + 1
if tour == len(main1) and tour == len(main2):
   print("=")
elif tour == len(main2) or (tour < len(main1) and main1[tour] < main2[tour]):
   print(1)
else:
   print(2)
print(tour)


lettre=input()
nbLignes=int(input())
compte = 0
for loop in range(nbLignes):
    phrase=input()
    for l in range(len(phrase)):
        if phrase[l] == lettre:
            compte = compte +1
print(compte)


ligne=input()
caracteres=list(ligne)
for loop in range(len(ligne)):
    if caracteres[loop] == " ":
        caracteres[loop] = "_"
ligne = "".join(caracteres)
print(ligne)



def demande():
    code = 0
    while code != 4242:
        print("Entrez le code :")
        code=int(input())

demande()
print("Encore une fois.")
code = 0
demande()
print("Bravo.")


def demande(boncode):
    code = 0
    while code != boncode:
        print("Entrez le code :")
        code=int(input())

demande(4242)
print("Premier code bon.")
demande(2121)
print("Bravo.")


def ligneCaracteres(caractère, longueur):
   for iCol in range(longueur):
      print(caractère, end = "")
   print()

longueur=int(input())
ligneCaracteres("X", longueur)
ligneCaracteres("#", longueur)
ligneCaracteres("i", longueur)


def feuille(nbLignes, nbColonnes, motif):
    for loop in range(nbLignes):
        for loop in range(nbColonnes):
            print(motif, end="")
        print()

nbLignes=int(input())
nbColonnes=int(input())
motif=input()
feuille(nbLignes, nbColonnes, motif)


def min2(entier1, entier2):
    if entier1 < entier2:
        return entier1
    return entier2

minimum=int(input())
for loop in range(9):
    minimum = min2(minimum, int(input()))
print(minimum)


#RIP LE CRASH JAI TOUT PERDU APRES CE POINT...
#BAH GO TOUT RECOMMENCER :(

def ligne(nbX):
    print("X"*nbX, end="")

def rectangle(nbLignes,nbColonnes):
    if nbLignes > 2 and nbColonnes > 1:
        print("#"*nbColonnes, end="")
        print()
        for loop in range(nbLignes-2):
            print("#",(nbColonnes-4)*" ","#")
        print("#"*nbColonnes, end="")
    else:
        for loop in range(nbLignes):
            print("#"*nbColonnes)

def triangle(nbLignes2):
    if nbLignes2 > 2:
        print("@")
        for loop in range(nbLignes2-2):
            print("@", end="")
            print(loop*" ", end="")
            print("@")
        print("@"*(nbLignes2))
    else:
        for loop in range(nbLignes2):
            print("@"*(loop+1))

ok1=int(input())
ok2=int(input())
ok3=int(input())
ok4=int(input())
print()
ligne = ligne(ok1)
print()
print()
rectangle = rectangle(ok2,ok3)
print()
print()
triangle = triangle(ok4)


def conversionpieds(metre):
    conversion = metre*(1/0.3048)
    return conversion

def conversionlivres(gramme):
    conversion = gramme*(0.002205)
    return conversion

def conversionfahrenheit(celcius):
    conversion = 32+1.8*celcius
    return conversion

from math import *
nbConversions=int(input())
for loop in range(nbConversions):
    valeur=input()
    if "m" in valeur:
        valeur = valeur.split(" ")
        valeur = float(valeur[0])
        conversionpieds(valeur)
        print(round(conversionpieds(valeur),6), "p")
    elif "g" in valeur:
        valeur = valeur.split(" ")
        valeur = float(valeur[0])
        conversionlivres(valeur)
        print(round(conversionlivres(valeur),6), "l")
    elif "c" in valeur:
        valeur = valeur.split(" ")
        valeur = float(valeur[0])
        conversionfahrenheit(valeur)
        print(round(conversionfahrenheit(valeur),6), "f")


#FIN DES NIVEAUX 1 ET 2






































