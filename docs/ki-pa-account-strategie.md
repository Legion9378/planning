# KI-PA Account- und Datenzugriffsstrategie

Stand: 2026-06-03

## Ziel

Fuer spaetere KI-Assistenz- und PA-Workflows soll klar sein, welche Accounts und Datenquellen bevorzugt genutzt werden, ohne private iCloud-Daten unnoetig breit freizugeben.

## Entscheidung

- Google/Gmail ist der bevorzugte Kommunikations- und Automationskanal fuer KI-Workflows.
- iCloud bleibt das private Apple-Oekosystem fuer iPhone, iPad, Hauptkalender und persoenliche Daten.
- Fuer KI-PA-Aufgaben soll Google als Assistenz-Schicht dienen, nicht als kompletter Ersatz fuer iCloud.

## Begruendung

- Codex und andere KI-Tools sind aktuell besser an Google-Dienste angebunden als an iCloud.
- Gmail, Google Drive, Docs, Sheets und Google Calendar sind fuer Zusammenfassungen, Reports, strukturierte Ablage und laengere Workflows praktischer.
- Telegram bleibt fuer kurze Statusupdates geeignet, wird aber bei laengeren Workflows schnell unuebersichtlich.
- iCloud Mail und iCloud Calendar haben aktuell keinen vergleichbar fertigen Codex-Connector wie Gmail/Google.

## iCloud-Daten fuer PA-Aufgaben

Der relevante iCloud-Nutzungsfall ist nicht primaer Automationstermine, sondern PA-Arbeit:

- Terminuebersichten
- Tages- und Wochenzusammenfassungen
- Vorbereitungshinweise zu Terminen
- Mailuebersichten
- Mailzusammenfassungen
- Erkennen von Aufgaben oder Rueckfragen aus Kommunikation

## Technische Einordnung

- iCloud Kalender: direkter Zugriff waere am ehesten ueber CalDAV sinnvoll.
- iCloud Kontakte: CardDAV, falls spaeter gebraucht.
- iCloud Mail: IMAP/SMTP, aber sensibler und fuer KI-PA-Workflows zuerst zurueckhaltend behandeln.
- Fuer Apple-Zugriffe waeren voraussichtlich app-spezifische Passwoerter bzw. ein Custom-MCP, Script oder Bridge-Dienst noetig.

## Empfohlener Start

1. Einen dedizierten Google/Gmail-Account fuer KI-Kommunikation und Assistenz einrichten.
2. Labels/Ordner fuer Action, Waiting, Reports, Done und Errors vorbereiten.
3. Google Drive als Ablage fuer Reports, Zwischenergebnisse und laengere Aufgaben nutzen.
4. iCloud-Kalenderzugriff nur gezielt und bevorzugt lesend pruefen, zunaechst ueber CalDAV.
5. iCloud Mail nicht als ersten Schritt anbinden; stattdessen wichtige Mails bei Bedarf an den Assistenz-Gmail-Account weiterleiten oder manuell teilen.
6. Falls iCloud-Kalenderdaten genutzt werden, moeglichst mit separatem Kalender oder begrenzter Freigabe starten.

## Datenschutzprinzip

KI-Workflows sollen nur Zugriff auf Daten bekommen, die fuer die konkrete PA-Aufgabe erforderlich sind. Breiter Vollzugriff auf private iCloud-Mailboxen oder komplette Kalender ist zu vermeiden, solange ein schmalerer Workflow ausreicht.
