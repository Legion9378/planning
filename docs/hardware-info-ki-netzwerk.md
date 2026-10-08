# Hardware-Info KI-Netzwerk

Stand und Owner-Bestätigung: 2026-10-07, gemeinsamer Memory-Review mit Björn.

## Zweck und Nachweisgrenze

Diese Datei ist der zentrale, bei Bedarf zu ladende Kurzverweis für die bestätigte Hardware-Rollenplanung des KI-Netzwerks. Sie ergänzt [Hardware und OS-Stand](hardware-und-os-stand.md) und [Node-Rollen und Architekturregeln](ki-netzwerk-node-rollen.md). Bei abweichenden älteren Rollenangaben gilt diese Owner-Bestätigung.

Eine bestätigte Rolle ist keine Behauptung, dass das Gerät eingerichtet, erreichbar oder sein Dienst produktiv in Betrieb ist. Vor Eingriffen Hostname/IP, OS, SSH-Zugang, Dienste und Datenträger live prüfen. Nicht das Betriebssystem aus einem Gerätenamen ableiten. Historische Modell-/Softwarekandidaten nicht ohne Prüfung installieren.

## Bestätigte Rollen

| Gerät | Rolle / Planungsstand | Einschränkung |
| --- | --- | --- |
| Pi 4 Webserver | Webserver | Rolle bestätigt; Dienste und Erreichbarkeit hier nicht neu geprüft. |
| Zweiter Pi 4 / `nas-pi` | NAS; Adminuser `nas` | Frühere OMV8-/OMV-Extras-Installation im Betriebs-Skill dokumentiert. Laut Björn gebootet; ausschließlich Systemdisk angeschlossen, zusätzliche Datenplatten fehlen noch. |
| RK3588 | Eigene Hermes-Agent-Instanz für CJ | Kein allgemeines Modell-Backend auf diesem Node aus der Rolle ableiten. |
| Pi 5 / 8 GB | Frühere Firmen-/Orchestrator-Rolle ist bedingt | **Wenn CJ als Company erstellt wird, ist die Rolle des Pi 5 offen.** Keine Ersatzrolle vergeben und keine feste Orchestrator-Zuweisung fortschreiben. Ob diese Bedingung bereits erfüllt ist, wurde hier nicht festgestellt. |
| BMAX B1 Pro / Gemini Lake N4000 | FalkorDB bei Bedarf | Bedarfs-/Planungskandidat, kein Installationszwang oder Nachweis eines laufenden FalkorDB-Dienstes. |
| Jasper Lake / Toolserver | Tool-/Script-Server | Bestehender Hardwarekontext nennt N5109 und historische N5105-Angaben; konkrete CPU bei Zugriff prüfen. |
| BMAX B6 Pro | Rolle offen | ComfyUI-CPU ist nur eine Möglichkeit, kein beschlossener Auftrag. |
| Mac Mini | Semi-autonomer Coder | Kein NAS; eigenes Scheduling und eventuell OpenCode sind Planungsbestandteile, keine hier nachgewiesene Umsetzung. |
| NUC und Ryzen | Modellserver | Modelle, Runtime und Kapazität anhand der realen Geräte prüfen; kein neu bestätigter Inferenz-/Betriebsnachweis. |

## Administration und physische Ausstattung

- Josie ist als Netzwerk-/Systemadmin mit Einrichtung, Pflege und Wartung beauftragt; `nas-pi` gehört ausdrücklich zum Netzwerk.
- Außer Laptop und mobilen Geräten sind keine zusätzlichen Bildschirme/Tastaturen für die übrigen Rechner vorhanden: SSH/headless-first und real verfügbaren Recovery-Weg prüfen.
- Adminauftrag ersetzt nicht die konkrete Freigabe destruktiver, sicherheitskritischer oder produktionsrelevanter Änderungen.
- Für NAS-Datenplatten zuerst Anschluss, Modell/Seriennummer/Größe und Storage-Plan klären; Systemdisk nicht als freie Datenplatte behandeln.
- Passwörter nicht in Hardware-/Wiki-Dateien speichern.
- Diese Datei wird bei Netzwerk-/Hardwareaufgaben referenziert; die vollständige Rollenliste gehört nicht zusätzlich in das globale Prompt-Memory.

## Quellen und verwandter Kontext

- Björns Bestätigung im Memory-Review am 2026-10-07: „Wenn CJ als Company erstellt wird, wäre der Pi5 auch offen. Der Rest stimmt soweit!“; Freigabe zur eigenen Hardware-Info-Datei.
- [Hardware und OS-Stand](hardware-und-os-stand.md): weitere Spezifikationen, OS-/Netzwerk-/NAS-Hinweise mit ihrem jeweiligen Nachweisstand.
- [KI-Netzwerk Node-Rollen](ki-netzwerk-node-rollen.md): weitere Architektur- und historische Abgrenzungsregeln.
- [Headless-Betrieb in der LLM-Wiki](../../llm-wiki/kb/lokale-agent-services-und-jobflow-templates.md).

Keine Geräte, Dienste oder Datenträger wurden bei Erstellung dieser Datei verändert. Keine neue SSH-/Live-Prüfung ausgeführt.
