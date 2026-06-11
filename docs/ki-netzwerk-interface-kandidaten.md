# KI-Netzwerk, Interface und Laptop: Kandidatenliste

Stand: 2026-06-09

Diese Liste sammelt Kandidaten aus der Planungsnotiz `Fragen zu Artikeln die eine Verbesserung zu KI-Netz, verbundenem standalone Interface und Laptop sein koennen.md`.

Sie ist keine Architekturentscheidung. Einzelne Tools und Artikel muessen separat geprueft werden, bevor sie in die Zielarchitektur uebernommen werden.

Aktuelle Hardware- und Node-Rollen stehen in `docs/ki-netzwerk-node-rollen.md`. Diese Datei hat Vorrang vor aelteren Chat-History-Annahmen zu Pi5, pi4web, pi4eva, bmax, Pi400, DietPi, lokalem Gitea und LocalAI-Verteilung.

Jeder neue Artikel oder Toolvorschlag muss zusaetzlich durch den Low-Budget-/CPU-first-Filter: reale Hardware, RAM, fehlende nutzbare GPU, Stromkosten, Wartung, Stabilitaet, State, Rechte, Logging und Review. Cloud-, GPU- oder Parallelismus-Annahmen gelten nur als Pattern-Kandidaten, bis sie auf Björns Zielhardware praktisch tragfaehig sind.

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
- Einordnung: Mudler-Projekt aus demselben Umfeld wie LocalAI; MCP-aehnlicher Skill-Dienst, der Skills bereitstellen soll, ohne dass die KI diese selbst installieren muss.
- Prueffragen:
  - Kann SkillServer Skripte und Tools stabil im lokalen Netzwerk bereitstellen?
  - Passt die Architektur zu Hermes-Agent, lokalen Modellservern und spaeteren Worker-Nodes?
  - Laesst sich der Einsatz ohne unnoetige Node.js-/npm-Abhaengigkeit betreiben?
  - Gibt es ein brauchbares Rechte-, Isolation- und Logging-Modell?
  - Kann er Skills als kontrollierte Tool-Schicht bereitstellen, ohne Workflow-Steuerung oder State-Authority zu uebernehmen?

### fastsdcpu

- Quelle: <https://github.com/rupeshs/fastsdcpu>
- Rolle: moeglicher Bildgenerator fuer KI-Netzwerk und Interface.
- Status: Analyse-Kandidat.
- Korrektur: wieder aufnehmen, weil API-Faehigkeit fuer spaetere Jobflows wichtiger ist als reine Browserbedienung.
- Prueffragen:
  - Reicht die CPU-Performance fuer lokale Bildgenerierung oder nur fuer kleine/experimentelle Jobs?
  - Passt der Dienst auf vorhandene Hardware, ohne den Modellbetrieb zu blockieren?
  - Kann er spaeter sauber hinter Interface, Queue oder Toolserver betrieben werden?
  - Sind API, Queueing, Fehlerbehandlung und Rechte-/Pfadmodell fuer Hermes-Agent nutzbar?
  - Lassen sich Seed, Aufloesung, Face-Fix/GFPGAN, Sampler und Steps reproduzierbar testen?
  - Werden mehrere Varianten als Batch/mehrere Generierungen statt als Mehrfachmotiv in einem Bild erzeugt?
- Nicht als aktiver Pfad:
  - AirLLM-/Layerstreaming-Ideen fuer Bildmodelle aus der fruehen Chat-History.

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
- Standard-Chatmodell-Sprachregel:
  - Diese Rolle ist kein Testplatzhalter, sondern der dauerhafte UI/API-Standard.
  - Ziel ist DE/EN-Stabilitaet mit Denglisch-Toleranz, keine aggressive Multilingualitaet.
  - Sprachdrift darf hoechstens Richtung Englisch gehen; Italienisch, Franzoesisch, Spanisch oder andere Sprachen sind fuer Normalantworten Ausschlussgrund.
  - Regionale Sprach-Fine-Tunes wie `-it`, `-fr` oder `-es` sind fuer diese Rolle ungeeignet.
  - Wenn die LocalAI-Gallery kein passendes Modell liefert, wird diese Rolle in die Hugging-Face-/Phase-2-Auswahl verschoben.
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

