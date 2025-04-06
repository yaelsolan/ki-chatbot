# 🤖 Simulierter KI-Chatbot (Demo-Version ohne API)

print("🤖 Willkommen! Dies ist ein einfacher (simulierter) KI-Chatbot.")
print("Du kannst mit mir schreiben. Zum Beenden: 'exit'")

antworten = {
    "hallo": "Hallo! Wie kann ich dir helfen?",
    "was ist künstliche intelligenz": "Künstliche Intelligenz ist die Fähigkeit von Maschinen, Aufgaben zu lösen, die normalerweise menschliche Intelligenz erfordern.",
    "was ist der unterschied zwischen ki und ml": "KI ist der Überbegriff. Maschinelles Lernen (ML) ist ein Teil davon, der sich auf das Lernen aus Daten konzentriert.",
    "nenn mir ein beispiel für ml": "Ein Beispiel für ML ist ein Spamfilter, der aus bisherigen E-Mails lernt.",
    "wie kann ich ki im alltag nutzen": "Du kannst KI in Sprachassistenten, Navigationssystemen oder bei Produktempfehlungen nutzen.",
    "danke": "Gern geschehen!",
}

while True:
    frage = input("Du: ").lower()
    if frage == "exit":
        print("Chatbot: Auf Wiedersehen!")
        break

    antwort = antworten.get(frage, "Das habe ich leider nicht verstanden.")
    print("Chatbot:", antwort)
