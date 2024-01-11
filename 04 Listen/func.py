import random

import numpy as np


# Aufgabe 1
def aufgabe_eins():
    random_numbers = [0] * 100
    for i in range(len(random_numbers)):
        random_numbers[i] = (random.randint(0, 100))
    for number in random_numbers:
        if number > 90:
            print(number)


# Aufgabe 2
def aufgabe_zwei():
    # spielbrett = [[0, 0, 0, 0, 0]] * 5
    spielbrett = np.zeros(([5, 5]))
    counter = 5
    while counter > 0:
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if spielbrett[x][y] == 1:
            continue
        else:
            spielbrett[x][y] = 1
            print(spielbrett)
            counter -= 1
    print(spielbrett)

    while 1 in spielbrett:
        input_x = int(input("Eingabe x: "))
        input_y = int(input("Eingabe y: "))
        count_hits = 0
        if spielbrett[input_y][input_x] == 1:
            count_hits += 1
            spielbrett[input_y][input_x] = 2
            print(f'Getroffen! Glückwunsch der {count_hits} Treffer')
        elif spielbrett[input_x][input_y] == 2:
            print("Bereits getroffen")
        else:
            print("Daneben")

    print("Spiel beendet")


aufgabe_zwei()
