"""
Système de Veille Académique - Scrapers Spécialisés
===================================================

Ce module contient les scrapers spécialisés pour les différentes plateformes
d'emploi académique, chacun adapté à la structure spécifique du site.

Auteur: Assistant IA Manus
Date: Juin 2025
"""

import requests
from bs4 import BeautifulSoup
import time
import random
import json
from datetime import datetime
import re
from urllib.parse import urljoin, urlparse
import logging
from typing import List, Dict, Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import ALL_KEYWORDS, POSITION_TYPES, DEFAULT_HEADERS, REQUEST_DELAYS

logger = logging.getLogger(__name__)


class EuraxessScraper:
    """Scraper spécialisé pour Euraxess."""
    
    def __init__(self, session: requests.Session):
        self.session = session
        
    def scrape(self) -> List[Dict]:
        """
        Scrape les offres sur Euraxess.
        
        Returns:
            Liste des offres trouvées
        """
        logger.info("Début du scraping d'Euraxess")
        jobs = []
        
        # URLs de recherche ciblées
        search_urls = [
            "https://euraxess.ec.europa.eu/jobs/search?keywords=social+sciences",
            "https://euraxess.ec.europa.eu/jobs/search?keywords=digital+humanities",
            "https://euraxess.ec.europa.eu/jobs/search?keywords=technology+studies",
            "https://euraxess.ec.europa.eu/jobs/search?keywords=blockchain",
            "https://euraxess.ec.europa.eu/jobs/search?keywords=cryptocurrency"
        ]
        
        for search_url in search_urls:
            try:
                response = self.session.get(search_url, timeout=30)
                if response.status_code != 200:
                    continue
                    
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Euraxess utilise une structure spécifique
                job_elements = soup.find_all('div', class_=['views-row', 'job-item'])
                
                for job_element in job_elements:
                    job_info = self._extract_euraxess_job(job_element, search_url)
                    if job_info and self._is_relevant(job_info):
                        jobs.append(job_info)
                        
                # Délai entre les pages
                time.sleep(random.uniform(2, 4))
                
            except Exception as e:
                logger.error(f"Erreur Euraxess pour {search_url}: {e}")
                continue
        
        logger.info(f"Euraxess: {len(jobs)} offres trouvées")
        return jobs
    
    def _extract_euraxess_job(self, job_element, base_url: str) -> Optional[Dict]:
        """Extrait les informations d'une offre Euraxess."""
        try:
            # Titre
            title_elem = job_element.find(['h2', 'h3'], class_=['title', 'job-title'])
            title = title_elem.get_text(strip=True) if title_elem else ''
            
            # Institution
            institution_elem = job_element.find(['div', 'span'], class_=['institution', 'employer'])
            institution = institution_elem.get_text(strip=True) if institution_elem else ''
            
            # Lien
            link_elem = job_element.find('a', href=True)
            job_url = urljoin(base_url, link_elem['href']) if link_elem else ''
            
            # Localisation
            location_elem = job_element.find(['span', 'div'], class_=['location', 'country'])
            location = location_elem.get_text(strip=True) if location_elem else ''
            
            # Date limite
            deadline_elem = job_element.find(['span', 'div'], class_=['deadline', 'closing-date'])
            deadline = deadline_elem.get_text(strip=True) if deadline_elem else 'À vérifier'
            
            return {
                'source': 'Euraxess',
                'title': title,
                'institution': institution,
                'url': job_url,
                'location': location,
                'deadline': deadline,
                'found_date': datetime.now().isoformat(),
                'teaching': 'À vérifier',
                'language': 'À vérifier',
                'description': 'Voir lien pour détails'
            }
            
        except Exception as e:
            logger.error(f"Erreur extraction Euraxess: {e}")
            return None
    
    def _is_relevant(self, job_info: Dict) -> bool:
        """Vérifie si l'offre est pertinente selon nos critères."""
        text = f"{job_info['title']} {job_info['institution']} {job_info.get('description', '')}"
        text_lower = text.lower()
        
        # Recherche de mots-clés pertinents
        for keyword in ALL_KEYWORDS:
            if keyword.lower() in text_lower:
                return True
                
        # Recherche de types de postes
        for position_type in POSITION_TYPES:
            if position_type.lower() in text_lower:
                return True
                
        return False


