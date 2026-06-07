# KI-Netzwerk, Interface und Laptop: Kandidatenliste

Stand: 2026-06-05

Diese Liste sammelt Kandidaten aus der Planungsnotiz `Fragen zu Artikeln die eine Verbesserung zu KI-Netz, verbundenem standalone Interface und Laptop sein koennen.md`.

Sie ist keine Architekturentscheidung. Einzelne Tools und Artikel muessen separat geprueft werden, bevor sie in die Zielarchitektur uebernommen werden.

Aktuelle Hardware- und Node-Rollen stehen in `docs/ki-netzwerk-node-rollen.md`. Diese Datei hat Vorrang vor aelteren Chat-History-Annahmen zu Pi5, pi4web, pi4eva, bmax, Pi400, DietPi, lokalem Gitea und LocalAI-Verteilung.

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
- Aktuelle Laptop-Grenze:
  - 32 GB RAM reichen nicht automatisch fuer produktiven lokalen KI-Betrieb, wenn Browser, Codex, Editor, Docker-Dienste und andere Programme parallel laufen.
  - Gemma4-e4B unter Ollama war auf dem Laptop bei einzelnen Auftraegen mit bis zu fuenf Stunden Laufzeit nicht als interaktiver Hermes-Agent-Arbeitsmotor brauchbar.
  - Lokale Modelle muessen deshalb Antwortzeit, RAM-Verbrauch und Blockierverhalten auf der Zielhardware praktisch bestehen, bevor sie mehr als Testkandidaten sind.
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
- Korrektur: Spaetere OpenClaw-/Tree-KG-Chatplanungen setzen keine Zielkomponente. Tree-KG wird durch LLM-Wiki plus spaeter ggf. FalkorDB ersetzt.
- Nicht uebernehmen:
  - OpenClaw als Produkt.
  - Community-Skill-Registry als Vertrauensquelle.
  - konkrete OpenClaw-Workspace-Struktur.

## OpenRouter Hybrid-Gateway

- Quelle: Chat-History `chatgpt-webserver-und-ki-netzwerk---openrouter-localai-integration`
- Rolle: externer/Hybrid-Zugang fuer Modelle, die lokal nicht sinnvoll laufen oder als Vergleich/Fallback gebraucht werden.
- Status: relevant, aber nur hinter kontrollierter Bridge/Gateway.
- Regeln:
  - OpenRouter nicht direkt unkontrolliert aus Agenten heraus nutzen.
  - Budgetgrenzen, Logging, Provider-/Modellauswahl und Datenschutzpruefung vorsehen.
  - sensible Inhalte nur mit expliziter Freigabe ueber externe Provider schicken.
  - keine alten LocalAI-/Swarm-/DietPi-Annahmen aus der Fruehplanung uebernehmen.
  - Dummy-Services aus der alten Planung sind Platzhalter, keine Infrastruktur.

## Mobile Git / Working Copy

- Quelle: Chat-History `chatgpt-webserver-und-ki-netzwerk---working-copy-ios-app`
- Status: verworfen.
- Grund:
  - Working Copy ermoeglicht lokalen Git-Workflow wie Bearbeiten und Committen.
  - Wichtige Repo-Admin-Aktionen wie ueberfluessige Repositories loeschen muessen trotzdem ueber die GitHub-Weboberflaeche laufen.
  - Damit loest Working Copy nicht das eigentliche Ziel, GitHub-Verwaltung am iPad ohne Weboberflaeche abzudecken.
- Regel:
  - Mobile Git-Clients werden nur wieder geprueft, wenn sie die benoetigten Admin-Aktionen oder eine saubere Alternative dazu bieten.
  - Bis dahin: Repo-Administration ueber GitHub-Weboberflaeche oder geeigneten Codex/GitHub-Workflow.

## MCP-Git Gateway und Admin-Webhooks

