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
