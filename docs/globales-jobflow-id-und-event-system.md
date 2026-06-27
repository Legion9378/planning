# Globales Jobflow ID- und Event-System

Stand: 2026-06-24
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-qwen-3-5-small-modelle-2026-05-07T02-39-51-373Z.md`

## Gesetzte Entscheidung

Das globale ID-System bleibt:

```text
30 Stellen
Base62
globaler Counter
```

Die Laenge ist gesetzt, weil der ID-Raum mit `62^30` praktisch langfristig nicht knapp wird.

## ID-Ebenen

```text
Project-ID
Job-ID
Step-ID
Event-ID
Report-ID
Message-ID
Agent-Instance-ID
```

Alle relevanten Ebenen werden in einer Referenz-/Metadatenstruktur registriert.

## Pflichtmetadaten

Jede ID soll speichern:

- ID,
- Typ,
- Parent-ID,
- Timestamp,
- Status,
- Quelle/Ausloeser,
- Projekt-/Jobflow-Bezug,
- optionale Output-/Report-Referenz.

## Step-IDs

Jeder Jobflow-Step bekommt eine eigene ID:

- Analyse,
- Rewrite,
- Review,
- Self-Healing,
- Validator-Check,
- Tool-Ausfuehrung,
- Scheduler-Pause,
- Resume,
- Finalisierung.

## Loops

Loops werden als eigene Steps mit Iterationen gespeichert:

```text
step_type: review
iteration: 2
parent_job_id: <job_id>
```

Nichts wird blind ueberschrieben; jede Korrekturbewegung bleibt nachvollziehbar.

## Scheduler-Events

Scheduler-Uebergaenge sind Systemevents:

- Pause,
- Resume,
- State gespeichert,
- Workcycle-Ende,
- Fehler beim Resume,
- Job haengt/failt.

Low-Priority-Events erscheinen trotzdem in Statusberichten.

## Qwen-Small-Kontext

Die Qwen-Small-Planung aus der Quelle betrifft das spaetere KI-Netzwerk, nicht Josies Laptop.

Historische Rollenplanung:

- 0.8B: Postmaster / Agentic Communication Daemon,
- 2B: lokales Chat-/Fallback-Modell fuer Netzwerk-/OpenWebUI-/OpenClaw-Kontext,
- 9B: Analyse-/Reasoning-Modell auf Netzwerk-Hardware wie NUC.

Vor Umsetzung ist fuer jedes konkrete Modell ein aktueller Modell-/Infra-Check Pflicht. Die historischen Qwen-Rollen sind Kandidaten, keine finale Modellbindung, weil beim aktiven KI-Netzwerk-Aufbau neuere, bessere oder kleinere Modelle verfuegbar sein koennen.

Zu pruefen:

- aktueller Modellname,
- GGUF/Runtime-Verfuegbarkeit,
- RAM/VRAM,
- Host-Zuordnung,
- Performance,
- Kontextfenster,
- Rollenqualitaet.
