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

## 2. Modellprofile und Story-Rollen

- Quelle: Chat-History `chatgpt-interne-gedankengange-bei-deepseek-2026-05-07T01-25-39-774Z`.
- Status: Planungsregel; konkrete LocalAI-/Modellrunner-Pfade muessen spaeter gegen die aktuelle Installation geprueft werden.
- Grundregel: Storyarbeit wird nicht ueber ein einzelnes Universalprofil geplant, sondern ueber getrennte Rollen/Profile.
- Vorgesehene Profile:
  - SFW-Storyprofil fuer oeffentliche/YouTube-taugliche Fassungen;
  - privates NSFW-Storyprofil fuer interne Rohfassungen;
  - Lore-/Worldbuilding-Profil fuer Kanon, Crossover-Regeln, Kontinuitaet und Power-Scaling;
  - Kapitelgenerator-Profil fuer lange, konsistente Kapitel mit definierter Ausfuehrlichkeit;
  - Rewrite-/Public-Fassung-Profil fuer Entschaerfung auf PG-13, PG-16 oder eine spaeter festgelegte Zielstufe;
  - Web-/Blog-/Begleittext-Profil fuer Website, Medium, Substack und Projekttexte.
- Inspirationsangaben werden als Stil- und Strukturhinweise genutzt, nicht als Kopierauftrag.
- Sichtbare Reasoning-/Gedankengang-Ausgaben duerfen nur als Diagnosematerial behandelt werden; Entscheidungen brauchen Quellen, Tests, Review oder menschliche Freigabe.
- Beispiel fuer spaeteres Story-Profiling:
  - Stil-/Strukturinspiration aus `Balancing Realities`, `Beginning a New Path`, `A Third Path To The Future` und Autorenmix stargatesg1fan1, vimesenthusiast, robst, Rorschach's Blot;
  - Realitaetswechsel-Mechanik angelehnt an `Sliders`, aber ohne Zeitlimit;
  - danach folgen Crossover-Liste, Grundmechanik, Power-Scaling, Ton und Beschraenkungen.

## 3. Action- und Humor-Regel

- Quelle: Chat-History `chatgpt-jobflow-fur-ki-projekte-2026-05-07T01-52-30-533Z.md`.
- Status: verbindliche Story-DNA fuer Action-Szenen.
- Grundregel: Action bleibt erdnah, physisch plausibel, lesbar und konsequenzbewusst.
- Gewalt ist situativ und funktional; Wirkung zaehlt mehr als Spektakel.
- Humor ist erlaubt, wenn er punktuell, kurz und aus Charakterdynamik, Timing oder physischem Kontrast entsteht.
- Vergleich: Avengers-Timing ja, Deadpool-Dauerfeuer nein.
- Nicht erlaubt:
  - Meta-Humor oder Durchbrechen der vierten Wand;
  - Slapstick-Framing als Grundton;
  - cartoonhafte Gewalt-Eskalation;
  - Gags, die Spannung, Stakes oder Konsequenzen zerstoeren.
- Reviewer prueft: Kippt die Szene in Albernheit? Zerstoert der Gag Spannung oder Konsequenzen?

## 4. TTS Pipeline
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
- TTS-Auswahl muss budgetschonend erfolgen: zuerst kostenlose, lokale oder sehr guenstige Loesungen pruefen; keine kostenpflichtigen Cloud-/Abo-Dienste als Default.
- Sprachfokus fuer Story-/Content-Betrieb: Deutsch und Englisch. Aeltere mehrsprachige Pi5-/Translator-Modellmappings werden nicht weitergefuehrt.
- TTS-Regie ist sprachspezifisch: Deutsche und englische Fassungen brauchen eigene Aussprache-, Betonungs-, Pausen- und Sprecherhinweise statt blinder Uebernahme aus der jeweils anderen Sprache.
- TTS-/Voice-Reader-Woerterbuecher muessen gegen die konkrete Ziel-App-Syntax formatiert werden. Keine Standardannahmen uebernehmen: erst Doku oder funktionierendes Beispiel pruefen, dann mit 2-3 Eintraegen testimportieren, danach groessere Listen erzeugen. Fuer Voice Dream Reader ist jeder Eintrag als eigene Zeile noetig; zusammengeklebte Eintraege oder nicht akzeptierte Kommentarzeilen verhindern den Import.


### Masterdraft, TTS-Tags und kontextabhaengige Aussprache

