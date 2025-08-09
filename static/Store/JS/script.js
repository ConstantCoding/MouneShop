let scrollContainer = document.querySelector(".gallery")
let btq_nav = document.querySelector(".btq_nav")
let navbar = document.querySelector(".navbar")

let backBtn = document.getElementById("backBtn")
let nextBtn = document.getElementById("nextBtn")
let back = document.getElementById("back")
let next = document.getElementById("next")
let w_container = document.querySelector(".w-wrapper")
let back2 = document.querySelector(".b1")
let next2 = document.querySelector(".b2")
let w_container2 = document.getElementById("w2")
let lastScrollTop = 0

nextBtn.addEventListener("click", ()=>{
    scrollContainer.style.scrollBehavior = "smooth"
    scrollContainer.scrollLeft += 150
})
backBtn.addEventListener("click", ()=>{
    scrollContainer.style.scrollBehavior = "smooth"
    scrollContainer.scrollLeft -= 150
})


next.addEventListener("click", ()=>{
    w_container.style.scrollBehavior = "smooth"
    w_container.scrollLeft += 200
})
back.addEventListener("click", ()=>{
    w_container.style.scrollBehavior = "smooth"
    w_container.scrollLeft -= 200
})
next2.addEventListener("click", ()=>{
    w_container2.style.scrollBehavior = "smooth"
    w_container2.scrollLeft += 200
})
back2.addEventListener("click", ()=>{
    w_container2.style.scrollBehavior = "smooth"
    w_container2.scrollLeft -= 200
})