- Quelle: Chat-History `chatgpt-webserver-und-ki-netzwerk---programmiersprachen-fur-mcp-server`
- Rolle: zentrale Git- und Admin-Task-Schicht fuer das spaetere KI-Netzwerk.
- Status: Architekturpattern, kein konkreter Stack.
- Git-Regeln:
  - Worker-KIs bekommen nicht automatisch direkte Git-/SSH-Rechte.
  - Aenderungen, neue Dateien oder Fetch-Anfragen laufen ueber einen MCP-Git-Dienst.
  - `pull`, `commit`, `push`, Export und Import brauchen Scope, Branch/Ref, Pfad, Locking, Queue und Audit Log.
  - Lokales Git auf dem NAS kann als Arbeitsablage dienen.
  - Codex kann spaeter regelmaessig pruefen und nach GitHub synchronisieren.
- Webhook-Regeln:
  - Webhook-APIs sind primaer fuer automatische Administration, Pflege, Status, Trigger und interne Automatisierung vorgesehen.
  - Die lokale KI soll nach Moeglichkeit nicht aktiv in User-Interaktionen auf Support, Blog oder Kommentaren eingreifen.
  - Public-Actions brauchen Review/Freigabe.

## LocalAI-Familie / Image-Gate

- Quelle: Chat-History `chatgpt-webserver-und-ki-netzwerk---jina-reranker-einsatzmoglichkeiten`
- Status: Korrektur- und Pruefregel, keine Jina-Reranker-Entscheidung.
- Regeln:
  - LocalAGI nicht als separate Zielkomponente einplanen.
  - Alte LocalAI-/LocalAGI-/LocalRecall-Notizen nur gegen den aktuellen LocalAI-Stand bewerten.
  - Vor Docker-/Compose-Planung pruefen: Image existiert, Tags existieren, Pull funktioniert, Dockerfile oder Build-Anleitung ist aktuell.
  - Leere go-skynet-/Quay-Repos sind Warnsignal und keine Architekturgrundlage.

## Story-KI Rollenmodell

- Quelle: Chat-History `chatgpt-webserver-und-ki-netzwerk---ki-fur-geschichten-und-horbucher`
- Status: Architekturprinzip aus historischer Fruehplanung.
- Kontext:
  - Die Datei gehoert zum anfaenglichen Hardware-Aufbau fuer lokale KI, die Stories automatisiert oder semi-automatisiert erstellen sollte.
  - Konkrete damalige Hardwareannahmen werden nicht als aktuelles Runbook uebernommen.
- Regeln:
  - Story-KI nicht als einzelnes Modell planen.
  - Control Plane, Modelrunner, Lore-/Memory-/RAG-Kontext, Schreibprozess, State-Speicherung und Review getrennt halten.
  - Hardware unter 16 GB RAM nicht als Haupt-KI oder Modelrunner einplanen.
  - Pi5 hoechstens als Orchestrator-, Tool- oder Hilfsrolle betrachten.
  - `LocalAGI` nur historisch lesen; aktuelle Planung fasst die alte LocalAI-/LocalAGI-/LocalRecall-Familie als `LocalAI` zusammen.
  - Story-Output braucht Review- und Freigabepunkte, bevor Automatisierung oder Publikation angeschlossen werden.

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

## Hermes-Agent Skill Library

- Quelle: Medium-PDF `9 Agent Skills Repos I Tried`
- Rolle: Pruef- und Aufbaupfad fuer eine eigene kontrollierte Skill Library.
- Status: Pattern und Kandidatenliste, keine automatische Installation externer Skills.
- Grundstruktur:
  - `SKILL.md` als zentrale Anweisungsdatei.
  - optionale `scripts/`, `references/`, `examples/` und `templates/`.
  - Skill-Discovery nach Aufgabe, nicht dauerhafte Kontextinjektion.
