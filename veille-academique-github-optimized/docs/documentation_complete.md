# 🎯 Système de Veille Académique - Documentation Complète

## Vue d'Ensemble

Le **Système de Veille Académique** est une solution complète et automatisée pour surveiller les offres d'emploi académique dans le domaine des sciences humaines et sociales appliquées aux technologies, avec une spécialisation sur les cryptomonnaies, la blockchain, la gouvernance algorithmique et les Science & Technology Studies (STS).

### 🎯 Objectifs

- **Automatiser** la recherche d'offres d'emploi sur 40+ plateformes académiques
- **Filtrer intelligemment** les résultats selon vos mots-clés spécialisés
- **Centraliser** toutes les informations dans une interface moderne
- **Sauvegarder** automatiquement sur Google Drive pour la persistance
- **Alerter** en temps réel sur les nouvelles opportunités pertinentes

### 🏗️ Architecture du Système

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (React)                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐│
│  │   Dashboard     │ │   Recherche     │ │  Configuration  ││
│  │   Statistiques  │ │   Filtrage      │ │   Alertes       ││
│  └─────────────────┘ └─────────────────┘ └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              │ API REST
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND (Flask)                          │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐│
│  │   Scraping      │ │   Google Auth   │ │   Base de       ││
│  │   Multi-sources │ │   Google Drive  │ │   Données       ││
│  └─────────────────┘ └─────────────────┘ └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                 MODULES DE SCRAPING                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐│
│  │   Academic      │ │   Euraxess      │ │   Selenium      ││
│  │   Positions     │ │   H-Net         │ │   (Galaxie)     ││
│  └─────────────────┘ └─────────────────┘ └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## 📁 Structure des Fichiers

### Répertoire Principal : `/home/ubuntu/`

```
veille_academique/                    # 🐍 Modules Python de scraping
├── config.py                        # Configuration générale
├── scraper.py                       # Module principal de scraping
└── specialized_scrapers.py          # Scrapers spécialisés

veille-academique-frontend/          # ⚛️ Interface React
├── src/
│   ├── App.jsx                      # Interface principale
│   ├── App.css                      # Styles personnalisés
│   └── components/ui/               # Composants UI
├── package.json                     # Dépendances React
└── index.html                       # Page HTML principale

veille-academique-backend/           # 🌐 API Flask
├── src/
│   ├── main.py                      # Serveur principal
│   ├── routes/
│   │   ├── scraping.py             # Routes de scraping
│   │   └── google_auth.py          # Authentification Google
│   └── models/                      # Modèles de données
├── venv/                           # Environnement virtuel Python
└── requirements.txt                # Dépendances Python
```

## 🔧 Technologies Utilisées

### Frontend
- **React 18** - Framework JavaScript moderne
- **Tailwind CSS** - Framework CSS utilitaire
- **shadcn/ui** - Composants UI élégants
- **Framer Motion** - Animations fluides
- **Lucide Icons** - Icônes modernes

### Backend
- **Flask** - Framework web Python
- **SQLite** - Base de données locale
- **Google APIs** - Authentification et Drive
- **Flask-CORS** - Communication cross-origin

### Scraping
- **Requests** - Requêtes HTTP
- **BeautifulSoup4** - Parsing HTML
- **Selenium** - Sites JavaScript complexes
- **Pandas** - Manipulation de données

## 🎯 Sources de Données Configurées

### Plateformes Principales (10)
1. **Galaxie/Antares** (France) - Postes enseignants-chercheurs
2. **Academic Positions EU** - Postes européens
3. **Euraxess** - Réseau européen de recherche
4. **Jobs.ac.uk** - Postes académiques UK
5. **H-Net Job Guide** - Sciences humaines internationales
6. **Chronicle of Higher Education** - Postes US
7. **AcademicJobsOnline.org** - Plateforme académique US
8. **THEunijobs** - Times Higher Education
9. **HigherEdJobs** - Postes enseignement supérieur
10. **APEC** - Cadres France

### Écoles d'Ingénieurs (8)
- Mines ParisTech, Télécom Paris, INSA Lyon
- UTC, CentraleSupélec, Polytechnique
- ENPC, ENSAE

### Laboratoires STS Spécialisés (16)
- IFRIS, CSI Mines Paris, LATTS, CEMS
- Médialab Sciences Po, CITE CNAM
- ETH Zurich STS, Utrecht Data School
- Weizenbaum Institut, CNRS SHS, EHESS
- Et 5 autres laboratoires spécialisés

### Réseaux Académiques (8)
- Academia.net, ResearchGate Jobs
- Nature Careers, Science Careers
- VersatilePhD, PostdocJobs
- Academic Transfer, University World News

**Total : 42 sources surveillées automatiquement**



## 🔍 Mots-Clés de Recherche Configurés

### Cryptomonnaies et Blockchain (6)
- `crypto`, `cryptocurrency`, `cryptomonnaie`, `cryptomonnaies`
- `blockchain`, `bitcoin`, `ethereum`, `web3`, `defi`
- `smart contract`, `contrat intelligent`, `token`, `nft`

