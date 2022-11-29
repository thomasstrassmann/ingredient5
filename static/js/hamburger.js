/* Nav bar inspired by Miguel Nunez, source: https://www.youtube.com/watch?v=flItyHiDm7E) */

const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener('click', () =>{
hamburger.classList.toggle("active");
navMenu.classList.toggle("active");
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () =>{
hamburger.classList.remove("active");
navMenu.classList.remove("active");
}));