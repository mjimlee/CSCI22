const user = document.getElementById("js_user_info");
const popup = document.getElementById("js_user_items_popup");

user.addEventListener('click', function() {
    popup.classList.toggle("active");
});