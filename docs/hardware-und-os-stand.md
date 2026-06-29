# Hardware und OS-Stand

Stand: 2026-06-27

Diese Datei sammelt den aktuellen Hardware- und Betriebssystemstand. Aeltere Chat-History-Dateien koennen Schreibfehler, alte RAM-Werte, alte Rollen oder veraltete OS-Annahmen enthalten.

## Aktuelle Arbeitsgeraete und Nodes

### HP EliteBook 830 G6

- Aktueller Laptop, auf dem Hermes/Codex betrieben wird.
- Wurde urspruenglich mit 16 GB RAM verkauft.
- Ist mittlerweile auf 32 GB RAM aufgeruestet.
- Die interne SSD ist ausgefallen.
- Aktuelle Systemplatte: externe USB-HDD mit 2 TB.
- Calibre muss wieder installiert werden; Nutzung erfolgt als GUI-Tool.

### Pi 4 Webserver

- Rolle: Webserver.
- Perspektivische Self-Hosted-Dienste: Nextcloud, Gitea und WordPress-basierte Website.
- Externe Erreichbarkeit/watcion.eu bleibt offen, bis Tailscale Funnel getestet wurde.
- Keine KI-Instanz.

### Zweiter Pi 4 NAS

- Rolle: NAS, voraussichtlich OMV-basiert.
- Keine aktive KI-Rolle.

### RK3588-Rechner

- 8 GB RAM.
- Rolle: eigene Hermes-Agent-Instanz fuer CJ.
- Ubuntu 22.04 bleibt installiert.
- Grund: vorinstallierte und zusaetzlich installierte Tools fuer die Rockchip-NPU.
- NPU bleibt Pruefkontext fuer Spezialaufgaben, keine gesetzte LLM-Beschleunigung.

### Pi 5 8 GB

- Rolle: Paperclip-aehnliche Firmenstruktur mit CJ als CEO.
- 8 GB RAM.
- Kein Modellrunner unter aktueller RAM-Regel.

### BMAX B1 Pro / Gemini Lake N4000

- 8 GB RAM.
- Systemdisk: ca. 370-380 GB.
- Rolle: FalkorDB bei Bedarf, wenn Graph plus Vector produktiv gebraucht werden.
- Zur eindeutigen Abgrenzung vom BMAX B6 Pro ueber `BMAX B1 Pro` oder `Gemini Lake N4000` benennen.
- Kein Modellrunner unter aktueller RAM-Regel.
- Alte Angaben von ca. 470-480 GB Systemdisk waren eine fehlerhafte Erkennung und sind verworfen.

### Intel N5105 / Jasper Lake

- 8 GB RAM.
- Rolle: Tool- und Script-Server.
- Wird allgemein `N5105` oder `Jasper` genannt, weil die CPU-Generation Jasper Lake ist.
- Kein Modellrunner unter aktueller RAM-Regel.

### BMAX B6 Pro

- Rolle: aktuell keine feste Rolle.
- Moeglicher Kandidat: ComfyUI-CPU-Host.
- Konkrete Nutzung spaeter gegen RAM, CPU-Geschwindigkeit, Strom, Kuehlung und Wartbarkeit pruefen.

### Mac Mini Late 2012

- Kein NAS.
- Rolle: semi-autonomer Coder mit eigenem Scheduler, vielleicht OpenCode.
- RAM: 16 GB.
- Interner Speicher: vermutlich 2x 4 TB SATA SSD.
- Nicht Metal-faehig; keine Exo-/MLX-/Apple-Silicon-Rolle.

### NUC und Ryzen/Risen

- Rolle: parallel laufende Modellserver.
- Konkrete Modellzuweisungen spaeter nach Runtime, RAM, Performance und Rollenbedarf festlegen.

### iPad Air 5. Generation

- M1-Chip.
- RAM: standardmaessig 8 GB.
- Speichergoesse aktuell nicht sicher notiert.
- Relevant fuer iPad-Workflows wie GarageBand, iMovie, Dateiaustausch und mobile Arbeit.

### Coral Dual TPU

- Vorhandenes oder moeglicherweise nutzbares Zusatzmodul.
- Aktuell keine gesetzte Rolle.
- Nur als Pruefkontext fuer spaetere Spezialbeschleunigung fuehren; keine Annahme, dass LLM-, RWKV- oder RNN-Workloads damit praktisch beschleunigt werden.

## OS-Regel

- Soweit nicht anders notiert, laufen die Ubuntu-Server- und Xubuntu-Systeme auf 26.04.
- Ausnahmen:
  - RK3588-Rechner bleibt auf Ubuntu 22.04 wegen Rockchip-NPU-Tools.
  - lokaler Webserver laeuft unter YunoHost.

## Veraltete Annahmen

- Chat-History `chatgpt-gpu-offloading-optimierung` enthaelt aeltere Rollen-/RAM-Annahmen wie zwei 32-GB-Worker, N5105 als Chatserver, Pi400 als festes Kommunikationsgateway und LocalAI-/GPU-Offloading-Planung. Diese Angaben sind historisch und werden nicht gegen den aktuellen Hardwarestand uebernommen.
- `HP EliteBook 820` war ein laengerer Schreibfehler; gemeint ist das HP EliteBook 830 G6.
- Mac Mini als NAS ist ueberholt.
- Alte 4-GB-RAM-Angaben fuer den Mac Mini sind ueberholt.
- Xubuntu/Ubuntu-Server-24.04-Annahmen aus aelteren Chat-History-Dateien sind nicht der aktuelle Standard.
- VPS fuer dauerhaft online laufenden Hermes-Agent ist gestrichen, um Extrakosten zu sparen.
