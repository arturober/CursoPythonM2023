"""Clase DAO para trabajar con Tareas"""
from dataclasses import dataclass
from sqlite3 import Connection
from modelo.tarea import Tarea


@dataclass
class TareaDAO:
    db: Connection

    @staticmethod
    def tarea_factory(cursor, row):
        return Tarea(row[0], row[1], bool(row[2]))

    def get_all(self) -> list[Tarea]:
        self.db.row_factory = (
            TareaDAO.tarea_factory
        )  # Nos devuelve resultados como tareas
        cursor = self.db.cursor()
        return cursor.execute("SELECT * FROM tarea").fetchall()

    def get(self, id: int) -> Tarea:
        self.db.row_factory = (
            TareaDAO.tarea_factory
        )  # Nos devuelve resultados como tareas
        cursor = self.db.cursor()
        return cursor.execute("SELECT * FROM tarea WHERE id = ?", (id,)).fetchone()

    def insert(self, tarea: Tarea) -> None:
        with self.db as db:  # Commit automático
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO tarea(descripcion, realizada) VALUES(?, ?)",
                (tarea.descripcion, tarea.realizada),
            )
            tarea.id = cursor.lastrowid  # Última id autogenerada

    def update(self, tarea: Tarea) -> None:
        with self.db as db:  # Commit automático
            cursor = db.cursor()
            cursor.execute(
                "UPDATE tarea SET descripcion = ?, realizada = ? WHERE id = ?",
                (tarea.descripcion, tarea.realizada),
            )

    def delete(self, id: int) -> None:
        with self.db as db:  # Commit automático
            cursor = db.cursor()
            cursor.execute(
                "DELETE FROM tarea WHERE id = ?",
                (id,),
            )
