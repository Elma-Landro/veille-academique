import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
from src.models.user import db
from src.routes.user import user_bp
from src.routes.scraping import scraping_bp
from src.routes.google_auth import google_auth_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'veille_academique_secret_key_2025'

# Configuration CORS pour permettre les requêtes depuis le frontend
CORS(app, origins=["http://localhost:5173", "http://localhost:3000", "https://*.replit.app", "https://*.replit.dev"], supports_credentials=True)

# Enregistrement des blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(scraping_bp, url_prefix='/api')
app.register_blueprint(google_auth_bp, url_prefix='/api')

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/api/health')
def health_check():
    """Point de contrôle de santé de l'API."""
    return jsonify({
        'status': 'healthy',
        'message': 'API Veille Académique opérationnelle',
        'version': '1.0.0'
    })

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """Sert les fichiers statiques du frontend."""
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return jsonify({
                'message': 'API Veille Académique',
                'endpoints': [
                    '/api/health',
                    '/api/scraping/run',
                    '/api/scraping/status',
                    '/api/scraping/results',
                    '/api/auth/google'
                ]
            })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

