
let textList = [];

// Fonction pour afficher/masquer les détails des projets
function toggleDetails(button) {
    const details = button.nextElementSibling;
    details.style.display = details.style.display === "block" ? "none" : "block";
    button.textContent = details.style.display === "block" ? "Masquer détails" : "Voir détails";
}

// Bouton pour télécharger le CV
document.getElementById("cv-button").addEventListener("click", () => {
    window.open("CV_Développeuse_Mareme.pdf", "_blank"); // Ton CV doit être placé dans le dossier du site
});

//----------------------- popup---------------------
let currentIndex = 0;
const images = document.querySelectorAll('.carousel-img');

function openPopup(button) {
    const popup = document.getElementById('popup');
    const title = button.getAttribute('data-title');
    const text = button.getAttribute('data-text');
    const imageList = button.getAttribute('data-images').split(',');

    popup.querySelector('.popup-text h3').textContent = title;
    popup.querySelector('.popup-text p').textContent = text;

    const imageContainer = popup.querySelector('.carousel-images');
    imageContainer.innerHTML = '';

    imageList.forEach((filename, i) => {
        const img = document.createElement('img');
        img.src = `imagesProjets/${filename.trim()}`;
        img.className = 'carousel-img' + (i === 0 ? ' active' : '');
        imageContainer.appendChild(img);
    });

    popup.style.display = 'flex';
    currentIndex = 0;

    const paginationContainer = popup.querySelector('.carousel-pagination');
    paginationContainer.innerHTML = '';

    imageList.forEach((_, i) => {
        const page = document.createElement('span');
        page.className = 'page-number' + (i === 0 ? ' active' : '');
        page.textContent = i + 1;
        page.onclick = () => goToImage(i);
        paginationContainer.appendChild(page);
    });

    // Récupération des texte pour chaque image
    textList = button.getAttribute('data-captions')?.split('|') || [];
    const caption = document.getElementById('carousel-text');
    caption.textContent = textList[0] || '';

}


function closePopup() {
    document.getElementById('popup').style.display = 'none';
}

// Fermer le popup si on clique en dehors du contenu
window.addEventListener('click', function (e) {
    const popup = document.getElementById('popup');
    const content = popup.querySelector('.popup-content');
    if (e.target === popup && !content.contains(e.target)) {
        closePopup();
    }
});


function updateCarousel() {
    const images = document.querySelectorAll('.carousel-img');
    images.forEach((img, i) => {
        img.classList.toggle('active', i === currentIndex);
    });

    const caption = document.getElementById('carousel-text');
    caption.textContent = textList[currentIndex] || '';
}


function nextImage() {
    const images = document.querySelectorAll('.carousel-img');
    currentIndex = (currentIndex + 1) % images.length;
    updateCarousel();
}

function prevImage() {
    const images = document.querySelectorAll('.carousel-img');
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateCarousel();
}

// défilement (glissement gauche=>droite)
let startX = 0;

document.getElementById('popup').addEventListener('touchstart', function (e) {
    startX = e.touches[0].clientX;
});

document.getElementById('popup').addEventListener('touchend', function (e) {
    const endX = e.changedTouches[0].clientX;
    const diff = startX - endX;

    if (Math.abs(diff) > 50) {
        if (diff > 0) {
            nextImage(); // swipe gauche → image suivante
        } else {
            prevImage(); // swipe droite → image précédente
        }
    }
});

function goToImage(index) {
    currentIndex = index;
    updateCarousel();
    updatePagination();
}

function updatePagination() {
    const pages = document.querySelectorAll('.page-number');
    pages.forEach((page, i) => {
        page.classList.toggle('active', i === currentIndex);
    });
}
// Fonction pour afficher/masquer les détails des projets
function toggleDetails(button) {
    const details = button.nextElementSibling;
    details.style.display = details.style.display === "block" ? "none" : "block";
    button.textContent = details.style.display === "block" ? "Masquer détails" : "Voir détails";
}

// Bouton pour télécharger le CV
document.getElementById("cv-button").addEventListener("click", () => {
    window.open("CV_Développeuse_Mareme.pdf", "_blank"); // Ton CV doit être placé dans le dossier du site
});

// --- NAVBAR responsive ---
const navToggle = document.getElementById("nav-toggle");
const navMenu = document.getElementById("nav-menu");

navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("active");
});

// --- Smooth scroll ---
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        document.querySelector(targetId).scrollIntoView({ behavior: 'smooth' });
        navMenu.classList.remove("active");
    });
});

// Feedback visuel du formulaire de contact
document.getElementById("contact-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const feedback = document.getElementById("form-feedback");
    feedback.textContent = "✅ Votre message a bien été envoyé ! Merci.";
    e.target.reset();
    setTimeout(() => {
        feedback.textContent = "";
    }, 4000);
});
