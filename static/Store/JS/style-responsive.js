let menu_button = document.getElementById("menu")
let btn_boutique = document.querySelectorAll(".btq")
let compte_icon = document.getElementById("compte")
let box = document.querySelector(".box")

const croix = document.getElementById("croix")
const banner = document.querySelector(".banner")

menu_button.addEventListener("click", (event) => {
    event.preventDefault()
    banner.classList.add("ban-responsive")
})
croix.addEventListener("click", function (event) {
    event.preventDefault()
    banner.classList.remove("ban-responsive")
})

compte_icon.addEventListener("mouseover", ()=>{
    box.style.display = "block"
})
compte_icon.addEventListener("mouseout", ()=>{
    box.style.display = "none"
})