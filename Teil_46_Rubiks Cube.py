from ursina import *
from itertools import product


app = Ursina()


def update():
    print_on_screen("Proyecto Final: 'Cubo Rubik'",
                    scale=2, position=(-.3, .4))
    print_on_screen("El boton derecho del mouse permite manipular el cubo. \n El scroll permite ajustar el tamaño del cubo. \n w, e, r, permiten rotar las caras del cubo en el eje y "
                    "\n s, d, f, permiten rotar el eje x. \n x, c, v, permiten rotar el eje z.", scale=1, position=(-.3, -.3))


def eltern_kind_beziehung(achse, schicht):
    for w in würfel:
        w.position, w.rotation = round(w.world_position, 1), w.world_rotation
        w.parent = scene

    zentrum.rotation = 0

    for w in würfel:
        if eval(f'w.position.{achse}') == schicht:
            w.parent = zentrum


def input(key):
    if key not in rot_dict:
        return
    achse, schicht, winkel = rot_dict[key]
    eltern_kind_beziehung(achse, schicht)
    shift = held_keys['shift']
    eval(
        f'zentrum.animate_rotation_{achse} ({-winkel if shift else winkel}, duration = 0.01)')


window.borderless = False
window.size = (800, 800)
window.position = (200, 200)
EditorCamera()

zentrum = Entity()

rot_dict = {'w': ['y', 1, -90], 'e': ['y', 0, -90], 'r': ['y', -1, -90],
            's': ['x', -1, -90], 'd': ['x', 0, -90], 'f': ['x', 1, -90],
            'x': ['z', -1, 90], 'c': ['z', 0, 90], 'v': ['z', 1, 90]}

würfel = []
for pos in product((-1, 0, 1), repeat=3):
    würfel.append(Entity(model='Teil_46_model.obj',
                  texture='Teil_46_texture.png', position=pos, scale=0.5))

app.run()
