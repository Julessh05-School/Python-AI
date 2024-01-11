"""Stacks"""
# Stacks werden durch Listen bzw. Arrays repräsentiert.
# Ein Stack besitzt eine abstrakte Datenstruktur.
# Es gilt hier das LIFD-Prinzip (Last-In-First-Out).

# Initialisierung eines leeren Stapels
stack = []

# Push: Hinzufügen eines Elements zum Stack
stack.append(22)
stack.append(0)
stack.append(184)
stack.append(33)
stack.append(89)

# Pop: Entnehmen und Entfernen des obersten Elements
element = stack.pop()

# Peek oder Top: Entnehmen ohne Entfernen des obersten Elements
peek = stack[-1]

# isEmpty: Überprüfen ob der Stack leer ist
leer = len(stack) == 0
