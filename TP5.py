#!/usr/bin/env python3
#coding: utf-8
# Jérôme DELECLUSE - TP 5 PROG

from turtle import *


##### Le module turtle #####

# Questions

"""
forward() va toujours de l'avant, dans la direction pointée par la tortue.
Si la tortue pointe vers le bas, forward() tracera un trait vers le bas.
Elle n'est pas obligée de tracer un trait: si la fonction penup() a été
invoquée avant, la tortue avancera mais sans tracer de trait.

forward() dessine vers l'arrière avec un argument négatif (par contre elle
pointe toujours dans la même direction)

left() et right() ont par défaut des arguments en degrès. Il suffit d'essayer
avec par exemple left(90) et d'autres valeurs pour se rendre compte que la tortue
fonctionne en degrés.

goto(): place la tortue au point de coordonnées spécifiées.
Un trait est dessiné si penup() n'a pas été évoqué.

"""

# Lignes parallèles

"""
penup()
goto(-100,-100)
pendown()
pencolor('red')
goto(0, 300)
penup()
goto(100,-100)
pendown()
pencolor('green')
goto(200, 300)
"""


##### Dessiner des carrés #####

speed(0)  # Accélère la tortue

def carre(x):
    """
    Procédure dessinant un carré à partir de la position courante de la tortue.
    Le côté du carré est x
    """
    
    pendown()               # Au cas où le stylo serait levé
    for i in range(0, 4):
        forward(x)
        left(90)
        i = i + 1

"""
clearscreen()
carre(100)
carre(75)
"""

# La tortue se trouve dans la même position qu'avant l'appel de ma fonction

def dixCarres(x):
    """ Dessine 10 carrés alignés, de longueur x et espacés de 5 """

    for i in range(1, 11):
        carre(x)
        penup()
        forward(x + 5)
        pendown()

"""
clearscreen()
penup()
goto(-300, 0)
pendown()
dixCarres(50)
"""

def centCarres(x):
    """ Dessine 100 carrés arrangés en grand carré, de longueur x et espacés de 5 """
    for i in range(1, 11):
        dixCarres(50)
        penup()
        forward(-10 * (x + 5))
        left(90)
        forward(x + 5)
        right(90)
        pendown()

"""
clearscreen()
penup()
goto(-300, -300)
pendown()
centCarres(50)
"""

def carresEmboites():
    """ Dessine 50 carrés emboîtés ayant un sommet commun.
    La longueur des carrés varie de 10 en 10"""

    for i in range(0, 50):
        carre(10 * i + 10)

"""
clearscreen()
penup()
goto(-300, -300)
carresEmboites()
"""


def carres_tournants(n):
    """ Imprime 100 carrés de côté 100 pivotants autour d'un sommet commun. """

    angle = 360 / n

    for i in range(0, n):
        carre(100)
        right(angle)

"""
speed(0)
carres_tournants(7)
"""


##### Polygones convexes #####

"""
Pour un carré, on tourne de 360 / 4 degrés
Pour un polygine de n côtés: 360 / n degrés

"""

def polygone_reg_convexe(n ,l):
    
    pendown()               # Au cas où le stylo serait levé
    for i in range(0, n):
        forward(l)
        left(360 / n)

"""
clearscreen()
penup()
goto(-200, 200)
pendown()
polygone_reg_convexe(4,100)

penup()
goto(200, 200)
pendown()
polygone_reg_convexe(5,100)

penup()
goto(-200, -200)
pendown()
polygone_reg_convexe(6,100)

penup()
goto(200, -200)
pendown()
polygone_reg_convexe(7,100)
"""



##### Polygones étoilés #####
speed(3)
def polygone_etoile(n, l, k):
    pendown()
    for i in range(0, n):
        left(360 - k * 360 / n)
        forward(l)

"""
clearscreen()
penup()
goto(-200, 200)
pendown()
polygone_etoile(5, 150, 2)      


penup()
goto(200, 200)
pendown()
polygone_etoile(7, 150, 3) 

penup()
goto(-200, -200)
pendown()
polygone_etoile(8, 150, 3)

penup()
goto(200, -200)
pendown()
polygone_etoile(9, 150, 4) 


Un hexagone ayant 6 cotés et 6 angles, si on va par exemple de 2 angles en 2
angles, on obtient un triangle (6 / 2 = 3 cotés).
De 3 en 3, on obtient une ligne.
"""


