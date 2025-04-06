# 🤖 KI-Chatbot mit OpenAI

Ein praktisches Lernprojekt zur Erstellung eines einfachen KI-Chatbots mit Python.  
Das Projekt demonstriert die Nutzung der OpenAI-API sowie eine alternative lokale Demo-Version – ideal für Einsteigerinnen im Bereich Künstliche Intelligenz.

---

## 🧠 Funktionen

| Version | Beschreibung |
|--------|--------------|
| `KI_Chatbot_OpenAI.py` | Verbindet sich mit der OpenAI-API (z. B. GPT-3.5-Turbo) und simuliert einen echten KI-Chat. |
| `KI_Chatbot_OpenAI_Mockversion.py` | Eine lokal laufende Version mit vordefinierten Antworten – ohne API-Key, ideal zum Testen und Präsentieren. |

---

## ▶️ Ausführen (mit OpenAI-API)

1. Bibliothek installieren:
```bash
pip install openai
```

2. Persönlichen API-Key bei OpenAI erstellen:  
   [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

3. Im Code den Key einfügen:
```python
client = OpenAI(api_key="DEIN_API_KEY_HIER")
```

4. Starten:
```bash
python KI_Chatbot_OpenAI.py
```

---

## 🟨 Alternativ: Demo-Version ohne API

Einfach ausführen:

```bash
python KI_Chatbot_OpenAI_Mockversion.py
```

> Diese Version enthält feste Antworten und funktioniert offline.

---

## 💡 Lernziele

- Einstieg in die Nutzung von Sprachmodellen per API
- Verarbeitung von Nutzereingaben
- Simpler Konsolen-Dialog mit KI-Systemen
- Abgrenzung zwischen echter API-Nutzung und lokaler Simulation

---

👩‍💻 Entwickelt von Yael Solan  
📅 April 2025  
🔗 [GitHub-Profil ansehen](https://github.com/yaelsolan)
