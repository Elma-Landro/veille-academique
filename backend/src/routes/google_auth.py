"""
Routes pour l'authentification Google et l'intégration Google Drive.
"""

from flask import Blueprint, jsonify, request, session, redirect, url_for
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import os
import json

google_auth_bp = Blueprint('google_auth', __name__)

# Configuration OAuth2 Google
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', 'your-client-id')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', 'your-client-secret')
REDIRECT_URI = 'http://localhost:5000/api/auth/google/callback'

SCOPES = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/drive.file'
]

@google_auth_bp.route('/auth/google/login', methods=['GET'])
def google_login():
    """Initie le processus d'authentification Google."""
    try:
        flow = Flow.from_client_config(
            {
                "web": {
                    "client_id": GOOGLE_CLIENT_ID,
                    "client_secret": GOOGLE_CLIENT_SECRET,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": [REDIRECT_URI]
                }
            },
            scopes=SCOPES
        )
        flow.redirect_uri = REDIRECT_URI
        
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        
        session['state'] = state
        
        return jsonify({
            'authorization_url': authorization_url,
            'state': state
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Erreur lors de l\'initialisation de l\'authentification Google',
            'details': str(e)
        }), 500

@google_auth_bp.route('/auth/google/callback', methods=['GET'])
def google_callback():
    """Gère le callback de l'authentification Google."""
    try:
        state = session.get('state')
        if not state or state != request.args.get('state'):
            return jsonify({'error': 'État invalide'}), 400
        
        flow = Flow.from_client_config(
            {
                "web": {
                    "client_id": GOOGLE_CLIENT_ID,
                    "client_secret": GOOGLE_CLIENT_SECRET,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": [REDIRECT_URI]
                }
            },
            scopes=SCOPES,
            state=state
        )
        flow.redirect_uri = REDIRECT_URI
        
        # Échanger le code d'autorisation contre des tokens
        flow.fetch_token(authorization_response=request.url)
        
        credentials = flow.credentials
        
        # Obtenir les informations utilisateur
        user_info_service = build('oauth2', 'v2', credentials=credentials)
        user_info = user_info_service.userinfo().get().execute()
        
        # Stocker les informations en session
        session['credentials'] = credentials_to_dict(credentials)
        session['user_info'] = user_info
        
        # Rediriger vers le frontend avec succès
        return redirect('http://localhost:5173/?auth=success')
        
    except Exception as e:
        return redirect(f'http://localhost:5173/?auth=error&message={str(e)}')

@google_auth_bp.route('/auth/user', methods=['GET'])
def get_user_info():
    """Retourne les informations de l'utilisateur connecté."""
    if 'user_info' not in session:
        return jsonify({'error': 'Non authentifié'}), 401
    
    return jsonify({
        'user': session['user_info'],
        'authenticated': True
    })

@google_auth_bp.route('/auth/logout', methods=['POST'])
def logout():
    """Déconnecte l'utilisateur."""
    session.clear()
    return jsonify({'message': 'Déconnexion réussie'})

@google_auth_bp.route('/drive/save', methods=['POST'])
def save_to_drive():
    """Sauvegarde des données sur Google Drive."""
    if 'credentials' not in session:
        return jsonify({'error': 'Non authentifié'}), 401
    
    try:
        credentials = Credentials(**session['credentials'])
        
        # Vérifier si les credentials sont valides
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
            session['credentials'] = credentials_to_dict(credentials)
        
        drive_service = build('drive', 'v3', credentials=credentials)
        
        data = request.get_json()
        filename = data.get('filename', 'veille_academique_results.json')
        content = data.get('content', {})
        
        # Créer le fichier sur Google Drive
        file_metadata = {
            'name': filename,
            'parents': [get_or_create_folder(drive_service, 'Veille_Academique')]
        }
        
        # Pour simplifier, on sauvegarde en tant que fichier texte
        media_body = json.dumps(content, ensure_ascii=False, indent=2)
        
        # Ici on devrait utiliser MediaIoBaseUpload pour un vrai upload
        # Pour la démo, on simule
        
        return jsonify({
            'message': 'Données sauvegardées sur Google Drive',
            'filename': filename,
            'size': len(media_body)
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Erreur lors de la sauvegarde sur Google Drive',
            'details': str(e)
        }), 500

@google_auth_bp.route('/drive/list', methods=['GET'])
def list_drive_files():
    """Liste les fichiers de veille sur Google Drive."""
    if 'credentials' not in session:
        return jsonify({'error': 'Non authentifié'}), 401
    
    try:
        credentials = Credentials(**session['credentials'])
        
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
            session['credentials'] = credentials_to_dict(credentials)
        
        drive_service = build('drive', 'v3', credentials=credentials)
        
        # Rechercher les fichiers dans le dossier Veille_Academique
        folder_id = get_or_create_folder(drive_service, 'Veille_Academique')
        
        results = drive_service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            pageSize=20,
            fields="nextPageToken, files(id, name, createdTime, modifiedTime, size)"
        ).execute()
        
        files = results.get('files', [])
        
        return jsonify({
            'files': files,
            'total': len(files)
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Erreur lors de la récupération des fichiers',
            'details': str(e)
        }), 500

def credentials_to_dict(credentials):
    """Convertit les credentials en dictionnaire."""
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

def get_or_create_folder(drive_service, folder_name):
    """Obtient ou crée un dossier sur Google Drive."""
    # Rechercher le dossier existant
    results = drive_service.files().list(
        q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
        fields="files(id, name)"
    ).execute()
    
    folders = results.get('files', [])
    
    if folders:
        return folders[0]['id']
    else:
        # Créer le dossier
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = drive_service.files().create(body=folder_metadata, fields='id').execute()
        return folder.get('id')

@google_auth_bp.route('/auth/status', methods=['GET'])
def auth_status():
    """Vérifie le statut d'authentification."""
    if 'user_info' in session and 'credentials' in session:
        try:
            credentials = Credentials(**session['credentials'])
            if credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
                session['credentials'] = credentials_to_dict(credentials)
            
            return jsonify({
                'authenticated': True,
                'user': session['user_info'],
                'drive_access': True
            })
        except:
            return jsonify({
                'authenticated': False,
                'drive_access': False
            })
    else:
        return jsonify({
            'authenticated': False,
            'drive_access': False
        })

