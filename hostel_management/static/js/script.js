console.log("SSMR Hostel Management System Loaded");

// ======================================================
// DOM Ready
// ======================================================

document.addEventListener("DOMContentLoaded", function () {

    // ==========================================
    // Mobile Sidebar Toggle
    // ==========================================

    const menuToggle = document.getElementById("menuToggle");
    const sidebar = document.querySelector(".sidebar");
    const overlay = document.getElementById("sidebarOverlay");

    if (menuToggle && sidebar) {

        menuToggle.addEventListener("click", function () {

            sidebar.classList.toggle("active");

            if (overlay) {
                overlay.classList.toggle("active");
            }

        });

    }

    if (overlay && sidebar) {

        overlay.addEventListener("click", function () {

            sidebar.classList.remove("active");
            overlay.classList.remove("active");

        });

    }

    // ==========================================
    // Live Date & Time
    // ==========================================

    function updateDateTime() {

        const element = document.getElementById("liveDateTime");

        if (!element) return;

        const now = new Date();

        const date = now.toLocaleDateString("en-IN", {

            weekday: "long",
            day: "numeric",
            month: "short",
            year: "numeric"

        });

        const time = now.toLocaleTimeString("en-IN", {

            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit"

        });

        element.innerHTML = `${date} | ${time}`;

    }

    updateDateTime();

    setInterval(updateDateTime, 1000);

    // ==========================================
    // Counter Animation
    // ==========================================

    const counters = document.querySelectorAll(".counter");

    counters.forEach(function (counter) {

        const original = counter.innerText;

        const target = parseInt(original.replace(/[^\d]/g, ""));

        if (isNaN(target)) return;

        let current = 0;

        const increment = Math.max(1, Math.ceil(target / 80));

        function animate() {

            if (current < target) {

                current += increment;

                if (current > target) {

                    current = target;

                }

                if (original.includes("₹")) {

                    counter.innerHTML =
                        "₹ " + current.toLocaleString("en-IN");

                } else {

                    counter.innerHTML =
                        current.toLocaleString("en-IN");

                }

                requestAnimationFrame(animate);

            }

        }

        animate();

    });

    // ==========================================
    // Bootstrap Toast
    // ==========================================

    document.querySelectorAll(".autoToast").forEach(function (toastEl) {

        const toast = new bootstrap.Toast(toastEl, {

            delay: 3000

        });

        toast.show();

    });

    // ==========================================
    // Current Year
    // ==========================================

    const currentYear = document.getElementById("currentYear");

    if (currentYear) {

        currentYear.innerHTML = new Date().getFullYear();

    }

    // ==========================================
    // Student Photo Preview
    // ==========================================

    const photoInput = document.getElementById("id_photo");

    const preview = document.getElementById("previewImage");

    if (photoInput && preview) {

        photoInput.addEventListener("change", function (e) {

            const file = e.target.files[0];

            if (file) {

                preview.src = URL.createObjectURL(file);

                preview.classList.remove("d-none");

            }

        });

    }

});