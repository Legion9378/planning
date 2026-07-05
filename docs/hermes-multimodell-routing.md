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

## Offene Pruefpunkte

- Welche lokalen Llama.App-Modelle decken aktuell `creative/draft` ab?
- Welches Modell/Provider-Profil ist fuer `structure/reasoning` auf dem Laptop vs. im KI-Netzwerk sinnvoll?
- Welche Tasks brauchen zwingend Tool-Faehigkeit und sollten beim Hermes-Hauptmodell bleiben?
- Wie wird die Rollenwahl in Hermes-Konfig, Skills oder Jobflow-Templates praktisch abgebildet?
