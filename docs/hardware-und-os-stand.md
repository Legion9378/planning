# Hardware und OS-Stand

Stand: 2026-06-09

Diese Datei sammelt den aktuellen Hardware- und Betriebssystemstand. Aeltere Chat-History-Dateien koennen Schreibfehler, alte RAM-Werte, alte Rollen oder veraltete OS-Annahmen enthalten.

## Aktuelle Arbeitsgeraete und Nodes

### HP EliteBook 830 G6

- Aktueller Laptop, auf dem Codex betrieben wird.
- Wurde urspruenglich mit 16 GB RAM verkauft.
- Ist mittlerweile auf 32 GB RAM aufgeruestet.
- Die interne SSD ist ausgefallen.
- Aktuelle Systemplatte: externe USB-HDD mit 2 TB.
- Calibre muss wieder installiert werden; Nutzung erfolgt als GUI-Tool.

### Mac Mini Late 2012

- Kein NAS.
- Geplante Rolle: OpenCode und Agent Brain beziehungsweise Code-RAG-/Tool-Zusatz.
- RAM: von 4 GB auf das Maximum 16 GB aufgeruestet.
- Interner Speicher: vermutlich 2x 4 TB SATA SSD.
- Nicht Metal-faehig; keine Exo-/MLX-/Apple-Silicon-Rolle.

### iPad Air 5. Generation

- M1-Chip.
- RAM: standardmaessig 8 GB.
- Speichergoesse aktuell nicht sicher notiert.
- Relevant fuer iPad-Workflows wie GarageBand, iMovie, Dateiaustausch und mobile Arbeit.

### RK3588-Rechner

- 8 GB RAM.
- Ubuntu 22.04 bleibt installiert.
- Grund: vorinstallierte und zusaetzlich installierte Tools fuer die Rockchip-NPU.

### BMAX B1 Pro / BMAX B1 / N4000

- 8 GB RAM.
- Systemdisk: ca. 370-380 GB.
- In fruehen Chat-History-Dateien teilweise als `N4000-Node` beschrieben.
- Zur eindeutigen Abgrenzung vom BMAX B6 Pro entweder als `BMAX B1`, `BMAX B1 Pro` oder ueber den Prozessor `N4000` benennen.
- Aktuelle Rolle: Toolserver und moeglicher Datenbankserver.
- Zielkandidat fuer FalkorDB, falls Graph plus Vector spaeter produktiv gebraucht wird.
- Kein Modellrunner unter aktueller RAM-Regel.
- Alte Angaben von ca. 470-480 GB Systemdisk waren eine fehlerhafte Erkennung und sind verworfen.

### BMAX B6 Pro / Intel i5-1030NG7

- 16 GB RAM.
- Separat vom BMAX B1/N4000.
- Wurde als Modellserver-Kandidat angesprochen.
- Konkrete Modellrunner-Rolle muss spaeter gegen Stromverbrauch, RAM, Runner, Geschwindigkeit und Wartung geprueft werden.

### Intel N5105 / Jasper

- 8 GB RAM.
- Wird allgemein `N5105` oder `Jasper` genannt, weil die CPU-Generation Jasper Lake ist.
- Aktuelle Rolle: Toolserver.
- Kein Modellrunner unter aktueller RAM-Regel.

### Coral Dual TPU

- Vorhandenes oder moeglicherweise nutzbares Zusatzmodul.
- Aktuell keine gesetzte Rolle.
- Nur als Pruefkontext fuer spaetere Spezialbeschleunigung fuehren; keine Annahme, dass LLM-, RWKV- oder RNN-Workloads damit praktisch beschleunigt werden.

### Lokaler Webserver

- Soll spaeter veroeffentlicht werden.
- Laeuft unter YunoHost.
- Keine KI-Instanz.
- Kein Ubuntu-/Xubuntu-Zielsystem.

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
