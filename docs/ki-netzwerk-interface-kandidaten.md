# KI-Netzwerk, Interface und Laptop: Kandidatenliste

Stand: 2026-06-05

Diese Liste sammelt Kandidaten aus der Planungsnotiz `Fragen zu Artikeln die eine Verbesserung zu KI-Netz, verbundenem standalone Interface und Laptop sein koennen.md`.

Sie ist keine Architekturentscheidung. Einzelne Tools und Artikel muessen separat geprueft werden, bevor sie in die Zielarchitektur uebernommen werden.

## Aktive Analyse-Kandidaten

### SkillServer

- Quelle: <https://github.com/mudler/skillserver>
- Rolle: moeglicher Werkzeugkanal fuer KI-Netzwerk und Interface.
- Status: Analyse-Kandidat.
- Prueffragen:
  - Kann SkillServer Skripte und Tools stabil im lokalen Netzwerk bereitstellen?
  - Passt die Architektur zu Hermes-Agent, lokalen Modellservern und spaeteren Worker-Nodes?
  - Laesst sich der Einsatz ohne unnoetige Node.js-/npm-Abhaengigkeit betreiben?
  - Gibt es ein brauchbares Rechte-, Isolation- und Logging-Modell?

### fastsdcpu

- Quelle: <https://github.com/rupeshs/fastsdcpu>
- Rolle: moeglicher Bildgenerator fuer KI-Netzwerk und Interface.
- Status: Analyse-Kandidat.
- Prueffragen:
  - Reicht die CPU-Performance fuer lokale Bildgenerierung oder nur fuer kleine/experimentelle Jobs?
  - Passt der Dienst auf vorhandene Hardware, ohne den Modellbetrieb zu blockieren?
  - Kann er spaeter sauber hinter Interface, Queue oder Toolserver betrieben werden?

### DeepGen 1.0

- Quelle: Medium-PDF `A 5B Model that Proves Smarter Architecture Beats an 80B Giant`
- Rolle: moeglicher multimodaler Kandidat fuer Bildgenerierung, Editing und Textrendering.
- Status: Analyse-Kandidat.
- Prueffragen:
  - Sind Gewichte, Code, Lizenz und Hardwarebedarf praktisch nutzbar?
  - Laeuft das Modell auf vorhandener oder geplanter Hardware sinnvoll?
  - Ist der Nutzen gegenueber fastsdcpu oder anderen lokalen Bilddiensten gross genug?
  - Wie gut funktionieren Deutsch/Englisch-Prompts, Story-Kontext und Bildbearbeitung?

## Offene Artikel und Themen

- Token-Einsparung und Speedup:
  - `Anthropic Just Solved AI Agent Bloat - 150K Tokens Down to 2K`
- Startup-Token- und Zeit-Optimierung:
  - `I Cut Claude Code Exploration Time and Costs by 30% With One Tool`
- Repo-/Job-Abschlusskopien:
  - `How I Set Up My Repo So AI Can Write and Review 100% of My Code` - verarbeitet als Guardrails-/Policy-Gate-Pattern; keine 100-Prozent-Autonomie.
- Uebersetzungs-Worker:
  - `The Open-Source DeepL Alternative Is Here` - verarbeitet als Translation-Worker-Kandidat; HY-MT1.5-1.8B/7B spaeter testen.
- Validator-Idee:
  - TMR/Samsung-7M nur pruefen, falls ein real nutzbarer Download und belastbare Quellen verfuegbar sind.

## Gestrichene Punkte

- Node.js-Vermeidung als feste Leitplanke ist hinfaellig.
- FastAPI-WebUI ist hinfaellig.
- Nanobot war nicht ernsthaft im Gespraech und wird nicht weiter verfolgt.

## Arbeitsregel

Diese Kandidatenliste dient nur als Wegweiser fuer spaetere Einzelbesprechungen. Keine Komponente wird aus dieser Liste heraus direkt installiert oder als Architektur-Baustein gesetzt.
