# KI-Netzwerk Setup-Loops und Node-Checks

Stand: 2026-07-06
Status: Planungsregel / konkrete Umsetzung spaeter gegen aktuelle Hardware testen
Quelle: Chat-History `chatgpt-jasper-lake-n5105-details-2026-05-07T01-45-34-678Z.md`

## Einordnung

Die alte Checkliste enthaelt viel historische LocalAGI-/LocalAI-/Ubuntu-24.04-/Coqui-/SD1.5-Planung. Uebernommen werden nur die von Bjoern als weiterhin relevant markierten Punkte: 5, 6, 7, 8, 13, 14 und teilweise 17.

Diese Punkte werden auf den aktuellen Zielrahmen abgebildet: Hermes-Agent + Paperclip mit eigenem Agentic-Layer und Orchestrator; CJ als Haupt-KI, Josie als Netzwerk-/Systemadmin.

## Relevante Punkte aus der alten Liste

### Punkt 5: Gemeinsamer KI-Storage als Pruef-/Bedarfspfad

Alte Formulierung: KI-Storage-LV per NFS fuer KI-Netzwerk und Laptop exportieren.

Aktuelle Uebernahme:

- Gemeinsamer Storage fuer KI-Netzwerk und lokalen Laptop bleibt als Bedarfsklasse relevant.
- NFS ist dabei nicht automatisch gesetzt, weil aktuelle Node-Rollen NFS aus der alten DietPi-Zeitlinie fuer Start-Workflows verwerfen.
- Spaeter frisch pruefen:
  - OMV-/NAS-Freigabe;
  - NFS;
  - SMB;
  - SSHFS/rsync;
  - Git/Git-LFS;
  - dedizierter Artefakt-/Modellspeicher;
  - Hermes-/MCP-nahe Dienste.
- Ziel: Modelle, Artefakte, Projektdateien oder grosse Zwischenergebnisse nur dann zentralisieren, wenn es Wartung und Jobflows vereinfacht.

### Punkt 6: Lokale Hermes/Josie-Werkbank auf dem Laptop

Alte Formulierung: Laptop Standalone-AGI-Stack installieren.

Aktuelle Uebernahme:

- Die heutige Entsprechung dieses Punktes ist bereits vorhanden: die lokale Hermes-/Codex-/Josie-Arbeitsumgebung auf dem HP EliteBook 830 G6.
- Josie arbeitet hier als lokale Werkbank fuer Planung, Archivsichtung, Tests, Entwicklung, Toolpruefung und Vorbereitung von KI-Netzwerk-Aufgaben.
- Der Laptop bleibt trotzdem kein automatischer KI-Netzwerk-Node, kein dauerhafter Worker und kein Pflicht-Queue-Host.
- Lokale Tests, manuelle Modelle, TTS-/Bildmodellpruefungen und Vorbereitungsarbeiten koennen hier stattfinden, wenn der aktuelle Auftrag es verlangt.
- Keine Wiederbelebung von LocalAGI als Zielkomponente.

### Punkt 7: Manuelle Bildmodell-/SD-Tests auf dem Laptop

Alte Formulierung: Stable-Diffusion-1.5-Modelle auf Laptop downloaden; grosse SD-Modelle nur manuell wegen 32 GB RAM.

Aktuelle Uebernahme:

- Manuelle lokale Bildmodell-Tests auf dem Laptop bleiben moeglich.
- Das gilt als Werkbank-/Experimentierpfad, nicht als produktiver KI-Netzwerk-Worker.
- Konkrete Modelle wie DreamShaper, Anything, Realistic Vision oder SD1.5-Basis werden nicht automatisch uebernommen; aktuelle Modell-, Lizenz- und Toolpruefung ist Pflicht.
- Aktuelle Bildworkflow-Planung separat beachten: EasyDiffusion laeuft auf dem HP EliteBook manuell per Browser-WebUI relativ gut, wenn auch langsam, hat aber keine API/Webhooks fuer Josie/CJ/Agenten; ComfyUI-CPU bleibt API-faehiger Kandidat; keine SD-Last auf kleinen 8-GB-Workern als Default.

### Punkt 8: Lokale TTS-Tests auf dem Laptop

Alte Formulierung: Coqui-TTS + XTTS auf Laptop installieren.

Aktuelle Uebernahme:

- Lokale TTS-/Voice-Tests auf dem Laptop bleiben als Test-/Werkbankpfad relevant.
- Coqui/XTTS sind historische Kandidaten, keine gesetzte Loesung.
- Auswahl spaeter gegen Wartbarkeit, Deutsch/Englisch, Kosten, Stimmeignung, Exportformat, CPU/RAM-Verbrauch und Storytelling-Workflow testen.
- Story-Vertonung folgt der aktuellen Regel: CJ/Josie/Daphne lesen szenenweise; Audio-Chunks werden spaeter zusammengelegt und mit Ambientsound unterlegt.

### Punkt 13: Swap/mmap/Concurrency-Policy pro Node

Alte Formulierung: Swap + mmap auf Workern setzen und Concurrency-Limits definieren.

Aktuelle Uebernahme:

