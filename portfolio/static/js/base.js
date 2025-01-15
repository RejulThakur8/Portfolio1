const buttons = document.querySelector("#button");
let body = document.querySelector("body");


if (localStorage.getItem("theme") === "dark") {
    body.classList.add("dark-theme");
    buttons.innerHTML = "Alice Mode";
} else {
    body.classList.remove("dark-theme");
    buttons.innerHTML = "Dark Mode";
}

buttons.addEventListener("click", () => {
    if (body.classList.contains("dark-theme")) {
        body.classList.remove("dark-theme");
        buttons.innerHTML = "Dark Mode";
        localStorage.setItem("theme", "light"); 
    } else {
        body.classList.add("dark-theme");
        buttons.innerHTML = "Alice Mode";
        localStorage.setItem("theme", "dark"); 
    }
    
});


const resume = document.querySelector("#btn").addEventListener('click', () => {
    alert("Resume is downloading!");
})