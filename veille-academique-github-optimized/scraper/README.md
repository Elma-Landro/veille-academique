# 🔍 Scraper - Modules Python

## Description
Modules Python pour le scraping automatisé des sources académiques, avec gestion intelligente des erreurs et scoring de pertinence.

## 🔧 Installation

### Prérequis
- Python 3.11+
- Chrome/Chromium (pour Selenium)

### Étapes d'Installation
```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Installer ChromeDriver (automatique avec selenium)
# Ou télécharger manuellement depuis https://chromedriver.chromium.org/
```

## ⚙️ Configuration

### Fichier config.py
Personnaliser les paramètres :
```python
# Mots-clés de recherche
KEYWORDS = [
    "blockchain", "cryptocurrency", "governance",
    # Ajouter vos termes spécialisés
]

# Sources à scraper
SOURCES = {
    "academic_positions": {
        "url": "https://academicpositions.com",
        "active": True
    },
    # Ajouter vos sources
}

# Paramètres de scraping
SCRAPING_CONFIG = {
    "delay_between_requests": 2,  # secondes
    "max_retries": 3,
    "timeout": 30
}
```

## 🚀 Utilisation

### Scraping Basique
```bash
# Scraper toutes les sources
python scraper.py

# Scraper des sources spécifiques
python scraper.py --sources academic_positions euraxess

# Utiliser des mots-clés personnalisés
python scraper.py --keywords blockchain governance crypto
```

### Scraping Programmé
```python
from scraper import JobScraper

# Créer une instance
scraper = JobScraper()

# Lancer le scraping
results = scraper.scrape_all_sources()

# Sauvegarder les résultats
scraper.save_results(results, format='json')
```

## 📁 Structure

```
scraper/
├── config.py                    # Configuration principale
├── scraper.py                   # Scraper principal
├── specialized_scrapers.py      # Scrapers spécialisés
├── requirements.txt             # Dépendances Python
├── results/                     # Résultats de scraping
│   ├── jobs_YYYY-MM-DD.json    # Données JSON
│   └── jobs_YYYY-MM-DD.csv     # Export CSV
└── README.md                   # Cette documentation
```

## 🎯 Modules Principaux

### scraper.py
Classe principale `JobScraper` :
- Gestion des sources multiples
- Rate limiting automatique
- Scoring de pertinence
- Sauvegarde des résultats

### specialized_scrapers.py
Scrapers spécialisés pour :
- Academic Positions EU
- Euraxess
- Galaxie/Odyssée
- Sites d'écoles spécifiques

### config.py
Configuration centralisée :
- 54 sources académiques
- 42 mots-clés spécialisés
- Paramètres de scraping

## 🔍 Fonctionnalités Avancées

### Scoring de Pertinence
```python
def calculate_relevance_score(job_data, keywords):
    """
    Calcule un score de 0.0 à 1.0 basé sur :
    - Présence des mots-clés dans le titre
    - Correspondance avec la description
    - Réputation de l'institution
    """
    score = 0.0
    # Algorithme de scoring...
    return score
```

### Gestion des Erreurs
- Retry automatique en cas d'échec
- Logging détaillé des opérations
- Gestion des timeouts et rate limits
- Sauvegarde des erreurs pour debug

### Support Multi-Format
```python
# Sauvegarder en JSON
scraper.save_results(results, format='json')

# Sauvegarder en CSV
scraper.save_results(results, format='csv')

# Sauvegarder en base de données
scraper.save_to_database(results)
```

## 🔧 Personnalisation

### Ajouter une Nouvelle Source
1. Ajouter l'URL dans `config.py`
2. Créer un scraper spécialisé dans `specialized_scrapers.py`
3. Tester avec `python scraper.py --sources nouvelle_source`

### Modifier les Mots-Clés
```python
# Dans config.py
CUSTOM_KEYWORDS = [
    "votre_domaine_specifique",
    "technologie_emergente",
    "methodologie_recherche"
]
```

### Ajuster le Scoring
Modifier la fonction `calculate_relevance_score()` pour :
- Pondérer différemment les critères
- Ajouter de nouveaux facteurs
- Personnaliser pour votre domaine

## 📊 Résultats

### Format JSON
```json
{
  "title": "Postdoc in Blockchain Research",
  "institution": "KU Leuven",
  "location": "Belgium",
  "type": "Postdoc",
  "deadline": "2025-08-18",
  "url": "https://...",
  "relevance_score": 0.95,
  "keywords_found": ["blockchain", "governance"],
  "scraped_at": "2025-06-18T15:30:00Z"
}
```

### Statistiques
- Nombre total d'offres trouvées
- Répartition par type de poste
- Scores de pertinence moyens
- Sources les plus productives

## 🐛 Dépannage

### Erreur : "ChromeDriver not found"
```bash
# Installer ChromeDriver
pip install webdriver-manager
```

### Erreur : "Rate limited"
Augmenter le délai dans `config.py` :
```python
SCRAPING_CONFIG["delay_between_requests"] = 5
```

### Erreur : "Timeout"
Augmenter le timeout :
```python
SCRAPING_CONFIG["timeout"] = 60
```

## 📈 Performance

### Optimisations
- Scraping parallèle (avec prudence)
- Cache des résultats récents
- Scraping incrémental
- Filtrage précoce des résultats

### Monitoring
```bash
# Logs détaillés
python scraper.py --verbose

# Mode debug
python scraper.py --debug
```

