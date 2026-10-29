document.addEventListener("DOMContentLoaded", function () {
    const galleryItems = Array.from(
        document.querySelectorAll(".gallery-item")
    );

    const lightbox = document.getElementById(
        "gallery-lightbox"
    );

    if (!lightbox || galleryItems.length === 0) {
        return;
    }

    const lightboxImage = lightbox.querySelector(
        ".gallery-lightbox-image"
    );

    const counter = lightbox.querySelector(
        ".gallery-counter"
    );

    const previousButton = lightbox.querySelector(
        ".gallery-previous"
    );

    const nextButton = lightbox.querySelector(
        ".gallery-next"
    );

    const closeButton = lightbox.querySelector(
        ".gallery-close"
    );

    let currentIndex = 0;
    let previouslyFocusedElement = null;
    let touchStartX = 0;
    let touchEndX = 0;

    function showImage(index) {
        if (index < 0) {
            currentIndex = galleryItems.length - 1;
        } else if (index >= galleryItems.length) {
            currentIndex = 0;
        } else {
            currentIndex = index;
        }

        const selectedItem = galleryItems[currentIndex];

        lightboxImage.src = selectedItem.dataset.gallerySrc;
        lightboxImage.alt = selectedItem.dataset.galleryAlt || "";

        counter.textContent =
            `${currentIndex + 1} / ${galleryItems.length}`;
    }

    function openGallery(index) {
        previouslyFocusedElement = document.activeElement;

        showImage(index);

        lightbox.classList.add("is-open");
        lightbox.setAttribute("aria-hidden", "false");

        document.body.classList.add("gallery-is-open");

        if (galleryItems.length === 1) {
            previousButton.hidden = true;
            nextButton.hidden = true;
        } else {
            previousButton.hidden = false;
            nextButton.hidden = false;
        }

        closeButton.focus();
    }

    function closeGallery() {
        lightbox.classList.remove("is-open");
        lightbox.setAttribute("aria-hidden", "true");

        document.body.classList.remove("gallery-is-open");

        lightboxImage.src = "";
        lightboxImage.alt = "";

        if (previouslyFocusedElement) {
            previouslyFocusedElement.focus();
        }
    }

    function showPreviousImage() {
        showImage(currentIndex - 1);
    }

    function showNextImage() {
        showImage(currentIndex + 1);
    }

    galleryItems.forEach(function (item, index) {
        item.addEventListener("click", function () {
            openGallery(index);
        });
    });

    previousButton.addEventListener(
        "click",
        showPreviousImage
    );

    nextButton.addEventListener(
        "click",
        showNextImage
    );

    closeButton.addEventListener(
        "click",
        closeGallery
    );

    lightbox.addEventListener("click", function (event) {
        if (event.target === lightbox) {
            closeGallery();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (!lightbox.classList.contains("is-open")) {
            return;
        }

        if (event.key === "Escape") {
            closeGallery();
        }

        if (event.key === "ArrowLeft") {
            showPreviousImage();
        }

        if (event.key === "ArrowRight") {
            showNextImage();
        }
    });

    lightbox.addEventListener(
        "touchstart",
        function (event) {
            touchStartX = event.changedTouches[0].screenX;
        },
        {
            passive: true,
        }
    );

    lightbox.addEventListener(
        "touchend",
        function (event) {
            touchEndX = event.changedTouches[0].screenX;

            const swipeDistance = touchEndX - touchStartX;
            const minimumSwipeDistance = 50;

            if (swipeDistance > minimumSwipeDistance) {
                showPreviousImage();
            }

            if (swipeDistance < -minimumSwipeDistance) {
                showNextImage();
            }
        },
        {
            passive: true,
        }
    );
});