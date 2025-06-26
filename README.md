# 🎯 Système de Veille Académique

> **Automatisation intelligente de la recherche d'emplois académiques en sciences humaines et sociales appliquées aux technologies**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/react-18.0+-blue.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/flask-3.0+-blue.svg)](https://flask.palletsprojects.com/)

## 📋 Description

Système automatisé de veille académique spécialement conçu pour les chercheurs en **sciences humaines et sociales** (économie, sociologie, ethnographie) travaillant sur les **technologies émergentes** (blockchain, cryptomonnaies, gouvernance algorithmique).

### 🎯 Fonctionnalités Principales

- **🔍 Scraping Intelligent** : Surveillance automatique de 54+ sources académiques
- **🎯 Scoring de Pertinence** : Algorithme de matching basé sur 42 mots-clés spécialisés
- **🌐 Interface Moderne** : Dashboard React avec recherche temps réel
- **🔗 Intégration Cloud** : Sauvegarde Google Drive et authentification
- **📊 Analyse Avancée** : Tendances du marché et recommandations stratégiques

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.11+
- Node.js 18+
- Git

### Installation

```bash
# 1. Cloner le repository
git clone https://github.com/votre-username/veille-academique.git
cd veille-academique

# 2. Backend (API Flask)
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 3. Frontend (Interface React)
cd ../frontend
npm install

# 4. Scraper (Modules Python)
cd ../scraper
pip install -r requirements.txt
```

### Lancement

```bash
# Terminal 1 - Backend
cd backend && source venv/bin/activate && python src/main.py

# Terminal 2 - Frontend
cd frontend && npm run dev

# Terminal 3 - Scraper (optionnel)
cd scraper && python scraper.py
```

Accédez à l'interface : `http://localhost:5173`

## 📁 Structure du Projet

```
veille-academique/
├── backend/          # API Flask + routes
├── frontend/         # Interface React
├── scraper/          # Modules de scraping Python
├── docs/            # Documentation
└── README.md        # Ce fichier
```

## 🎯 Sources Surveillées

### Plateformes Principales
- **Academic Positions EU** - Offres européennes
- **Jobs.ac.uk** - Royaume-Uni
- **Euraxess** - Réseau européen de recherche
- **Galaxie/Odyssée** - France (MCF/PR)

### Institutions Spécialisées
- **Sciences Po** (Médialab)
- **EHESS** (Anthropologie économique)
- **CNRS** (SHS)
- **Max Planck Institute** (Sciences sociales)

## 🔧 Configuration

### Mots-clés de Recherche
Le système utilise 42 mots-clés optimisés pour votre profil :

**Domaines SHS :**
- economics, sociology, anthropology, ethnography
- political economy, economic anthropology
- digital humanities, science technology studies

**Technologies :**
- blockchain, cryptocurrency, bitcoin, ethereum
- digital governance, algorithmic governance
- fintech, digital money, central bank digital currency

[Configuration complète](scraper/config.py)

## 📊 Utilisation

### Interface Web
1. **Dashboard** : Vue d'ensemble des offres trouvées
2. **Recherche** : Filtrage par mots-clés, localisation, date
3. **Scoring** : Pertinence automatique (0.0-1.0)
4. **Export** : CSV, JSON, PDF

### API REST
```bash
# Lancer un scraping
curl -X POST http://localhost:5000/api/scraping/start

# Récupérer les résultats
curl http://localhost:5000/api/jobs

# Statistiques
curl http://localhost:5000/api/stats
```

## 🤝 Contribution

Ce projet est sous licence **GPL v3** - Logiciel libre et copyleft.

### Comment Contribuer
1. Fork le projet
2. Créer une branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit (`git commit -m 'Ajout nouvelle fonctionnalité'`)
4. Push (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence GPL v3. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

**Logiciel libre et copyleft** - Toute modification ou redistribution doit rester sous GPL v3.

## 🆘 Support

- **Issues** : [GitHub Issues](https://github.com/votre-username/veille-academique/issues)
- **Discussions** : [GitHub Discussions](https://github.com/votre-username/veille-academique/discussions)

## 🏆 Auteurs

- **Développement initial** : Manus AI
- **Conception SHS** : Spécialisé pour économie/sociologie/ethnographie + blockchain

---

*Système de veille académique spécialisé pour les chercheurs SHS travaillant sur les technologies émergentes*

