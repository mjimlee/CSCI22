const user = document.getElementById("js_user_info");
const popup = document.getElementById("js_user_items_popup");
    
user.addEventListener('click', function() {
    popup.classList.toggle("active");
});

const mobileIcon = document.getElementById("js_mobile_icon");
const mobileNavDisplay = document.getElementById("js_items");

mobileIcon.addEventListener('click', function() {
    mobileNavDisplay.classList.toggle("active");
});