## Rollenmodell und Orchestrator

- Quelle: Chat-History `chatgpt-architektur-integration-und-vorschlage`.
- Status: Architekturregel, keine Toolentscheidung.
- Rollen:
  - PA beziehungsweise Hermes-Agent-Frontend: dialogisch.
  - Reasoner: analytisch.
  - Validator: kontrollierend.
  - Orchestrator: modellfrei beziehungsweise semantikfrei.
- Regel:
  - Der Orchestrator ist Dispatcher, Workflow-Controller, State-Manager und Regelvollstrecker.
  - Governance, Jobflows, Policies und Björns Freigabe sind der eigentliche Entscheidungsrahmen.
  - SkillServer darf Tool Discovery und Execution Hooks liefern, aber keine Workflow-Steuerung oder State-Authority.
- Korrekturen:
  - SurrealDB, PageIndex, LocalAGI, Nanobot und FastAPI-WebUI aus dieser fruehen Datei nicht als Zielstand uebernehmen.
  - RWKV/RNN nur als Low-RAM-/Long-Context-/Spezialhardware-Pruefkontext fuehren, nicht als gesetztes Modell.
  - Rockchip-NPU und Coral Dual TPU sind Pruefkontexte, keine bestaetigte Beschleunigungsstrategie.

## Closed-Loop-Jobflow und Snapshot-Pattern

- Quelle: Chat-History `chatgpt-architekturvergleich-und-entwurf`.
- Status: Architekturpattern, kein OpenClaw-/Vercel-/Supabase-Stack.
- Uebernehmen:
  - Proposal, Policy/Approval, Mission, Steps, Worker, Event, Trigger/Reaction und Heartbeat als Denkmodell fuer Jobflows.
  - Active Tables als volatile Runtime-Flaeche.
  - Snapshots in Persistent Memory, nicht dauerhaft in Active Tables.
  - Double-Buffer-/Ping-Pong-Prinzip: inaktives Set schreiben, validieren, umschalten, altes Set erst danach loeschen.
  - Knowledge Graph oder spaetere Graph-/Vector-Schichten erst nach erfolgreichem Commit aktualisieren.
- Nicht uebernehmen:
  - Pi400 als gesetzter Persistent-Memory-Core.
  - PageIndex.
  - NanoCluster, Jasper, SHIMMY oder fruehe N4000-Rollen als aktuelle Zielarchitektur.
- Namensregel:
  - `BMAX B1`/`BMAX B1 Pro`/`N4000` ist der 8-GB-Tool-/FalkorDB-Kandidat.
  - `BMAX B6 Pro`/`i5-1030NG7` ist ein getrennter 16-GB-Modellserver-Kandidat.
  - `Jasper` meint den N5105-Toolserver.
  - Pi400 hat aktuell keine feste Rolle.

## Agentic Project Workflow Generator

- Quelle: Chat-History `chatgpt-artikel-lesen-und-umsetzen`.
- Status: fest geplant, noch nicht implementieren.
- Zweck:
  - Project Workflows aus generischen Workflow Templates erzeugen.
  - Project Workflows versioniert im Projekt speichern.
  - normale Jobausfuehrung von Workflow-Erstellung trennen.
- Ablauf:
  - Interface nimmt Björns Auftrag entgegen.
  - Interface-Modell nutzt Routing-Tabelle fuer Anwendungsfall und Zielmodell.
  - passender Reasoner liest Workflow Templates und Prompt Templates.
  - Reasoner erzeugt Project Workflow aus Vorlage und Projektvorgaben.
  - Project Memory wird bei Neuanlage nicht automatisch gelesen.
  - Project Memory wird nur bei Aenderung, Fortsetzung oder Reparatur bestehender Project Workflows genutzt.