- Speicherstrategie pro Node bleibt Pflichtpruefung.
- Pro Node spaeter definieren:
  - RAM real verfuegbar;
  - Swap-Datei oder Swap-Partition;
  - swappiness/IO-Auswirkung;
  - mmap-Unterstuetzung der Runtime;
  - maximale gleichzeitige heavy jobs;
  - Temperatur-/Stabilitaetsgrenzen;
  - Verhalten bei OOM/Timeout.
- Konkrete alte Werte wie 8-16 GB Swap oder `max 1 heavy job` sind Startannahmen, keine finale Vorgabe.

### Punkt 14: Hardwarebeschleuniger-Gate fuer Jasper/N5105 und Coral

Alte Formulierung: Jasper Lake vor Kompilierung pruefen, ob M.2 E-Key Slot PCIe-Lane fuer Coral Dual Edge TPU liefert.

Aktuelle Uebernahme:

- Hardwarebeschleuniger werden nicht anhand von Slotnamen eingeplant.
- Vor Nutzung pruefen:
  - liefert der Slot wirklich die benoetigten PCIe-/USB-/I2C-Lanes;
  - BIOS/UEFI erlaubt Nutzung;
  - Kernel/Driver funktionieren;
  - Runtime/Framework unterstuetzt das Modul;
  - Zielworkload profitiert praktisch.
- Coral Dual TPU bleibt Pruefkontext fuer Spezialaufgaben, nicht fuer LLM-/RWKV-/RNN-Baseline.
- N5105/Jasper bleibt nach aktuellem Rollenstand Tool-/Script-Server ohne Modellrunner-Pflicht.

### Punkt 17 teilweise: RK3588/Rockchip-NPU-Pruefpfad

Alte Formulierung: RK3588 Ubuntu flashen, Radxa NPU Tools installieren, LocalAI kompilieren.

Aktuelle Uebernahme:

- RK3588 bleibt wegen vorhandener Rockchip-/NPU-Tooling-Lage auf Ubuntu 22.04.
- NPU/Rockchip-Tools bleiben Pruefkontext fuer Spezialaufgaben.
- Keine LocalAI-Pflicht und keine gesetzte LLM-Beschleunigung.
- Spaeter pruefen:
  - welche NPU-Tools wirklich installiert/funktional sind;
  - welche Modell-/Inference-Formate unterstuetzt werden;
  - ob Hermes-/Tool-/Service-Rollen davon profitieren;
  - ob die Wartung den Nutzen rechtfertigt.

## Setup-Loops als Arbeitsprinzip

Wenn KI-Netzwerk-Softwareaufbau beginnt, wiederkehrende Schritte als Loops behandeln:

- OS-/Flash-/Baseline-Loop;
- Node-Update-/Hardening-/SSH-Loop;
- Service-Install-/Healthcheck-Loop;
- Runtime-/Tool-Test-Loop;
- Modell-/TTS-/Bildmodell-Test-Loop;
- Agent-/Jobflow-Test-Loop;
- nach jedem groesseren Block ein Funktionstest.

## Nicht uebernehmen

- LocalAGI/LocalAI als aktive Zielarchitektur.
- ddclient/Infomaniak als aktueller Zielweg ohne neue Freigabe.
- Alte LVM/iSCSI/NFS-Struktur als automatisch gesetzt.
- SD1.5/Coqui/XTTS-Konkretnamen als aktuelle Auswahl.
- Mac Mini als TTS-Worker aus dieser alten Liste.
- Ubuntu-24.04-Annahmen als aktueller Standard.

## Headless-/SSH-First bei Node-Setup und Flashing

Quelle: Chat-History `chatgpt-ki-server-aus-altgerat-2026-05-07T01-16-24-838Z.md`.

- Bei Server-/Node-/Build-/Flash-Systemen zuerst pruefen, ob der gesamte Ablauf headless per SSH erledigt werden kann.
- Monitor, Tastatur und Maus nicht als Setup-Voraussetzung einplanen, wenn der Zielhost per SSH erreichbar und administrierbar ist.
- Vor Flash-/Build-Aufgaben pruefen:
  - Zielhost per SSH erreichbar;
  - benoetigte USB-/OTG-/Backplane-/serielle Geraete werden vom Zielhost erkannt;
  - Logs, Fehlerausgaben und Recovery-Pfad sind verfuegbar;
  - Herstellerdoku fuer Flashmodus/Bootmodus liegt vor;
  - ein lokaler physischer Eingriff ist nur Plan B, nicht Default.
- Korrektur: Der damals als Alder-Lake-Rechner bezeichnete Rechner stellte sich spaeter als Jasper Lake/N5105 heraus; das war ein Beschreibungsfehler des asiatischen Verkaeufers.
- LM3H-/NanoCluster-Hardware ist noch vorhanden, aber aktuell nicht eingeplant. Falls sie spaeter wieder relevant wird: LM3H nicht wie Raspberry-Pi-Boards behandeln; eMMC/USB/OTG/Backplane-Flashweg frisch anhand Herstellerdoku pruefen.
- Alte LocalAGI-/SSI-/Alder-Lake-Master-Node-Annahmen nicht uebernehmen.

