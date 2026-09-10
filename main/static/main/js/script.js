document.addEventListener("DOMContentLoaded", function () {
    const password = document.getElementById("password");
    const togglePassword = document.getElementById("togglePassword");

    if (password && togglePassword) {
        togglePassword.addEventListener("click", function () {

            if (password.type === "password") {
                password.type = "text";
                togglePassword.classList.replace("fa-eye", "fa-eye-slash");
            } else {
                password.type = "password";
                togglePassword.classList.replace("fa-eye-slash", "fa-eye");
            }

        });
    }
    const confirmPassword = document.getElementById("confirmPassword");
    const toggleConfirmPassword = document.getElementById("toggleConfirmPassword");

    if (confirmPassword && toggleConfirmPassword) {
        toggleConfirmPassword.addEventListener("click", function () {

            if (confirmPassword.type === "password") {
                confirmPassword.type = "text";
                toggleConfirmPassword.classList.replace("fa-eye", "fa-eye-slash");
            } else {
                confirmPassword.type = "password";
                toggleConfirmPassword.classList.replace("fa-eye-slash", "fa-eye");
            }

        });
    }

});
const faqQuestions = document.querySelectorAll(".faq-question");

faqQuestions.forEach(question => {

    question.addEventListener("click", () => {

        const item = question.parentElement;

        item.classList.toggle("active");

    });

});
document.addEventListener("DOMContentLoaded", function () {

    const search = document.getElementById("destinationSearch");

    const cards = document.querySelectorAll(".destination-card");

    const noResults = document.getElementById("noResults");

    search.addEventListener("keyup", function () {

        const value = search.value.toLowerCase();

        let found = false;

        cards.forEach(card => {

            const country = card.querySelector("h2").textContent.toLowerCase();

            if (country.includes(value)) {

                card.style.display = "block";

                found = true;

            } else {

                card.style.display = "none";

            }

        });

        if (found) {

            noResults.style.display = "none";

        } else {

            noResults.style.display = "block";

        }

    });

});
document.querySelectorAll(".togglePassword").forEach(icon => {
    icon.addEventListener("click", function () {

        const input = this.previousElementSibling;

        if (input.type === "password") {
            input.type = "text";
            this.classList.replace("fa-eye", "fa-eye-slash");
        } else {
            input.type = "password";
            this.classList.replace("fa-eye-slash", "fa-eye");
        }

    });
});
document.addEventListener("DOMContentLoaded", function () {

    const menuToggle = document.getElementById("menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (menuToggle && navLinks) {

        menuToggle.addEventListener("click", function () {

            navLinks.classList.toggle("mobile-menu-open");

            const isOpen = navLinks.classList.contains("mobile-menu-open");

            menuToggle.setAttribute("aria-expanded", isOpen);

            if (isOpen) {
                menuToggle.innerHTML = '<i class="fa-solid fa-xmark"></i>';
            } else {
                menuToggle.innerHTML = '<i class="fa-solid fa-bars"></i>';
            }

        });

    }

});