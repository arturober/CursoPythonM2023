"use strict";

const http = new Http();
const form = document.getElementById("formTarea");
const lista = document.getElementById("lista");

function addTareaLista(tarea) {
  const li = document.createElement("li");
  li.append(`${tarea.descripcion} (${(tarea.realizada ? "Realizada" : "No realizada")}) `);
  const btBorrar = document.createElement("button");
  btBorrar.append("Borrar");
  btBorrar.style.color = "red";
  btBorrar.addEventListener("click", (e) => {
    http.delete(`http://localhost:5000/tareas/${tarea.id}`).then(() => {
        li.remove();
    });
  });

  li.append(btBorrar);

  const btRealizar = document.createElement("button");
  btRealizar.append("Realizar");
  btRealizar.style.color = "green";
  btRealizar.addEventListener("click", e => {
    tarea.realizada = true;
    http.put(`http://localhost:5000/tareas/${tarea.id}`, tarea).then(tarea => {
        li.firstChild.textContent = `${tarea.descripcion} (${(tarea.realizada ? "Realizada" : "No realizada")}) `;
    });
  });
  li.append(btRealizar);
  lista.append(li);
}

http.get("http://localhost:5000/tareas").then((tareas) => {
  tareas.forEach((t) => {
    addTareaLista(t);
  });
});

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const tarea = {
    descripcion: form.descripcion.value,
    realizada: false,
  };

  http.post("http://localhost:5000/tareas", tarea).then((tarea) => {
    addTareaLista(tarea);
    form.descripcion.value = "";
  }).catch(error => {
    alert("Error al añadir tarea");
  });
});
