import numpy as np

'''Listen'''

# Eine Liste ist eine geordnete Datenstruktur aus Elementen.
# Innerhalb der Programmierung werden Listen oft durch Arrays repräsentiert

# Initialisierung mit eckigen Klammern
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mit der numpy Bibliothek ist die Verarbeitung deutlich leistungsstärker
np_liste = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Es gibt veränderbare (mutable) und unveränderbare (immutable) Listen
tuple_liste = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  # Tupel (Tuple) entspricht immutable
np_tuple_liste = np.array((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

np_tuple_liste[0] = 100

# Listen können unterschiedliche Datentypen enthalten
liste = [1, 2.1, True, "Hallo"]
np_liste = np.array([1, 2.1, True, "Hallo"])

# Zugriff auf die Elemente in der Liste
# -1 bedeutet Zugriff auf das letzte Element
print(liste[-1])
print(np_liste[2])

# Prüfen der Anwesenheit eines Elements in der Liste mit dem In-Operator
if 1 in liste:
    print("1 ist in drin")
if 1 in np_liste:
    print("1 ist in np liste")

# Länge bzw. Dimension einer Liste abrufen
length = len(liste)
np_list_length = len(np_liste)
np_length = np.size(np_liste)

# Slicing ist der Zugriff auf Teile der Liste
print(liste[2:6])
print(np_liste[2:6])

for i in liste:
    print(i, end=' ')

for i in range(np.size(np_liste)):
    print(np_liste[i], end=' ')

# Verschachtelung von Listen zu mehrdimensionalen Arrays
vliste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_vliste = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Zugriff auf ein Element in einer Liste
print(np_vliste[0][0])
