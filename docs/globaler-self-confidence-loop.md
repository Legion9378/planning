# Globaler Self-Confidence Loop und Modell-Validierung

Stand: 2026-10-07 (HP-Verfügbarkeit korrigiert; Architekturziel unverändert)
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-planer-und-cot-risiken-2026-05-07T02-23-09-981Z.md`

## Entscheidung

Self-Confidence ist global: jeder Step, jedes Modell, jede Aufgabe kann eine Self-Confidence erzeugen. Diese wird nicht als Wahrheit akzeptiert, sondern als Signal fuer strukturelle Validierung genutzt.

## Grundregel

Confidence darf nicht aus CoT, sprachlicher Ueberzeugung oder sauber klingender Begruendung abgeleitet werden. Sie muss als Stabilitaetsindex unter Variation verstanden werden.

## Step-Ablauf

Jeder relevante Step erzeugt:

- Ergebnis,
- strukturierte Metadaten,
- Self-Confidence,
- ggf. Begruendung bei Confidence ueber der Normalgrenze,
- Referenzen auf Input, State und Output.

Bei historisch `> 1.0` bis maximal `1.2`:

1. Event an Rekursiv-Reasoner / Validator.
2. Validator bekommt nicht einfach nur die Begruendung.
3. Validator rekonstruiert das Problem unabhaengig neu.
4. Validator erzeugt eigene Confidence.
5. Orchestrator vergleicht Ergebnis, Flags, Constraints und Confidence-Differenz.
6. Divergenz wird als Risiko- oder Review-Signal behandelt.

## Statistik / Drift-Monitoring

Zu erfassen:

- Confidence-Verteilung pro Modell,
- Confidence-Verteilung pro Tasktyp,
- Validator-Divergenz,
- Haeufung knapp unterhalb der Trigger-Schwelle,
- Zusammenhang zwischen Confidence und spaeterer realer Korrektheit,
- Fehlerfaelle trotz hoher Confidence.

Zusaetzlich sollten Stichproben auch unterhalb der Schwelle validiert werden, damit Modelle nicht systematisch knapp unter dem Trigger bleiben.

## Modellkandidaten-Flag

Historisch genannt:

- Falcon H1R als Planer/Haupt-Reasoner,
- Samsung TRM als rekursiver Reasoner/Validator.

Status: **Kandidaten / zu pruefen**.

Vor Festlegung muss geprueft werden:

- Laeuft das Modell sinnvoll auf Bjoerns Infrastruktur?
- Welche Quantisierung ist noetig?
- Reicht RAM/VRAM?
- Ist die Geschwindigkeit fuer die Rolle brauchbar?
- Passt das Kontextfenster?
- Ist die Runtime kompatibel?
- Ist das Modell fuer Planer/Reviewer/Validator-Aufgaben qualitativ geeignet?

Diese Modellnamen duerfen nicht als harte Architekturvoraussetzung behandelt werden, solange die Infra-Pruefung fehlt.

## Aktuelle Verfügbarkeit auf dem HP

Owner-Auskunft im Memory-Review 2026-10-07: Der lokale Self-Confidence-Validator ist auf dem HP aus Ressourcengründen nicht nutzbar. Beim kurzfristigen Check liefen Hermes, Firefox für das Dashboard, zwei bis drei kleinere Anwendungen und die normalen Betriebssystemprozesse. Ein kleines Modell über Llama.App war laut Björn so langsam, dass die Geschwindigkeit beinahe in Minuten pro Token statt Token pro Sekunde beschrieben werden musste. Keine exakten Messwerte oder Modellidentität liegen vor; keine technische Ursachenfeststellung daraus ableiten.

Björn hat das Llama.App-Backend vorerst deaktiviert. Das ist Owner-Auskunft, kein neuer Live-Servicecheck. Keine automatische Reaktivierung oder lokale Validator-Inferenz auf dem HP. Eine Neubewertung benötigt einen separaten Auftrag; ein Ersatz-Node oder Ersatzmodell ist nicht festgelegt. Quellen-/Toolprüfungen fortsetzen, fehlende unabhängige Modellvalidierung offenlegen und zwingende ungeklärte Review-Gates eskalieren statt als bestanden auszugeben.

## Historische lokale Standardroutine

Die frühere Einrichtung dokumentierte folgenden systemd-User-Service; diese Referenz belegt keine aktuelle Verfügbarkeit und ist kein Startauftrag:

```bash
systemctl --user status llama-validator.service
/home/work/.local/bin/self-confidence-review --health
```

Endpoint:

```text
http://127.0.0.1:4014/v1/chat/completions
```

Primäres Modell:

```text
Qwen/Qwen3-4B-GGUF:Q4_K_M
```

Manueller Review-Aufruf:

```bash
/home/work/.local/bin/self-confidence-review "Input: <zu pruefende Self-Confidence/Begruendung>"
```

Einsatzregel:

- Bei `Self-Confidence > 1.0`: Validator-Review auslösen.
- Bei sehr glatter, aber unbelegter Begründung: Validator-Review auslösen.
- Bei Review-/Freigabe-/Sicherheitsentscheidungen: Validator als unabhängiges Signal nutzen.
- Bei normaler, einfacher Ausführung ohne Confidence-Behauptung: nicht unnötig blockieren.

## Josie-Regel

Wenn ein Modell eine Begruendung liefert, ist diese kein Beweis. Josie muss zwischen Plausibilitaet, Validierung und realer Ausfuehrbarkeit unterscheiden. Ein freigegebener und verfügbarer Validator liefert ein Review-/Routing-Signal, keine absolute Wahrheit. Der lokale HP-Validator ist derzeit ausgeschlossen; die Architekturplanung bedeutet keine Betriebsfreigabe.
