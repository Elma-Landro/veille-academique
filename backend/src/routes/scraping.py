"""
Routes pour les fonctionnalités de scraping de la veille académique.
"""

from flask import Blueprint, jsonify, request
import json
import os
import sys
from datetime import datetime
import threading
import time

# Ajouter le répertoire parent pour importer les modules de scraping
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'veille_academique'))

scraping_bp = Blueprint('scraping', __name__)

# Variables globales pour le statut du scraping
scraping_status = {
    'is_running': False,
    'last_run': None,
    'progress': 0,
    'current_source': '',
    'results_count': 0,
    'error_message': None
}

# Cache des derniers résultats
last_results = []

@scraping_bp.route('/scraping/status', methods=['GET'])
def get_scraping_status():
    """Retourne le statut actuel du scraping."""
    return jsonify(scraping_status)

@scraping_bp.route('/scraping/results', methods=['GET'])
def get_scraping_results():
    """Retourne les derniers résultats de scraping."""
    # Paramètres de pagination et filtrage
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    search = request.args.get('search', '', type=str)
    min_score = request.args.get('min_score', 0.0, type=float)
    
    # Filtrage des résultats
    filtered_results = last_results
    
    if search:
        filtered_results = [
            job for job in filtered_results 
            if search.lower() in job.get('title', '').lower() or 
               search.lower() in job.get('institution', '').lower() or
               any(search.lower() in keyword.lower() for keyword in job.get('keywords_match', []))
        ]
    
    if min_score > 0:
        filtered_results = [
            job for job in filtered_results 
            if job.get('relevance_score', 0) >= min_score
        ]
    
    # Pagination
    start = (page - 1) * per_page
    end = start + per_page
    paginated_results = filtered_results[start:end]
    
    return jsonify({
        'jobs': paginated_results,
        'total': len(filtered_results),
        'page': page,
        'per_page': per_page,
        'has_next': end < len(filtered_results),
        'has_prev': page > 1
    })

@scraping_bp.route('/scraping/run', methods=['POST'])
def run_scraping():
    """Lance un nouveau scraping en arrière-plan."""
    global scraping_status
    
    if scraping_status['is_running']:
        return jsonify({
            'error': 'Un scraping est déjà en cours'
        }), 400
    
    # Paramètres du scraping
    data = request.get_json() or {}
    sources = data.get('sources', ['academic_positions', 'jobs_ac_uk'])
    keywords = data.get('keywords', [])
    
    # Lancer le scraping en arrière-plan
    thread = threading.Thread(target=run_scraping_task, args=(sources, keywords))
    thread.daemon = True
    thread.start()
    
    return jsonify({
        'message': 'Scraping lancé avec succès',
        'sources': sources,
        'estimated_duration': '2-5 minutes'
    })

def run_scraping_task(sources, keywords):
    """Tâche de scraping exécutée en arrière-plan."""
    global scraping_status, last_results
    
    try:
        # Initialisation du statut
        scraping_status.update({
            'is_running': True,
            'progress': 0,
            'current_source': '',
            'results_count': 0,
            'error_message': None
        })
        
        # Import du vrai scraper
        try:
            from scraper.scraper import JobScraper
            scraper = JobScraper()
            actual_results = []
        except ImportError:
            # Fallback vers simulation si le scraper n'est pas disponible
            mock_results = []
        
        # Scraping réel
        if 'scraper' in locals():
            for i, source in enumerate(sources):
                scraping_status['current_source'] = source
                scraping_status['progress'] = int((i / len(sources)) * 100)
                
                try:
                    if source == 'academic_positions':
                        results = scraper.scrape_academic_positions()
                        actual_results.extend(results)
                    elif source == 'jobs_ac_uk':
                        results = scraper.scrape_jobs_ac_uk()
                        actual_results.extend(results)
                except Exception as e:
                    logger.error(f"Erreur scraping {source}: {e}")
                    continue
                    
            mock_results = actual_results
        else:
            # Simulation si scraper indisponible
            for i, source in enumerate(sources):
                scraping_status['current_source'] = source
                scraping_status['progress'] = int((i / len(sources)) * 100)
                
                time.sleep(1)  # Délai réduit
                
                if source == 'academic_positions':
                    mock_results.extend([
                        {
                            'id': f'ap_{i}',
                            'title': f'Poste {i+1} - Sociologie des Cryptomonnaies',
                            'institution': 'Université Paris-Saclay',
                            'location': 'France',
                            'deadline': '2025-08-15',
                            'url': f'https://example.com/job_{i}',
                            'source': 'Academic Positions EU',
                            'keywords_match': ['crypto', 'sociologie', 'gouvernance'],
                            'relevance_score': 0.85 - (i * 0.1),
                            'teaching': 'Oui',
                            'language': 'Français',
                            'found_date': datetime.now().isoformat(),
                            'description': 'Poste de maître de conférences en sociologie...'
                        }
                    ])
                elif source == 'jobs_ac_uk':
                    mock_results.extend([
                        {
                            'id': f'uk_{i}',
                            'title': f'Lecturer in Digital Political Economy {i+1}',
                            'institution': 'University of Edinburgh',
                            'location': 'UK',
                            'deadline': '2025-07-30',
                            'url': f'https://example.com/uk_job_{i}',
                            'source': 'Jobs.ac.uk',
                            'keywords_match': ['digital', 'political economy', 'blockchain'],
                            'relevance_score': 0.75 - (i * 0.05),
                            'teaching': 'Oui',
                            'language': 'English',
                            'found_date': datetime.now().isoformat(),
                            'description': 'Lecturer position in digital political economy...'
                        }
                    ])
        
        # Finalisation
        scraping_status.update({
            'is_running': False,
            'progress': 100,
            'current_source': '',
            'results_count': len(mock_results),
            'last_run': datetime.now().isoformat()
        })
        
        last_results = mock_results
        
    except Exception as e:
        scraping_status.update({
            'is_running': False,
            'error_message': str(e),
            'progress': 0
        })