- Fuer Codex und spaetere lokale Agenten interessante Zusatz-Skills:
  - Obsidian Markdown/Bases/Canvas fuer Novel-Writer-Vault und Lore.
  - Story Bible / Lore Consistency fuer Multi-Crossover-Fanfiction.
  - Voice Calibration / Humanizer fuer Björns Schreibstil.
  - Content Repurposing und SEO Content fuer Artikel, Newsletter, Produktseiten und Landingpages.
  - UI Design-System Briefing als Ergaenzung zu bestehenden Web-App-Skills.
  - Frontend Implementation Review fuer React, HTMX, HTML/CSS und responsive States.
  - E-Commerce Listing / Checkout Copy / Shop Ops fuer Gumroad-aehnliche digitale Produkte.
- Regeln:
  - Community-Skills erst pruefen.
  - externe Inhalte untrusted behandeln.
  - keine Secrets in Skills.
  - Tool- und Shop-Aktionen nur mit Rechte-, Draft- und Audit-Regeln.

### Claude-Skills / LLMWiki

- Quelle: Chat-History `chatgpt-erinnerung-zu-ideen`
- Status: direkt integrierbarer Skill-Layer laut Bjoerns Korrektur zur Readme, keine Grundsatzanalyse noetig.
- Ziel:
  - LLMWiki-Skills fuer LLM-Wiki nutzbar machen.
  - Skills fuer OpenCode, Codex und Hermes-Agent wiederverwendbar halten.
  - Einbindung ueber Rechte, Discovery, Versionierung, Review und Jobflow-/Memory-Anbindung planen.
- Nicht uebernehmen:
  - OpenCode-Ersatz.
  - ungepruefte Toolrechte oder Secrets in Skills.

## Hermes-Agent CEO und Jobflow-Firma

- Quelle: Medium-PDF `Paperclip AI`
- Rolle: Firmenmetapher und Organisationsmodell fuer Hermes-Agent, nicht Paperclip als Software.
- Status: Architekturidee fuer das KI-Netzwerk.
- Grundidee:
  - Hermes-Agent ist CEO.
  - einzelne Jobflows sind spezialisierte Firmenarme.
  - jeder Firmenarm bekommt eigene Agentensteuerung, Regeln, State und Artefaktorte.
  - Paperclip reicht als Software nicht aus, weil das Ziel mehrere Jobflow-Firmenarme unter einem zentralen CEO braucht.
- Hardware-Regel:
  - kein ungezaehmter Parallelbetrieb auf schwacher Hardware.
  - sequenzieller Parallelismus ueber Warteschlange.
  - pro Jobflow maximal zwei Stunden Arbeitsfenster.
  - wenn ein Workflow-Step frueher fertig ist, endet das Arbeitsfenster frueher.
  - danach State speichern, Modell entladen, zehn bis fuenfzehn Minuten Pause.
  - beim naechsten Durchlauf wird ein existierender Job-State geladen statt neu gestartet.
- Routing-Regel:
  - Hermes-Agent muss normalen Assistenzchat von echten Firmenarbeitsanweisungen unterscheiden.
  - Die persoenliche Assistentin kann CEO sein, darf aber nicht jede kleine Chat-Aufgabe als Firmenjob interpretieren.
- Governance-Regel:
  - Budget Caps pro Jobflow, Firmenarm oder Ressourcenklasse.
  - Atomic Checkout, damit ein Step nur von einem Worker gehalten wird.
  - Goal Ancestry, damit jeder Step Ziel, Mission und Nicht-Ziele kennt.
  - Board Approval Gate fuer riskante Aktionen, neue Rechte, Veroeffentlichungen und Kostensteigerungen.
  - Evidence Gate: Reasoning-Traces und Self-Checks sind Diagnosematerial, aber keine Beweise; riskante Entscheidungen brauchen Tool-Evidenz, Tests, Logs, Quellen, Cross-Checks oder Bjoerns Freigabe.
