# Hermes Multimodell-Routing

Stand: 2026-07-05
Status: Planungsregel / Modellkandidaten muessen frisch geprueft werden
Quelle: Chat-History `chatgpt-turboquant-auf-cpu-nutzung-2026-05-07T07-47-25-193Z.md`

## Kurzthese

Bjoerns lokale Agenten- und Story-Workflows sollen nicht auf ein einziges "perfektes" Hybridmodell optimiert werden. Stabiler ist rollenbasiertes Multimodell-Routing: verschiedene Modelle oder Provider werden je nach Aufgabe eingesetzt und vor produktiver Nutzung praktisch geprueft.

## Rollenmodell

- `creative/draft`: private Rohentwuerfe, Story-Brainstorming, freie Varianten.
- `structure/reasoning`: Gliederung, Logik, Kontinuitaet, Kapitelstruktur, Entschaerfung auf Zielstufe.
- `agent/tools`: Hermes-/Tool-Ausfuehrung, Code, Dateiarbeit, API-/CLI-Jobs.
- `validator/reviewer`: Gegenpruefung von Fakten, Content-Stufe, Rechte-/Publishing-Risiken, Stil- und Lore-Konsistenz.

## Regeln

1. Modell-Merges sind Kandidaten, keine Architektur.
   - Deckard-/Heretic-/Gemma-/Hermes-Modelle aus alten Chats duerfen nicht als aktuelle Empfehlung gelten.
   - Vor Einsatz immer neu pruefen: Hardware, RAM/VRAM, Runtime, Quantisierung, Kontextfenster, Lizenz, Verfuegbarkeit, Geschwindigkeit und Output-Qualitaet.

2. Private Rohentwuerfe und Public-/YouTube-Fassungen bleiben getrennt.
   - Unzensiertere lokale Modelle sind nur fuer private Rohentwuerfe/Brainstorming geeignet.
   - Oeffentliche Fassungen brauchen Rewrite, Review und Zielstufen-Freigabe.

3. Routing ist Workflow-Logik.
   - Die Entscheidung "welches Modell fuer welchen Schritt" gehoert in Jobflow-/Skill-/Konfigurationslogik, nicht in ad-hoc Prompt-Gefuehl.
   - Reviewer-/Validator-Schritte duerfen andere Modelle verwenden als Creative-Draft-Schritte.

4. Kein blindes "bestes Modell".
   - Ein leistungsstaerkeres Modell kann fuer eine Rolle schlechter sein als ein kleineres, stabileres Modell.
   - Modellwahl wird pro Aufgabe und Zielsystem getestet.


## System-Level-MoE fuer Coding-Domaenen

- Quelle: Chat-History `chatgpt-voraussetzungen-fur-ki-entwicklung-2026-05-07T02-11-33-240Z.md`.
- Status: Planungsregel; spaeterer Abgleich auf real vorhandener Hardware ist Pflicht.
- Kein Ziel: eigenes echtes MoE-/Foundation-Modell trainieren. Das ist mit Bjoerns Hardware nicht realistisch und gehoert in GPU-Cluster-/Forschungsinfrastruktur.
- Zielprinzip: MoE-aehnliches Verhalten auf Systemebene:
  - Orchestrator waehlt Modell, Tool, Adapter oder Workflow-Rolle;
  - spezialisierte Coding-/Web-/SQL-/Reviewer-Komponenten bearbeiten Teilaufgaben;
  - Validatoren pruefen Ergebnisse;
  - Memory/Kontext haelt Aufgabenstand und Entscheidungen.
- Coding-Domaenen muessen mindestens Python, Web/Frontend, Backend/API und SQL/SQLite beruecksichtigen. SQL ist nicht optional, weil portable Apps Einstellungen und Laufzeitdaten oft lokal speichern muessen.
- Adapter/LoRA koennen spaeter als Soft-MoE-Variante geprueft werden, sind aber keine Startvoraussetzung.
- Konkrete Umsetzung erst nach Hardware-Inventar pruefen: CPU/RAM/VRAM, Modellserver, Runtime, Netzwerk, OS, Strom/Kuehlung, Wartbarkeit und Tool-Faehigkeit.

## Offene Pruefpunkte

- Welche lokalen Llama.App-Modelle decken aktuell `creative/draft` ab?
- Welches Modell/Provider-Profil ist fuer `structure/reasoning` auf dem Laptop vs. im KI-Netzwerk sinnvoll?
- Welche Tasks brauchen zwingend Tool-Faehigkeit und sollten beim Hermes-Hauptmodell bleiben?
- Wie wird die Rollenwahl in Hermes-Konfig, Skills oder Jobflow-Templates praktisch abgebildet?
