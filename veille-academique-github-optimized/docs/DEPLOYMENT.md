# 📦 Instructions de Déploiement GitHub

## 🚀 Étape 1 : Upload sur GitHub (Interface Web)

### Créer le Repository
1. **Aller sur GitHub.com** et se connecter
2. **Cliquer sur le bouton vert "New"** (ou "Nouveau")
3. **Nom du repository :** `veille-academique`
4. **Description :** `Système de veille automatisée pour postes académiques en STS/blockchain`
5. **Visibilité :** Public (recommandé) ou Private
6. **Cocher "Add a README file"** : ❌ NON (on a déjà le nôtre)
7. **Cliquer "Create repository"**

### Upload des Fichiers
1. **Sur la page du repository vide**, cliquer **"uploading an existing file"**
2. **Glisser-déposer** tous les fichiers du ZIP décompressé
3. **Ou cliquer "choose your files"** et sélectionner tous les fichiers
4. **Message de commit :** `Initial commit - Système de veille académique complet`
5. **Cliquer "Commit changes"**

## 🌐 Étape 2 : Activer GitHub Pages

### Configuration Pages
1. **Aller dans Settings** (onglet en haut du repository)
2. **Scroller jusqu'à "Pages"** (dans le menu de gauche)
3. **Source :** Deploy from a branch
4. **Branch :** main
5. **Folder :** / (root)
6. **Cliquer "Save"**

### Attendre le Déploiement
- ⏱️ **Temps d'attente :** 2-5 minutes
- 🔗 **URL finale :** `https://votre-username.github.io/veille-academique`
- ✅ **Vérification :** Un badge vert apparaîtra quand c'est prêt

## ⚙️ Étape 3 : Configuration Automatique

### GitHub Actions (Automatique)
Les workflows sont déjà configurés dans `.github/workflows/` :
- **deploy.yml :** Déploiement automatique à chaque push
- **tests.yml :** Tests automatiques du code

### Variables d'Environnement (Optionnel)
1. **Settings** > **Secrets and variables** > **Actions**
2. **Ajouter ces secrets** (si vous voulez Google Auth) :
   - `GOOGLE_CLIENT_ID` : Votre ID client Google
   - `GOOGLE_CLIENT_SECRET` : Votre secret client Google

## 🔧 Étape 4 : Développement Local

### Cloner pour Développement
```bash
# Cloner le repository
git clone https://github.com/votre-username/veille-academique.git
cd veille-academique

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python src/main.py

# Frontend (nouveau terminal)
cd frontend
npm install
npm run dev

# Scraper (nouveau terminal)
cd scraper
pip install -r requirements.txt
python scraper.py
```

## 📱 Étape 5 : Utilisation via Interface Web

### Modifications Simples
1. **Aller sur GitHub.com** > votre repository
2. **Naviguer vers le fichier** à modifier
3. **Cliquer sur l'icône crayon** (Edit this file)
4. **Faire vos modifications**
5. **Scroll en bas** > ajouter un message de commit
6. **Cliquer "Commit changes"**

### Ajouter de Nouveaux Fichiers
1. **Dans le repository**, cliquer **"Add file"** > **"Create new file"**
2. **Taper le nom** (avec extension, ex: `nouveau-fichier.md`)
3. **Ajouter le contenu**
4. **Commit** avec un message descriptif

## 🎯 Étape 6 : Déploiement Décentralisé (Optionnel)

### Préparation Swarm
```bash
# Build de production
cd frontend
npm run build

# Le dossier dist/ contient les fichiers à déployer
```

### Upload sur Swarm
1. **Installer Swarm CLI** ou utiliser une interface web
2. **Upload du dossier dist/**
3. **Récupérer le hash Swarm**
4. **Configurer ENS** (Ethereum Name Service) si souhaité

## 📊 Monitoring et Maintenance

### Vérifications Régulières
- ✅ **GitHub Actions** : Vérifier que les builds passent
- ✅ **GitHub Pages** : Tester l'URL publique
- ✅ **Issues** : Répondre aux problèmes signalés
- ✅ **Pull Requests** : Examiner les contributions

### Mises à Jour
1. **Modifier les fichiers** via l'interface web GitHub
2. **Ou cloner localement** pour des changements importants
3. **Les déploiements** se font automatiquement via GitHub Actions

## 🆘 Résolution de Problèmes

### Build Failed
1. **Aller dans Actions** (onglet du repository)
2. **Cliquer sur le build échoué**
3. **Examiner les logs d'erreur**
4. **Corriger le problème** et recommiter

### Pages Non Accessible
1. **Vérifier Settings** > **Pages** > que la source est bien configurée
2. **Attendre 5-10 minutes** après le premier déploiement
3. **Vérifier Actions** > que le déploiement s'est bien passé

### Erreurs de Dépendances
1. **Vérifier package.json** et **requirements.txt**
2. **S'assurer** que toutes les dépendances sont listées
3. **Tester localement** avant de pousser sur GitHub

---

🎉 **Félicitations ! Votre système de veille académique est maintenant déployé et accessible publiquement !**