- Rollen:
  - Story-/NSFW-Reasoner fuer Hauptstory, weitere NSFW-Storyflows und Rewrite-Regeln zu PG-13, PG-16 oder spaeter festgelegter Zielstufe.
  - Standard-Reasoner fuer allgemeine Project Workflows.
  - Coding-Reasoner wie Fireball oder spaeterer Ersatz fuer OpenCode-/Coding-Workflows.
- Review:
  - Kritischer Reviewer und Retry-Loop sind Teil des Jobflows.
  - Ein externer Supervisor ist keine Pflichtschicht.
  - Eskalation erst, wenn die definierte Loop-Grenze erreicht ist und das Ergebnis weiter nicht passt.
- Nicht uebernehmen:
  - `execution_profiles`.
  - Chroma als Zielkomponente.
  - Claude-Code-Hooks als direkte Architektur.
- Laufzeitregel:
  - Standard bleibt: bis zu 2 Stunden Arbeit, State speichern, Modell/schwere Ressourcen entladen, 10-20 Minuten Pause.
  - Laptop-/Buerojobs duerfen engere Loop-Regeln im jeweiligen Jobflow selbst bekommen.

## Interface-Fallback und LoRA-Policy

- Quelle: Chat-History `chatgpt-fahrmodus-und-hardware-stack`.
- Status: Architekturentscheidung.
- KB-Verweis: `llm-wiki/kb/interface-fallback-und-lora-policy.md`.
- Entscheidung:
  - CJ beziehungsweise die zentrale Interface-/Management-Schicht nutzt keine LoRAs.
  - `SoulMD`, relevante Teile von `UserMD` und `AgentMD` bleiben Prompt-/Memory-/Steuerdatei-basiert.
  - Grund: CJ muss auf externe Modelle wie ChatGPT/OpenRouter ausweichen koennen; externe Modelle unterstuetzen lokale LoRAs nicht.
  - LoRA-Abhaengigkeiten in CJ wuerden beim Fallback Inkonsistenz erzeugen und Debugging erschweren.
- Subagenten-Regel:
  - Subagenten duerfen LoRAs nutzen, wenn sie lokal/spezialisiert laufen und kein identischer externer Fallback gefordert ist.
  - LoRAs dienen dort als Kontext-Kompression, Stil-/Fachwissens-Spezialisierung oder Faehigkeitsoptimierung.
  - Rechte, Governance, Review- und Approval-Regeln duerfen nicht ausschliesslich in Modellgewichten versteckt werden.
- Architekturcheck:
  - Laeuft die Komponente auch extern? Wenn ja, keine lokalen modellgebundenen Abhaengigkeiten.
  - Muss Verhalten ueber alle Modelle identisch bleiben? Wenn ja, Prompt/Memory/Steuerdatei statt LoRA.
  - Ist die Komponente nur lokaler spezialisierter Worker? Dann LoRA optional pruefen.

## Fundamentale Architekturentscheidungen: Dual-Engine-Agentensystem

- Quelle: Chat-History `chatgpt-fahrmodus-aktiviert`.
- Status: Architekturentscheidung, nur Abschnitt 3 wurde uebernommen; sonstige Inhalte der Quelle wurden verworfen.
- KB-Verweis: `llm-wiki/kb/agentic-system-architecture-dual-engine.md`.
- Kernentscheidung:
  - Das System trennt dauerhaft zwischen Interface-Engine und Produktions-Engine.
  - Die Interface-Engine fuehrt Dialog, Intent-Klaerung, Routing, kurze Vorschlaege, UI-Hilfen und Nachfrage-Logik aus.
  - Die Produktions-Engine verarbeitet echte Jobs mit Artefakten, State, Tests, Logs, Evidence und Review-Gates.
  - Ein User-Satz darf nicht automatisch zum Produktionsjob werden; Intent, Scope und Risiko muessen geroutet werden.
- Jobflow-Template-Regel:
  - Jobflows sind wiederverwendbare Templates, aber konkrete Project Workflows werden pro Projekt erzeugt und versioniert.
  - Templates bleiben unveraendert, solange kein bewusstes Template-Update beschlossen wird.
  - Laufende Jobs arbeiten gegen einen stabilen Snapshot statt gegen bewegliche Prompt-/Template-Zustaende.
