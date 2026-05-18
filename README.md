# MyFirstChatbot: Chef Cuisinier

Chatbot conversationnel en CLI qui joue le rôle d'un chef cuisinier français étoilé. Tourne entièrement en local grâce à [Ollama](https://ollama.com) — aucune clé API, aucun coût.

> Projet réalisé dans le cadre d'un apprentissage de l'agentique et des LLMs — 4ème année ingénierie informatique, INSA Rouen.

---
## Démo

![Démo du chatbot](assets/demo_chatbot.gif)

---

## Fonctionnalités

- Conversation multi-tour avec mémoire de l'historique
- Streaming de la réponse mot par mot
- Commande `reset` pour réinitialiser la mémoire
- Commande `save` pour sauvegarder la conversation en JSON
- Commande `quit` pour quitter
- Personnalité configurable via `config.py`
- Gestion des erreurs API

---

## Stack technique

| Outil | Rôle |
|---|---|
| Python 3.12 | Langage |
| [Ollama](https://ollama.com) | Inférence locale |
| Mistral 7B | Modèle de langage |
| openai SDK | Client API (compatible Ollama) |
| python-dotenv | Gestion des variables d'environnement |

---

## Installation

### Prérequis

- Mac avec [Homebrew](https://brew.sh) ou équivalent
- Python 3.12+

### 1. Clone le projet

```bash
git clone https://github.com/TON_PSEUDO/chatbot-llm
cd chatbot-llm
```

### 2. Installe Ollama et le modèle

```bash
brew install ollama
brew services start ollama
ollama pull mistral
```

### 3. Crée l'environnement Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Lance le chatbot

```bash
python3 main.py
```

---

## Utilisation

```
Entrez une requête après >>>, quit pour quitter,
reset pour remettre à 0 la mémoire, save pour enregistrer.

>>> Bonjour, qui es-tu ?
>>> Donne moi une recette de blanquette de veau
>>> save
>>> reset
>>> quit
```

Les conversations sauvegardées sont stockées dans `history/` au format JSON.

---

## Structure du projet

```
chatbot-llm/
├── main.py          # point d'entrée
├── chatbot.py       # logique du chatbot (streaming, historique, commandes)
├── config.py        # system prompt et paramètres du modèle
├── requirements.txt
├── history/         # conversations sauvegardées (ignoré par git)
│   └── .gitkeep
└── .gitignore
```

---

## Personnalisation

Modifie `config.py` pour changer la personnalité du chatbot :

```python
MODEL = "mistral"       # ou llama3, phi3, gemma...
TEMPERATURE = 0.3       # 0 = réponses stables, 1 = créatif

SYSTEM_PROMPT = """Tu es un chef cuisinier français étoilé...."""
```

Tu peux aussi remplacer `mistral` par n'importe quel modèle disponible sur Ollama :

```bash
ollama pull llama3
ollama pull phi3
ollama pull gemma
```

---

## Ce que j'ai appris

- Appels API LLM avec le SDK openai
- Gestion de l'historique de conversation (format `messages`)
- Streaming token par token
- Séparation de la logique en modules Python
- Persistance de données en JSON
- Gestion d'erreurs robuste avec `try/except`

---

## Prochaines étapes

- [ ] Implémenter un système RAG pour donner accès à des recettes externes
- [ ] Passer à un agent capable de rechercher des recettes en ligne

---

## Auteur

**Kawtar El Gueddari** — [GitHub](https://github.com/kawtareg) · INSA Rouen Normandie
