from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv
import os
import logging
from datetime import datetime
import json

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Configuration OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Vérification de la clé API
if not openai.api_key:
    logger.error("Clé API OpenAI manquante!")
    raise ValueError("La clé API OpenAI est requise. Veuillez définir OPENAI_API_KEY dans votre fichier .env")

@app.route('/')
def home():
    """Page d'accueil du chat IA"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint pour le chat avec l'IA"""
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({"error": "Message manquant"}), 400
        
        user_message = data['message'].strip()
        
        if not user_message:
            return jsonify({"error": "Message vide"}), 400
        
        # Log de la requête
        logger.info(f"Requête reçue: {user_message[:50]}...")
        
        # Appel à l'API OpenAI
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": "Tu es un assistant IA français utile, amical et professionnel. Réponds toujours en français de manière claire et concise."
                },
                {"role": "user", "content": user_message}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        # Log de la réponse
        logger.info(f"Réponse IA générée: {ai_response[:50]}...")
        
        return jsonify({
            "response": ai_response,
            "timestamp": datetime.now().isoformat(),
            "model": "gpt-3.5-turbo"
        })
        
    except openai.AuthenticationError:
        logger.error("Erreur d'authentification OpenAI")
        return jsonify({"error": "Erreur d'authentification avec l'API OpenAI"}), 401
        
    except openai.RateLimitError:
        logger.error("Limite de taux OpenAI dépassée")
        return jsonify({"error": "Limite de requêtes dépassée. Veuillez réessayer plus tard."}), 429
        
    except openai.APIError as e:
        logger.error(f"Erreur API OpenAI: {str(e)}")
        return jsonify({"error": "Erreur du service IA. Veuillez réessayer."}), 500
        
    except Exception as e:
        logger.error(f"Erreur inattendue: {str(e)}")
        return jsonify({"error": "Une erreur inattendue s'est produite"}), 500

@app.route('/health')
def health_check():
    """Endpoint de vérification de santé pour le déploiement"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "AI Chat Assistant"
    })

@app.route('/api/info')
def api_info():
    """Informations sur l'API"""
    return jsonify({
        "name": "AI Chat Assistant",
        "version": "1.0.0",
        "description": "Assistant IA conversationnel en français",
        "model": "gpt-3.5-turbo",
        "endpoints": {
            "chat": "/chat",
            "health": "/health"
        }
    })

@app.errorhandler(404)
def not_found(error):
    """Gestion des erreurs 404"""
    return jsonify({"error": "Page non trouvée"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Gestion des erreurs 500"""
    logger.error(f"Erreur serveur: {str(error)}")
    return jsonify({"error": "Erreur interne du serveur"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    logger.info(f"Démarrage du serveur sur le port {port}")
    logger.info(f"Mode debug: {debug}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)