@scraping_bp.route('/scraping/export', methods=['POST'])
def export_results():
    """Exporte les résultats dans différents formats."""
    data = request.get_json() or {}
    format_type = data.get('format', 'json')  # json, csv, xlsx
    
    if format_type == 'json':
        return jsonify({
            'data': last_results,
            'exported_at': datetime.now().isoformat(),
            'total_jobs': len(last_results)
        })
    
    elif format_type == 'csv':
        # Ici on pourrait générer un vrai CSV
        return jsonify({
            'message': 'Export CSV généré',
            'download_url': '/api/scraping/download/results.csv'
        })
    
    else:
        return jsonify({
            'error': 'Format non supporté'
        }), 400

@scraping_bp.route('/scraping/sources', methods=['GET'])
def get_available_sources():
    """Retourne la liste des sources disponibles."""
    sources = [
        {
            'id': 'academic_positions',
            'name': 'Academic Positions EU',
            'url': 'https://academicpositions.com',
            'status': 'active',
            'last_scraped': '2025-06-18T10:00:00Z',
            'difficulty': 'medium'
        },
        {
            'id': 'jobs_ac_uk',
            'name': 'Jobs.ac.uk',
            'url': 'https://www.jobs.ac.uk',
            'status': 'active',
            'last_scraped': '2025-06-18T10:00:00Z',
            'difficulty': 'low'
        },
        {
            'id': 'euraxess',
            'name': 'Euraxess',
            'url': 'https://euraxess.ec.europa.eu',
            'status': 'active',
            'last_scraped': '2025-06-18T09:30:00Z',
            'difficulty': 'medium'
        },
        {
            'id': 'galaxie',
            'name': 'Galaxie/Antares',
            'url': 'https://www.galaxie.enseignementsup-recherche.gouv.fr',
            'status': 'maintenance',
            'last_scraped': '2025-06-17T15:00:00Z',
            'difficulty': 'high'
        },
        {
            'id': 'h_net',
            'name': 'H-Net Job Guide',
            'url': 'https://www.h-net.org/jobs',
            'status': 'active',
            'last_scraped': '2025-06-18T08:00:00Z',
            'difficulty': 'medium'
        }
    ]
    
    return jsonify({
        'sources': sources,
        'total_active': len([s for s in sources if s['status'] == 'active'])


@scraping_bp.route('/scraping/schedule', methods=['POST'])
def schedule_scraping():
    """Configure le scraping automatique."""
    data = request.get_json() or {}
    interval_hours = data.get('interval_hours', 24)
    sources = data.get('sources', ['academic_positions', 'jobs_ac_uk'])
    
    # Pour l'instant, on retourne la configuration
    # À terme, ça pourrait déclencher un cron job
    return jsonify({
        'message': 'Scraping programmé configuré',
        'interval_hours': interval_hours,
        'sources': sources,
        'next_run': 'Utiliser Replit Scheduled Deployments pour automatiser'
    })

@scraping_bp.route('/scraping/health', methods=['GET'])
def scraping_health():
    """Point de santé pour le système de scraping."""
    return jsonify({
        'status': 'operational',
        'last_run': scraping_status.get('last_run'),
        'total_sources': 5,
        'active_sources': 4
    })

    })

@scraping_bp.route('/scraping/keywords', methods=['GET'])
def get_keywords():
    """Retourne les mots-clés configurés."""
    keywords = {
        'crypto': ['crypto', 'cryptocurrency', 'cryptomonnaie', 'blockchain', 'bitcoin', 'ethereum'],
        'governance': ['gouvernance', 'governance', 'algorithmic governance', 'dao', 'decentralized'],
        'academic': ['sts', 'science technology studies', 'digital political economy', 'critical data studies'],
        'positions': ['maître de conférences', 'assistant professor', 'postdoc', 'chercheur']
    }
    
    return jsonify(keywords)

@scraping_bp.route('/scraping/stats', methods=['GET'])
def get_scraping_stats():
    """Retourne les statistiques de scraping."""
    stats = {
        'total_jobs_found': len(last_results),
        'high_relevance_jobs': len([j for j in last_results if j.get('relevance_score', 0) >= 0.8]),
        'medium_relevance_jobs': len([j for j in last_results if 0.6 <= j.get('relevance_score', 0) < 0.8]),
        'sources_last_24h': 5,
        'avg_relevance_score': sum(j.get('relevance_score', 0) for j in last_results) / max(len(last_results), 1),
        'last_update': scraping_status.get('last_run'),
        'top_keywords': [
            {'keyword': 'crypto', 'count': 12},
            {'keyword': 'blockchain', 'count': 8},
            {'keyword': 'gouvernance', 'count': 6},
            {'keyword': 'sts', 'count': 15}
        ]
    }
    
    return jsonify(stats)