- Quelle: Chat-History `chatgpt-youtube-video-analyse-2026-05-07T03-13-02-534Z.md`.
- Ein Masterdraft darf sparsame TTS-Tags enthalten, muss aber weiterhin wie ein normaler Originaltext lesbar bleiben.
- Aus dem Masterdraft entstehen zwei Outputs:
  - TTS-Version: Aussprache-, Rhythmus- und Pausenoptimierung fuer Audio;
  - Clean-Kapitel/Roman-Version: geglaettet, ohne TTS-Tags, mit originaler Schreibweise.
- Minimaler Start-Tag-Satz:
  - `[TTS:pause=short]`
  - `[TTS:pause=long]`
  - `[TTS:pronounce=Name->Aussprache]`
  - `[TTS:emphasis=word]`
  - `[TTS:speed=slow]`
- Tags werden sparsam gesetzt: Namen, problematische Aussprache, Pausen, Schluesselstellen. Keine Tags in jeden Satz und keine erzwungene Emotionssteuerung.
- Aussprache-Mapping ist kontextabhaengig, nicht nur wortbasiert. Dasselbe Schriftbild kann je nach Figur, Geschlecht, Canon oder Sprache anders ausgesprochen werden.
  - Beispiel: `Jean-Luc Picard` und `Jean Delacour` -> maskulin/franzoesische Aussprache.
  - Beispiel: `Jean Grey` -> feminin/englische Aussprache.
- Ausspracheersetzungen gelten nur fuer die TTS-Version. Die Clean-Kapitelversion behaelt die korrekte Originalschreibweise.
- Vor Massenerzeugung muessen TTS-Tags und Pronunciation-Mappings gegen das konkrete Zieltool getestet werden.


### Drei-Sprecherinnen-Szenenlesung fuer Audio und Video

- Quelle: Chat-History `chatgpt-zusammenfassung-der-konversation-2026-05-07T08-35-19-932Z.md` plus Bjoerns Korrektur.
- Fuer Story-Vertonungen sind drei Sprecherinnen/Hosts geplant: CJ, Josie und Daphne.
- Startziel ist keine komplexe Multispeaker-Dialogproduktion mit vielen Figurenstimmen, sondern eine szenenweise Lesung:
  - eine Sprecherin liest eine Szene;
  - pro Szene werden emotionale Einstellungen gesetzt;
  - leicht hoerbare Atempausen duerfen zur Natuerlichkeit beitragen;
  - danach Wechsel zur naechsten Szene/Sprecherin.
- Vorteil: Die TTS-Synthese bleibt einfacher, weil nicht innerhalb jeder Szene staendig Sprecherrollen gewechselt werden muessen.
- Produktionslogik:
  1. Szene als eigenen Audio-Chunk rendern.
  2. Emotion, Tempo, Pausen und Aussprache pro Szene pruefen.
  3. Szenen-Audios zusammenlegen.
  4. Ambientsound/Hintergrundatmo darunterlegen.
  5. Die finale Audiospur als Vorlage fuer das Video verwenden.
- Tooling fuer Zusammenlegen/Mixing bleibt offen: ffmpeg, Audacity, pydub oder spaeter passende Pipeline-Tools pruefen.
- Konkrete TTS-Modelle/Provider werden nicht aus alten Coqui-/YourTTS-/Bark-/XTTS-Listen uebernommen, sondern frisch gegen Qualitaet, Kosten, Wartbarkeit, Stimmeignung und Deutsch/Englisch getestet.


### Voice-Cloning-Grenzen und charakterbasierte Stimmen

- Quelle: Chat-History `chatgpt-hailo-10-hat-pi-5-2026-05-07T01-46-48-306Z.md`.
- Standard fuer Story-/Audiobook-Stimmen sind generische, selbst gestaltete oder charakterbasierte Stimmen, nicht erkennbare Imitationen realer Personen.
- Fuer CJ, Josie und Daphne sollen eigene charakterbasierte Stimmen entstehen; sie duerfen nicht nach bekannten Sprecherinnen, Schauspielerinnen oder anderen realen Personen benannt oder vermarktet werden.
- Voice-Cloning ist nur in klar legitimen Faellen akzeptabel:
  - Bjoern nutzt seine eigene Stimme mit eigener Stimmprobe;
  - eine Person hat ausdruecklich zugestimmt;
  - assistive Nutzung mit klarer Zweckbindung, z. B. bessere Verstaendlichkeit fuer die betroffene Person;
  - keine Taeuschung ueber Identitaet oder Urheberschaft.
