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
