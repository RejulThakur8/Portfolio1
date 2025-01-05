const buttons = document.querySelector("#button");
let body = document.querySelector("body");

buttons.addEventListener("click", () => {
    if (body.classList.contains("dark-theme")){
        body.classList.remove("dark-theme");
        buttons.innerHTML = "Dark Mode";
    } else {
        currentmode = "light";
        body.classList.add("dark-theme");
        buttons.innerHTML = "Light Mode";
    }
    
});