### Gouvernance et Infrastructure (10)
- `gouvernance`, `governance`, `algorithmic governance`
- `gouvernance algorithmique`, `infrastructure numérique`
- `digital infrastructure`, `infrastructure digitale`
- `dao`, `daos`, `decentralized`, `décentralisé`
- `polycentric governance`, `gouvernance polycentrique`

### Disciplines Académiques (16)
- `science technology studies`, `sts`, `sciences techniques société`
- `digital political economy`, `économie politique numérique`
- `critical data studies`, `études critiques des données`
- `money as institution`, `monnaie institution`
- `sociologie des crises`, `sociology of crisis`
- `institutionnalisme`, `économie politique critique`
- `critical political economy`

### Types de Postes (10)
- `maître de conférences`, `maitre de conferences`, `mcf`
- `professeur junior`, `professeur assistant`
- `assistant professor`, `associate professor`, `senior lecturer`
- `chercheur cnrs`, `chercheur inria`, `chercheur ifris`
- `post-doc senior`, `postdoc senior`, `senior postdoc`
- `responsable de programme`, `responsable de chaire`
- `chercheur invité`, `visiting researcher`, `visiting scholar`
- `fellow`, `research fellow`, `senior fellow`

**Total : 42 mots-clés surveillés**

## 🎨 Fonctionnalités de l'Interface

### 📊 Tableau de Bord Principal
- **Statistiques en temps réel** : Total scrapé, offres pertinentes, sources actives
- **Dernière mise à jour** : Horodatage de la dernière exécution
- **Métriques visuelles** : Cartes colorées avec animations

### 🔍 Recherche et Filtrage
- **Recherche instantanée** : Filtrage en temps réel par titre, institution, mots-clés
- **Tri par pertinence** : Score automatique basé sur les mots-clés
- **Filtres avancés** : Par source, date, score minimum

### 📋 Affichage des Offres
- **Cartes détaillées** : Titre, institution, localisation, date limite
- **Score de pertinence** : Indicateur visuel coloré (vert/jaune/orange)
- **Mots-clés correspondants** : Badges colorés des termes trouvés
- **Informations complètes** : Source, enseignement, langue, date de découverte
- **Liens directs** : Accès direct aux offres originales

### ⚙️ Configuration
- **Mots-clés personnalisables** : Ajout/suppression de termes de recherche
- **Fréquence de scraping** : Configuration des intervalles automatiques
- **Alertes email** : Notifications pour offres haute pertinence
- **Sources actives** : Activation/désactivation des plateformes

### 🔄 Scraping Automatisé
- **Lancement manuel** : Bouton avec animation de progression
- **Scraping programmé** : Exécution quotidienne automatique
- **Suivi en temps réel** : Barre de progression et source en cours
- **Gestion d'erreurs** : Retry automatique et logging détaillé

## 🔐 Authentification et Persistance

### Google Sign-In
- **Connexion sécurisée** : OAuth2 avec Google
- **Profil utilisateur** : Récupération des informations de base
- **Sessions persistantes** : Maintien de la connexion

### Google Drive Integration
- **Sauvegarde automatique** : Résultats stockés dans dossier dédié
- **Historique complet** : Conservation de tous les scrapings
- **Synchronisation** : Accès depuis n'importe quel appareil
- **Formats multiples** : JSON, CSV, Excel

## 🚀 Système de Scoring Intelligent

### Calcul de Pertinence
```python
Score = Σ(poids_mot_clé × présence) + bonus_type_poste

Pondération :
- Mots-clés très spécifiques (crypto, blockchain) : 0.3
- Mots-clés importants (gouvernance, STS) : 0.2  
- Autres mots-clés : 0.1
- Types de postes recherchés : 0.1
```

### Classification Automatique
- **🟢 Score ≥ 0.8** : Très pertinent (priorité haute)
- **🟡 Score 0.6-0.8** : Pertinent (priorité moyenne)
- **🟠 Score < 0.6** : Peu pertinent (priorité basse)

## 📈 Gestion des Performances

### Rate Limiting Intelligent
- **Délais aléatoires** : 2-5 secondes entre requêtes
- **Rotation User-Agents** : Évitement de la détection
- **Retry automatique** : 3 tentatives en cas d'échec
- **Délai d'erreur** : 10 secondes après échec

### Optimisations
- **Scraping parallèle** : Traitement simultané des sources
- **Cache intelligent** : Évitement des doublons
- **Filtrage précoce** : Élimination rapide des non-pertinents
- **Compression données** : Stockage optimisé

## 🔧 Configuration Technique

### Variables d'Environnement
```bash
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
FLASK_SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db
```

### Ports et Services
- **Frontend React** : http://localhost:5173
- **Backend Flask** : http://localhost:5000
- **API Endpoints** : /api/health, /api/scraping/*, /api/auth/*

### Dépendances Principales
```
Frontend : React 18, Tailwind CSS, Framer Motion
Backend  : Flask 3.1, SQLAlchemy, Google APIs
Scraping : Requests, BeautifulSoup4, Selenium
```