##### Mouvement brownien #####

from random import randint

def dessine_rect(x, y):
    """ Dessine un rectangle bleu de longueur x et y, centré """
    penup()
    goto(-x / 2, y / 2)
    pendown()
    color("blue")
    for i in range(0,2):
        forward(x)
        right(90)
        forward(y)
        right(90)

def tortue_sortie(z):
    """ Renvoie True si la tortue se trouve dans un carré de coté z, centré """

    coord = z / 2
    res = False

    if(xcor() < coord and xcor() > -coord and ycor() < coord and ycor() > -coord):
        res = True

    return res


""" TESTS
dessine_carre(400)
goto(222, 100)
print(tortue_sortie(400))
goto(222, -250)
print(tortue_sortie(400))
goto(150, -50)
print(tortue_sortie(400))
"""

def brown(x):
    """
    Simule le mouvement brownien d'une particule dans un fluide.
    Le mouvement s'eefectura tant que la particule est dans un carré
    centré de longueur x
    """
    
    dessine_rect(x, x)
    color("green")
    penup()
    goto(0, 0)
    pendown()
    
    while(tortue_sortie(x)):
        angle = randint(0, 359)
        longueur = randint(10, 30)
        left(angle)
        forward(longueur)

# brown(400)



##### Billard #####

from math import tan, fabs, acos, sqrt, pi


def billard(a, b, xb, yb, angle, rebonds):
    """
    Définit la trajectoire d'une boule de billard selon la taille de la table,
    le nombre de bandes à faire, la position initiale.
    xb et yb sont les coordonnées initiales de la boule.
    angle est l'angle de départ.
    rebonds est le nombre de rebonds qu'elle doit effectuer
    :CU: angle >= 0 et xb <= a/2 et yb <= b/2 en valeur absolue
    """

    # Vérification des conditions de départ
    assert(angle >= 0), "Entrez un angle positif!"
    assert((fabs(xb) <= a / 2) & (fabs(yb) <= b / 2)), "Interdit de jouer par terre!"
    
    dessine_rect(a, b)

    angle = angle % 360 # Cas où l'utilisateur rentrerait un angle supérieur à 360°

    penup()
    goto(xb, yb)
    pendown()
    left(angle)

    
    
    # La droite de trajectoire de la bille: y = Ax + B
    A = tan(angle)
    print("A=", A)
    B = yb - A * xb
    print("B=", B)

    # Si l'angle est à 0, intersection avec la droite x = a / 2
    if(angle == 0):
        Y = yb
        X = a / 2
        
    # Si l'angle est à 90°, intersection avec la droite y = b / 2
    elif(angle == 90):
        X = xb
        Y = b / 2

    # Si l'angle est à 180°, intersection avec la droite x = - a / 2
    elif(angle == 180):
        Y = yb
        X = -a / 2

    # Si l'angle est de 270°, intersection avec la droite y = - b / 2
    elif(angle == 270):
        Y = -b / 2
        X = xb

    # Cas où l'angle est strictement compris entre 0 et 90°
    elif((angle > 0) & (angle < 90)):
        # On calcule l'angle à partir duquel la bille rebondira sur la bande supérieur et non
        # celle à droite
        angleRef = 180 * acos((a / 2 - xb) / sqrt(pow((a/2 - xb), 2) + pow((b / 2 - yb), 2))) / pi
        print("angleRef =", angleRef)

        if(angle == angleRef):
            X = a / 2
            Y = b / 2
        elif(angle < angleRef):
            X = a / 2
            Y = A * X + B
        elif(angle > angleRef):
            Y = b / 2
            X = (Y - B) / A

    # Cas où l'angle est strictement compris entre 90° et 180°
    elif((angle > 90) & (angle < 180)):
        angleRef = fabs(90 - 180 * acos((a / 2 - xb) / sqrt(pow((a/2 - xb), 2) + pow((b / 2 - yb), 2))) / pi)
        print(angleRef)

        if(angle - 90 == angleRef):
            X = -a / 2
            Y = b / 2
        elif(angle - 90 < angleRef):
            X = -a / 2
            Y = A * X + B
        elif(angle - 90 > angleRef):
            Y = b / 2
            X = (Y - B) / A




    goto(X, Y)
    penup()
    goto(2000,2000)
    

    
billard(300, 200, 0, 0, 25, 2)

    





