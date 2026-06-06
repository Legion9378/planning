# KI-Netzwerk, Interface und Laptop: Kandidatenliste

Stand: 2026-06-05

Diese Liste sammelt Kandidaten aus der Planungsnotiz `Fragen zu Artikeln die eine Verbesserung zu KI-Netz, verbundenem standalone Interface und Laptop sein koennen.md`.

Sie ist keine Architekturentscheidung. Einzelne Tools und Artikel muessen separat geprueft werden, bevor sie in die Zielarchitektur uebernommen werden.

## Aktive Analyse-Kandidaten

### Open CoreUI

- Quelle: Medium-PDF `Open CoreUI`
- Rolle: moeglicher leichter Desktop-/Web-Client fuer lokale/LAN-Nutzung.
- Status: Analyse-Kandidat, kein gesetztes Frontend.
- Prueffragen:
  - Kann Open CoreUI Hermes-Agent als Control Plane ansprechen, statt selbst Orchestrator zu sein?
  - Sind Desktop, Mobile oder Web-Nutzung fuer Björns Workflow ausreichend?
  - Wie reif sind Security, Session-Verwaltung, Datei-Handling und Logs?
  - Ist der Rust-/Tauri-/Single-Binary-Ansatz auf Zielhardware stabil?

### SkillServer

- Quelle: <https://github.com/mudler/skillserver>
- Rolle: moeglicher Werkzeugkanal fuer KI-Netzwerk und Interface.
- Status: Analyse-Kandidat.
- Prueffragen:
  - Kann SkillServer Skripte und Tools stabil im lokalen Netzwerk bereitstellen?
  - Passt die Architektur zu Hermes-Agent, lokalen Modellservern und spaeteren Worker-Nodes?
  - Laesst sich der Einsatz ohne unnoetige Node.js-/npm-Abhaengigkeit betreiben?
  - Gibt es ein brauchbares Rechte-, Isolation- und Logging-Modell?

### fastsdcpu

- Quelle: <https://github.com/rupeshs/fastsdcpu>
- Rolle: moeglicher Bildgenerator fuer KI-Netzwerk und Interface.
- Status: Analyse-Kandidat.
- Prueffragen:
  - Reicht die CPU-Performance fuer lokale Bildgenerierung oder nur fuer kleine/experimentelle Jobs?
  - Passt der Dienst auf vorhandene Hardware, ohne den Modellbetrieb zu blockieren?
  - Kann er spaeter sauber hinter Interface, Queue oder Toolserver betrieben werden?

### DeepGen 1.0

- Quelle: Medium-PDF `A 5B Model that Proves Smarter Architecture Beats an 80B Giant`
- Rolle: moeglicher multimodaler Kandidat fuer Bildgenerierung, Editing und Textrendering.
- Status: Analyse-Kandidat.
- Prueffragen:
  - Sind Gewichte, Code, Lizenz und Hardwarebedarf praktisch nutzbar?
  - Laeuft das Modell auf vorhandener oder geplanter Hardware sinnvoll?
  - Ist der Nutzen gegenueber fastsdcpu oder anderen lokalen Bilddiensten gross genug?
  - Wie gut funktionieren Deutsch/Englisch-Prompts, Story-Kontext und Bildbearbeitung?

## Offene Artikel und Themen

- Token-Einsparung und Speedup:
  - `Anthropic Just Solved AI Agent Bloat - 150K Tokens Down to 2K`
- Startup-Token- und Zeit-Optimierung:
  - `I Cut Claude Code Exploration Time and Costs by 30% With One Tool`
- Repo-/Job-Abschlusskopien:
  - `How I Set Up My Repo So AI Can Write and Review 100% of My Code` - verarbeitet als Guardrails-/Policy-Gate-Pattern; keine 100-Prozent-Autonomie.
- Uebersetzungs-Worker:
  - `The Open-Source DeepL Alternative Is Here` - verarbeitet als Translation-Worker-Kandidat; HY-MT1.5-1.8B/7B spaeter testen.
- Validator-Idee:
  - TMR/Samsung-7M nur pruefen, falls ein real nutzbarer Download und belastbare Quellen verfuegbar sind.

## Q4 Chatmodell-Fallbacks

- Primaerer Bezugspunkt: Gemma4-e4B.
- Lizenzstatus: Gemma 4 ist fuer die Modellfamilie mit Apache 2.0 als bestaetigtem Pluspunkt notiert.
- Fallback-Kandidat: Qwen 3.5 oder Qwen 3.6 bis 9B, falls Gemma4-e4B Probleme macht.
- Zusaetzlicher Testkandidat: Gemma4 12B Midrange.
- Pruefzeitpunkt: Q4.
- Vor Entscheidung pruefen:
  - Verfuegbarkeit und Modellstand.
  - Lizenz erneut am konkreten Modellstand pruefen.
  - Chat-Template und Tool-/Agentenkompatibilitaet.
  - RAM/VRAM-Bedarf und Quantisierung.
  - Laufbarkeit mit geplanter lokaler Runner-Schicht.
  - reale Antwortqualitaet fuer Deutsch, Chat, Planung und einfache Assistenz.
  - Long-Context-Recall statt nur Context-Window-Groesse.

## Hermes-Agent Toolcalling-Ergaenzung

- Quelle: Medium-PDF `How I built a fully functional AI agent using Gemma3 270M, FunctionGemma, and EmbeddingGemma`
- Rolle: Hintergrund-Orchestrierung fuer Chatmodelle ohne eigenes oder schwaches Toolcalling.
- Status: Architektur-Pattern, kein konkreter Stack.
- Ziel:
  - Intent Routing.
  - Tool-Auswahl ueber Function-/Routing-Schicht.
  - Retrieval-/Embedding-Unterstuetzung.
  - Tool Registry mit festen Schemas.
  - Execution Logs fuer Audit, Memory und spaetere Verbesserung.

## Hermes-Agent Vergleichsquelle OpenClaw

- Quelle: Medium-PDF `How OpenClaw Works`
- Rolle: Vergleichsquelle fuer Gateway, Sessions, Skills, Context Assembly und Memory-on-demand.
- Status: Architekturvergleich, keine Software-Infrastruktur.
- Nicht uebernehmen:
  - OpenClaw als Produkt.
  - Community-Skill-Registry als Vertrauensquelle.
  - konkrete OpenClaw-Workspace-Struktur.

## Hermes-Agent Steuerdateien

- Quelle: Medium-PDF `OpenClaw Automation- The 30 Prompts and Instructions Guide`
- Rolle: Beispielquelle fuer portable Agent-Steuerdateien.
- Status: Pattern, keine OpenClaw-Template-Uebernahme.
- Relevante Dateirollen:
  - Identitaet/Ton, z. B. `SOUL.md`.
  - Arbeitsregeln, z. B. `AGENTS.md`, `agent.md` oder `CLAUDE.md`.
  - Nutzer-/Projektkontext, z. B. `USER.md`.
  - proaktive Checks, z. B. `HEARTBEAT.md`.
- Regel: `CLAUDE.md` ist als Claude-spezifischer Name fuer eine allgemeine Agent-Regeldatei zu behandeln.

## Gestrichene Punkte

- Node.js-Vermeidung als feste Leitplanke ist hinfaellig.
- FastAPI-WebUI ist hinfaellig.
- Nanobot war nicht ernsthaft im Gespraech und wird nicht weiter verfolgt.

## Arbeitsregel

Diese Kandidatenliste dient nur als Wegweiser fuer spaetere Einzelbesprechungen. Keine Komponente wird aus dieser Liste heraus direkt installiert oder als Architektur-Baustein gesetzt.
