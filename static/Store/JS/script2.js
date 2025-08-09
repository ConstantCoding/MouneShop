let scrollContainer = document.querySelector(".gallery")
let btq_nav = document.querySelector(".btq_nav")
let navbar = document.querySelector(".navbar")

let backBtn = document.getElementById("backBtn")
let nextBtn = document.getElementById("nextBtn")
let backBtn2 = document.querySelector(".b1")
let nextBtn2 = document.querySelector(".b2")
let backBtn3 = document.querySelector(".b3")
let nextBtn3 = document.querySelector(".b4")
let container = document.querySelector(".p-wrapper")
let container2 = document.querySelector(".t-wrapper")
let lastScrollTop = 0

nextBtn.addEventListener("click", ()=>{
    scrollContainer.style.scrollBehavior = "smooth"
    scrollContainer.scrollLeft += 200
})
backBtn.addEventListener("click", ()=>{
    scrollContainer.style.scrollBehavior = "smooth"
    scrollContainer.scrollLeft -= 200
})

nextBtn2.addEventListener("click", ()=>{
    container.style.scrollBehavior = "smooth"
    container.scrollLeft += 200
})
backBtn2.addEventListener("click", ()=>{
    container.style.scrollBehavior = "smooth"
    container.scrollLeft -= 200
})
nextBtn3.addEventListener("click", ()=>{
    container2.style.scrollBehavior = "smooth"
    container2.scrollLeft += 200
})
backBtn3.addEventListener("click", ()=>{
    container2.style.scrollBehavior = "smooth"
    container2.scrollLeft -= 200
})