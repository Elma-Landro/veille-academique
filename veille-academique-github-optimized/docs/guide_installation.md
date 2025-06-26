# 🛠️ Guide d'Installation et de Déploiement
*Instructions détaillées étape par étape pour débutants*

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir :
- **Un ordinateur** avec Windows, Mac ou Linux
- **Une connexion internet** stable
- **Un navigateur web** moderne (Chrome, Firefox, Safari, Edge)
- **Un compte Google** (pour l'authentification et la sauvegarde)

## 🔧 Installation Locale (Développement)

### Étape 1 : Préparation de l'Environnement

#### Sur Windows
1. **Téléchargez Python 3.11** depuis https://python.org
2. **Installez Python** en cochant "Add to PATH"
3. **Téléchargez Node.js** depuis https://nodejs.org
4. **Installez Node.js** avec les paramètres par défaut

#### Sur Mac
1. **Ouvrez Terminal** (Applications > Utilitaires > Terminal)
2. **Installez Homebrew** : `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. **Installez Python** : `brew install python@3.11`
4. **Installez Node.js** : `brew install node`

#### Sur Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3.11-pip nodejs npm
```

### Étape 2 : Télécharger les Fichiers

#### Option A : Via GitHub (Recommandé)
1. **Allez sur GitHub** : https://github.com/votre-username/veille-academique
2. **Cliquez** sur le bouton vert "Code"
3. **Sélectionnez** "Download ZIP"
4. **Décompressez** le fichier dans un dossier de votre choix

#### Option B : Copie Manuelle
1. **Créez un dossier** `veille-academique` sur votre Bureau
2. **Copiez** tous les fichiers fournis dans ce dossier
3. **Respectez** la structure des dossiers

### Étape 3 : Installation du Backend (API)

1. **Ouvrez un terminal/invite de commandes**
2. **Naviguez** vers le dossier backend :
   ```bash
   cd chemin/vers/veille-academique-backend
   ```
3. **Créez un environnement virtuel** :
   ```bash
   python3.11 -m venv venv
   ```
4. **Activez l'environnement** :
   - Windows : `venv\Scripts\activate`
   - Mac/Linux : `source venv/bin/activate`
5. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

### Étape 4 : Installation du Frontend (Interface)

1. **Ouvrez un nouveau terminal**
2. **Naviguez** vers le dossier frontend :
   ```bash
   cd chemin/vers/veille-academique-frontend
   ```
3. **Installez les dépendances** :
   ```bash
   npm install
   ```

### Étape 5 : Configuration Google (Optionnel)

#### Créer un Projet Google Cloud
1. **Allez sur** https://console.cloud.google.com
2. **Créez un nouveau projet** : "Veille Académique"
3. **Activez les APIs** :
   - Google Drive API
   - Google+ API (pour l'authentification)

#### Obtenir les Clés
1. **Allez dans** "Identifiants" > "Créer des identifiants" > "ID client OAuth"
2. **Type d'application** : Application Web
3. **URI de redirection** : `http://localhost:5000/api/auth/google/callback`
4. **Notez** votre Client ID et Client Secret

#### Configuration des Variables
1. **Créez un fichier** `.env` dans le dossier backend
2. **Ajoutez** :
   ```
   GOOGLE_CLIENT_ID=votre-client-id
   GOOGLE_CLIENT_SECRET=votre-client-secret
   ```

## 🚀 Lancement du Système

### Démarrage Automatique (Recommandé)

#### Script de Démarrage Windows (`start.bat`)
```batch
@echo off
echo Démarrage du système de veille académique...

cd veille-academique-backend
call venv\Scripts\activate
start python src/main.py

cd ..\veille-academique-frontend
start npm run dev

echo Système démarré !
echo Frontend: http://localhost:5173
echo Backend: http://localhost:5000
pause
```

#### Script de Démarrage Mac/Linux (`start.sh`)
```bash
#!/bin/bash
echo "Démarrage du système de veille académique..."

# Démarrage du backend
cd veille-academique-backend
source venv/bin/activate
python src/main.py &

# Démarrage du frontend
cd ../veille-academique-frontend
npm run dev &

echo "Système démarré !"
echo "Frontend: http://localhost:5173"
echo "Backend: http://localhost:5000"
```

### Démarrage Manuel

#### Terminal 1 : Backend
```bash
cd veille-academique-backend
source venv/bin/activate  # ou venv\Scripts\activate sur Windows
python src/main.py
```

#### Terminal 2 : Frontend
```bash
cd veille-academique-frontend
npm run dev
```

### Vérification du Fonctionnement

1. **Ouvrez votre navigateur**
2. **Allez sur** http://localhost:5173
3. **Vérifiez** que l'interface se charge correctement
4. **Testez** le bouton "Lancer Scraping"

## 🌐 Déploiement en Production

### Option 1 : GitHub Pages + Netlify (Gratuit)

#### Préparation du Frontend
1. **Buildez l'application** :
   ```bash
   cd veille-academique-frontend
   npm run build
   ```
2. **Le dossier `dist/`** contient les fichiers à déployer

#### Déploiement sur Netlify
1. **Allez sur** https://netlify.com
2. **Créez un compte** gratuit
3. **Glissez-déposez** le dossier `dist/` sur Netlify
4. **Notez** l'URL fournie (ex: https://votre-app.netlify.app)

#### Déploiement du Backend sur Heroku
1. **Créez un compte** sur https://heroku.com
2. **Installez Heroku CLI**
3. **Créez une app** :
   ```bash
   heroku create votre-app-backend
   ```
4. **Déployez** :
   ```bash
   git add .
   git commit -m "Deploy backend"
   git push heroku main
   ```

### Option 2 : Serveur VPS (Avancé)

#### Prérequis
- **Serveur Linux** (Ubuntu 20.04+)
- **Nom de domaine** (optionnel)
- **Certificat SSL** (Let's Encrypt)

#### Installation sur Serveur
```bash
# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Installation des dépendances
sudo apt install python3.11 python3.11-pip nodejs npm nginx

# Clonage du projet
git clone https://github.com/votre-username/veille-academique.git
cd veille-academique

# Installation backend
cd veille-academique-backend
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Installation frontend
cd ../veille-academique-frontend
npm install
npm run build

# Configuration Nginx
sudo nano /etc/nginx/sites-available/veille-academique
```

#### Configuration Nginx
```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    # Frontend
    location / {
        root /path/to/veille-academique-frontend/dist;
        try_files $uri $uri/ /index.html;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### Service Systemd pour le Backend
```ini
[Unit]
Description=Veille Académique Backend
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/path/to/veille-academique-backend
Environment=PATH=/path/to/veille-academique-backend/venv/bin
ExecStart=/path/to/veille-academique-backend/venv/bin/python src/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### Option 3 : Déploiement Décentralisé (Blockchain)

#### Préparation pour IPFS/Swarm
1. **Buildez l'application** statique
2. **Optimisez** les fichiers pour le web décentralisé
3. **Configurez** les liens relatifs

#### Déploiement sur IPFS
```bash
# Installation IPFS
wget https://dist.ipfs.io/go-ipfs/v0.12.0/go-ipfs_v0.12.0_linux-amd64.tar.gz
tar -xvzf go-ipfs_v0.12.0_linux-amd64.tar.gz
sudo mv go-ipfs/ipfs /usr/local/bin/

# Initialisation
ipfs init

# Ajout du site
ipfs add -r dist/

# Publication
ipfs name publish <hash-retourné>
```

#### Configuration ENS (Ethereum Name Service)
1. **Achetez un domaine** .eth sur https://app.ens.domains
2. **Configurez** le record IPFS avec le hash de votre site
3. **Votre site** sera accessible via votre-domaine.eth

## 🔧 Maintenance et Mises à Jour

### Mise à Jour du Code

#### Via GitHub
1. **Téléchargez** la nouvelle version
2. **Remplacez** les fichiers existants
3. **Redémarrez** les services

#### Via Git (Avancé)
```bash
git pull origin main
cd veille-academique-backend
source venv/bin/activate
pip install -r requirements.txt

cd ../veille-academique-frontend
npm install
npm run build
```

### Sauvegarde des Données

#### Sauvegarde Locale
```bash
# Base de données
cp veille-academique-backend/src/database/app.db backup/

# Configuration
cp veille-academique-backend/.env backup/

# Logs
cp veille-academique-backend/*.log backup/
```

#### Sauvegarde Google Drive
- **Automatique** : via l'intégration Google Drive
- **Manuelle** : export des résultats depuis l'interface

### Monitoring et Logs

#### Vérification de Santé
- **Frontend** : http://localhost:5173
- **Backend** : http://localhost:5000/api/health

#### Logs d'Erreur
```bash
# Logs backend
tail -f veille-academique-backend/veille_academique.log

# Logs système (Linux)
sudo journalctl -u veille-academique -f
```

## 🆘 Dépannage Courant

### Problèmes d'Installation

#### "Python non trouvé"
- **Vérifiez** l'installation de Python
- **Ajoutez** Python au PATH système
- **Utilisez** `python3.11` au lieu de `python`

#### "npm non trouvé"
- **Réinstallez** Node.js
- **Redémarrez** votre terminal
- **Vérifiez** avec `node --version`

#### "Permission denied"
- **Linux/Mac** : utilisez `sudo` si nécessaire
- **Windows** : exécutez en tant qu'administrateur

### Problèmes de Fonctionnement

#### "Port déjà utilisé"
- **Changez** le port dans la configuration
- **Tuez** le processus existant :
  - Windows : `taskkill /f /im python.exe`
  - Mac/Linux : `pkill -f python`

#### "Erreur de connexion API"
- **Vérifiez** que le backend est démarré
- **Testez** http://localhost:5000/api/health
- **Redémarrez** les deux services

#### "Scraping ne fonctionne pas"
- **Vérifiez** votre connexion internet
- **Attendez** quelques minutes (sites lents)
- **Consultez** les logs d'erreur

## 📞 Support Technique

### Ressources Utiles
- **Documentation** : `documentation_complete.md`
- **Guide utilisateur** : `guide_utilisation.md`
- **Tests** : `rapport_tests.md`

### Informations Système
- **Version Python** : 3.11+
- **Version Node.js** : 18+
- **Navigateurs supportés** : Chrome 90+, Firefox 88+, Safari 14+

### Contact
- **GitHub Issues** : Pour signaler des bugs
- **Documentation** : Pour les questions techniques
- **Email** : support@veille-academique.com (si configuré)

---

**🎉 Installation Terminée !** Votre système de veille académique est maintenant opérationnel. Consultez le guide d'utilisation pour commencer à l'utiliser efficacement.

