# 💼 Portfolio - Mareme LO

---

## 🎯 À Propos

Portfolio moderne et interactif présentant mes projets en **data analysis** et **développement d'applications**. Site entièrement responsive avec animations CSS, carousel dynamique et formulaire de contact fonctionnel.

**Objectif** : Contrat d'apprentissage en Data Analysis / Développement (janvier 2026)

---

## 🛠 Technologies

**Frontend**
- HTML5 / CSS3 (Grid, Flexbox, Animations)
- JavaScript (Vanilla) : Carousel, Popup, Navigation responsive
- Materialize CSS

**Backend**
- Python 3.x
- Flask : Routes, Gestion emails (SMTP)

**Déploiement**
- GitHub Pages 

---

## ✨ Fonctionnalités

- ✅ **Header animé** avec photo et présentation
- ✅ **Section Projets** : Grille responsive avec popup/carousel d'images
- ✅ **Section Compétences** : Actuelles + Objectifs 2025
- ✅ **Formulaire Contact** : Backend Flask avec envoi d'emails
- ✅ **Navbar sticky** avec logo personnalisé
- ✅ **Menu burger** responsive
- ✅ **Smooth scroll** et animations CSS

---

## 📁 Structure du Projet

```
PORTEFEUILLE.CV - V1/
│
├── index.html              # Page principale
├── index.css               # Styles globaux
├── index.js                # Scripts (carousel, popup, navigation)
├── index.py                # Backend Flask
│
├── imagesProjets/          # Screenshots des projets
│   ├── P3_img1_accueil.png
│   ├── P3_img2_parametres.png
│   └── ...
│
├── mareme_logo_modern.svg  # Logo personnalisé
├── Photo_profil.jpg        # Photo de profil
├── CV_Développeuse_Mareme.pdf  # CV téléchargeable
└── README.md               # Documentation
```

---

## 🚀 Installation & Lancement

### 1. Cloner le projet
```bash
git clone https://github.com/maremelo-financialdev/portfolio.git
cd portfolio
```

### 2. Frontend (Simple)
```bash
# Ouvrir index.html dans le navigateur
# OU utiliser un serveur local :
python -m http.server 8000
# Accès : http://localhost:8000
```

## 🎨 Projets Présentés

| Projet | Stack | Description |
|--------|-------|-------------|
| **Calculs Financiers Photovoltaïque** | Excel, VBA | Outil d'analyse financière pour investissements énergétiques |
| **Portfolio Interactif** | HTML, CSS, JS, Flask | Site moderne avec animations et backend Python |
| **Application Facturation Web** | HTML, CSS, JS, Python, MySQL | Gestion clients/produits avec dashboard |
| **Application Facturation Excel** | Excel, VBA | Outil de facturation automatisé |
| **CV Web** | HTML, CSS, JS, Materialize | CV interactif en ligne |

---

## 📋 Code JavaScript - Fonctionnalités

### Carousel d'Images Dynamique
```javascript
// Gestion du carousel avec navigation tactile
function openPopup(button) {
    // Charge les images et captions dynamiquement
    // Pagination automatique
}

// Swipe mobile (gauche/droite)
popup.addEventListener('touchstart/touchend', handleSwipe);
```

### Navigation Responsive
```javascript
// Menu burger mobile
navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("active");
});

// Smooth scroll
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', smoothScroll);
});
```

### Formulaire Contact
```javascript
// Validation et feedback visuel
form.addEventListener("submit", (e) => {
    e.preventDefault();
    // Envoi au backend Flask
    feedback.textContent = "✅ Message envoyé !";
});
```

---

## 🗺 Roadmap

- [x] Structure HTML + CSS responsive
- [x] Animations et transitions
- [x] Carousel dynamique avec JS
- [x] Backend Flask + formulaire contact
- [x] Logo SVG personnalisé
- [ ] Mode sombre (dark mode)
- [ ] Variables CSS pour thème dynamique
- [ ] Optimisation SEO
- [ ] Progressive Web App (PWA)

---

## 📞 Contact

**Mareme LO**  
📧 [maremelo616@gmail.com](mailto:maremelo616@gmail.com)  
📱 +33 6 22 11 97 15  
💼 [LinkedIn](https://www.linkedin.com/in/mareme-lo-9013aa157)  
💻 [GitHub](https://github.com/maremelo-financialdev)

---

<div align="center">

**Fait avec ❤️ par Mareme LO**

⭐ Si ce projet vous plaît, n'hésitez pas à lui donner une étoile !

</div>