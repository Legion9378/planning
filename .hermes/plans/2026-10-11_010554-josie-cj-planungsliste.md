# Josie / CJ – Planungsliste und Zuständigkeiten

**Stand:** 2026-10-11, Besprechung mit Björn.
**Ziel:** Sichtbar trennen, was Josie hier nutzt, was später CJ übernehmen soll und was beide verwenden können.
**Architektur:** Bestehende Hermes-Funktionen, Skills und Projekt-Repos zuerst nutzen. Keine zweite Company oder zusätzliche permanente HP-Infrastruktur allein aus dieser Liste ableiten.
**Technik:** Hermes, lokale Git-Repos, Scripts; MarkItDown als frühes Integrationsprojekt.

## Leseregeln

- Diese Datei ist eine Planungs- und Zuständigkeitsliste, kein Installations- oder Live-Betriebsnachweis.
- „Beide“ bedeutet wiederverwendbare Verfahren/Tools, nicht automatisch gemeinsame Laufzeit, Datenzugriff oder gleichzeitige Schreibrechte.
- Vorgeschlagene Zuständigkeiten und spätere Vorhaben sind noch keine Einzelfreigaben für Systemänderungen.
- Keine zusätzliche Priorisierung außer MarkItDown als einem der ersten Projekte festgelegt.
- LLM-Wiki ist laut Björn bereits aktiv in Benutzung und wird nicht erneut als offenes Projekt geführt.
- Keine automatische Verarbeitung von `/home/work/Archiv_entpackt`; jede Datei bleibt vorher interaktiv zu besprechen.

## A. Hier bei Josie

| Thema | Zuständigkeit | Stand / Beleggrenze | Nächster Schritt |
| --- | --- | --- | --- |
| Hermes-Chats und Tool-Arbeit | Josie | In dieser Sitzung genutzt; keine vollständige Betriebsprüfung aller Oberflächen | Bestehenden Zugang erhalten |
| Stiller Conduit-Updatejob | Josie | `0ab4cc71f1f2`: Script-only, `no_agent=true`, lokale Erfolgs-/Fehlerablage, 20-Minuten-Intervall; Einstellungen gelesen, Script mit simulierten Rückgabecodes geprüft; neuer Echtlauf nicht geprüft | Bei Bedarf später realen Cron-Lauf prüfen; keine alten Chats löschen |
| Projektprüfung vor größeren Aufgaben | Beide; zuerst Josie | Regel dokumentiert; keine hier nachgewiesene vollständige Automatisierung | Bestehende Projekt-/Statusquellen prüfen, dann fehlenden Ablauf ergänzen |
| Dauerhafte Checkpoints / Arbeitsstand | Beide; zuerst Josie | Geplant; vorhandene Umsetzung projektbezogen prüfen | Minimalen Status mit fertigen Schritten, offenen Punkten und Artefaktpfaden festlegen |
| Wiederverwendbare Jobflow-Templates | Beide; zuerst Josie | Geplant; vorhandene Templates vor Neubau inventarisieren | Einen konkreten wiederkehrenden Aufgabentyp auswählen |
| Quellen-, Test- und Qualitätsprüfungen | Beide | Quellen-/Toolprüfungen hier genutzt; umfassende Workflow-Abdeckung nicht geprüft | Aufgabeabhängige Abnahmekriterien verwenden, keine pauschalen Confidence-Werte |
| System-/Netzwerkadministration | Josie | Zuständigkeit dokumentiert; Zustand einzelner Nodes hier nicht live geprüft | Bei konkretem Auftrag Zielsystem, SSH und Dienste prüfen; kritische Änderungen nur freigegeben |

## B. Frühes Projekt: MarkItDown installieren und integrieren

