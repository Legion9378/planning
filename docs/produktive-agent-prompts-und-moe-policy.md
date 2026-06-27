# Produktive Agent Prompts und MoE Policy

Stand: 2026-06-24
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-ralph-loop-in-jobflows-2026-05-07T02-13-28-031Z.md`

## Production-Prompt-Regel

Produktive Jobflow-Templates nutzen keine psychologischen Trigger als Standard.

Nicht als Default:

- `$200 tip`,
- `I bet you can't`,
- kuenstliche Challenge-/Motivationssprache,
- emotionale Dringlichkeit als Qualitaetsersatz,
- unbegrenzte Self-Reflection.

Stattdessen:

- klare Rolle,
- konkrete Aufgabe,
- Constraints,
- strukturierter Ablauf,
- Beleg-/Toolpflicht,
- begrenzte Self-Evaluation,
- Confidence-Gating,
- Review-/Validator-Ausloeser.

## Creative Mode

Fuer Story, Design, Brainstorming und Stilfindung duerfen Prompts freier und kreativer sein. Das ist aber ein anderer Modus als Production Mode.

## Rollendefinition

Detailed Persona bedeutet im Produktionskontext: praezise Rollenbeschreibung.

Beispiele:

- Runtime/Sprache,
- Architekturverantwortung,
- Performance-/Memory-Budget,
- keine erfundenen APIs,
- Testpflicht,
- Reviewpflicht,
- Begruendungspflicht.

## Self-Evaluation

Self-Evaluation wird nur begrenzt eingesetzt:

```text
Output erzeugen
  -> Konsistenz pruefen
  -> Confidence/Risiken melden
  -> bei Auffaelligkeit Validator/Review ausloesen
```

Keine endlosen Selbstverbesserungsschleifen.

## MoE-Regel

MoE reduziert Compute, nicht Speicherbedarf.

Alle Experten muessen im Speicher liegen, auch wenn pro Token nur wenige aktiv sind.

Daher gilt fuer Bjoerns CPU-first-/Low-Power-Planung:

- MoE nicht aktiv verfolgen, solange keine grosse GPU, viel VRAM oder grosser Unified-Memory-Host geplant ist.
- Dense-Modelle plus Review-/Validator-Loops sind bevorzugt.
- Bestehende Rollen-/Workflow-Planung bleibt wichtiger als beeindruckende Modellgroesse.

## Geeignete Strategie

- 7B/14B Dense-Modelle,
- klare Prompt-Contracts,
- getrennte Reviewer/Validatoren,
- Self-Confidence-Validator,
- Agentenebene als eigenes System-MoE.

## Separat pruefen

Model2Vec und LEANN wurden nur erwaehnt, nicht analysiert. Bei Bedarf separate Quellenpruefung.
