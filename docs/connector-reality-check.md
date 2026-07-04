# Connector Reality Check

Stand: 2026-07-04
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-teilgesprach-risen-kaufberatung-2026-05-07T03-07-51-042Z.md`

## Kernaussage

Externe ChatGPT-/App-Connectoren sind nicht als produktive Arbeitsgrundlage einzuplanen, solange sie nicht real verifiziert liefern:

- Repo-/Dataset-Sichtbarkeit,
- Dateiinhalte,
- Schreib-/Aenderungsaktionen,
- reproduzierbare Fehler-/Statusmeldungen,
- klare Berechtigungs- und Scope-Anzeige.

Ein Login oder sichtbarer Account reicht nicht.

## Beobachtetes Muster

In der Quelle wurden GitHub- und HuggingFace-Connectoren so erlebt:

```text
Login funktioniert.
Account wird erkannt.
Repos/Datasets werden nicht geliefert.
Arbeiten im Repo ist nicht moeglich.
Reconnect/Freigaben halfen nicht.
```

Bjorns Analogie:

```text
Der Karton ist da, aber der Inhalt fehlt.
```

Das beschreibt den Unterschied zwischen beworbener Funktion und real nutzbarer Arbeitsfaehigkeit.

## Arbeitsregel

Fuer ernsthafte Workflows nicht auf Connector-Versprechen verlassen.

Stattdessen bevorzugen:

- lokale Git-Repos,
- echte CLI-Tools wie `git`/`gh`/provider-spezifische CLIs,
- API-Zugriffe, die wirklich getestet wurden,
- Hermes-Tools mit verifizierbarer Dateisystem-/Terminal-/Web-Ausgabe,
- eigene lokale Workflows mit lesbaren Logs und reproduzierbaren Checks.

## Verifikation vor Einplanung

Ein Connector gilt erst als brauchbar, wenn mindestens getestet wurde:

1. Repo/Dataset sichtbar?
2. konkrete Datei lesbar?
3. kleine Testdatei oder Testbranch sicher schreibbar?
4. Aenderung danach extern sichtbar?
5. Fehler bei fehlendem Scope eindeutig diagnostizierbar?

Wenn diese Checks nicht bestanden sind, bleibt der Connector Spielerei/Experiment und wird nicht als produktiver Architekturbaustein geplant.

## Nicht aus der Quelle uebernehmen

- Risen-/Ryzen-Hardware-Rollen aus dieser Teilwiederholung; aktuelle Rollen stehen separat.
- alte OpenClaw-/DeepBlue-/LocalAGI-Begriffe als aktuelle Architektur.
- emotionale Bewertung als technische Tatsache; relevant ist der reproduzierbare Nutzbarkeitsgap.