class HNetScraper:
    """Scraper spécialisé pour H-Net."""
    
    def __init__(self, session: requests.Session):
        self.session = session
        
    def scrape(self) -> List[Dict]:
        """
        Scrape les offres sur H-Net.
        
        Returns:
            Liste des offres trouvées
        """
        logger.info("Début du scraping de H-Net")
        jobs = []
        
        try:
            # H-Net a une page principale de jobs
            response = self.session.get("https://www.h-net.org/jobs/job_browse.php", timeout=30)
            if response.status_code != 200:
                return jobs
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # H-Net liste les jobs dans des tableaux ou des listes
            job_elements = soup.find_all(['tr', 'div'], class_=['job', 'posting'])
            
            for job_element in job_elements:
                job_info = self._extract_hnet_job(job_element)
                if job_info and self._is_relevant(job_info):
                    jobs.append(job_info)
                    
        except Exception as e:
            logger.error(f"Erreur H-Net: {e}")
        
        logger.info(f"H-Net: {len(jobs)} offres trouvées")
        return jobs
    
    def _extract_hnet_job(self, job_element) -> Optional[Dict]:
        """Extrait les informations d'une offre H-Net."""
        try:
            # H-Net a une structure particulière, souvent en tableau
            title_elem = job_element.find(['a', 'td'], string=re.compile(r'Professor|Lecturer|Research'))
            title = title_elem.get_text(strip=True) if title_elem else ''
            
            # Institution souvent dans la cellule suivante
            institution_elem = job_element.find(['td', 'span'], string=re.compile(r'University|College|Institute'))
            institution = institution_elem.get_text(strip=True) if institution_elem else ''
            
            # Lien vers l'offre complète
            link_elem = job_element.find('a', href=True)
            job_url = urljoin("https://www.h-net.org", link_elem['href']) if link_elem else ''
            
            return {
                'source': 'H-Net',
                'title': title,
                'institution': institution,
                'url': job_url,
                'location': 'International',
                'deadline': 'À vérifier',
                'found_date': datetime.now().isoformat(),
                'teaching': 'Probable',
                'language': 'English',
                'description': 'Voir lien pour détails'
            }
            
        except Exception as e:
            logger.error(f"Erreur extraction H-Net: {e}")
            return None
    
    def _is_relevant(self, job_info: Dict) -> bool:
        """Vérifie la pertinence pour H-Net."""
        text = f"{job_info['title']} {job_info['institution']}"
        text_lower = text.lower()
        
        # H-Net est plus orienté sciences humaines, donc critères plus larges
        relevant_terms = ALL_KEYWORDS + [
            'digital', 'technology', 'media', 'internet', 'computer',
            'innovation', 'society', 'culture', 'politics'
        ]
        
        for term in relevant_terms:
            if term.lower() in text_lower:
                return True
                
        return False


class ChronicleHEScraper:
    """Scraper spécialisé pour Chronicle of Higher Education."""
    
    def __init__(self, session: requests.Session):
        self.session = session
        
    def scrape(self) -> List[Dict]:
        """
        Scrape les offres sur Chronicle of Higher Education.
        
        Returns:
            Liste des offres trouvées
        """
        logger.info("Début du scraping de Chronicle of Higher Education")
        jobs = []
        
        # URLs de recherche ciblées
        search_urls = [
            "https://jobs.chronicle.com/jobs/?keywords=social+sciences",
            "https://jobs.chronicle.com/jobs/?keywords=digital+humanities",
            "https://jobs.chronicle.com/jobs/?keywords=technology+studies"
        ]
        
        for search_url in search_urls:
            try:
                response = self.session.get(search_url, timeout=30)
                if response.status_code != 200:
                    continue
                    
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Chronicle utilise une structure de liste de jobs
                job_elements = soup.find_all(['div', 'article'], class_=['job-item', 'listing'])
                
                for job_element in job_elements:
                    job_info = self._extract_chronicle_job(job_element, search_url)
                    if job_info and self._is_relevant(job_info):
                        jobs.append(job_info)
                        
                time.sleep(random.uniform(2, 4))
                
            except Exception as e:
                logger.error(f"Erreur Chronicle pour {search_url}: {e}")
                continue
        
        logger.info(f"Chronicle of Higher Education: {len(jobs)} offres trouvées")
        return jobs
    
    def _extract_chronicle_job(self, job_element, base_url: str) -> Optional[Dict]:
        """Extrait les informations d'une offre Chronicle."""
        try:
            # Titre
            title_elem = job_element.find(['h2', 'h3', 'a'], class_=['title', 'job-title'])
            title = title_elem.get_text(strip=True) if title_elem else ''
            
            # Institution
            institution_elem = job_element.find(['div', 'span'], class_=['employer', 'institution'])
            institution = institution_elem.get_text(strip=True) if institution_elem else ''
            
            # Lien
            link_elem = job_element.find('a', href=True)
            job_url = urljoin(base_url, link_elem['href']) if link_elem else ''
            
            # Localisation
            location_elem = job_element.find(['span', 'div'], class_=['location'])
            location = location_elem.get_text(strip=True) if location_elem else ''
            
            return {
                'source': 'Chronicle of Higher Education',
                'title': title,
                'institution': institution,
                'url': job_url,
                'location': location,
                'deadline': 'À vérifier',
                'found_date': datetime.now().isoformat(),
                'teaching': 'Probable',
                'language': 'English',
                'description': 'Voir lien pour détails'
            }
            
        except Exception as e:
            logger.error(f"Erreur extraction Chronicle: {e}")
            return None
    
    def _is_relevant(self, job_info: Dict) -> bool:
        """Vérifie la pertinence pour Chronicle."""
        text = f"{job_info['title']} {job_info['institution']}"
        text_lower = text.lower()
        
        for keyword in ALL_KEYWORDS:
            if keyword.lower() in text_lower:
                return True
                
        return False


