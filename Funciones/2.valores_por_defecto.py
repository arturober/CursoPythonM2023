def info_punto(x=1, y=1):
    print(f"Coordenadas {x=}, {y=}")


info_punto()  # Coordenadas x=1 (por defecto) y=1 (por defecto)
info_punto(6)  # Coordenadas x=6, y=1 (por defecto)
info_punto(4, 7)  # Coordenadas x=4, y=7
info_punto(y=9)  # Coordenadas x=1 (por defecto), y=9

# Ejercicio planteado

def precio_total(producto, precio, impuesto=0.21):
    print(f"{producto}: {precio*(1+impuesto)} euros")

precio_total("pan", 2, 0.05)
precio_total("pan", 2)
precio_total(precio=2, producto="pan")
