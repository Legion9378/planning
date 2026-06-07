# Storytelling & Video Workflow für CJ & Josie (Version 1.0)

## Ziele
- Private NSFW Storytelling-Drafts in Englisch (nur für Björn)
- Szenenweise Struktur für kleine Audio-Chunks
- Konsistente weibliche Stimmen (CJ & Josie) mit Referenzaudio
- Video: Sitzende Vorleserin im Sessel + wechselnde statische Hintergrundbilder
- Ressourcenschonend auf Xubuntu 24.04 + später KI-Netzwerk

## 1. Story Generation
- Vollständig NSFW-fähig in Englisch
- Szenenweise; die Szenenlaenge folgt dem Inhalt, grob von sehr kurz bis etwa fuenf Minuten Audio.
- Jede Szene wird zuerst als fast finale Kapitel-Szene geschrieben und enthaelt zusaetzlich TTS-Direktiven.
- TTS-Marker koennen Sprecher, Narrator, Betonung, Aussprachehilfen und Synthesehinweise steuern.
- Nach Review/Rewrite entstehen nacheinander zwei Fassungen:
  - TTS-Script mit Markern.
  - Lesefassung ohne Marker fuer das Kapitel.
- Es gibt keinen separaten Polishing-Step ausserhalb der Workflow-Kontrollschritte.

## 2. TTS Pipeline
- Referenzaudio pro Charakter (einmal aufnehmen oder generieren)
- Optionen:
  - Lokale Lösungen (Piper TTS, StyleTTS 2, Tortoise-TTS)
  - Online (ElevenLabs - sehr gute Qualität, Clone-Funktion)
  - Später: Direkter Aufruf über KI-Netzwerk
- TTS muss nicht zwingend KI-basiert sein. Entscheidend ist ein brauchbarer Audiobook-Workflow mit Dateiausgabe, Deutsch/Englisch und spaeterer Konvertierbarkeit.
- Historischer Bezug: Unter Windows XP funktionierte bereits ein Workflow mit `Text-to-Speech 3`, MP3-Ausgabe und optional ruhiger Hintergrundmusik.
- Mehrstimmige Dialoge bleiben als spaetere Formatidee erhalten. Dafuer braucht der Text klare Dialog-/Voice-Marker, statt manuell aus Chat-Apps kopiert zu werden.
- Zielpfad: Storytext -> Audiobook-Skript -> TTS/Mehrstimmen-Ausgabe -> Mixing -> optionales Video mit bis zu drei Hosts/Lesenden.
- Piper, Coqui und weitere TTS-Loesungen bleiben Testkandidaten. Coqui wird nicht automatisch ausgeschlossen, aber als Wartungsrisiko markiert, weil es seit einiger Zeit nicht mehr aktiv weiterentwickelt wird.
- Der Mac Mini ist nicht als TTS-Host eingeplant; er bleibt fuer OpenCode und Agent Brain im KI-Netzwerk reserviert.

## 3. Video Production
- Avatar-Bild (sitzend im Sessel)
- Statische Hintergrundbilder pro Szene
- Tools-Empfehlung:
  - **CapCut** (einfach, gut für Mobile + Desktop)
  - **Shotcut** oder **DaVinci Resolve** (kostenlos auf Linux)
  - iMovie + GarageBand auf iPad als Alternative

## 4. Musik und Hintergrundaudio

- Ace Step 1.5 ist als Open-Source-Alternative zu Suno AI ein wieder aufzunehmender Testkandidat.
- Frueherer Test scheiterte an einem Gradio-Fehler; dieser Fehler wurde kurz vor dem Ausfall der internen SSD gefunden, aber nicht mehr praktisch nachgetestet.
- Naechster Schritt: Installation/Test wiederholen und Gradio-Version, Startfehler, Logs und Fix dokumentieren.
- Offen: weitere Tools fuer Audiodateien, nutzbare Hintergrundmusik und loopbare Tracks recherchieren.
- GarageBand bleibt fuer spaeteres manuelles Mixing relevant.

## 5. Technik
- Laptop: Xubuntu 24.04 LTS
- Spätere Verlagerung ins KI-Netzwerk
- Verarbeitung ist als CPU-basierter Workflow zu planen; keine nutzbare iGPU, dGPU oder eGPU voraussetzen.

## 6. Collector-Jobflow

- Ein OpenFang-inspirierter Collector bleibt als spaeterer eigener Jobflow vorgesehen.
- Zweck: semi-automatische Informationssammlung fuer Story-Grundlagen, Crossover-Lore, Quellenlisten und andere Projektkontexte.
- Der Collector kann andere Jobflows vorbereiten, laeuft aber mit eigenem State und eigener Review-Grenze.
- Collector-Ergebnisse sind Input, keine automatisch uebernommene Wahrheit.

Weitere Details werden ergänzt.
