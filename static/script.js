const selectRaza = document.getElementById("raza");
const divResultado = document.getElementById("resultado");
const divHistorial = document.getElementById("historial");
const formulario = document.getElementById("formulario-perro");

  // Llenar el select con razas desde la Api

async function cargarRazas() {
  const respuesta = await fetch("/razas");
  const razas = await respuesta.json();

  razas.forEach(raza => {
    const opcion = document.createElement("option");
    opcion.value = raza;
    opcion.textContent = raza.charAt(0).toUpperCase() + raza.slice(1);
    selectRaza.appendChild(opcion);
  });
}

  // Obtener imagen desde la Api

async function obtenerImagenPerro(raza) {
  const url = raza ? `/perro?raza=${raza}` : "/perro";
  const respuesta = await fetch(url);
  const datos = await respuesta.json();
  return datos.imagen;
}

  // Manejar formulario

formulario.addEventListener("submit", async (e) => {
  e.preventDefault();
  const raza = selectRaza.value;
  const urlImagen = await obtenerImagenPerro(raza);

  // Mostrar resultado

  divResultado.innerHTML = `<h2>Resultado:</h2><img src="${urlImagen}" alt="Perro">`;

  // Guardar historial

  const imgHistorial = document.createElement("img");
  imgHistorial.src = urlImagen;
  imgHistorial.alt = "Historial perro";

  imgHistorial.addEventListener("click", () => {
    divResultado.innerHTML = `<h2>Resultado:</h2><img src="${imgHistorial.src}" alt="Perro">`;
  });

  divHistorial.prepend(imgHistorial);
});

// Cargar razas al inicio

cargarRazas();