- Worker-Kandidat:
  - Falcon-H1R-7B als unabhaengiger Jobflow-Reasoner pruefen.
  - Rolle: Plaene, Risiken, Alternativen, Abschlusskriterien und Zwischenergebnisse bewerten.
  - Nicht als autonomer Entscheider; Evidence Gate und Board Approval bleiben davor.
  - Vor Nutzung: Lizenz, Acceptable Use, Runner/GGUF, RAM, Deutsch/Englisch, Tool-/Agentenkompatibilitaet und `confidently wrong` testen.
- Nicht uebernehmen:
  - Paperclip-Plattform.
  - Paperclip-Company-Templates.
  - parallele Agentenarme ohne Ressourcen- und State-Grenzen.

## Web-Research-Tools fuer Codex und Hermes-Agent

- Quelle: Medium-PDF `How to Add Free Web Search to Your Local GPT-OSS-20B Setup`
- Rolle: Randnotiz und Bestaetigung fuer bereits geplante Web-Tool-Schicht.
- Status: SearXNG und Firecrawl sind als Tools eingeplant; keine neue UI-Architektur.
- Zielrollen:
  - SearXNG: lokale Websuche und Ergebnislisten.
  - Firecrawl: Webseitenabruf, Crawling, Extraktion und besser strukturierte Webdaten.
  - Hermes-Agent: kontrollierte Tool-Auswahl, Quellenpruefung, Zusammenfassung und Logging.
  - Codex: bei Bedarf Recherche- und Quellenwerkzeug, nicht unkontrollierte Web-Injektion.
- Nicht uebernehmen:
  - Open WebUI als gesetztes Frontend.
  - GPT-OSS-20B/vLLM als Zielsetup.
  - Proxy-/Tor-/Public-Exposure-Komplexitaet fuer den lokalen Standardbetrieb.

## Embedding-Testkandidat Model2Vec

- Quelle: Medium-PDF `Make Sentence Transformers 50x Smaller and 500x Faster with Model2Vec`
- Rolle: spaeterer Testkandidat fuer fertige kleine CPU-first Embedding-Modelle.
- Status: kein aktiver Distillation-Plan.
- Einordnung:
  - fertige Model2Vec-/Potion-Modelle koennen spaeter fuer Retrieval, Vorfilterung oder Routing getestet werden.
  - eigene Distillation ist aktuell wahrscheinlich zu schwer fuer vorhandene Rechenleistung und RAM.
  - Benchmark-Claims muessen lokal geprueft werden.
- Nicht uebernehmen:
  - eigene Distillation als kurzfristige Aufgabe.
  - Model2Vec als gesetzte Embedding-Infrastruktur.
  - `50x`/`500x`-Claims als belastbare Planungsannahme.

## Exo AI Cluster

- Quelle: Medium-PDF `I Turned Two Macs Into an 80B AI Cluster`
- Rolle: Randnotiz zu Geraete-Pooling, kein aktiver Kandidat.
- Status: aktuell nicht einplanen.
- Grund:
  - GPU ist fuer Björns vorhandene Hardware aktuell nicht der Pfad.
  - alter Mac Mini Late 2012 ist nicht Metal-faehig.
  - Artikel ist stark Apple-Silicon-/MLX-/Metal-orientiert.
  - 80B-/TPS-Angaben sind nicht auf Björns Hardware uebertragbar.
- Merken:
  - spaeter koennen mehrere lokale Worker hinter Hermes-Agent/Gateway haengen.
  - zuerst stabile Single-Node-Basis aufbauen.
  - `DeepBlue` war historisch als Exo-aehnlicher "Deep Blue fuer Arme" aus drei bis vier Rechnern gedacht; diese virtuelle-Supercomputer-Annahme wird nicht weiter als Zielarchitektur gefuehrt.

## Universelles Jobframework Laptop und Netzwerk

