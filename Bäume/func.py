class Node:
    def __init__(self, value):
        self.l = None
        self.r = None
        self.head = value

    def is_left_empty(self):
        return self.l is None

    def is_right_empty(self):
        return self.r is None


# Passt das so?
def print_tree(w):
    if w is not None:
        print("Pre-order:")
        print(w.head)
        print_tree(w.r)
        print_tree(w.l)
        print("In-order:")
        print_tree(w.l)
        print(w.head)
        print_tree(w.r)
        print("Post-order:")
        print_tree(w.l)
        print_tree(w.r)
        print(w.head)


# Baum erzeugen
wurzel = Node(1)
wurzel.l = Node(2)
wurzel.r = Node(3)
wurzel.l.l = Node(4)
wurzel.l.r = Node(5)
wurzel.l.r.l = Node(6)

# Kind abfragen
print("Wurzel links leer?", wurzel.l.is_left_empty())
print("Wurzel rechts leer?", wurzel.r.is_right_empty())
print_tree(wurzel)
