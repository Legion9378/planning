# KI-Netzwerk Node-Rollen

Stand: 2026-06-27

Diese Datei ist der aktuelle Planungsstand fuer die Rollen der vorhandenen Netzwerkgeraete. Aeltere Chat-History-Dateien koennen fruehere Annahmen enthalten und duerfen nicht ohne diese Korrekturen als Zielarchitektur gelesen werden.

Hardware- und OS-Details stehen in `docs/hardware-und-os-stand.md`.

## Grundregeln

- Unter 16 GB RAM wird vorerst kein Modellrunner geplant, ausser Björn setzt explizit eine Spezialrolle.
- Kleine Geraete koennen Orchestrierung, Tools, Storage oder Dienste uebernehmen, aber keine produktive lokale LLM-Inference.
- Tailscale und GitHub funktionieren fuer den Start ausreichend; lokales Gitea/watcion.eu ist offen, bis Tailscale Funnel praktisch getestet wurde.
- DDNS ist kein aktueller Zielweg fuer externen Zugriff; spaeter Tailscale Funnel pruefen.
- DietPi ist verworfen, weil die stark reduzierte Distribution in Björns Test bei Netzwerkfreigaben/NFS praktische Rechteprobleme verursacht hat.
- NFS gehoert zur alten DietPi-Zeitlinie und wird fuer die aktuellen KI-/Content-Workflows nicht eingeplant. Austausch, Taskfluss und Versionierung laufen stattdessen ueber GitHub/Tailscale und spaeter ggf. MCP-nahe Dienste.
- Der frueher geplante VPS fuer eine dauerhaft online laufende Hermes-Agent-Instanz wird gestrichen, um Extrakosten zu sparen. Diese VPS-Entscheidung ist unabhaengig von Tailscale Funnel/watcion.eu.

## Aktuelle Node-Rollen

### Pi 4 Webserver

- Rolle: Webserver.
- Soll perspektivisch Self-Hosted-Dienste tragen, soweit das Webserver-Konzept/funnelbasierte Erreichbarkeit passt.
- Geplante Dienste im Self-Hosted-Kontext: Nextcloud, Gitea und WordPress-basierte Website.
- Keine KI-Instanz.

### Zweiter Pi 4 NAS

- Rolle: NAS, voraussichtlich OMV-basiert.
- Keine aktive KI-Rolle.
- Keine Delegations-/Worker-Rolle aus fruehen LocalAI-Planungen uebernehmen.

### RK3588-Rechner

- Rolle: eigene Hermes-Agent-Instanz fuer CJ, ohne Modell-Backend.
- 8 GB RAM.
- Bleibt auf Ubuntu 22.04 wegen Rockchip-NPU-Tools.
- NPU ist ein Pruefkontext fuer Spezialaufgaben, aber keine gesetzte LLM-/RWKV-/RNN-Beschleunigung.
- Die fruehere VPS/OpenClaw-Rolle wird nicht als VPS-Abhaengigkeit gelesen: CJ bekommt hier eine eigene Hermes-Agent-Instanz.
- Nicht automatisch als Lightweight-Modellrunner planen; Modell-Backends laufen spaeter auf separat geeigneten Runner-/Compute-Nodes.

### Pi 5 8 GB

- Rolle: Orchestrator fuer die selbstgebaute Paperclip-Alternative mit eigenem Agentic-Layer.
- Kein Modellrunner, solange das Geraet unter 16 GB RAM bleibt.
- Umsetzung ist eigene lokale Struktur, nicht Paperclip als Softwarepflicht.
- Moegliche Aufgaben: Orchestrierung, Firmen-/Jobflow-Struktur, Status, Trigger, Queue, Gateway-nahe Funktionen und CJ-CEO-Struktur.

### Bmax B1 Pro / Gemini Lake N4000

- Rolle: FalkorDB-Kandidat/-Host fuer Graph-/Vector-nahe Knowledge-/Memory-Aufgaben.
- Zweck: Graph plus Vector, wenn produktiv gebraucht.
- 8 GB RAM.
- Systemdisk: ca. 370-380 GB.
- Kein Modellrunner unter aktueller RAM-Regel.
- FalkorDB bleibt Bedarfskandidat, kein Startzwang.

### Intel N5109 / Jasper-Lake-Toolserver

- Rolle: Tool- und Script-Server.
- 8 GB RAM.
- Hinweis: Aeltere Quellen/Notizen nennen teils N5105/Jasper; Bjoerns aktuelle Korrektur fuer diese Rolle lautet N5109 ToolServer. Reale CPU-Bezeichnung bei Hardwarezugriff pruefen.
- Kein Modellrunner unter aktueller RAM-Regel.
- Aufgaben muessen als leichte Dienste, Tools, Bridge, Queue-Hilfen oder andere nicht-inferenzlastige Funktionen geplant werden.