**Priorität:** Von Björn als eines der ersten ausführbaren Projekte benannt.
**Zuständigkeit:** Umsetzung zunächst bei Josie; Tool/Workflow später auch für CJ nutzbar.
**Status:** Vereinbarter lokaler Startumfang installiert und getestet: MarkItDown 0.1.8 im isolierten Projekt `/home/work/Local-git/document-markdown/`, CLI `document-to-markdown`, Hermes-Skill `local-document-markdown`. 26 automatisierte Tests bestanden; realer CLI-Einzellauf und Verzeichnisbatch mit zehn eigenen Testdokumenten erfolgreich. Abnahme und Grenzen: `document-markdown/QA.md` und `README.md`.
**Ziel:** Dokumente im bestätigten Startumfang lokal nach Markdown konvertieren. Weitere freie Plugins erst nach gesonderter Prüfung und Entscheidung.

### Bestätigter Startumfang und Import-Chat

Björns Entscheidung vom 2026-10-11 nach Besprechung der Kosten-/Netzwerkgrenzen:

- Startumfang: DOCX, XLSX, XLS, PPTX, PDF mit Textschicht, HTML, CSV, JSON, XML und EPUB.
- Nicht im Startumfang: ZIP-Verarbeitung, Scans/Bild-OCR, Audio, YouTube, Azure und andere Cloud-/kostenpflichtige Dienste.
- Outlook-Unterstützung entfällt ausdrücklich; Björn nutzt Outlook nicht.
- Freie zusätzliche Plugins bleiben eine spätere, gesondert geprüfte Erweiterung, keine Pflicht für den ersten lokalen Start.
- Dokumentenimport wird in einem eigenen Chat ähnlich dem Memory-Review besprochen und durchgeführt. Dieser Chat ist vorgesehen, hier noch nicht erstellt.
- Keine automatische Massenverarbeitung oder Archivübernahme aus dieser Zustimmung ableiten; Originale erhalten und einzelne Importaufträge im vorgesehenen Chat klären.

### Umfang und Grenzen

- MarkItDown-Basis, optionale Formatabhängigkeiten und Drittanbieter-Plugins getrennt erfassen: `[all]` ist nicht gleich „alle Plugins“.
- Alle auffindbaren freien Plugins auf Lizenz, Wartung, Kompatibilität, Ressourcenbedarf und Netzwerk-/Dienstabhängigkeiten prüfen; geeignete installieren und testen, Ausschlüsse begründen.
- „Kostenloses Paket“ und „kostenlos nutzbare Funktion“ unterscheiden. Keine kostenpflichtigen APIs, Azure-Dienste, Abos oder Dokumentuploads automatisch aktivieren.
- OCR benötigt gesonderte Abnahme. Das dokumentierte `markitdown-ocr` nutzt einen LLM-Vision-Client; ohne Client wird OCR übersprungen. Paketinstallation allein ist kein funktionierender OCR-Nachweis.
- Kein lokales LLM-/Vision-Backend auf dem HP automatisch reaktivieren.
- Python-/Paketmanager- und Installationszustand vor Umsetzung live prüfen; isolierte Umgebung statt Eingriff in Hermes-Abhängigkeiten.
- Originaldateien nicht verändern; Markdown-Ausgabe separat, kein stilles Überschreiben.
- Integration zunächst lokal/on demand, keine Watchfolder, Cron-Konvertierung oder dauerhaften Dienste ohne Bedarf.

### Ursprüngliche Umsetzungsschritte / spätere Erweiterungen

Der bestätigte Startumfang hat Vorrang vor der ursprünglichen Gesamtidee. Die folgenden Punkte zu vollständiger Plugin-Inventur und OCR sind Erweiterungsplanung, keine noch fehlende Pflicht für die lokale Startabnahme.

