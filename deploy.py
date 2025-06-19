#!/usr/bin/env python3
"""
Script de déploiement pour AI Assistant
Facilite le déploiement sur Render et la configuration
"""

import os
import sys
import subprocess
import secrets
from pathlib import Path

def print_banner():
    """Affiche la bannière du script"""
    print("""
🤖 AI Assistant - Script de Déploiement
========================================
    """)

def check_requirements():
    """Vérifie que tous les fichiers requis sont présents"""
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html',
        'README.md'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Fichiers manquants: {', '.join(missing_files)}")
        return False
    
    print("✅ Tous les fichiers requis sont présents")
    return True

def create_env_file():
    """Crée le fichier .env avec les variables d'environnement"""
    env_file = Path('.env')
    
    if env_file.exists():
        print("⚠️  Le fichier .env existe déjà")
        response = input("Voulez-vous le remplacer ? (y/N): ")
        if response.lower() != 'y':
            return
    
    # Générer une clé secrète
    secret_key = secrets.token_urlsafe(32)
    
    env_content = f"""# Configuration OpenAI
OPENAI_API_KEY=votre_clé_api_openai_ici

# Configuration Flask
SECRET_KEY={secret_key}
FLASK_ENV=development

# Configuration Serveur
PORT=5000
"""
    
    with open(env_file, 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print("✅ Fichier .env créé")
    print("⚠️  N'oubliez pas de remplacer 'votre_clé_api_openai_ici' par votre vraie clé API OpenAI")

def test_local():
    """Teste l'application localement"""
    print("\n🧪 Test local de l'application...")
    
    try:
        # Vérifier que les dépendances sont installées
        import flask
        import openai
        print("✅ Dépendances installées")
    except ImportError as e:
        print(f"❌ Dépendance manquante: {e}")
        print("Installez les dépendances avec: pip install -r requirements.txt")
        return False
    
    # Vérifier la clé API
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  Clé API OpenAI non configurée")
        print("Configurez votre clé API dans le fichier .env")
        return False
    
    print("✅ Configuration OK")
    return True

def git_setup():
    """Configure Git pour le déploiement"""
    print("\n📦 Configuration Git...")
    
    # Vérifier si Git est installé
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git n'est pas installé ou n'est pas dans le PATH")
        return False
    
    # Initialiser Git si nécessaire
    if not Path('.git').exists():
        subprocess.run(['git', 'init'], check=True)
        print("✅ Repository Git initialisé")
    
    # Ajouter tous les fichiers
    subprocess.run(['git', 'add', '.'], check=True)
    
    # Vérifier s'il y a des changements
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    if not result.stdout.strip():
        print("✅ Aucun changement à commiter")
        return True
    
    # Faire le commit
    subprocess.run(['git', 'commit', '-m', 'Update AI Assistant'], check=True)
    print("✅ Changements commités")
    
    return True

def deploy_instructions():
    """Affiche les instructions de déploiement"""
    print("""
🚀 Instructions de Déploiement sur Render
=========================================

1. Créez un compte sur Render.com
2. Cliquez sur "New +" → "Web Service"
3. Connectez votre repository GitHub
4. Configurez le service :
   - Name: ai-assistant
   - Environment: Python 3
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
   - Plan: Free

5. Variables d'environnement à configurer :
   - OPENAI_API_KEY: Votre clé API OpenAI
   - SECRET_KEY: (généré automatiquement)

6. Cliquez sur "Create Web Service"

Votre application sera accessible sur : https://votre-app.onrender.com

📝 Notes importantes :
- Assurez-vous que votre clé API OpenAI est valide
- Le déploiement prend 2-3 minutes
- L'application peut prendre quelques secondes à démarrer après inactivité
    """)

def main():
    """Fonction principale"""
    print_banner()
    
    if not check_requirements():
        sys.exit(1)
    
    # Menu interactif
    while True:
        print("\nOptions disponibles:")
        print("1. Créer le fichier .env")
        print("2. Tester l'application localement")
        print("3. Configurer Git")
        print("4. Afficher les instructions de déploiement")
        print("5. Quitter")
        
        choice = input("\nChoisissez une option (1-5): ").strip()
        
        if choice == '1':
            create_env_file()
        elif choice == '2':
            test_local()
        elif choice == '3':
            git_setup()
        elif choice == '4':
            deploy_instructions()
        elif choice == '5':
            print("👋 Au revoir !")
            break
        else:
            print("❌ Option invalide")

if __name__ == '__main__':
    main() 