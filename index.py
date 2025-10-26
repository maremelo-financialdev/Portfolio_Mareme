from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
import smtplib
from email.message import EmailMessage
import os
import re
from functools import wraps
from datetime import datetime, timedelta

# Configuration Flask adaptée à ta structure
app = Flask(__name__, 
            template_folder='.',  # Templates à la racine
            static_folder='.',
            static_url_path='')

app.secret_key = os.environ.get('FLASK_SECRET', 'change_me_in_production')

# Simple rate limiting en mémoire
request_history = {}

def rate_limit(max_requests=5, window_seconds=3600):
    """Limiteur de requêtes simple"""
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            ip = request.remote_addr
            now = datetime.now()
            
            # Nettoyage des anciennes entrées
            if ip in request_history:
                request_history[ip] = [
                    req_time for req_time in request_history[ip]
                    if now - req_time < timedelta(seconds=window_seconds)
                ]
            else:
                request_history[ip] = []
            
            # Vérification limite
            if len(request_history[ip]) >= max_requests:
                flash("Trop de requêtes. Réessayez dans 1 heure.", "error")
                return redirect(url_for('home'))
            
            request_history[ip].append(now)
            return f(*args, **kwargs)
        return wrapped
    return decorator

# === ROUTES ===

@app.route("/")
def home():
    """Page d'accueil"""
    return render_template("index.html")

@app.route('/cv')
def cv():
    """Téléchargement du CV"""
    try:
        return send_from_directory('.', 'CV_Développeuse_Mareme.pdf')
    except FileNotFoundError:
        flash("CV non disponible.", "error")
        return redirect(url_for('home'))

@app.route('/contact', methods=['POST'])
@rate_limit(max_requests=5, window_seconds=3600)  # 5 emails/heure
def contact():
    """Traitement du formulaire de contact"""
    try:
        # Récupération et nettoyage des données
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        # ===== VALIDATION =====
        
        # Champs obligatoires
        if not all([name, email, message]):
            flash("Tous les champs sont obligatoires.", "error")
            return redirect(url_for('home'))
        
        # Validation nom (2-100 caractères, lettres et espaces)
        if len(name) < 2 or len(name) > 100:
            flash("Le nom doit contenir entre 2 et 100 caractères.", "error")
            return redirect(url_for('home'))
        
        # Validation email avec regex
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            flash("Email invalide.", "error")
            return redirect(url_for('home'))
        
        # Validation message (10-2000 caractères)
        if len(message) < 10:
            flash("Le message doit contenir au moins 10 caractères.", "error")
            return redirect(url_for('home'))
        
        if len(message) > 2000:
            flash("Le message est trop long (max 2000 caractères).", "error")
            return redirect(url_for('home'))
        
        # ===== CONFIGURATION SMTP =====
        
        SMTP_HOST = os.environ.get('SMTP_HOST')
        SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
        SMTP_USER = os.environ.get('SMTP_USER')
        SMTP_PASS = os.environ.get('SMTP_PASS')
        
        if not all([SMTP_HOST, SMTP_USER, SMTP_PASS]):
            flash("Service d'envoi non configuré (mode test).", "error")
            print("⚠️ Configuration SMTP manquante. Configurez les variables d'environnement.")
            return redirect(url_for('home'))
        
        # ===== CONSTRUCTION EMAIL =====
        
        email_msg = EmailMessage()
        email_msg['Subject'] = f'Portfolio Contact - {name}'
        email_msg['From'] = SMTP_USER
        email_msg['To'] = SMTP_USER
        email_msg['Reply-To'] = email  # Permet de répondre directement
        
        email_msg.set_content(
            f"Nouveau message depuis le portfolio\n\n"
            f"Nom : {name}\n"
            f"Email : {email}\n\n"
            f"Message :\n{message}\n\n"
            f"---\n"
            f"IP : {request.remote_addr}\n"
            f"Date : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        
        # ===== ENVOI SMTP =====
        
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(email_msg)
        
        print(f"✅ Email envoyé - De: {email}, IP: {request.remote_addr}")
        flash("✅ Message envoyé avec succès ! Merci pour votre message.", "success")
        return redirect(url_for('home'))
        
    except smtplib.SMTPAuthenticationError:
        print("❌ Erreur d'authentification SMTP - Vérifiez vos identifiants")
        flash("Erreur d'authentification email. Contactez l'administrateur.", "error")
        return redirect(url_for('home'))
        
    except smtplib.SMTPException as e:
        print(f"❌ Erreur SMTP: {str(e)}")
        flash("Erreur d'envoi. Veuillez réessayer plus tard.", "error")
        return redirect(url_for('home'))
        
    except Exception as e:
        print(f"❌ Erreur inattendue: {str(e)}")
        flash("Une erreur est survenue. Veuillez réessayer.", "error")
        return redirect(url_for('home'))

# ===== GESTIONNAIRES D'ERREURS =====

@app.errorhandler(404)
def not_found(e):
    flash("Page non trouvée.", "error")
    return redirect(url_for('home'))

@app.errorhandler(500)
def server_error(e):
    print(f"❌ Erreur 500: {str(e)}")
    flash("Erreur serveur. Veuillez réessayer.", "error")
    return redirect(url_for('home'))

# ===== LANCEMENT =====

if __name__ == "__main__":
    print("\n" + "="*50)
    print("Serveur Flask - Portfolio Mareme LO")
    print("="*50)
    print(f" URL: http://127.0.0.1:5000")
    print(f" SMTP configuré: {'✅' if os.environ.get('SMTP_USER') else '❌'}")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)