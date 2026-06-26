# Lokale Agent Services und Jobflow Templates

Stand: 2026-06-24
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-prompt-zusammenfassung-erstellen-2026-05-07T08-35-50-651Z.md`

## Entscheidung

Fuer das spaetere headless KI-Netzwerk sind systemd-Services Pflicht fuer alle persistenten Komponenten. Ein dauerhaft offenes Terminal ist kein Zielzustand.

## Betriebsregel

Persistente Komponenten:

- laufen als systemd-User- oder systemd-Systemdienste,
- besitzen Healthcheck oder Statuskommando,
- schreiben Logs in journalctl oder definierte Logdateien,
- koennen ohne Desktop/Terminal starten,
- haben klare Start-/Stop-/Restart-Kommandos.

CLI-Tools sind Clients oder Trigger, nicht der permanente Dienst.

## Pattern

```text
systemd service
  -> haelt Router/Worker/Agent/Validator dauerhaft bereit

CLI/API/Queue client
  -> triggert konkreten Task
  -> liest Status/Output
  -> schreibt neuen Job in Queue
```

Aktuelles Vorbild:

```text
llama-validator.service
  -> lokaler Validator-Router auf Port 4014

self-confidence-review
  -> CLI-Client fuer konkrete Reviews
```

## Jobflow Prompt-Templates

Prompt-Templates werden als Jobqueue-Vorlagen behandelt.

Ziel:

```text
bestehender Jobflow
  -> Template auswaehlen
  -> Projekt-/Taskvariablen anpassen
  -> neuen aktiven Job in Warteschlange erzeugen
```

Das vereinfacht neue Projekte innerhalb desselben Jobflow-Typs, ohne jedes Mal den kompletten Auftrag neu zu formulieren.

## Anforderungen an spaetere Templates

- explizite Variablenliste,
- Defaultwerte,
- Pflichtfelder,
- Ziel-Queue oder Jobtyp,
- erwarteter Output,
- erlaubte Modelle/Agentenrollen,
- Abbruch-/Review-Regeln,
- Self-Confidence-/Validator-Regeln falls relevant.

## Nicht uebernehmen

Die alte Daphne-Datei ist keine aktuelle Implementierung:

- Code war nur simuliert,
- systemd-Beispiel war ein Einmal-Task,
- Shared State war naiv,
- Modellliste ist historisch,
- Daphne ist nicht automatisch aktuelle Zielkomponente.
