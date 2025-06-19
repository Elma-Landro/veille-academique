# 🎯 Système de Veille Académique

> **Automatisation intelligente de la recherche d'emplois académiques en sciences humaines et sociales appliquées aux technologies**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/React-18.0+-61DAFB.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000.svg)](https://flask.palletsprojects.com/)

## 📋 Description

Système complet de veille automatisée pour identifier les postes académiques (CDI, CDD, tenure track, chaire, post-docs) en sciences humaines et sociales appliquées aux technologies, avec un focus sur :

- **Cryptomonnaies et blockchain**
- **Gouvernance algorithmique** 
- **Infrastructures numériques**
- **Science & Technology Studies (STS)**
- **Économie politique critique**

## ✨ Fonctionnalités

### 🔍 Scraping Intelligent
- **54 sources** académiques surveillées automatiquement
- **42 mots-clés** spécialisés pour votre domaine
- **Scoring de pertinence** automatique (0.0-1.0)
- **Rate limiting** et gestion d'erreurs robuste

### 🌐 Interface Web Moderne
- **Dashboard** avec statistiques temps réel
- **Recherche et filtrage** des résultats
- **Design responsive** (desktop + mobile)
- **Authentification Google** intégrée

### ☁️ Intégration Cloud
- **Sauvegarde Google Drive** automatique
- **Alertes email** personnalisables
- **Export CSV/JSON** des résultats

### 🎯 Sources Surveillées

#### Plateformes Principales
- Academic Positions EU
- Euraxess
- Jobs.ac.uk
- H-Net Job Guide
- Chronicle of Higher Education

#### Institutions Françaises
- Galaxie/Odyssée
- APEC
- CNRS, EHESS, IFRIS
- Mines, Télécom, INSA, CentraleSupélec

#### Écoles de Commerce
- FNEGE, HEC, ESSEC, EDHEC
- EM Lyon, Audencia, SKEMA

## 🚀 Installation Rapide

### Prérequis
- Python 3.11+
- Node.js 20+
- Git

### 1. Cloner le Repository
```bash
git clone https://github.com/votre-username/veille-academique.git
cd veille-academique
```

### 2. Backend (Flask)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows
pip install -r requirements.txt
python src/main.py
```

### 3. Frontend (React)
```bash
cd frontend
npm install
npm run dev
```

### 4. Scraper (Python)
```bash
cd scraper
pip install -r requirements.txt
python scraper.py
```

## 📁 Structure du Projet

```
veille-academique/
├── 📂 backend/           # API Flask
│   ├── src/
│   │   ├── main.py       # Serveur principal
│   │   └── routes/       # Routes API
│   ├── requirements.txt
│   └── README.md
├── 📂 frontend/          # Interface React
│   ├── src/
│   │   ├── App.jsx       # Composant principal
│   │   └── components/   # Composants UI
│   ├── package.json
│   └── README.md
├── 📂 scraper/           # Modules Python
│   ├── config.py         # Configuration
│   ├── scraper.py        # Scraper principal
│   └── specialized_scrapers.py
├── 📂 docs/              # Documentation
├── 📂 assets/            # Images et ressources
└── 📂 .github/           # Workflows GitHub
```

## 🔧 Configuration

### Variables d'Environnement
Créer un fichier `.env` dans le dossier `backend/` :

```env
# Google API (optionnel)
GOOGLE_CLIENT_ID=votre_client_id
GOOGLE_CLIENT_SECRET=votre_client_secret

# Configuration scraping
SCRAPING_DELAY=2
MAX_RETRIES=3
```

### Personnalisation des Mots-Clés
Modifier `scraper/config.py` :

```python
KEYWORDS = [
    # Vos mots-clés spécialisés
    "blockchain", "cryptocurrency", "governance",
    # Ajouter vos termes
]
```

## 🎯 Utilisation

### Interface Web
1. Ouvrir http://localhost:5173
2. Cliquer sur "Lancer Scraping"
3. Consulter les résultats avec scores de pertinence
4. Exporter en CSV/JSON

### Ligne de Commande
```bash
cd scraper
python scraper.py --sources academic_positions euraxess --keywords blockchain governance
```

### API REST
```bash
# Lancer un scraping
curl -X POST http://localhost:5000/api/scraping/start

# Récupérer les résultats
curl http://localhost:5000/api/scraping/results
```

## 📊 Exemples de Résultats

Le système a trouvé ces **vraies offres** lors des tests :

### 🏆 KU Leuven - Postdoc Blockchain (Score: 0.95)
- **Domaines :** Blockchain, Ethereum, Web3
- **Publié :** 18 juin 2025
- **Deadline :** 18 août 2025
- **Contact :** tom.vancutsem@kuleuven.be

### 🏆 Mohammed VI Polytechnic - Cryptography (Score: 0.91)
- **Domaines :** Blockchain, Cryptographie quantique
- **Salaire :** 2000 USD/mois
- **Localisation :** Maroc

## 🤝 Contribution

### Pour les Débutants GitHub
1. **Fork** ce repository via l'interface web GitHub
2. **Modifier** les fichiers directement sur GitHub
3. **Créer une Pull Request** via l'interface web

### Développement Local
```bash
# Créer une branche
git checkout -b feature/nouvelle-fonctionnalite

# Faire vos modifications
git add .
git commit -m "Ajout nouvelle fonctionnalité"

# Pousser les changements
git push origin feature/nouvelle-fonctionnalite
```

## 📈 Déploiement

### GitHub Pages (Étape 1)
1. Aller dans **Settings** > **Pages**
2. Sélectionner **Source** : Deploy from a branch
3. Choisir **Branch** : main
4. Le site sera disponible sur `https://votre-username.github.io/veille-academique`

### Déploiement Décentralisé (Étape 2)
```bash
# Build pour production
cd frontend && npm run build

# Déployer sur Swarm (optionnel)
# Instructions détaillées dans docs/deployment.md
```

## 📚 Documentation

- [📖 Guide d'Installation Détaillé](docs/guide_installation.md)
- [👤 Guide d'Utilisation](docs/guide_utilisation.md)
- [🔧 Documentation Technique](docs/documentation_complete.md)
- [🧪 Rapport de Tests](docs/rapport_tests.md)

## 🐛 Résolution de Problèmes

### Erreurs Communes

**Erreur : "Module not found"**
```bash
# Réinstaller les dépendances
pip install -r requirements.txt
npm install
```

**Erreur : "Port already in use"**
```bash
# Changer le port dans la configuration
# Backend : modifier main.py ligne 15
# Frontend : modifier vite.config.js
```

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteurs

- **Développeur Principal** - Système de veille académique
- **Contributeurs** - Voir [CONTRIBUTORS.md](CONTRIBUTORS.md)

## 🙏 Remerciements

- **Academic Positions EU** pour l'API publique
- **Euraxess** pour les données européennes
- **Communauté STS** pour les retours et suggestions

---

⭐ **N'hésitez pas à mettre une étoile si ce projet vous aide dans votre recherche académique !**

