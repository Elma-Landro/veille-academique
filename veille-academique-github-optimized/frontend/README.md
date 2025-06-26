# 🌐 Frontend - Interface React

## Description
Interface utilisateur moderne et responsive pour le système de veille académique, développée avec React et Vite.

## 🔧 Installation

### Prérequis
- Node.js 20+
- npm ou yarn

### Étapes d'Installation
```bash
# 1. Installer les dépendances
npm install

# 2. Démarrer le serveur de développement
npm run dev
```

L'application sera accessible sur `http://localhost:5173`

## 🎨 Fonctionnalités

### 📊 Dashboard
- Statistiques en temps réel
- Graphiques de performance
- Indicateurs de santé du système

### 🔍 Recherche et Filtrage
- Recherche par mots-clés
- Filtres par institution, type de poste, localisation
- Tri par pertinence, date, deadline

### 📱 Design Responsive
- Compatible desktop, tablette, mobile
- Interface tactile optimisée
- Animations fluides

### 🔐 Authentification
- Connexion Google intégrée
- Gestion des sessions
- Profil utilisateur

## 📁 Structure

```
frontend/
├── src/
│   ├── App.jsx              # Composant principal
│   ├── App.css              # Styles globaux
│   ├── components/          # Composants réutilisables
│   │   ├── Dashboard.jsx    # Tableau de bord
│   │   ├── JobList.jsx      # Liste des offres
│   │   └── SearchBar.jsx    # Barre de recherche
│   └── utils/               # Utilitaires
├── public/                  # Fichiers statiques
├── package.json             # Dépendances Node.js
├── vite.config.js          # Configuration Vite
└── README.md               # Cette documentation
```

## 🎯 Composants Principaux

### App.jsx
Composant racine gérant :
- État global de l'application
- Navigation entre onglets
- Communication avec l'API backend

### Dashboard
- Affichage des statistiques
- Boutons d'action (lancer scraping)
- Indicateurs de statut

### JobList
- Liste paginée des offres
- Scores de pertinence
- Liens vers les offres originales

## 🔧 Configuration

### Variables d'Environnement
Créer un fichier `.env` :
```env
VITE_API_URL=http://localhost:5000
VITE_GOOGLE_CLIENT_ID=votre_client_id_google
```

### Personnalisation du Style
Modifier `src/App.css` pour :
- Couleurs du thème
- Polices et typographie
- Animations et transitions

## 🚀 Build et Déploiement

### Build de Production
```bash
npm run build
```

### Prévisualisation
```bash
npm run preview
```

### Déploiement GitHub Pages
```bash
# Build automatique via GitHub Actions
# Voir .github/workflows/deploy.yml
```

## 🔍 Développement

### Ajouter un Nouveau Composant
1. Créer le fichier dans `src/components/`
2. Importer dans `App.jsx`
3. Ajouter les styles dans `App.css`

### Intégration API
```javascript
// Exemple d'appel API
const response = await fetch(`${import.meta.env.VITE_API_URL}/api/scraping/results`);
const data = await response.json();
```

## 🐛 Dépannage

### Erreur : "Module not found"
```bash
npm install
```

### Erreur : "Port 5173 already in use"
Modifier `vite.config.js` :
```javascript
export default defineConfig({
  server: {
    port: 3000
  }
})
```

### Problème de CORS
Vérifier que le backend autorise les requêtes depuis `http://localhost:5173`

