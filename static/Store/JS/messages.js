document.addEventListener("DOMContentLoaded", function(){
    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(function(alert){
        setTimeout(function(){
            alert.style.transition = "opacity 1s ease-out";
            alert.style.opacity = "0";

        setTimeout(()=> {
            alert.remove();
        }, 1000)
        }, 4000)
    });
});