# KI-Netzwerk Job-Scheduling und Checkpointing

Stand: 2026-07-06
Status: Planungsregel / konkrete Werte spaeter testen
Quelle: Chat-History `chatgpt-hp-t630-thin-client-bewertung-2026-05-07T02-39-20-960Z.md`

## Kurzthese

Das KI-Netzwerk soll langlaufende Agenten-/Jobflow-Arbeit nicht als unbegrenzte Dauerlast ausfuehren. Stattdessen werden Jobs in nachvollziehbare Slices/Steps zerlegt, an Step- oder Commit-Grenzen gespeichert und spaeter aus technischem State fortgesetzt.

## Grundprinzip

1. Job/Step laeuft bis zu einer definierten Grenze.
2. Technischer State/Checkpoint wird gespeichert.
3. Job gibt Ressourcen frei oder rotiert aus der aktiven Queue.
4. Andere Jobs koennen laufen.
5. Spaeter wird der Job aus seinem State fortgesetzt.

Die frueher genannten Werte `2 Stunden Laufzeit / 10 Minuten Pause` sind historische Planungswerte und keine harte finale Vorgabe. Konkrete Slice-Laengen muessen spaeter gegen reale Nodes, Thermik, Modell-/Tool-Laufzeiten, Wartbarkeit und Fehlerverhalten getestet werden.

## State ist nicht Memory

- Global-/Projekt-Memory: dauerhaftes Wissen, Regeln, Projektkontext.
- Arbeits-/Session-Layer: temporaerer Kontext eines Agents oder Steps.
- Checkpoint/State: technischer Arbeitszustand eines Jobs, damit er nach Pause, Fehler oder Rotation fortgesetzt werden kann.

Diese Ebenen duerfen nicht vermischt werden. Ein Checkpoint ersetzt kein Memory; Memory ersetzt keinen reproduzierbaren Job-State.

## Commit-Barrieren und Step-Grenzen

Checkpointing soll an nachvollziehbaren Grenzen passieren:

- nach abgeschlossenen Teilaufgaben;
- vor/ nach Reviewer- oder Validator-Schritten;
- vor externen Side Effects;
- nach Schreib-/Commit-Barrieren;
- bei laengeren Story-, Code-, Analyse- oder Recherche-Slices.

Ziel: Keine halbfertigen, unpruefbaren Zwischenzustaende als final behandeln.

## Queue-Rotation

Mehr Worker erhoehen nicht nur parallele Kapazitaet, sondern auch die Rotationsgeschwindigkeit der Queue. Dadurch kommen mehrere Jobs schneller wieder an die Reihe, ohne dass ein einzelner Node dauerhaft von einem Job blockiert wird.

## Nicht aus dieser Quelle uebernehmen

- Keine alten OpenClaw-/Pi5-/HP-T630-Rollen als aktuelle Architektur.
- Kein SLURM/HTCondor als Pflichttool; nur das Scheduling-Prinzip ist relevant.
- Keine Wiederbelebung alter LocalRecall/Mem0-Begriffe.
- Keine finale Zeitvorgabe ohne Hardwaretest.

## Aktueller Architekturrahmen

Diese Regel wird spaeter auf das aktuelle KI-Netzwerk-Ziel angewendet: Hermes-Agent + Paperclip mit eigenem Agentic-Layer und Orchestrator; CJ als Haupt-KI, Josie als Netzwerk-/Systemadmin.

## Worker-Klassen und Infrastruktur-/Compute-Trennung

Quelle: Chat-History `chatgpt-linkanalyse-und-alternativen-2026-05-07T02-27-54-557Z.md`; aktualisiert durch Bjoerns Korrektur vom 2026-07-08.

### Grundregel

Parallelitaet entsteht im KI-Netzwerk nicht dadurch, dass der Scheduler beliebig komplexer wird, sondern durch mehrere passende Worker/Runner, die Jobs parallel in ihren eigenen Grenzen bearbeiten koennen.

Der Orchestrator muss spaeter entscheiden koennen:

- welche Worker/Runner verfuegbar sind;
- wie viel RAM/CPU/NPU/IO sie haben;
- welche Modell-/Tool-Backends dort sinnvoll laufen;
- welche Jobs leicht, mittel, schwer oder toolbasiert sind;
- welche Nodes Infrastruktur tragen und deshalb nicht mit Modelllast belastet werden sollen.

### Trennung

- Infrastruktur-/Support-Nodes: Orchestrierung, Datenbank/Knowledge, Toolserver, Queue-/Status-/Bridge-Dienste. Diese Nodes sollen keine schweren Modelle laden.
- Compute-/Model-Worker: Modellserver/Runner fuer leichte, mittlere oder schwere Modelljobs. Konkrete Zuordnung bleibt spaeter zu testen.

### Aktuelle Rollen-Korrektur

- N4000: FalkorDB-Kandidat/-Host fuer Graph-/Vector-nahe Knowledge-/Memory-Aufgaben.
- RK3588: Hermes-Agent-Instanz ohne Modell-Backend. Die NPU bleibt Pruefkontext, aber dieser Node wird nicht automatisch als Modellrunner geplant.
- Pi 5: kann als Orchestrator die selbstgebaute Paperclip-Alternative mit eigenem Agentic-Layer tragen.
- N5109: ToolServer. Aeltere N5105/Jasper-Bezeichnungen aus Quellen muessen gegen den realen Geraetestand geprueft werden; die aktuelle Korrektur setzt die ToolServer-Rolle, nicht eine Modellrunner-Rolle.
- Restliche Compute-/Runner-Aufteilung wird spaeter ausgetueftelt und nicht aus dieser Quelle final uebernommen.

### Worker-Klassen als Planungsmodell

- Light: kurze Analysen, Klassifikation, kleine Hilfsmodelle oder toolnahe Vorverarbeitung — nur falls ein dafuer geeigneter Runner/Node bestaetigt ist.
- Medium: laengere Textanalyse, Story-/Planungsjobs, Standard-LLM-Aufgaben — spaeter gegen RAM/Runtime pruefen.
- Heavy: grosse Reasoning-/Analyse-/Pipeline-Jobs — nur auf ausreichend dimensionierten Modellservern.
- Tool-only: Skripte, Parser, API-Bridges, Pre-/Postprocessing ohne lokales Modell-Backend.

### Nicht final uebernehmen

- OpenClaw als aktueller Orchestrator.
- Pi400/VPS-Control-Plane aus der alten Quelle.
- SurrealDB als konkrete DB-Entscheidung.
- 2h/10m als harte finale Zeitregel.
- Alte konkrete Node-Zuweisungen als finaler Stand, soweit sie durch neuere Rollenplanung oder Bjoerns Korrektur ersetzt wurden.

