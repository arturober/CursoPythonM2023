def info_punto(x, y):
    print(f"Coordenadas {x=}, {y=}")


info_punto(3, 10)  # Coordenadas x=3, y=10
info_punto(y=10, x=3)  # Coordenadas x=3, y=10


def info_punto_3d(x, y, z):
    print(f"Coordenadas {x=}, {y=}, {z=}")


info_punto_3d(4, 7, 2)
info_punto_3d(z=2, y=7, x=4)  # Coordenadas x=4, y=7, z=2
info_punto_3d(4, z=2, y=7)  # Coordenadas x=4, y=7, z=2

punto = {"x": 4, "y": 7, "z": 4}

info_punto_3d(**punto)  # Coordenadas x=4, y=7, z=2
info_punto_3d(punto['x'], punto['y'], punto["z"]) # Coordenadas x=4, y=7, z=2
