# CJ Global Interceptor Memory

Stand: 2026-06-23
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-openwolf-fur-openclaw-2026-05-07T07-43-08-934Z.md`

## Entscheidung

CJ bekommt einen eigenen, komplett isolierten globalen Interceptor Memory Layer. Dieser Layer ist nicht projektbezogen wie bei operativen Agenten, sondern dauerhaft global und auf Bjoerns Entscheidungslogik, Muster, Systemregeln und Gespraechskontinuitaet ausgerichtet.

## Systemtrennung

### Agenten

- Scope: Projekt + Agent-global
- Fokus: Files, Code, konkrete Tasks, Jobstate
- Ziel: reproduzierbare Ausfuehrung, operative Effizienz
- Regeltyp: strikt, simpel, ausfuehrungsorientiert

### CJ

- Scope: global only
- Fokus: Denkprozesse, Entscheidungen, Systemlogik, wiederkehrende Muster von Bjoern
- Ziel: strategische Effizienz, kleine Kontexte, stabile Gespraechskontinuitaet
- Regeltyp: bewertend, abwaegend, strukturierend, kontrollierend

## Load-Regeln

- CJ laedt CJ-Regeln, CJ-Patterns und globale Bjoern-/System-Constraints.
- Agenten laden Agent-Regeln, Projektzustand und operative Jobdaten.
- CJ-Memory und Agent-Memory werden nicht automatisch vermischt.
- Gemeinsame Ground Truth muss explizit kuratiert werden.

## Designfolgen

- Getrennte Rule Loader fuer CJ und Agenten.
- Getrennte Prompt-/Policy-Schichten.
- Getrennte Memory-Scope-Regeln.
- CJ darf reflektieren und bewerten, aber startet keine operativen Jobs ohne Bjoerns Freigabe.
- Agenten duerfen CJ-Strategiekontext nicht unkontrolliert als Ausfuehrungskontext uebernehmen.

## Josie/CJ-Verhaltensregel

Unklare Begriffe werden validiert statt interpretiert. Besonders bei neuen Tools, Nischenbegriffen und Architekturentscheidungen wird vor grossen Ableitungen nachgefragt oder die Annahme klar markiert.

## Noch zu klaeren

- Endgueltiger Speicherort fuer CJ-Memory.
- Welche Informationen als CJ-Pattern, Constraint oder Ground Truth klassifiziert werden.
- Wie Freigabe zwischen CJ-Reflection und Agent-Execution technisch abgebildet wird.
