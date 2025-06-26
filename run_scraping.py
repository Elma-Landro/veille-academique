
#!/usr/bin/env python3
"""
Script autonome pour le scraping académique.
Peut être utilisé avec Replit Scheduled Deployments.
"""

import sys
import os
import requests
import json
from datetime import datetime

# Ajouter le répertoire du scraper au path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scraper'))

def run_scheduled_scraping():
    """Lance un scraping programmé et envoie les résultats à l'API."""
    print(f"🚀 Début du scraping programmé - {datetime.now()}")
    
    try:
        # Import du scraper
        from scraper.scraper import JobScraper
        
        # Lancement du scraping
        scraper = JobScraper()
        results = scraper.run_full_scraping()
        
        print(f"✅ Scraping terminé: {results['stats']['total_scraped']} offres trouvées")
        
        # Optionnel: envoyer les résultats à l'API backend
        api_url = os.environ.get('API_URL', 'http://localhost:5000/api')
        try:
            response = requests.post(
                f"{api_url}/scraping/results/update",
                json=results['jobs'],
                timeout=30
            )
            if response.status_code == 200:
                print("📤 Résultats envoyés à l'API avec succès")
        except Exception as e:
            print(f"⚠️ Erreur lors de l'envoi à l'API: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du scraping: {e}")
        return False

if __name__ == "__main__":
    success = run_scheduled_scraping()
    sys.exit(0 if success else 1)
