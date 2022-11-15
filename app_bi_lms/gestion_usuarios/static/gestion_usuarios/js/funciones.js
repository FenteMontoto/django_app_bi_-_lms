let flecha_izq = document.getElementById("flecha_izquierda")
let flecha_der = document.getElementById("flecha_derecha")
let sidebar = document.getElementById("sidebar")
let linkitos = document.getElementById("linkitos_ul")


flecha_izq.addEventListener('click', () => {
    flecha_izq.style.visibility = 'hidden'
    flecha_der.style.visibility = 'visible'
    sidebar.style.width = "10vh"
    linkitos.style.display = "none"
});

flecha_der.addEventListener('click', () => {
    flecha_der.style.visibility = 'hidden'
    flecha_izq.style.visibility = 'visible'
    sidebar.style.width = "25%"
    linkitos.style.display = ""
});