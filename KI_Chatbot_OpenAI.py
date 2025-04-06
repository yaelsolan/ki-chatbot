# 🤖 KI-Chatbot mit OpenAI – kompatibel mit openai>=1.0.0

import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

# 📌 Setze deinen OpenAI API-Schlüssel hier ein
client = OpenAI(api_key="DEIN_API_KEY_HIER")


# 🧠 Start des Chats
print("🤖 Willkommen! Dies ist ein einfacher KI-Chatbot (zum Beenden: 'exit')")

messages: list[ChatCompletionMessageParam] = []

while True:
    frage = input("Du: ")
    if frage.lower() == "exit":
        print("Chatbot: Auf Wiedersehen!")
        break

    messages.append({"role": "user", "content": frage})

    try:
        antwort = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        inhalt = antwort.choices[0].message.content
        print("Chatbot:", inhalt.strip())
        messages.append({"role": "assistant", "content": inhalt})
    except Exception as e:
        print("Fehler bei der API-Anfrage:", str(e))
