# Planer-Agent Project-Existence-Gate

Stand: 2026-06-27
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-slm-von-grund-auf-bauen-2026-05-07T01-34-43-708Z.md`

## Kernaussage

Vor groesseren Jobs darf kein neuer Projektkontext blind gestartet werden. Der Planer-Agent prueft zuerst, ob das Projekt bereits existiert und wo der aktuelle Stand liegt.

## Project-Existence-Gate

Vor Jobstart pruefen:

1. Existiert das Projekt bereits?
2. Wo liegt das Projekt im Git-/Repo-Backend?
3. Welche Planning-/KB-/Metadaten existieren?
4. Was ist der letzte bekannte Stand?
5. Welche Artefakte gibt es bereits?
6. Was ist der naechste sinnvolle Schritt?
7. Gibt es offene Review-/Blocker-/Freigabe-Punkte?

Ziel:

```text
Nicht doppelt planen.
Nicht neue Projekte erzeugen, wenn vorhandene existieren.
Nicht Token verschwenden, wenn sichtbare Projektgeschichte geladen werden kann.
```

## Aktuelle Backend-Begriffe

Die alte Quelle spricht von `LocalRecall + Gitea`.

Aktuell vorsichtig uebersetzen als:

- LLM-Wiki,
- Planning-Dokumente,
- lokale Git-Repos unter `/home/work/Local-git`,
- Source-Register / KB-Log,
- spaeter ggf. GitHub, Gitea oder FalkorDB.

`watcion.eu`/Gitea bleibt offen, bis Tailscale Funnel getestet wurde. Die Regel ist backend-unabhaengig: Projektstatus muss mit dem jeweils realen Git-/Planning-/Recall-Backend synchronisiert werden.

## Sequenziell vs. parallel

Die Quelle formuliert sehr streng `ein aktiver Job zur Zeit`.

Aktuelle Korrektur:

- pro Projekt/Jobflow soll die Kontrolllogik nachvollziehbar und sequenziell bleiben;
- global darf es kontrollierte Parallelitaet geben, wenn die Modellserver stabil laufen;
- fuer das KI-Netzwerk werden Modellserver-Kapazitaeten fuer CJ selbst, CJs Subagents und den semi-autonomen Coder benoetigt.

## Job-States

Minimaler Statussatz:

```text
planned
running
needs_review
blocked
done
```

Diese States koennen spaeter mit dem globalen 30-stelligen Base62-ID-/Event-System verbunden werden.

## SLM-Regel

SLMs sind nicht das Fundament.

Erst kommen:

- Projektzustand,
- Metadaten,
- Jobflow-State,
- Tools,
- Validator-/Review-Gates,
- Git-/Planning-Synchronisation.

SLMs koennen spaeter optionale Helfer sein fuer:

- Intent-Erkennung,
- unscharfe Klassifikation,
- Log-/Pattern-Erkennung.

Kein SLM-Training oder SLM-Neubau ist Startvoraussetzung.

## Nicht uebernehmen

Aus der alten Quelle nicht als aktuelle Architektur uebernehmen:

- Pi400 als Supervisor-MCP-Pflicht,
- konkrete alte `*-mcp`-Namen als Zielbausteine,
- Gitea als Pflichtbackend,
- LocalRecall als eigenstaendige aktuelle Komponente,
- keine Parallelitaet im gesamten Netzwerk,
- SLM von Grund auf bauen,
- automatische Repo-Anlage ohne Review,
- alte JSON-Beispiele als Schema.