1. Vorhandene Installation/Converter/Integrationen und lokale Regeln prüfen. Projektablage unter `/home/work/Local-git` festlegen; keine vorhandenen Projekte blind duplizieren.
2. Offizielle Dokumentation, Paketversionen und Plugin-Kandidaten recherchieren. Plugin-Matrix mit Quelle, Lizenz, kostenlosen Funktionsgrenzen und Teststatus erstellen.
3. Isolierte Installation der geprüften Formatabhängigkeiten und freien Plugins durchführen; Versionen und reproduzierbare Installation dokumentieren.
4. CLI-Konvertierung mit selbst erzeugten Testdateien prüfen: PDF mit Textlayer, DOCX, PPTX, XLSX, HTML, CSV und EPUB; weitere angebotene Formate ergänzen. Scans separat behandeln.
5. Echte Markdown-Inhalte prüfen: Überschriften, Listen, Tabellen, Links, Unicode; bei fehlenden Fähigkeiten Grenzen explizit dokumentieren.
6. Hermes-Integration wählen und umsetzen: möglichst kleiner vorhandener CLI-/Skill-Aufruf; zusätzliche Plugin-/MCP-Schicht nur bei belegtem Nutzen. Vor Hermes-Änderungen passende Hermes-Referenzen laden.
7. End-to-End aus einer Agentenaufgabe testen: zugelassene Datei -> Konvertierung -> Markdown-Artefakt -> lesbares Ergebnis. Plugins explizit aktivieren, wo erforderlich.
8. Fehlerfälle testen: fehlende Datei, ungeeignetes Format, fehlende OCR-Abhängigkeit, Ausgabekollision. Keine Quellen überschreiben und keine unbemerkten Cloudaufrufe.
9. Installation, Plugin-Abdeckung, Tests, Grenzen und späteren CJ-Nutzungspfad dokumentieren; Listenstatus erst nach belegter Abnahme ändern.

**Startabnahme:** Funktionierender lokaler Aufruf und Agenten-End-to-End-Test für Einzeldatei und Batch; vereinbarte Formate getestet; Format-/OCR-Grenzen sichtbar; keine bezahlten Dienste oder Drittanbieter-Plugins aktiviert; keine Archivdateien verwendet. Vollständige Plugin-Matrix bleibt spätere Erweiterung.

**Primärquelle:** https://github.com/microsoft/markitdown (in dieser Sitzung gelesen).

## C. Später hauptsächlich bei CJ

| Thema | Zuständigkeit | Stand | Rolle von Josie / Voraussetzung |
| --- | --- | --- | --- |
| Company-/CEO-Koordination mehrerer Arbeitsbereiche | CJ | Zielrolle; aktuellen Company-Umsetzungsstand vor Erweiterung prüfen | Josie betreut technische Integration und Betrieb; keine zweite konkurrierende Company |
| Dauerhafte fachliche Jobflow-Koordination | CJ | Geplant / vorhandenen Runtime-Stand prüfen | Vorlagen und Tools können gemeinsam genutzt werden |
| CJ-Hermes-Instanz auf RK3588 | CJ-Laufzeit; Josie Einrichtung | Hardware-Rolle bestätigt, Betrieb hier nicht geprüft | Headless-/SSH-Prüfung und konkreter Installationsauftrag erforderlich |
| Semi-autonomer Coder auf Mac Mini | Eigener Coder; spätere CJ-Koordination als Vorschlag | Geplant; OpenCode nur Kandidat | Josie richtet auf konkreten Auftrag ein; Modell-/Schedulingpfad vorher prüfen |
| Dauerhafter Collector-Jobflow | CJ als spätere Koordination vorgeschlagen; beide können Ergebnisse nutzen | Geplant | Erst Quellenregeln, Review und State; keine ungeprüfte Übernahme |

## D. Bei beiden möglich

