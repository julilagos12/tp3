#1
import string
texte= input("Entrez un texte: ")
texte_minuscule=texte.lower()
print("texte en minuscule:", texte_minuscule)
texte_sans_ponctuation=("")
for caractere in texte_minuscule:
    if caractere not in string.punctuation:
        texte_sans_ponctuation+=caractere
print("texte sans ponctuation:", texte_sans_ponctuation)

mots=texte_sans_ponctuation.split() #split() permet de séparer les mots
#mots uniques
#mots_uniques=[]
#for apple in mot #RENDUE LAAAA

#calculer longeur des mots
total_lettres=0
nombre_de_mots=len(mots)#compter le nombre de mots
for apple in mots: #basically for mot in texte_sans_ponctuation
    total_lettres+=len(apple) #pour chaque mot, ajouter la longueur du mot, donc on va avoir le nombre total de lettres
if nombre_de_mots>0: #verifier quil y a des mots pour faire la moyenne
    moyenne=total_lettres/nombre_de_mots 
else: #si pas de mots
    moyenne=0
print("nombre de mots:", nombre_de_mots)
print("nombre total de lettres:", total_lettres)
print("moyenne de lettres par mot:", moyenne)

x=5<5
print(x)
print(not x)
ch="Bonjour"
print(ch[0], ch[1])
print("on"in ch)
print("a" in ch)
ch1="Benjamin"
print(ch + ch1 + "!")
ma_chaine = 'Bonjour'
for c in ma_chaine:
    print(c)

a, b, c = 1, 1, 1
# a & b servent au calcul des termes successifs
# c'est un simple compteur
print(b) # affichage du premier terme
while c<15: # nous afficherons 15 termes au total
    a, b, c = b, a+b, c+1
    print(b)

reponse = input("Voulez-vous entrer un nombre? (o/n)")
somme = nb = 0
while reponse != 'n':
    nouveau_nombre = float(input("Veuillez entrer un nombre: "))
    nb += 1
    somme += nouveau_nombre
    reponse = input("Voulez-vous entrer un nombre? (o/n)")
moyenne = somme / nb if nb != 0 else "N/A"
print(f"La moyenne de la suite de nombres est {moyenne}")









        