- Nicht erlaubt als Default:
  - Stimmen realer Personen ohne Zustimmung nachbauen;
  - Marketing wie "klingt wie <bekannte Person>";
  - absichtliche Annaherung an reale Sprecherinnen/Sprecher;
  - Voice-Cloning als Ersatz fuer Rechteklaerung.
- Generische TTS-Stimmen und leichte Anpassungen von Pitch, Tempo oder Klangfarbe innerhalb einer nicht-identitaetsnahen Stimme sind der risikoaermere Standard.

## 5. Video Production
- Avatar-Bild (sitzend im Sessel)
- Statische Hintergrundbilder pro Szene
- Tools-Empfehlung:
  - **CapCut** (einfach, gut für Mobile + Desktop)
  - **Shotcut** oder **DaVinci Resolve** (kostenlos auf Linux)
  - iMovie + GarageBand auf iPad als Alternative

## 6. Musik und Hintergrundaudio

- Ace Step 1.5 ist als Open-Source-Alternative zu Suno AI ein wieder aufzunehmender Testkandidat.
- Frueherer Test scheiterte an einem Gradio-Fehler; dieser Fehler wurde kurz vor dem Ausfall der internen SSD gefunden, aber nicht mehr praktisch nachgetestet.
- Naechster Schritt: Installation/Test wiederholen und Gradio-Version, Startfehler, Logs und Fix dokumentieren.
- Offen: weitere Tools fuer Audiodateien, nutzbare Hintergrundmusik und loopbare Tracks recherchieren.
- GarageBand bleibt fuer spaeteres manuelles Mixing relevant.

## 7. Technik
- Laptop: Xubuntu 24.04 LTS
- Spätere Verlagerung ins KI-Netzwerk
- Verarbeitung ist als CPU-basierter Workflow zu planen; keine nutzbare iGPU, dGPU oder eGPU voraussetzen.

## 8. Collector-Jobflow

- Ein OpenFang-inspirierter Collector bleibt als spaeterer eigener Jobflow vorgesehen.
- Zweck: semi-automatische Informationssammlung fuer Story-Grundlagen, Crossover-Lore, Quellenlisten und andere Projektkontexte.
- Der Collector kann andere Jobflows vorbereiten, laeuft aber mit eigenem State und eigener Review-Grenze.
- Collector-Ergebnisse sind Input, keine automatisch uebernommene Wahrheit.

Weitere Details werden ergänzt.

## 9. Character-Style-Regel fuer Bildgenerierung

- Quelle: Chat-History `chatgpt-fast-dllm-und-vision-modelle`.
- Status: als Regel uebernommen.
- KB-Verweis: `llm-wiki/kb/character-style-80s-cel-realistic-anatomy.md`.
- Grundregel: Zeichentrickstil in der Linienfuehrung, reale Anatomie in den Proportionen.
- Stilziel: 80er-Cel-Look mit frueher 90er-Anime-Influenz, aber ohne moderne Anime-Uebertreibung.
- Normalstandard:
  - realistische menschliche Proportionen;
  - natuerliche Beinlaenge;
  - ausgewogenes Torso-/Bein-Verhaeltnis;
  - biologisch plausible Teen- und Erwachsenenentwicklung;
  - keine ueberzogene Oberweite, Taille, Huefte, V-Form oder Superheldenmuskelung.
- Crossover-Override:
  - Marvel-/DC-/Superheldenkoerper sind nur erlaubt, wenn das Crossover explizit danach verlangt.
  - Der Override ist Ausnahme, nicht Standard.
- CPU-first-Hinweis:
  - Realistischere, weniger extreme Proportionen gelten als bildgenerierungsfreundlicher, weil sie weniger extreme Schatten, Kanten und Koerpervolumen erzwingen.

## 10. Image-Prompt-Feldstruktur

- Bildprompt-Generatoren muessen das Zielinterface beachten: Positive Prompt, Negative Prompt und ggf. Style-/LoRA-/Embedding-/Workflow-Felder.
- Positive Prompt wird modular aus `STYLE_CORE + FOCUS_PROFILE + SCENE_CONTENT` aufgebaut.
- Negative Prompt enthaelt nur unerwuenschte Merkmale und wird nicht mit positiven Stil-/Szenenteilen vermischt.
- Fuer EasyDiffusion gilt: Positive Prompt und Negative Prompt jeweils einzeilig halten; jede neue Zeile wird als neues Bild interpretiert.
- EasyDiffusion unterstuetzt CPU, bietet aber keine API/Webhooks fuer Josie. ComfyUI-CPU ist als naechster API-faehiger Bildworkflow-Pfad vorgesehen.
- Detailregel: `planning/docs/image-generation-prompt-field-structure.md`.

