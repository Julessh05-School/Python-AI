import turtle


def new_abbruch(a):
    return a + 1


def new_counter(c):
    return c + 1


def draw_next_l(t, c, a):
    c = new_counter(c)
    if c > 4:
        return
    a = new_abbruch(a)
    length = 100 / a
    t.left(135)
    t.forward(length / 2)
    t.right(90)
    t.forward(length)
    draw_next_l(t, c)
    t.right(90)
    t.forward(length)
    draw_next_l(t, c)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length / 2)


def draw_next_r(t, c, a):
    c = new_counter(c)
    if c > 4:
        return
    a = new_abbruch(a)
    length = 100 / a
    t.right(135)
    t.forward(length / 2)
    t.left(90)
    t.forward(length)
    draw_next_r(t, c)
    t.left(90)
    t.forward(length)
    draw_next_r(t, c)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length / 2)


def draw():
    counter = 0
    abbruch = 1
    t = turtle.Turtle()
    t.forward(50)
    t.left(90)
    t.forward(100)
    draw_next_r(t, counter, abbruch)
    t.left(90)
    t.forward(100)
    draw_next_l(t, counter, abbruch)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
