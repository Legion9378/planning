# KI-Artikel und Modellclaim Bewertungsregel

Stand: 2026-07-07
Status: Planungsregel
Quelle: Chat-History `chatgpt-ki-netzwerk-mit-nodes-2026-05-07T02-08-50-725Z.md`

## Kurzthese

KI-Artikel, Modellclaims und "X ist tot"-Schlagzeilen werden nicht als Architekturentscheidung uebernommen. Erst wird das Strukturprinzip extrahiert, dann gegen Bjoerns reale Hardware, Tooling, Wartbarkeit und Zielarchitektur geprueft.

## Hype-Artikel-Filter

Schlagzeilen wie:

- "RAG ist tot"
- "Prompt Engineering ist tot"
- "Fine-Tuning ist tot"
- "kleines Modell schlaegt GPT-4"
- "Image without GPU"
- "CPU-only 3x schneller"

bedeuten selten, dass eine Technik wirklich tot oder allgemein ueberlegen ist. Meist geht es um:

- einen Spezialfall;
- einen engen Benchmark;
- eine andere Retrieval-/Memory-Strategie;
- ein kleineres oder staerker strukturiertes Aufgabenprofil;
- Tokenreduktion statt echter Inferenzbeschleunigung;
- andere Hardwarevoraussetzungen;
- Marketing-Framing.

## RAG-Begriff sauber lesen

Wenn Artikel von "RAG" sprechen, meinen sie meistens klassisches RAG mit Vector-DB, oft eventuell kombiniert mit Graph-DB.

Bjoerns LLM-Wiki-Arbeit ist ebenfalls RAG-artig, aber anders umgesetzt:

- file-first / Markdown-first;
- Quellen, Notizen, KB-Seiten und Register statt primaer Vektorindex;
- explizite Links, Logs und Quellenentscheidungen;
- Suche/Index/Session-Kontext statt automatisch vorausgesetzter Vector-DB;
- strukturierter Recall ueber kuratierte Dateien.

Daraus folgt:

- "RAG ist tot" darf nicht auf alle retrieval-/knowledge-basierten Verfahren uebertragen werden.
- Es kann bedeuten: Ein bestimmtes Vector-DB-RAG-Muster ist ineffizient oder wird durch strukturierteren Memory/Page-Index/DB-State ersetzt.
- LLM-Wiki ist kein Gegenbeispiel zu RAG, sondern eine andere, kuratierte RAG-/Knowledge-Base-Form ohne Vector-DB als Pflicht.

## Spezialmodell vs. Allroundmodell

Wenn ein kleines Modell ein grosses Allroundmodell scheinbar schlaegt, zuerst pruefen:

- Welcher Benchmark?
- Wie eng ist die Aufgabe?
- Wurde der Input stark vorstrukturiert?
- Gab es Retrieval, Tooling, Vorverarbeitung oder Routing?
- Ist das Modell allgemein besser oder nur fuer diesen Spezialfall?

Regel: Spezialmodell-Erfolg ist kein Beweis fuer allgemeine Ueberlegenheit.

## Hardware-first-Pruefung

Vor jeder Uebernahme steht Bjoerns Hardware-Frage:

> Kann ich das mit meiner vorhandenen Hardware sinnvoll machen?

Prueffragen:

1. Welche Hardware wurde im Artikel genutzt?
2. CPU-only wirklich CPU-only oder versteckte GPU/AVX/Spezialhardware?
3. Welche Modellgroesse und Parameteranzahl?
4. Welche RAM-/VRAM-Anforderung?
5. Welche Quantisierung?
6. Welches Kontextfenster / Token Window?
7. Spezialmodell oder generisches Modell?
8. Welche Runtime / Runner / Betriebssystemannahmen?
9. Bleibt die Qualitaet erhalten oder wurde Geschwindigkeit gegen Qualitaet getauscht?
10. Realer Workflow oder synthetischer Benchmark?

## Relevante echte Hebel fuer Bjoerns Setup

Besonders interessant sind Claims zu:

- besserer Quantisierung bei gleicher Qualitaet;
- geringerem RAM-Footprint;
- effizienterer CPU-Inferenz;
- KV-Cache-Optimierung;
- schnellerer Prefill-Phase;
- CPU-tauglichem spekulativem Decoding;
- Token-Caching bei wiederholten Prompts;
- Prompt-Kompression;
- Token-Einsparung ohne Qualitaetsverlust;
- geringerem Modellwechsel-Overhead;
- klarer Tool-/Worker-/Routing-Architektur.

Weniger relevant als Startsignal:

- reine CUDA-/GPU-Kernel-Optimierung;
- 70B/100B/mehr-Parameter-Marketing;
- Benchmark-Siege ohne lokale Laufbarkeit;
- Artikel, die 32 GB+ RAM allein fuer das Modell voraussetzen, wenn Zielnode deutlich darunter liegt.

## Systemarchitektur schlaegt rohe Parameterzahl

Viele sehen nur das Hauptmodell im Chat. In agentischen Systemen arbeiten aber im Hintergrund oft:

- Worker-Modelle;
- Tool-Calling;
- Retrieval / KB / LLM-Wiki;
- Vorverarbeitung;
- State-Management;
- Routing-Logik;
- Validatoren;
- MCP-/Tool-Anbindung.

Deshalb ist ein einzelnes Modell selten die ganze Architektur. Fuer Bjoerns KI-Netzwerk gilt: Struktur, Disziplin, Speicherstrategie, Lade-/Entlade-Logik und Jobflow-Kontrolle sind wichtiger als rohe Parameterzahl.

## Nicht aus dieser Quelle uebernehmen

- Alte LocalAI-/MemLayer-Begriffe als aktuelle technische Komponenten.
- "RAG ist tot" als Regel.
- First Agent als gesetztes Tool.
- Page Index als fertige Implementierung, falls nicht separat gebaut/geplant.
- Shimi oder Backend-Komponenten aus dem Chatbeginn ohne frische Pruefung.
- Mac-Mini-/5-6-Node-Details aus der PDF-Frage als aktuelle Architektur.