- Shared-Core-Policy:
  - Core-Regeln, Tool-Schemas, Rechte, Logging, Memory-/State-Konventionen und Review-Gates sind gemeinsam nutzbare Infrastruktur.
  - Projekt- oder Jobflow-spezifische Regeln duerfen den Shared Core nicht stillschweigend ueberschreiben.
  - Aenderungen am Shared Core brauchen explizite Versionierung und Rueckwirkungskontrolle auf bestehende Jobflows.
- Review- und Evidence-Gates:
  - Riskante Aktionen, Kosten, Veroeffentlichung, Rechteausweitung, Loeschen, Git-Pushes und externe Datenweitergabe brauchen Gate/Approval.
  - Modell-Reasoning ist Diagnosematerial, aber kein Beweis; Belege kommen aus Dateien, Tests, Logs, Quellen, Tool-Ausgaben oder Bjoerns Freigabe.
- Nicht uebernehmen aus der Quelle:
  - sonstige Nebenpfade, Tool-/DB-Spekulationen oder Artikelideen aus derselben Chat-History.
  - keine automatische Vermischung von Interface-Chat, PA-Aufgaben und Produktionsausfuehrung.

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

### Hybrid-Coding-Loop mit OpenCode

- Quelle: Chat-History `chatgpt-artikelanalyse-modellbewertung`.
- Status: moegliche spaetere Planung, eingefroren bis OpenCode-Installation und lokale Modelltests.
- Idee:
  - Remote-Mix ueber OpenRouter als Denk-, Planungs-, Review- und Risiko-Schicht.
  - lokale Modelle als Writer fuer Code, Fixes und Tests, falls sie im KI-Netzwerk gut genug laufen.
  - OpenCode als Runtime fuer Tests.
- Grenzen:
  - Remote schreibt nicht, patcht nicht, erzeugt keine Tests und beeinflusst Runtime nicht direkt.
  - Konsolidierung muss deterministisch sein.
  - Remote-Veto nur fuer Architektur-/Security-Fragen.
- Phase 7:
  - Fehler im Test fuehrt nicht blind zurueck zur kompletten Planung.
  - Syntax/kleine Logik: Fix-Plan.
  - falsche Annahme: Review.
  - Architekturbruch: Planung.
  - wiederholter gleicher Fehler: Remote-Arbitration oder Eskalation.

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
  - Aktuelle Planung behandelt die fruehere LocalAI-/LocalAGI-/LocalRecall-Familie als zusammengefassten `LocalAI`-Kontext.
  - Laptop-LocalAI ist Werkbankbetrieb fuer aktive Sitzungen, kein dauerhafter Netzwerkdienst.

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

### Interface v1 Search Provider

- Quelle: Chat-History `chatgpt-artikelzusammenfassung-open-coreui`.
- Status: geplant als Interface-v1-Option, keine aktuelle Implementierung.
- Einordnung:
  - `web_search` ist ein Modell-Tool aus der Tool Registry, keine UI-Suche.
  - Das Tool wird nur aktiv, wenn ein Provider in den Einstellungen aktiviert und konfiguriert ist.
  - Einstellungen: aktiv/inaktiv, Provider- oder Base-URL, Query-Template, Timeout, maximale Trefferzahl.
  - Provider bleiben austauschbar: deaktiviert, SearXNG oder custom URL.
  - Keine Docker-Pflicht fuer den Provider festschreiben.
  - Suchergebnisse muessen strukturiert und begrenzt in den Modellkontext uebergeben werden.

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

## GSD / Multi-Agenten-Paket

- Quelle: Chat-History `chatgpt-gsd-bedeutung-erklaren-2026-05-07T02-38-52-595Z.md`
- Status: nicht als Zielsoftware uebernehmen.
- Einordnung:
  - GSD wurde als Multi-Agenten-Ansatz mit parallelen spezialisierten Agenten besprochen.
  - Fuer Bjoerns Low-Budget-/CPU-first-Netzwerk ist ein dauerhaft parallel arbeitendes Multi-Agenten-Paket nicht die Baseline.
  - Bestehende Hermes-/Jobflow-Regeln haben Vorrang: ein aktiver Jobkontext, State, Review, kontrollierte Ressourcen.