class SeleniumScraper:
    """
    Scraper utilisant Selenium pour les sites nécessitant JavaScript.
    Utilisé pour Galaxie et autres sites complexes.
    """
    
    def __init__(self):
        self.driver = None
        
    def setup_driver(self):
        """Configure le driver Selenium."""
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Mode sans interface graphique
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument(f'--user-agent={DEFAULT_HEADERS["User-Agent"]}')
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(10)
            return True
        except Exception as e:
            logger.error(f"Erreur initialisation Selenium: {e}")
            return False
    
    def scrape_galaxie(self) -> List[Dict]:
        """
        Scrape Galaxie (nécessite Selenium car site JavaScript).
        
        Returns:
            Liste des offres trouvées
        """
        logger.info("Début du scraping de Galaxie (Selenium)")
        jobs = []
        
        if not self.setup_driver():
            logger.error("Impossible d'initialiser Selenium pour Galaxie")
            return jobs
        
        try:
            # Galaxie nécessite souvent une authentification
            # Pour l'instant, on accède aux pages publiques
            self.driver.get("https://www.galaxie.enseignementsup-recherche.gouv.fr")
            
            # Attendre le chargement de la page
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Rechercher les liens vers les offres d'emploi
            job_links = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "emploi")
            job_links.extend(self.driver.find_elements(By.PARTIAL_LINK_TEXT, "recrutement"))
            
            for link in job_links[:10]:  # Limiter pour éviter la surcharge
                try:
                    link.click()
                    time.sleep(2)
                    
                    # Extraire les informations de la page
                    title = self.driver.title
                    url = self.driver.current_url
                    
                    # Rechercher du contenu pertinent
                    page_text = self.driver.find_element(By.TAG_NAME, "body").text
                    
                    if self._is_relevant_text(page_text):
                        job_info = {
                            'source': 'Galaxie',
                            'title': title,
                            'institution': 'Ministère Enseignement Supérieur',
                            'url': url,
                            'location': 'France',
                            'deadline': 'À vérifier',
                            'found_date': datetime.now().isoformat(),
                            'teaching': 'Oui',
                            'language': 'Français',
                            'description': page_text[:500] + '...'
                        }
                        jobs.append(job_info)
                    
                    self.driver.back()
                    time.sleep(2)
                    
                except Exception as e:
                    logger.error(f"Erreur lors du traitement d'un lien Galaxie: {e}")
                    continue
        
        except Exception as e:
            logger.error(f"Erreur générale Galaxie: {e}")
        
        finally:
            if self.driver:
                self.driver.quit()
        
        logger.info(f"Galaxie: {len(jobs)} offres trouvées")
        return jobs
    
    def _is_relevant_text(self, text: str) -> bool:
        """Vérifie si le texte contient des termes pertinents."""
        text_lower = text.lower()
        
        for keyword in ALL_KEYWORDS:
            if keyword.lower() in text_lower:
                return True
                
        for position_type in POSITION_TYPES:
            if position_type.lower() in text_lower:
                return True
                
        return False


def get_all_specialized_scrapers(session: requests.Session) -> List:
    """
    Retourne la liste de tous les scrapers spécialisés.
    
    Args:
        session: Session requests à partager
        
    Returns:
        Liste des instances de scrapers
    """
    return [
        EuraxessScraper(session),
        HNetScraper(session),
        ChronicleHEScraper(session),
        SeleniumScraper()  # Pas besoin de session pour Selenium
    ]