- Quelle: Chat-History `chatgpt-ki-planung-ideenexperiment`
- Status: Architekturregel, keine Modellentscheidung.
- Regeln:
  - Jobtypen wie Storywriting, Coding, Webcoding, Blogwriting, Translation, TTS und Research nutzen dieselbe Grundlogik.
  - Laptop und spaetere staerkere Hardware unterscheiden sich in Ressourcen, Geschwindigkeit, RAM und KB-/Recall-Reichweite, nicht im Ablauf.
  - Kein automatischer Parallelbetrieb mehrerer Agenten als Cluster-Annahme.
  - Ein Job laeuft seriell und deterministisch.
  - Nach Jobende oder Arbeitsfenster: State speichern, Modell oder schwere Ressourcen entladen.
  - Das, was das KI-Netzwerk "lernt", wird in KB/Memory/Recall gespeichert und kann vom Laptop genutzt werden.
- Nicht uebernehmen:
  - alte Modelllisten aus der Datei.
  - DeepBlue als aktueller Zielname.
  - Exo-/virtueller-Supercomputer-Planung als realistische Baseline.

## Modelluebergreifende Promptmuster

- Quelle: Medium-PDF `I Made Claude 45% Smarter`
- Rolle: Prompt-Pattern fuer Agenten und Chatmodelle, nicht Claude-spezifische Architektur.
- Status: teilweise uebernehmen.
- Einordnung:
  - Der Artikel ist stark aus Claude-/Cloud-Perspektive geschrieben.
  - Die Promptmuster sind aber auf andere KI-Systeme uebertragbar.
  - Björn hatte mit einem frueheren Artikel-Prompt bereits Erfolge bei ChatGPT, Grok und DeepSeek.
- Uebernehmen:
  - spezifische Rolle.
  - klares Ziel und Nicht-Ziel.
  - Methodik mit Arbeitsschritten.
  - Qualitaetskriterien und Self-Check.
  - sachliche Stakes, wenn sie echte Prioritaeten beschreiben.
- Nicht als Standard uebernehmen:
  - Trinkgeld-/Geld-Prompting.
  - aggressive Challenge-Sprache.
  - `45 Prozent smarter` oder aehnliche Claims als belastbare Aussage.

## Website-Frontend mit WordPress-Backend und HTMX

- Quelle: Medium-PDF `HTMX vs React`
- Rolle: Anstoss fuer das lokale Repo `/home/work/Local-git/Website`.
- Status: aktive Projektidee, nicht nur Randnotiz.
- Ziel:
  - WordPress als Backend, Admin, Content- und Datenbasis behalten.
  - oeffentliches Frontend durch eigene HTML/PHP/HTMX/JavaScript-Schicht ersetzen oder schrittweise abloesen.
  - schwere SPA-/Framework-Altlasten vermeiden, solange die Anforderungen server-driven loesbar sind.
- Regeln:
  - WordPress-Core bleibt updatefaehig; kein eingefrorener Core als Zielarchitektur.
  - WordPress-Core nicht direkt veraendern, wenn Theme, Plugin, Hook, Filter oder eigenes Modul reicht.
  - Eigene Plugins und Module werden lokal neu programmiert; bestehende Plugins/Module sind Referenz, kein Code-Copy.
  - Keine KI-Hintergrundsteuerung fuer Website-User-Interaktion oder aktive Seitenlogik einplanen.
  - HTMX ist bevorzugt fuer kleine Interaktionen, Formulare, Fragmente und serverseitig kontrollierte UI.
  - React bleibt moeglich, wenn echte Client-Komplexitaet entsteht.
  - Website-Repo soll nach Einrichtung eines eigenen GitHub-Remotes in den Local-git-Sync aufgenommen werden.

## Gestrichene Punkte

- Node.js-Vermeidung als feste Leitplanke ist hinfaellig.
- FastAPI-WebUI ist hinfaellig.
- Nanobot war nicht ernsthaft im Gespraech und wird nicht weiter verfolgt.

## Arbeitsregel

Diese Kandidatenliste dient nur als Wegweiser fuer spaetere Einzelbesprechungen. Keine Komponente wird aus dieser Liste heraus direkt installiert oder als Architektur-Baustein gesetzt.
