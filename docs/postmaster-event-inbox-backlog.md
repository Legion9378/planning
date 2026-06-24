# Postmaster Event Inbox - Backlog

Stand: 2026-06-23
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-pi-mono-und-openclaw-2026-05-07T02-40-14-311Z.md`

## Status

Deferred / ganz ans Ende der Planung.

## Begruendung

Der Postmaster bringt erst Nutzen, wenn das System sinnvoll auf Meldungen reagieren kann. Vorher produziert er nur strukturierte Meldungen, aber keine handlungsfaehige Infrastruktur.

Prioritaet:

1. Josie / Hermes-Agent lokal stabil und moeglichst fehlerfrei.
2. KI-Netzwerk grundlegend lauffaehig.
3. Danach Postmaster / Event-Inbox / Briefing-Schicht.

## Keine Ollama-Bindung

Ollama wird nicht als Kernpfad vermerkt, da Bjoern voraussichtlich nicht mehr auf Ollama setzen wird. Alle Loader-/Runtime-Ideen bleiben provider- und runtime-offen.

## Spaetere Architekturidee

```text
Event Source
  -> Inbox
  -> Postmaster Analyse
  -> Outbox / Routing
```

## Kategorien

- `Errors & Warnings`: sofortige oder priorisierte Meldungen
- `Events`: normale Statusmeldungen
- `Summaries`: Daily / Weekly / Monthly
- `Metrics`: nur fuer groessere Auswertungen, nicht fuer Kurzbriefings

## Gruppierung

Events werden spaeter nach Kategorie, Projekt, Job und Step gruppiert. Chronologie bleibt innerhalb eines Jobs erhalten, aber die globale Darstellung soll nicht als chaotischer Zeitstream erscheinen.

## CJ/Josie-Regel

CJ/Josie bekommt keine rohe Eventflut. Falls ein Postmaster gebaut wird, liefert er verdichtete, strukturierte Briefings.

## Offene Punkte fuer spaeter

- Event-Schema finalisieren
- Routing-Ziele definieren
- Briefing-Frequenzen definieren
- Fehler-/Warnungs-Eskalation definieren
- Integration in Hermes-Agent/KI-Netzwerk erst nach Stabilisierung
