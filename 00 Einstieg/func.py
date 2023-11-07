# -*- coding: utf-8 -*-

from math import sqrt, log10

# Aufgabe 1
def dialog():
    name = input("Wie heißt du?\n")
    print(f'Hallo {name}')
    zustand = input("Wie geht es dir?\n")
    print(f'Dir geht es also {zustand}')

# Taschenrechner
def tr():
    z1 = float(input("Gebe die erste Zahl ein:"))
    z2 = float(input("Gebe die zweite Zahl ein:"))
    summe = z1 + z2
    print(summe)

# Aufgabe 2
def fleischKauf():
    print("Guten Tag!")
    fleisch = input("Welche Fleischsorte möchten Sie?\n")
    gr = float(input(f'Wie viel Gramm {fleisch} möchten Sie?\n'))
    print(f'{gr} kg Fleisch vom {fleisch} wird für Sie vorbereitet.')
    print("Danke für Ihre Bestellung!")
    
#Aufgabe 3
def bmi():
    print("BMI-Rechner")
    gewicht = float(input("Geben Sie Ihr Gewicht in kg an!\n"))
    height = float(input("Geben Sie Ihre Größe in cm an!\n"))
    print(f'Ihr BMI-Index beträgt {gewicht/pow(height/100, 2)}')
    
# Aufgabe 4
def pythagoras():
    print("satz des Pythagoras: Berechnung der Hypotenuse")
    a = float(input("Geben Sie das Maß der Seitenlänge a in Meter an!\n"))
    b = float(input("Geben Sie das Maß der Seitenlänge b in Meter an!\n"))
    print(f'Die Seitenlänge c = {sqrt(pow(a, 2) * pow(b, 2))}')
    
# Aufgabe 5
def bits():
    print("Berechnung von Bitanzahl von einem Datentyp")
    n = int(input("Wie viele negative Zahlen lassen sich darstellen?\n"))
    p = int(input("Wie viele positive Zahlen lassen sich darstellen?\n"))
    print(f'Die Darstellung benötigt {(n + p) + 1} Bit')
    
# Aufgabe 6
def zins():
    k0 = float(input("Welches Kapital möchten Sie anlegen?\n"))
    e = int(input("Möchten Sie wissen wann ihr Gehalt einen bestimmten Wert erreicht (0) oder wie hoch Ihr Vermögen nach einer bestimmten Zeit ist (1)?\n"))
    if e == 1:
        t = float(input("Wie viele Jahre möchten Sie das Geld anlegen?\n"))
        p = float(input("Zu welchem Zinssatz (%) wird das Geld angelegt?\n"))
        print(f'Ihr Kapital beträgt nach {t} Jahren, bei einem Zinssatz von {p}% und einem Startkapital von {k0}€, {pow(k0 * ((p / 100) + 1), t)}€')
    else:
        kt = float(input("Welchen Wert möchten Sie durch die Anlage erreichen?\n"))
        p = float(input("Bei welchem Prozentsatz wird Ihr Geld angelegt?\n"))
        print(f'Sie müssen Ihr Startkapital von {k0}€ bei einem Prozentsatz von {p}% {log10(kt / k0) / log10(1 + p / 100)} Jahre anlegen, um Ihr Wunschkapital von {kt}€ zu erreichen')
        
# Aufgabe 7
def primZahlTester():
    zahl = int(input("Gib die zu prüfende Zahl ein:"))
    isPrim = True
    for i in range(2, (zahl - 1)):
        if zahl % i == 0:
            isPrim = False
            break
    print(f'Deine Zahl ({zahl}) ist {"eine" if isPrim else "keine"} Primzahl')