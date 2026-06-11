# KI-Netzwerk Node-Rollen

Stand: 2026-06-09

Diese Datei ist der aktuelle Planungsstand fuer die Rollen der vorhandenen Netzwerkgeraete. Aeltere Chat-History-Dateien koennen fruehere Annahmen enthalten und duerfen nicht ohne diese Korrekturen als Zielarchitektur gelesen werden.

Hardware- und OS-Details stehen in `docs/hardware-und-os-stand.md`.

## Grundregeln

- Unter 16 GB RAM wird vorerst kein Modellrunner geplant.
- Kleine Geraete koennen Orchestrierung, Tools, Storage oder Dienste uebernehmen, aber keine produktive lokale LLM-Inference.
- Tailscale und GitHub funktionieren fuer den Start ausreichend; lokales Gitea ist fuer die aktuelle Planung nicht vorgesehen und hoechstens spaeter optional.
- DDNS ist kein aktueller Zielweg fuer externen Zugriff; spaeter Tailscale Funnel pruefen.
- DietPi ist verworfen, weil die stark reduzierte Distribution in Björns Test bei Netzwerkfreigaben/NFS praktische Rechteprobleme verursacht hat.
- NFS gehoert zur alten DietPi-Zeitlinie und wird fuer die aktuellen KI-/Content-Workflows nicht eingeplant. Austausch, Taskfluss und Versionierung laufen stattdessen ueber GitHub/Tailscale und spaeter ggf. MCP-nahe Dienste.

## Aktuelle Node-Rollen

### Pi5

- Rolle: hoechstens Orchestrator-Level.
- Keine Rolle mehr als Haupt-KI.
- Kein Modellrunner, solange das Geraet unter 16 GB RAM bleibt.
- Moegliche spaetere Aufgaben: Routing, leichte Control-Plane-Dienste, Status, Trigger, Queue oder Gateway-nahe Funktionen.

### Web-/Mailserver

- Frueher in einer Chat-History als `pi4web` beschrieben; aktuelle Funktion: Web- und Mailserver.
- Laeuft unter YunoHost-Image.
- Keine KI-Instanz.
- Nicht als AdGuard/Caddy/LAMP-Zielstand behandeln; diese fruehere Annahme ist ueberholt.

### pi4eva

- Rolle: lokaler NAS.
- Keine aktive KI-Rolle.
- Keine Delegations-/Worker-Rolle aus den fruehen LocalAI-Planungen uebernehmen.

### BMAX B1 Pro / BMAX B1 / N4000

- Rolle: Toolserver und moeglicher Datenbankserver.
- 8 GB RAM.
- Systemdisk: ca. 370-380 GB.
- Zur eindeutigen Abgrenzung vom BMAX B6 Pro entweder als `BMAX B1`, `BMAX B1 Pro` oder ueber den Prozessor `N4000` benennen.
- Kandidat fuer spaetere Datenbankschichten, insbesondere falls FalkorDB fuer Graph plus Vector produktiv gebraucht wird.
- Keine GPU-/LocalAI-Bildworker-Annahme aus der fruehen Planung uebernehmen.
- Kein Modellrunner unter aktueller RAM-Regel.
- PageIndex-Speicherplanung aus fruehen Dateien ist verworfen.

### BMAX B6 Pro / Intel i5-1030NG7

- Rolle: Modellserver-Kandidat.
- 16 GB RAM.
- Getrennt vom BMAX B1/N4000 fuehren.
- Konkrete Nutzung erst nach Pruefung von Runner, RAM-Verbrauch, Geschwindigkeit, Stromkosten, Kuehlung und Wartbarkeit.

### Intel N5105 / Jasper

- Rolle: Toolserver.
- 8 GB RAM.
- `Jasper` bezeichnet diesen Rechner wegen Jasper-Lake-Generation.
- Keine Haupt-KI und kein Modellrunner unter aktueller RAM-Regel.
- Aufgaben muessen als leichte Dienste, Tools, Bridge, Queue-Hilfen oder andere nicht-inferenzlastige Funktionen geplant werden.

### RK3588-Rechner

- 8 GB RAM.
- Bleibt auf Ubuntu 22.04 wegen Rockchip-NPU-Tools.
- NPU ist ein Pruefkontext fuer Spezialaufgaben, aber keine gesetzte LLM-/RWKV-/RNN-Beschleunigung.
- Konkrete Audio-Aufgaben wie Wake Word, kleine Audio-Klassifikation, Feature Extraction oder Preprocessing werden erst nach praktischer Pruefung der vorhandenen NPU-Tools eingeplant.
- Kein gesetzter STT-, TTS-, LLM- oder Voice-Node.

### Pi400

- Aktuell keine feste Rolle.
- Fruehere Audio-/TTS- oder Worker-Rollen bleiben verworfen oder offen, bis eine neue Aufgabe definiert wird.

### Mac Mini Late 2012

- Kein NAS.
- RAM mittlerweile auf 16 GB aufgeruestet.
- Interner Speicher vermutlich 2x 4 TB SATA SSD.
- Geplante Rolle: OpenCode und Agent Brain beziehungsweise Code-RAG-/Tool-Zusatz.
- Keine Modellrunner-Pflicht und keine Exo-/MLX-Rolle.

### HP EliteBook 830 G6

- Aktueller Laptop und Codex-Arbeitsgeraet.
- 32 GB RAM.
- Interne SSD ausgefallen; aktuelle Systemplatte ist eine externe USB-HDD mit 2 TB.
- Calibre muss wieder als GUI-Tool installiert werden.
- Rolle: temporaere KI-Werkbank fuer aktive Sitzungen, Tests und Codex-Arbeit.
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
- Lokales Gitea ist aktuell nicht eingeplant; GitHub plus Tailscale reicht fuer den Einstieg.
