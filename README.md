# 🤖 AI Assistant - Chat IA Français

Un assistant IA conversationnel moderne et élégant, développé avec Flask et OpenAI GPT-3.5-turbo.

## ✨ Fonctionnalités

- 💬 Interface de chat moderne et responsive
- 🎨 Design élégant avec animations fluides
- 🌐 Support complet en français
- 📱 Interface adaptée mobile et desktop
- ⚡ Réponses rapides et intelligentes
- 🔒 Gestion sécurisée des erreurs
- 📊 Logs détaillés pour le monitoring

## 🚀 Déploiement Rapide

### Prérequis

- Python 3.8+
- Compte OpenAI avec clé API
- Compte GitHub
- Compte Render (gratuit)

### Installation Locale

1. **Cloner le repository**
```bash
git clone <votre-repo-url>
cd app
```

2. **Créer un environnement virtuel**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configuration**
Créer un fichier `.env` à la racine du projet :
```env
OPENAI_API_KEY=votre_clé_api_openai_ici
SECRET_KEY=votre_clé_secrète_ici
FLASK_ENV=development
```

5. **Lancer l'application**
```bash
python app.py
```

L'application sera accessible sur `http://localhost:5000`

## 🌐 Déploiement sur Render

### 1. Préparer le Repository GitHub

1. Créer un nouveau repository sur GitHub
2. Pousser votre code :
```bash
git init
git add .
git commit -m "Initial commit - AI Assistant"
git branch -M main
git remote add origin https://github.com/votre-username/votre-repo.git
git push -u origin main
```

### 2. Déployer sur Render

1. Aller sur [render.com](https://render.com) et créer un compte
2. Cliquer sur "New +" → "Web Service"
3. Connecter votre repository GitHub
4. Configurer le service :
   - **Name** : `ai-assistant` (ou votre nom préféré)
   - **Environment** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn app:app`
   - **Plan** : Free

### 3. Variables d'Environnement

Dans les paramètres du service Render, ajouter les variables d'environnement :
- `OPENAI_API_KEY` : Votre clé API OpenAI
- `SECRET_KEY` : Une clé secrète aléatoire

### 4. Déploiement

Cliquer sur "Create Web Service" et attendre le déploiement (2-3 minutes).

Votre application sera accessible sur : `https://votre-app.onrender.com`

## 📁 Structure du Projet

```
app/
├── app.py              # Application Flask principale
├── requirements.txt    # Dépendances Python
├── templates/
│   └── index.html     # Interface utilisateur
├── .env               # Variables d'environnement (à créer)
├── .gitignore         # Fichiers à ignorer par Git
└── README.md          # Ce fichier
```

## 🔧 Configuration

### Variables d'Environnement

| Variable | Description | Requis |
|----------|-------------|--------|
| `OPENAI_API_KEY` | Clé API OpenAI | ✅ |
| `SECRET_KEY` | Clé secrète Flask | ❌ (défaut généré) |
| `FLASK_ENV` | Environnement Flask | ❌ (défaut: production) |
| `PORT` | Port du serveur | ❌ (défaut: 5000) |

### Modèle OpenAI

L'application utilise GPT-3.5-turbo par défaut. Pour changer le modèle, modifier la ligne dans `app.py` :

```python
model="gpt-4"  # ou "gpt-3.5-turbo"
```

## 🛠️ Développement

### Ajouter de Nouvelles Fonctionnalités

1. **Nouveaux endpoints** : Ajouter dans `app.py`
2. **Interface** : Modifier `templates/index.html`
3. **Styles** : Modifier le CSS dans le HTML

### Tests Locaux

```bash
# Tester l'API
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Bonjour, comment allez-vous ?"}'

# Vérifier la santé
curl http://localhost:5000/health
```

## 🔍 Monitoring

### Logs

L'application génère des logs détaillés :
- Requêtes utilisateur
- Réponses IA
- Erreurs et exceptions

### Endpoints de Monitoring

- `/health` : Statut du service
- `/api/info` : Informations sur l'API

## 🚨 Dépannage

### Erreurs Communes

1. **Clé API manquante**
   ```
   ValueError: La clé API OpenAI est requise
   ```
   Solution : Vérifier que `OPENAI_API_KEY` est définie dans `.env`

2. **Erreur de connexion**
   ```
   Erreur de connexion. Veuillez vérifier votre connexion internet.
   ```
   Solution : Vérifier la connectivité et la clé API

3. **Limite de taux dépassée**
   ```
   Limite de requêtes dépassée. Veuillez réessayer plus tard.
   ```
   Solution : Attendre ou vérifier votre quota OpenAI

### Support

Pour toute question ou problème :
1. Vérifier les logs de l'application
2. Tester l'endpoint `/health`
3. Vérifier la configuration des variables d'environnement

## 📄 Licence

Ce projet est sous licence MIT. Libre d'utilisation et de modification.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

---

**Développé avec ❤️ en utilisant Flask et OpenAI** 