### Bmax B6 Pro

- Rolle: aktuell keine feste Rolle.
- Moeglicher Kandidat: ComfyUI-CPU-Host.
- Konkrete Nutzung erst nach Pruefung von Runner, RAM-Verbrauch, Geschwindigkeit, Stromkosten, Kuehlung und Wartbarkeit.

### Mac Mini Late 2012

- Kein NAS.
- RAM: 16 GB.
- Geplante Rolle: semi-autonomer Coder mit eigenem Scheduler, vielleicht OpenCode.
- Keine Modellrunner-Pflicht und keine Exo-/MLX-Rolle.

### NUC und Ryzen/Risen

- Rolle: parallel laufende Modellserver.
- Sie arbeiten als normale Modellserver/Runner parallel und koennen Standard-Jobqueues bzw. Jobflows abarbeiten.
- Diese kontrollierte Parallelitaet setzt voraus, dass beide Modellserver sinnvoll und stabil zum Laufen gebracht werden.
- Benötigte Modellserver-Kapazitaeten:
  - Modellserver fuer CJ selbst,
  - Modellserver fuer CJs Subagents,
  - Modellserver fuer den semi-autonomen Coder.
- Konkrete Modellzuweisung bleibt runtime-, RAM-, Performance- und Rollenabhaengig.

### HP EliteBook 830 G6

- Aktueller Laptop und Hermes-/Codex-Arbeitsgeraet.
- 32 GB RAM.
- Rolle: temporaere KI-Werkbank fuer aktive Sitzungen, Tests und lokale Entwicklung.
- Keine dauerhafte Zentrale, kein staendig laufender KI-Netzwerk-Worker und kein Pflicht-Queue-Host.

## Historische Korrektur: GPU-Offloading / LocalAI-Sharding

Quelle: Chat-History `chatgpt-gpu-offloading-optimierung-2026-05-07T03-12-02-249Z.md`.

Diese Quelle beschreibt eine aeltere Phase mit NUC/Ryzen-Worker-Annahmen, N5105-Chatserver-Idee, Pi400-Kommunikationsgateway und Pi5-Potenzialrolle. Der aktuelle Node-Rollenstand in dieser Datei hat Vorrang.

Uebernommen wird nur die Architekturregel:

- kein LocalAI-/Modell-Sharding als Baseline;
- keine virtuelle Supercomputer-/DeepBlue-Annahme;
- keine Rolle nur vergeben, weil Hardware vorhanden ist;
- kleine Geraete erst nach konkreter Reibung als leichte Dienste, Tools, Trigger, Queue-Hilfen oder Spezialdienste pruefen;
- keine Doppelrollen fuer Orchestrator, Postmaster/Gateway oder Chatserver einplanen.

## Verworfen / offen

- LocalAI-Instanzen pro Kleinrechner sind kein aktueller Zielstand.
- LocalAI-Swarm oder Delegation zwischen diesen Kleingeraeten ist verworfen.
- Automatische DietPi-Wartungsroutinen sind irrelevant, weil DietPi nicht weiter genutzt wird.
- watcion.eu/Gitea/externe Erreichbarkeit bleibt offen, bis Tailscale Funnel getestet wurde.
- Timber wird nicht als Tool-Kandidat fuer das KI-Netzwerk uebernommen.

## Workstation/Admin-Rechner vs. KI-Netzwerk-Node

- Quelle: Chat-History `chatgpt-image-vorbereitung-arm-rechner-2026-05-07T01-34-14-423Z.md`.
- Regel: Bjoerns lokaler Laptop oder eine lokale Workstation ist nicht automatisch ein KI-Netzwerk-Node.
- Workstation-/Admin-/Build-/Client-Rollen muessen strikt von Netzwerk-Node-Rollen getrennt werden.
- Ein Geraet wird nur dann als KI-Netzwerk-Node behandelt, wenn diese Rolle aktuell explizit bestaetigt wurde.
- Alte MOSIX2-/SSI-/LocalAI-/LM3H-/Pi400-Clusterannahmen aus dieser Quelle sind historisch und werden nicht in die aktuelle Hermes-Agent-/Paperclip-Netzwerkplanung uebernommen.
- Historische Zuständigkeitsnotizen wie "DeepSeek richtet den Laptop ein" gelten nicht als heutige Betriebsregel fuer Josie; aktuelle Aufgaben zaehlen.

