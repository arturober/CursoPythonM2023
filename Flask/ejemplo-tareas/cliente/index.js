"use strict";

const http = new Http();
const form = document.getElementById("formTarea");
const lista = document.getElementById("lista");

http.get("http://localhost:5000/tareas").then((tareas) => {
    tareas.forEach(t => {
        const li = document.createElement("li");
        li.append(t.descripcion);
        lista.append(li);
    });
});

form.addEventListener('submit', e => {
    e.preventDefault();
    const tarea = {
        descripcion: form.descripcion.value,
        realizada: false
    };

    http.post("http://localhost:5000/tareas", tarea).then(tarea => {
        const li = document.createElement("li");
        li.append(tarea.descripcion);
        lista.append(li);
    });
});
