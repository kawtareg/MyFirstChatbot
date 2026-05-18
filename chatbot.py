import os
import json
from openai import OpenAI, APIConnectionError
from dotenv import load_dotenv
from config import SYSTEM_PROMPT, MODEL, TEMPERATURE
from datetime import datetime

os.environ["NO_PROXY"] = "*"

load_dotenv()

client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="ollama",
)


def init_messages() -> list[dict]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
    ]

def stream_response(messages: list[dict]) -> str:
    full_reply = ""
    
    response = client.chat.completions.create(
            model=MODEL,
            temperature= TEMPERATURE,
            messages = messages,
            stream = True
        )
    
    for chunk in response:
        token = chunk.choices[0].delta.content
        if token is not None:
            print(token, end="", flush=True)
            full_reply += token
    
    print()
    return full_reply

def save_history(messages) -> str:
    os.makedirs("history", exist_ok=True)
    filepath = f"history/{datetime.now().strftime('%Y-%m-%d_%H-%M')}.json"    
    data = [m for m in messages if m["role"] != "system"]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return filepath

def chat() -> None:
    print("---------------")
    print("Entrez une requete après >>>, quit pour quitter, reset pour remettre à 0 la mémoire du chatbot et save pour enregistrer l'historique des conversations.")
    print("---------------\n")
    messages = init_messages()

    while True:
        query = input(">>>:").strip()

        if not query:
            continue

        if query == "reset":
            messages = init_messages()
            print("--- Mémoire réinitialisée ---\n")
            continue

        if query == "quit":
            break

        if query == "save":
            file_path = save_history(messages)
            print("Sauvegardé: ", file_path)
            continue

        messages.append({"role": "user", "content": query})

        try:
            reply = stream_response(messages)
            messages.append({"role": "assistant", "content": reply})

        except APIConnectionError:
            print("Erreur : Ollama n'est pas lancé. Fais 'brew services start ollama'")
            messages.pop()

        except Exception as e:
            print(f"Erreur inattendue : {e}")
            messages.pop()