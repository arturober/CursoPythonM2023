class Jugador:
    def __init__(self, nombre, edad, sueldo) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__sueldo = sueldo

    def __repr__(self) -> str:
        return f"{self.__nombre} - {self.__edad} - {self.__sueldo}"


class Equipo:
    def __init__(self, nombre):
        self.__jugadores = []
        self.__nombre = nombre

    def add_jugadores(self, *jugadores):
        self.__jugadores.extend(jugadores)

    def __repr__(self) -> str:
        s = f"{self.__nombre}\nLista de jugadores:\n"
        for j in self.__jugadores:
            s += "\t" + str(j) + "\n"

        return s

    @property
    def num_jugadores(self):
        return len(self.__jugadores)

e = Equipo("Patata CF")
e.add_jugadores(
    Jugador("Juan", 43, 24000),
    Jugador("Fran", 45, 26000),
    Jugador("Carlos", 46, 18000),
    Jugador("Miguel", 37, 50000),
)

print(e.num_jugadores)

e.add_jugadores(Jugador("Pepito", 38, 30000))

print(e.num_jugadores)