- Nicht uebernehmen:
  - GPU-/beschleunigerlastige Parallel-Agenten-Annahmen.
  - LangChain-/zweites-Orchestrator-Denken neben OpenClaw/Hermes-Agent.
  - digitale-Zwilling-/Familienassistenz-Idee als kurzfristige Zielarchitektur.
- Merken:
  - Persistenz ist kritisch: Messaging-/Memory-/State-Daten duerfen bei Neustart nicht verschwinden oder nur im Sessionkontext leben.
  - OpenClaw-/OpenCore-artige Systeme muessen auf Neustartverhalten, Nachrichtenpersistenz und State-Recovery geprueft werden.

## GPU-Offloading / LocalAI-Sharding historische Korrektur

- Quelle: Chat-History `chatgpt-gpu-offloading-optimierung-2026-05-07T03-12-02-249Z.md`
- Status: historische Planungsphase, nicht aktueller Zielstand.
- Uebernehmen:
  - Sharding/virtueller Supercomputer ist nicht die Baseline.
  - Mehrere Dienste/Worker brauchen klare Registry, Routing, Status und Lastinformation.
  - Hardware bekommt Rollen erst bei echtem Bedarf, nicht nur wegen Verfuegbarkeit.
  - Pi5 bleibt Potenzial-Knoten, bis konkrete Systemreibung sichtbar wird.
- Nicht uebernehmen:
  - GPU-Offloading als Standardpfad.
  - LocalAI-Swarm oder Modell-Sharding ueber Kleingeraete.
  - N5105/Jasper als Chat-Modellserver.
  - alte NUC/Ryzen-32-GB-Worker-Annahmen.
  - Pi400 als fest gesetztes Gateway, wenn spaetere Node-Rollen anderes festhalten.
- Aktueller Vorrang:
  - `docs/ki-netzwerk-node-rollen.md`
  - `docs/hardware-und-os-stand.md`

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
  - Der Laptop wird nicht automatisch als KI-Netzwerk-Node eingeplant, nur weil er verfuegbar ist.
- Nicht uebernehmen:
  - alte Modelllisten aus der Datei.
  - DeepBlue als aktueller Zielname.
  - Exo-/virtueller-Supercomputer-Planung als realistische Baseline.

## Collector als eigener Jobflow

- Quelle: Chat-History `chatgpt-openfang-collector-fur-crossover`
- Status: Jobflow-Idee, keine Toolentscheidung.
- Rolle:
  - semi-automatische Informationssammlung.
  - Story-Grundlagen, Crossover-Lore, Quellenlisten und andere Projektkontexte vorbereiten.
  - Ergebnisse fuer Story-, Lore-, Research- oder Website-Jobflows bereitstellen.
- Regeln:
  - OpenFang ist Inspiration, keine gesetzte Software.
  - Collector laeuft als eigener Jobflow mit eigenem State.
  - Collector-Ergebnisse brauchen Quellen, Status und Review, bevor sie in KB, LLM-Wiki, Obsidian oder Produktionsflows einfliessen.

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
  - Website und KI-Netzwerk bleiben getrennte Architekturbereiche; WordPress ist Website-CMS, nicht KI-Netzwerk-Frontend oder Control Plane.
  - HTMX ist bevorzugt fuer kleine Interaktionen, Formulare, Fragmente und serverseitig kontrollierte UI.
  - Server-driven UI: Der Server bleibt verantwortlich fuer fertige HTML-Seiten und HTML-Fragmente; HTMX fragt nach, das Frontend denkt nicht als SPA.
  - Headless/minimal-headless ist erlaubt: WordPress liefert Content/API/Admin, eine eigene HTML/PHP/HTMX-Schicht rendert oeffentlich.
  - React bleibt moeglich, wenn echte Client-Komplexitaet entsteht.
  - Konkrete Coding-Planung liegt im Website-Repo unter `/home/work/Local-git/Website/docs/frontend-architektur.md`.
  - Website-Repo soll nach Einrichtung eines eigenen GitHub-Remotes in den Local-git-Sync aufgenommen werden.



