# KI-Netzwerk Node-Rollen

Stand: 2026-06-07

Diese Datei ist der aktuelle Planungsstand fuer die Rollen der vorhandenen Netzwerkgeraete. Aeltere Chat-History-Dateien koennen fruehere Annahmen enthalten und duerfen nicht ohne diese Korrekturen als Zielarchitektur gelesen werden.

## Grundregeln

- Unter 16 GB RAM wird vorerst kein Modellrunner geplant.
- Kleine Geraete koennen Orchestrierung, Tools, Storage oder Dienste uebernehmen, aber keine produktive lokale LLM-Inference.
- Tailscale und GitHub funktionieren fuer den Start ausreichend; lokales Gitea ist optional und keine Startvoraussetzung.
- DietPi ist verworfen, weil die stark reduzierte Distribution in Björns Test bei Netzwerkfreigaben/NFS praktische Rechteprobleme verursacht hat.
- NFS ist dadurch nicht grundsaetzlich verworfen; Netzwerkfreigaben muessen aber unter der tatsaechlichen Ziel-Distribution Schreib-/Leserechte verlaesslich abbilden, bevor sie fuer produktive Workflows eingeplant werden.

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

### bmax

- Rolle: Toolserver und moeglicher Datenbankserver.
- Kandidat fuer spaetere Datenbankschichten, insbesondere falls FalkorDB fuer Graph plus Vector produktiv gebraucht wird.
- Keine GPU-/LocalAI-Bildworker-Annahme aus der fruehen Planung uebernehmen.

### Pi400

- Aktuell keine feste Rolle.
- Fruehere Audio-/TTS- oder Worker-Rollen bleiben verworfen oder offen, bis eine neue Aufgabe definiert wird.

## Verworfen / offen

- LocalAI-Instanzen pro Kleinrechner sind kein aktueller Zielstand.
- LocalAI-Swarm oder Delegation zwischen diesen Kleingeraeten ist verworfen.
- Automatische DietPi-Wartungsroutinen sind irrelevant, weil DietPi nicht weiter genutzt wird.
- Lokales Gitea bleibt optional; GitHub plus Tailscale reicht fuer den Einstieg.