| Thema | Josie hier | CJ später | Voraussetzung / Stand |
| --- | --- | --- | --- |
| MarkItDown-Dokumentkonvertierung | Lokaler Startumfang installiert, Skill und Einzel-/Batch-Aufruf getestet | Später in Dokument-/Recherche-Jobflows verwenden | Bei Josie nutzbar; CJ-Installation/-Zugriff noch nicht umgesetzt |
| Recherche / Collector-Verfahren | Gezielte beauftragte Rechercheläufe | Wiederkehrende fachliche Recherche koordinieren | Quellen und Review; keine automatische Dauerüberwachung |
| Story-/Content-Werkbank | Planung, Textarbeit und Review mit Björn | Spätere Produktionsjobflows koordinieren | Bestehende Repos und Produktionsreihenfolge zuerst laden |
| Website / WordPress / Browsergame | Entwickeln und testen | Fachliche Planung, Inhalte, Aufgabenkoordination | Konkreter Auftrag; Deployment separat freigeben |
| Projektprüfung, Templates und Checkpoints | Direktes Arbeitsverfahren | In koordinierte Jobflows übernehmen | Vorhandenes prüfen, gemeinsame Schreibkonflikte verhindern |
| Rollenbasiertes Multimodell-Routing | Nur mit verfügbaren, geprüften Backends | Später spezialisierte Worker/Modelle einsetzen | Keine zusätzliche HP-Modelllast als Pflicht |
| Audio-, Bild- und Video-Workflows | Vorbereiten und einzelne Schritte auf Auftrag durchführen | Spätere Produktionskoordination | Kosten, Runtime, Qualität und Ressourcen prüfen |

## E. Zurückgestellt / nicht als aktiver Auftrag führen

- **Postmaster / Event-Inbox:** weiterhin erst nach stabiler Basis; keine rohe Event- oder Push-Flut. Regeln für Ruhe und Eskalation vor Aktivierung vereinbaren.
- **Morning-Call-Integration:** bleibt geparkt.
- **Separater lokaler HP-Validator:** laut aktualisierter Planung hinfällig beziehungsweise aus Ressourcengründen nicht nutzbar; nicht automatisch reaktivieren.
- **Sensor Guard:** von Björn inzwischen als eigene frühere Idee wiedererkannt: sichtbarer Linux-Datenschutzindikator für Mikrofon-/Kameranutzung, kein Hardwareeinbau. Niedrige Priorität, da das Laptopdisplay derzeit überwiegend zugeklappt ist; nicht verworfen, aber kein aktueller Umsetzungsauftrag. Die alte Datei umfasst zusätzlich Bildschirmfreigaben. Herkunft laut Datei: `chatgpt-gsd-bedeutung-erklaren-2026-05-07T02-38-52-595Z.md`; im Planning-Git spätestens mit Commit `e70783c` aufgenommen. Alte Datei unverändert erhalten.

## Quellen / Nachweisstand

- `planning/docs/hardware-info-ki-netzwerk.md`: aktuelle bestätigte Hardware-Rollen.
- `planning/docs/ki-netzwerk-node-rollen.md`: Rollen und Grenzen, neuere Owner-Korrekturen haben Vorrang.
- `planning/docs/lokale-agent-services-und-jobflow-templates.md`: Betrieb, Templates und Projektprüfung.
- `planning/docs/storytelling-workflow.md`: Content-Werkbank und Produktionsfolge.
- `planning/docs/hermes-multimodell-routing.md`: geplantes Rollenrouting.
- `planning/docs/globaler-self-confidence-loop.md`: korrigierte HP-Validator-Verfügbarkeit.
- `planning/docs/postmaster-event-inbox-backlog.md`: bewusst spätere Event-Schicht.
- `planning/docs/sensor-guard-tray-monitor.md`: wiedererkannte frühere Idee, niedrige Priorität, kein aktueller Umsetzungsauftrag.

**Änderungen:** Planungsliste angelegt und Owner-Entscheidungen nachgeführt; lokales MarkItDown-Projekt, isolierte Installation, CLI und Default-Profil-Skill erstellt und getestet. Keine Remote-Node-Änderung, Archivverarbeitung, Commits oder Pushes.