## Auth-System mit Rotorcipher-Pepper (Eigenes Design)

- Quelle: Chat-History `chatgpt-enigma-funktionsweise-erklaeren-2026-05-07T01-23-00-308Z.md`
- Rolle: Auth-Baustein für Website, KI-Netzwerk-Interface, Hermes-Agent-Control-Plane, LocalAI-Dashboard
- Status: **Analyse-Kandidat** — **5 OFFENE BLOCKER** (siehe unten), KB-Seite existiert (`kb/password-rotor-pepper-pattern.md`), PHP+JS-Grundgerüst vorhanden
- KB: `kb/password-rotor-pepper-pattern.md`, `content/notes/enigma-rotorcipher-passwort-sicherheit-besprechung.md`
- Einordnung: Eigenes Passwort-Design — Rotorcipher (100 Rotoren + 4 Reflektoren) als fixer Pepper vor Argon2id, Webhosting-kompatibel (PHP 7.4+/8.x, Pure PHP), separate User/Admin-Encryption (25/50 Rotoren)

### 🚫 BLOCKER (müssen gelöst sein vor Integration/Entscheidung)

| # | Blocker | Beschreibung | Priorität |
|---|---|---|---|
| **B1** | **KDF/HMAC-Ableitung für Steps/Dirs** | Aktuell: unsicherer `srand(hexdec(substr(bin2hex(hash),0,8)))` Platzhalter in `rotor_preprocess_password()` → **muss ersetzt werden durch HMAC/KDF von Master-Key** (z.B. `hash_hmac('sha256', $seed, $master_key)`) | **KRITISCH** |
| **B2** | **HMAC über Metadaten** | User/Admin-Encryption speichert Metadaten (IV, Steps, Dirs, Final-State) ohne Integritätsschutz → **Metadaten-Manipulation möglich** → HMAC mit Server-Secret nötig | **KRITISCH** |
| **B3** | **Key-Rotation / Migration-Strategie** | Pepper-Wechsel = **alle Passwort-Hashes ungültig** → kein Migration-Pfad, keine Rotation, kein Rollback-Konzept → **muss vor Production gelöst sein** | **HOCH** |
| **B4** | **Security-Audit der Rotor-Implementierung** | Eigenes Krypto-Design → **externe Review nötig** (Side-Channel, Timing, Alphabet-Handling, State-Management) → kein Production-Einsatz ohne Audit | **KRITISCH** |
| **B5** | **WordPress-Plugin / Micro-Service Integration** | Konkreter Integrationspfad fehlt: `wp_hash_password`/`wp_check_password` Override via `mu-plugins` oder separater Micro-Service für KI-Netzwerk → **Entscheidung & Implementation nötig** | **HOCH** |

### Weitere offene Punkte (nach Blocker-Lösung)
- Admin-Key-Management: MFA, Zugriffsbegrenzung, Audit-Log, Backup-Strategie
- Eignung für KI-Netzwerk: Hermes-Agent → LocalAI → User-Management, Session-Handling, Token-Refresh
- Admin-Encryption (50 Rotoren) für System-Secrets, API-Keys, Config

- **Nicht als gesetzter Standard**: Erst nach **ALLE 5 BLOCKER gelöst** + Security-Hardening (KDF, HMAC, Rotation) + Tests

## Gestrichene Punkte

- Node.js-Vermeidung als feste Leitplanke ist hinfaellig.
- FastAPI-WebUI ist hinfaellig.
- Nanobot war nicht ernsthaft im Gespraech und wird nicht weiter verfolgt.

## Arbeitsregel

Diese Kandidatenliste dient nur als Wegweiser fuer spaetere Einzelbesprechungen. Keine Komponente wird aus dieser Liste heraus direkt installiert oder als Architektur-Baustein gesetzt.
