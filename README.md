# Flask QRCode Association

Une application web simple pour les associations permettant :
- La gestion sécurisée des membres via un système d’authentification
- L’enregistrement de nouveaux membres
- La génération automatique de QR codes uniques pour chaque membre
- L’accès à la fiche profil d’un membre en scannant son QR code

---

## 🔧 Fonctionnalités

- 🔐 Authentification avec gestion de sessions (login/mot de passe hashé)
- 📝 Formulaire d’inscription pour ajouter de nouveaux membres
- 🧾 Base de données SQLite pour stocker les utilisateurs et les membres
- 📇 QR code unique pour chaque membre redirigeant vers sa fiche profil
- 🔍 Affichage de la fiche membre lors du scan du QR code

---

## 📦 Stack technique

- [Flask](https://flask.palletsprojects.com/) — Framework web Python
- [SQLite](https://www.sqlite.org/index.html) — Base de données légère
- [Werkzeug Security](https://werkzeug.palletsprojects.com/) — Pour le hash des mots de passe
- [qrcode](https://pypi.org/project/qrcode/) — Génération d’images QR code
- [Bootstrap](https://getbootstrap.com/) (optionnel) — Pour une interface simple et responsive

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/tonpseudo/flask-qrcode-association.git
cd flask-qrcode-association
#2. Créer un environnement virtuel

python3 -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
#3. Installer les dépendances

pip install -r requirements.txt
#4. Lancer l’application

flask run
Accéder à http://127.0.0.1:5000

📁 Arborescence
cpp
Copier
Modifier
flask-qrcode-association/
│
├── app.py
├── models.py
├── auth.py
├── members.py
├── static/
│   └── qrcodes/
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── member_profile.html
├── requirements.txt
└── README.md
🔐 Sécurité
Les mots de passe sont hashés avec Werkzeug (bcrypt ou pbkdf2_sha256)

Les pages sensibles sont protégées via login requis

Chaque QR code contient une URL sécurisée de type /member/<uuid> (aucune info perso dans le QR)

Possibilité d’utiliser HTTPS + Auth Google pour production

✅ Exemple de flux
Un administrateur se connecte via /login

Il enregistre un nouveau membre via /register

Un QR code est généré et affiché

Ce QR code peut être scanné pour accéder à /member/<id> (profil public du membre)

📌 À faire
 Ajouter un rôle admin/utilisateur

 Interface d’édition/suppression de membres

 Téléchargement du QR code en PDF

 Ajout de vérification CSRF et meilleure gestion des erreurs

📝 Licence
Ce projet est open-source, sous licence MIT.