## 11. Content-Werkbank fuer Story, YouTube, Audiobook, Medium und Substack

- Quelle: Chat-History `chatgpt-github-und-agenthub-integration`.
- Status: als allgemeine Jobflow-Regel uebernommen.
- Grundregel: Content-Creation nutzt eine semipersistente Werkbank mit Reviewer-Checks, keine technische Sandbox wie beim Coding.
- Gilt fuer:
  - Storywriting;
  - YouTube-Skripte, Videostruktur, Titel/Thumbnail-/Beschreibungsvorbereitung;
  - Audiobook-Skripte, TTS-Fassungen, Kapitel-/Szenenfassungen;
  - Medium-Artikel;
  - Substack-Posts und Newsletter.
- Standardstruktur:
  - `state.json` fuer Jobstatus, aktuellen Abschnitt, offene Punkte und Artefaktpfade;
  - `brief/` fuer Auftrag, Zielgruppe, Plattform und Nicht-Ziele;
  - `outline/` fuer Struktur, Hook, Kapitel/Sektionen, CTA;
  - `drafts/` fuer versionierte Entwuerfe;
  - `research/` fuer Quellen und Material;
  - `analysis/` fuer Agentenanalysen;
  - `reviewer_feedback/` fuer Stil-, Fakten-, Rechte-, Plattform- und Qualitaetschecks;
  - `assets/` fuer Bilder, Audio, Thumbnails, Referenzen;
  - `platform_exports/` fuer plattformspezifische Fassungen;
  - `final/` fuer finalisierte Drafts.
- Reviewer ersetzen die Sandbox:
  - Story: Lore/Kanon, Stil, Ton, Kontinuitaet, Alters-/Content-Regeln.
  - YouTube: Hook, Watchtime-Struktur, Kapitel, visuelle Hinweise, Beschreibung, Titel/Thumbnail-Fit.
  - Audiobook: Sprecherrollen, TTS-Marker, Aussprache, Szenenlaenge, Audio-Tauglichkeit.
  - Medium/Substack: These, Lesefluss, Quellen, Ueberschriften, CTA, Publikationsrisiko.
- Reviewer liefern Feedback; Aenderungen passieren wieder in der Werkbank.
- Finalisierung erzeugt Draft-/Publish-Artefakte, aber keine automatische Veroeffentlichung ohne Freigabe.

## 12. Ruhrpottplatt-Fanfiction-Idee

- Quelle: Chat-History-Datei `chatgpt-ruhrpottplatt-siri-spruche-2026-05-07T01-27-34-643Z.md` wurde nicht besprochen; die Datei selbst enthaelt keine zu uebernehmende Detailplanung.
- Neue Idee von Bjoern: Fanfiction-Uebersetzungen in Ruhrpottplatt.
- Stilprinzip: grob vergleichbar mit Hennes Benders Asterix-Uebertragungen, nicht als exakte Kopie, sondern als Hinweis auf Tonalitaet, Dialektuebertragung und humorvolle Lokalisierung.
- Als spaeterer Content-/Story-Workflow-Kandidat fuehren; keine sofortige Umsetzung.


## 13. Rollenbasiertes Multimodell-Routing

- Quelle: Chat-History `chatgpt-turboquant-auf-cpu-nutzung-2026-05-07T07-47-25-193Z.md`.
- Detailplanung: `planning/docs/hermes-multimodell-routing.md`.
- Grundregel: Story- und Agentenarbeit wird nicht auf ein einzelnes Hybridmodell optimiert, sondern ueber Rollen/Profile geroutet.
- Rollen: creative/draft, structure/reasoning, agent/tools, validator/reviewer.
- Konkrete Deckard-/Heretic-/Gemma-/Hermes-Modellnamen aus alten Chats sind nur historische Kandidaten und muessen vor Einsatz frisch gegen Hardware, Runtime, Lizenz, Kontextfenster und Qualitaet geprueft werden.
- Private Rohentwuerfe duerfen andere Modelle nutzen als oeffentliche Fassungen; YouTube-/Publishing-Fassungen brauchen Rewrite und Review auf Zielstufe.
