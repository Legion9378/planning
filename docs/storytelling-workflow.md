# Storytelling & Video Workflow für CJ & Josie (Version 1.0)

## Ziele
- Private NSFW Storytelling-Drafts in Englisch (nur für Björn)
- Szenenweise Struktur für kleine Audio-Chunks
- Konsistente weibliche Stimmen (CJ & Josie) mit Referenzaudio
- Video: Sitzende Vorleserin im Sessel + wechselnde statische Hintergrundbilder
- Ressourcenschonend auf Xubuntu 24.04 + später KI-Netzwerk

## 1. Story Generation
- Vollständig NSFW-fähig in Englisch
- Szenenweise (max 200-400 Wörter pro Chunk)
- Jede Szene enthält TTS-Direktiven (Emotion, Pace, Tone, Pausen)

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

Weitere Details werden ergänzt.
