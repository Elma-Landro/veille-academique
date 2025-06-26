# 🚀 Backend - API Flask

## Description
API REST pour le système de veille académique, gérant le scraping, l'authentification Google et la sauvegarde des données.

## 🔧 Installation

### Prérequis
- Python 3.11+
- pip

### Étapes d'Installation
```bash
# 1. Créer un environnement virtuel
python -m venv venv

# 2. Activer l'environnement
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Installer les dépendances
pip install -r requirements.txt
```

## ⚙️ Configuration

### Variables d'Environnement
Créer un fichier `.env` :
```env
GOOGLE_CLIENT_ID=votre_client_id_google
GOOGLE_CLIENT_SECRET=votre_client_secret_google
FLASK_ENV=development
FLASK_DEBUG=True
```

### Configuration Google API (Optionnel)
1. Aller sur [Google Cloud Console](https://console.cloud.google.com/)
2. Créer un nouveau projet
3. Activer l'API Google Drive
4. Créer des identifiants OAuth 2.0
5. Ajouter les clés dans `.env`

## 🚀 Démarrage

```bash
# Démarrer le serveur de développement
python src/main.py
```

Le serveur sera accessible sur `http://localhost:5000`

## 📡 API Endpoints

### Santé du Service
```http
GET /api/health
```

### Scraping
```http
POST /api/scraping/start
GET /api/scraping/results
GET /api/scraping/status
```

### Authentification Google
```http
POST /api/auth/google/login
POST /api/auth/google/logout
GET /api/auth/google/status
```

### Sauvegarde Google Drive
```http
POST /api/drive/save
GET /api/drive/list
```

## 📁 Structure

```
backend/
├── src/
│   ├── main.py              # Serveur Flask principal
│   └── routes/
│       ├── scraping.py      # Routes de scraping
│       └── google_auth.py   # Routes d'authentification
├── requirements.txt         # Dépendances Python
├── .env.example            # Exemple de configuration
└── README.md               # Cette documentation
```

## 🔍 Développement

### Ajouter une Nouvelle Route
1. Créer un fichier dans `src/routes/`
2. Définir les endpoints Flask
3. Importer dans `main.py`

### Tests
```bash
# Tester l'API
curl http://localhost:5000/api/health

# Tester le scraping
curl -X POST http://localhost:5000/api/scraping/start
```

## 🐛 Dépannage

### Erreur : "Module not found"
```bash
pip install -r requirements.txt
```

### Erreur : "Port 5000 already in use"
Modifier le port dans `main.py` :
```python
app.run(host='0.0.0.0', port=5001, debug=True)
```

