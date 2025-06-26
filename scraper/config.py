"""
Système de Veille Académique - Configuration
============================================

Ce fichier contient toutes les configurations nécessaires pour le système de veille
des postes académiques en sciences humaines et sociales appliquées aux technologies.

Auteur: Assistant IA Manus
Date: Juin 2025
"""

# =============================================================================
# MOTS-CLÉS DE RECHERCHE
# =============================================================================

# Mots-clés principaux liés aux cryptomonnaies et blockchain
CRYPTO_KEYWORDS = [
    "crypto", "cryptocurrency", "cryptomonnaie", "cryptomonnaies",
    "blockchain", "bitcoin", "ethereum", "web3", "defi",
    "smart contract", "contrat intelligent", "token", "nft"
]

# Mots-clés liés à la gouvernance et aux infrastructures numériques
GOVERNANCE_KEYWORDS = [
    "gouvernance", "governance", "algorithmic governance", "gouvernance algorithmique",
    "infrastructure numérique", "digital infrastructure", "infrastructure digitale",
    "dao", "daos", "decentralized", "décentralisé", "décentralisée",
    "polycentric governance", "gouvernance polycentrique"
]

# Mots-clés académiques et disciplinaires
ACADEMIC_KEYWORDS = [
    "science technology studies", "sts", "sciences techniques société",
    "digital political economy", "économie politique numérique",
    "critical data studies", "études critiques des données",
    "money as institution", "monnaie institution", "monnaie comme institution",
    "sociologie des crises", "sociology of crisis", "institutionnalisme",
    "économie politique critique", "critical political economy"
]

# Combinaison de tous les mots-clés
ALL_KEYWORDS = CRYPTO_KEYWORDS + GOVERNANCE_KEYWORDS + ACADEMIC_KEYWORDS

# =============================================================================
# TYPES DE POSTES RECHERCHÉS
# =============================================================================

POSITION_TYPES = [
    "maître de conférences", "maitre de conferences", "mcf",
    "professeur junior", "professeur assistant",
    "assistant professor", "associate professor", "senior lecturer",
    "chercheur cnrs", "chercheur inria", "chercheur ifris",
    "post-doc senior", "postdoc senior", "senior postdoc",
    "responsable de programme", "responsable de chaire",
    "chercheur invité", "visiting researcher", "visiting scholar",
    "fellow", "research fellow", "senior fellow"
]

# =============================================================================
# SOURCES DE DONNÉES
# =============================================================================

# URLs des principales plateformes de recherche d'emploi académique
MAIN_SOURCES = {
    "galaxie": {
        "url": "https://www.galaxie.enseignementsup-recherche.gouv.fr",
        "name": "Galaxie / Antares (France)",
        "requires_auth": True,
        "scraping_difficulty": "high"
    },
    "odyssee": {
        "url": "https://www.galaxie.enseignementsup-recherche.gouv.fr/ensup//cand_recrutement_enseignants_chercheurs_Odyssee.htm",
        "name": "Odyssée - Recrutement Enseignants-Chercheurs",
        "requires_auth": False,
        "scraping_difficulty": "medium"
    },
    "academic_positions": {
        "url": "https://academicpositions.com",
        "name": "Academic Positions EU",
        "requires_auth": False,
        "scraping_difficulty": "medium"
    },
    "euraxess": {
        "url": "https://euraxess.ec.europa.eu/jobs",
        "name": "Euraxess - EU Research Jobs",
        "requires_auth": False,
        "scraping_difficulty": "medium"
    },
    "jobs_ac_uk": {
        "url": "https://www.jobs.ac.uk",
        "name": "Jobs.ac.uk",
        "requires_auth": False,
        "scraping_difficulty": "low"
    },
    "h_net": {
        "url": "https://www.h-net.org/jobs/job_browse.php",
        "name": "H-Net Job Guide",
        "requires_auth": False,
        "scraping_difficulty": "medium"
    },
    "chronicle_higher_ed": {
        "url": "https://jobs.chronicle.com",
        "name": "Chronicle of Higher Education",
        "requires_auth": False,
        "scraping_difficulty": "medium"
    },
    "academic_jobs_online": {
        "url": "https://academicjobsonline.org/ajo",
        "name": "AcademicJobsOnline.org",
        "requires_auth": False,
        "scraping_difficulty": "medium"
    },
    "theunijobs": {
        "url": "https://www.timeshighereducation.com/unijobs",
        "name": "THEunijobs (Times Higher Education)",
        "requires_auth": False,
        "scraping_difficulty": "medium"
    },
    "higher_ed_jobs": {
        "url": "https://www.higheredjobs.com",
        "name": "HigherEdJobs",
        "requires_auth": False,
        "scraping_difficulty": "low"
    },
    "apec": {
        "url": "https://www.apec.fr",
        "name": "APEC (France - Cadres)",
        "requires_auth": False,
        "scraping_difficulty": "medium"
    },
    "fnege": {
        "url": "https://fnege.org/offres_emploi/",
        "name": "FNEGE - Grandes Écoles de Commerce",
        "requires_auth": False,
        "scraping_difficulty": "medium"
    }
}

