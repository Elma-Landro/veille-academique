"""
Système de Veille Académique - Module Principal de Scraping
===========================================================

Ce module contient les classes et fonctions principales pour le scraping
automatisé des offres d'emploi académique sur les différentes plateformes.

Auteur: Assistant IA Manus
Date: Juin 2025
"""

import requests
from bs4 import BeautifulSoup
import time
import random
import json
import csv
from datetime import datetime, timedelta
import re
from urllib.parse import urljoin, urlparse
import logging
from typing import List, Dict, Optional, Tuple
import os

# Import de notre configuration
try:
    from .config import (
        MAIN_SOURCES, ENGINEERING_SCHOOLS, SPECIALIZED_SOURCES, ACADEMIC_NETWORKS,
        ALL_KEYWORDS, POSITION_TYPES, DEFAULT_HEADERS, REQUEST_DELAYS, MAX_RETRIES,
        REQUIRED_FIELDS
    )
except ImportError:
    from config import (
        MAIN_SOURCES, ENGINEERING_SCHOOLS, SPECIALIZED_SOURCES, ACADEMIC_NETWORKS,
        ALL_KEYWORDS, POSITION_TYPES, DEFAULT_HEADERS, REQUEST_DELAYS, MAX_RETRIES,
        REQUIRED_FIELDS
    )

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('veille_academique.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class JobScraper:
    """
    Classe principale pour le scraping des offres d'emploi académique.
    
    Cette classe gère :
    - Les requêtes HTTP avec gestion des erreurs et rate limiting
    - L'extraction et le parsing du contenu HTML
    - Le filtrage des résultats selon les mots-clés
    - La sauvegarde des données
    """
    
    def __init__(self):
        """Initialise le scraper avec les paramètres par défaut."""
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        self.results = []
        self.stats = {
            'total_scraped': 0,
            'total_relevant': 0,
            'sources_processed': 0,
            'errors': 0
        }
        
    def make_request(self, url: str, retries: int = MAX_RETRIES) -> Optional[requests.Response]:
        """
        Effectue une requête HTTP avec gestion des erreurs et rate limiting.
        
        Args:
            url: URL à requêter
            retries: Nombre de tentatives en cas d'échec
            
        Returns:
            Response object ou None en cas d'échec
        """
        for attempt in range(retries):
            try:
                # Délai aléatoire pour éviter la détection de bot
                delay = random.uniform(REQUEST_DELAYS['min_delay'], REQUEST_DELAYS['max_delay'])
                time.sleep(delay)
                
                logger.info(f"Requête vers {url} (tentative {attempt + 1}/{retries})")
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                
                return response
                
            except requests.exceptions.RequestException as e:
                logger.warning(f"Erreur lors de la requête vers {url}: {e}")
                if attempt < retries - 1:
                    time.sleep(REQUEST_DELAYS['error_delay'])
                else:
                    logger.error(f"Échec définitif pour {url} après {retries} tentatives")
                    self.stats['errors'] += 1
                    
        return None
    
    def calculate_relevance_score(self, text: str) -> Tuple[float, List[str]]:
        """
        Calcule un score de pertinence basé sur la présence de mots-clés.
        
        Args:
            text: Texte à analyser (titre + description du poste)
            
        Returns:
            Tuple (score, mots-clés trouvés)
        """
        text_lower = text.lower()
        found_keywords = []
        score = 0.0
        
        # Recherche des mots-clés avec pondération
        for keyword in ALL_KEYWORDS:
            if keyword.lower() in text_lower:
                found_keywords.append(keyword)
                # Pondération selon le type de mot-clé
                if keyword.lower() in ['crypto', 'blockchain', 'bitcoin', 'ethereum']:
                    score += 0.3  # Mots-clés très spécifiques
                elif keyword.lower() in ['gouvernance', 'governance', 'sts']:
                    score += 0.2  # Mots-clés importants
                else:
                    score += 0.1  # Autres mots-clés
        
        # Bonus pour les types de postes recherchés
        for position_type in POSITION_TYPES:
            if position_type.lower() in text_lower:
                score += 0.1
                break
                
        return min(score, 1.0), found_keywords
    
    def extract_job_info(self, job_element, source_name: str, base_url: str) -> Optional[Dict]:
        """
        Extrait les informations d'une offre d'emploi depuis un élément HTML.
        
        Args:
            job_element: Élément BeautifulSoup contenant l'offre
            source_name: Nom de la source (pour traçabilité)
            base_url: URL de base pour les liens relatifs
            
        Returns:
            Dictionnaire avec les informations extraites ou None
        """
        try:
            # Cette méthode sera spécialisée pour chaque source
            # Ici on définit la structure générale
            job_info = {
                'source': source_name,
                'found_date': datetime.now().isoformat(),
                'title': '',
                'institution': '',
                'url': '',
                'deadline': '',
                'keywords_match': [],
                'teaching': 'Unknown',
                'language': 'Unknown',
                'location': '',
                'description': '',
                'relevance_score': 0.0
            }
            
            return job_info
            
        except Exception as e:
            logger.error(f"Erreur lors de l'extraction pour {source_name}: {e}")
            return None
    
    def scrape_academic_positions(self) -> List[Dict]:
        """
        Scrape les offres sur Academic Positions EU.
        
        Returns:
            Liste des offres trouvées
        """
        logger.info("Début du scraping d'Academic Positions EU")
        jobs = []
        
        # URL de recherche avec filtres pour sciences sociales et Europe
        search_urls = [
            "https://academicpositions.com/jobs/social-sciences",
            "https://academicpositions.com/jobs/humanities", 
            "https://academicpositions.com/jobs/interdisciplinary"
        ]
        
        for search_url in search_urls:
            response = self.make_request(search_url)
            if not response:
                continue
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Recherche des éléments contenant les offres d'emploi
            job_elements = soup.find_all('div', class_=['job-item', 'position-item'])
            
            for job_element in job_elements:
                try:
                    # Extraction du titre
                    title_elem = job_element.find(['h2', 'h3', 'a'], class_=['title', 'job-title'])
                    title = title_elem.get_text(strip=True) if title_elem else ''
                    
                    # Extraction de l'institution
                    institution_elem = job_element.find(['span', 'div'], class_=['institution', 'employer'])
                    institution = institution_elem.get_text(strip=True) if institution_elem else ''
                    
                    # Extraction du lien
                    link_elem = job_element.find('a', href=True)
                    job_url = urljoin(search_url, link_elem['href']) if link_elem else ''
                    
                    # Extraction de la localisation
                    location_elem = job_element.find(['span', 'div'], class_=['location', 'country'])
                    location = location_elem.get_text(strip=True) if location_elem else ''
                    
                    # Calcul de la pertinence
                    full_text = f"{title} {institution} {location}"
                    relevance_score, keywords_found = self.calculate_relevance_score(full_text)
                    
                    # Ne garder que les offres pertinentes
                    if relevance_score > 0.1 or any(keyword.lower() in full_text.lower() for keyword in ALL_KEYWORDS):
                        job_info = {
                            'source': 'Academic Positions EU',
                            'title': title,
                            'institution': institution,
                            'url': job_url,
                            'location': location,
                            'keywords_match': keywords_found,
                            'relevance_score': relevance_score,
                            'found_date': datetime.now().isoformat(),
                            'deadline': 'À vérifier',
                            'teaching': 'À vérifier',
                            'language': 'À vérifier',
                            'description': 'Voir lien pour détails'
                        }
                        jobs.append(job_info)
                        logger.info(f"Offre trouvée: {title} - {institution}")
                        
                except Exception as e:
                    logger.error(f"Erreur lors du parsing d'une offre Academic Positions: {e}")
                    continue
        
        logger.info(f"Academic Positions EU: {len(jobs)} offres trouvées")
        return jobs
    
    def scrape_jobs_ac_uk(self) -> List[Dict]:
        """
        Scrape les offres sur Jobs.ac.uk.
        
        Returns:
            Liste des offres trouvées
        """
        logger.info("Début du scraping de Jobs.ac.uk")
        jobs = []
        
        # URLs de recherche pour différentes disciplines
        search_urls = [
            "https://www.jobs.ac.uk/search/?keywords=social+sciences",
            "https://www.jobs.ac.uk/search/?keywords=digital+humanities",
            "https://www.jobs.ac.uk/search/?keywords=technology+studies"
        ]
        
        for search_url in search_urls:
            response = self.make_request(search_url)
            if not response:
                continue
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Recherche des éléments contenant les offres
            job_elements = soup.find_all(['div', 'article'], class_=['job', 'vacancy', 'result'])
            
            for job_element in job_elements:
                try:
                    # Extraction similaire à Academic Positions
                    title_elem = job_element.find(['h2', 'h3', 'a'])
                    title = title_elem.get_text(strip=True) if title_elem else ''
                    
                    institution_elem = job_element.find(['span', 'div'], string=re.compile(r'University|College|Institute'))
                    institution = institution_elem.get_text(strip=True) if institution_elem else ''
                    
                    link_elem = job_element.find('a', href=True)
                    job_url = urljoin(search_url, link_elem['href']) if link_elem else ''
                    
                    # Calcul de la pertinence
                    full_text = f"{title} {institution}"
                    relevance_score, keywords_found = self.calculate_relevance_score(full_text)
                    
                    if relevance_score > 0.1:
                        job_info = {
                            'source': 'Jobs.ac.uk',
                            'title': title,
                            'institution': institution,
                            'url': job_url,
                            'keywords_match': keywords_found,
                            'relevance_score': relevance_score,
                            'found_date': datetime.now().isoformat(),
                            'location': 'UK',
                            'deadline': 'À vérifier',
                            'teaching': 'À vérifier',
                            'language': 'English',
                            'description': 'Voir lien pour détails'
                        }
                        jobs.append(job_info)
                        
                except Exception as e:
                    logger.error(f"Erreur lors du parsing Jobs.ac.uk: {e}")
                    continue
        
        logger.info(f"Jobs.ac.uk: {len(jobs)} offres trouvées")
        return jobs
    
    def run_full_scraping(self) -> Dict:
        """
        Lance le scraping complet sur toutes les sources configurées.
        
        Returns:
            Dictionnaire avec les résultats et statistiques
        """
        logger.info("=== DÉBUT DU SCRAPING COMPLET ===")
        start_time = datetime.now()
        
        all_jobs = []
        
        # Scraping des sources principales
        try:
            academic_positions_jobs = self.scrape_academic_positions()
            all_jobs.extend(academic_positions_jobs)
            self.stats['sources_processed'] += 1
        except Exception as e:
            logger.error(f"Erreur Academic Positions: {e}")
            
        try:
            jobs_ac_uk_jobs = self.scrape_jobs_ac_uk()
            all_jobs.extend(jobs_ac_uk_jobs)
            self.stats['sources_processed'] += 1
        except Exception as e:
            logger.error(f"Erreur Jobs.ac.uk: {e}")
        
        # Mise à jour des statistiques
        self.stats['total_scraped'] = len(all_jobs)
        self.stats['total_relevant'] = len([job for job in all_jobs if job['relevance_score'] > 0.3])
        
        # Tri par score de pertinence
        all_jobs.sort(key=lambda x: x['relevance_score'], reverse=True)
        
        # Sauvegarde des résultats
        self.save_results(all_jobs)
        
        end_time = datetime.now()
        duration = end_time - start_time
        
        logger.info(f"=== SCRAPING TERMINÉ en {duration} ===")
        logger.info(f"Sources traitées: {self.stats['sources_processed']}")
        logger.info(f"Offres trouvées: {self.stats['total_scraped']}")
        logger.info(f"Offres pertinentes: {self.stats['total_relevant']}")
        logger.info(f"Erreurs: {self.stats['errors']}")
        
        return {
            'jobs': all_jobs,
            'stats': self.stats,
            'duration': str(duration)
        }
    
    def save_results(self, jobs: List[Dict]) -> None:
        """
        Sauvegarde les résultats dans différents formats.
        
        Args:
            jobs: Liste des offres d'emploi trouvées
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Sauvegarde JSON
        json_filename = f"veille_academique_{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(jobs, f, ensure_ascii=False, indent=2)
        logger.info(f"Résultats sauvegardés en JSON: {json_filename}")
        
        # Sauvegarde CSV
        if jobs:
            csv_filename = f"veille_academique_{timestamp}.csv"
            with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=REQUIRED_FIELDS)
                writer.writeheader()
                for job in jobs:
                    # S'assurer que tous les champs requis sont présents
                    row = {field: job.get(field, '') for field in REQUIRED_FIELDS}
                    writer.writerow(row)
            logger.info(f"Résultats sauvegardés en CSV: {csv_filename}")


def main():
    """Fonction principale pour lancer le scraping."""
    print("🎯 Système de Veille Académique")
    print("=" * 50)
    print("Recherche de postes en sciences humaines et sociales")
    print("appliquées aux technologies (crypto, blockchain, STS)")
    print("=" * 50)
    
    # Initialisation du scraper
    scraper = JobScraper()
    
    # Lancement du scraping complet
    results = scraper.run_full_scraping()
    
    # Affichage des résultats
    print(f"\n📊 RÉSULTATS:")
    print(f"   • Sources traitées: {results['stats']['sources_processed']}")
    print(f"   • Offres trouvées: {results['stats']['total_scraped']}")
    print(f"   • Offres pertinentes: {results['stats']['total_relevant']}")
    print(f"   • Durée: {results['duration']}")
    
    if results['jobs']:
        print(f"\n🎯 TOP 5 DES OFFRES LES PLUS PERTINENTES:")
        for i, job in enumerate(results['jobs'][:5], 1):
            print(f"{i}. {job['title']} - {job['institution']}")
            print(f"   Score: {job['relevance_score']:.2f} | Mots-clés: {', '.join(job['keywords_match'][:3])}")
            print(f"   URL: {job['url']}")
            print()


if __name__ == "__main__":
    main()