# Sites d'écoles d'ingénieurs françaises
ENGINEERING_SCHOOLS = {
    "mines_paristech": "https://www.minesparis.psl.eu/Ecole/Recrutement/",
    "telecom_paris": "https://www.telecom-paris.fr/fr/lecole/recrutement",
    "insa_lyon": "https://www.insa-lyon.fr/fr/formation/recrutement",
    "utc": "https://www.utc.fr/universite/recrutement/",
    "centralesupelec": "https://www.centralesupelec.fr/fr/lecole/recrutement",
    "polytechnique": "https://www.polytechnique.edu/fr/recrutement",
    "enpc": "https://ecoledesponts.fr/recrutement",
    "ensae": "https://www.ensae.fr/ecole/recrutement",
    "institut_mines_telecom": "https://institutminestelecom.recruitee.com/nos-offres-d-emploi",
    "cesi": "https://www.cesi.fr/recrutement/?categ_poste%5B%5D=Recherche"
}

# Sites d'écoles de commerce et de gestion
BUSINESS_SCHOOLS = {
    "fnege": "https://fnege.org/offres_emploi/",
    "essca": "https://www.essca.eu/faculte-et-recherche/faculte/recrutement/postes-a-pourvoir-enseignants-chercheurs/",
    "hec": "https://www.hec.fr/fr/faculte-recherche/recrutement",
    "essec": "https://www.essec.edu/fr/faculte-recherche/recrutement/",
    "edhec": "https://www.edhec.edu/fr/faculte-et-recherche/recrutement",
    "em_lyon": "https://em-lyon.com/fr/faculte-recherche/recrutement",
    "audencia": "https://www.audencia.com/faculte-recherche/recrutement/",
    "skema": "https://www.skema.edu/faculte-recherche/recrutement"
}

# URLs des laboratoires et institutions spécialisées en STS
SPECIALIZED_SOURCES = {
    "ifris": "https://www.ifris.org",
    "csi_mines": "https://www.csi.mines-paristech.fr",
    "latts": "https://latts.cnrs.fr",
    "cems": "https://cems.ehess.fr",
    "medialab": "https://medialab.sciencespo.fr",
    "cite": "https://cite.cnam.fr",
    "mfo": "https://www.mfo.de",
    "eth_sts": "https://www.ethz.ch/en/the-eth-zurich/organisation/departments/humanities-social-and-political-sciences/sts.html",
    "utrecht_data": "https://dataschool.nl",
    "weizenbaum": "https://www.weizenbaum-institut.de",
    "gis_etudes_areales": "https://www.gis-reseau-asie.org",
    "cnrs_shs": "https://www.cnrs.fr/inshs",
    "ehess": "https://www.ehess.fr",
    "ehesp": "https://www.ehesp.fr",
    "msh": "https://www.msh-reseau.fr",
    "ined": "https://www.ined.fr"
}

# Réseaux académiques européens et internationaux
ACADEMIC_NETWORKS = {
    "academia_net": "https://www.academia-net.org",
    "researchgate_jobs": "https://www.researchgate.net/jobs",
    "nature_careers": "https://www.nature.com/naturecareers",
    "science_careers": "https://jobs.sciencecareers.org",
    "versatile_phd": "https://versatilephd.com/jobs/",
    "postdoc_jobs": "https://www.postdocjobs.com",
    "academic_transfer": "https://www.academictransfer.com",
    "university_world_news": "https://www.universityworldnews.com/jobs/"
}

# =============================================================================
# PARAMÈTRES DE SCRAPING
# =============================================================================

# Headers pour éviter la détection de bot
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# Délais entre les requêtes (en secondes)
REQUEST_DELAYS = {
    "min_delay": 2,    # Délai minimum entre deux requêtes
    "max_delay": 5,    # Délai maximum entre deux requêtes
    "error_delay": 10  # Délai après une erreur
}

# Nombre maximum de tentatives en cas d'échec
MAX_RETRIES = 3

# =============================================================================
# CONFIGURATION DES RÉSULTATS
# =============================================================================

# Champs à extraire pour chaque offre d'emploi
REQUIRED_FIELDS = [
    "title",           # Intitulé du poste
    "institution",     # Institution + département
    "url",            # Lien vers l'annonce
    "deadline",       # Date limite de candidature
    "keywords_match", # Mots-clés correspondants
    "teaching",       # Présence d'enseignement (oui/non)
    "language",       # Langue d'enseignement
    "location",       # Localisation
    "description",    # Description du poste
    "found_date"      # Date de découverte
]

# Format de sortie des résultats
OUTPUT_FORMATS = ["json", "csv", "html"]

# =============================================================================
# CONFIGURATION GOOGLE DRIVE (pour la persistance)
# =============================================================================

GOOGLE_DRIVE_CONFIG = {
    "folder_name": "Veille_Academique",
    "credentials_file": "credentials.json",
    "token_file": "token.json",
    "scopes": [
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive.metadata'
    ]
}

# =============================================================================
# CONFIGURATION DES ALERTES
# =============================================================================

ALERT_CONFIG = {
    "email_enabled": True,
    "daily_summary": True,
    "immediate_alerts": True,
    "min_relevance_score": 0.6  # Score minimum pour déclencher une alerte
}

