# Image Generation Prompt Field Structure

Stand: 2026-06-27
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-realistische-bildgenerierung-tipps-2026-05-07T02-21-24-633Z.md`

## Regel

Bildprompts werden zielinterface-kompatibel erzeugt.

Standardfelder:

```text
Positive Prompt
Negative Prompt
```

Optional je nach Interface:

```text
Styles
LoRA
Embeddings
Workflow-Parameter
Seed/Steps/CFG/Sampler/Groesse
```

## Positive Prompt

Positive Prompt enthaelt gewuenschte Merkmale:

```text
STYLE_CORE + FOCUS_PROFILE + SCENE_CONTENT
```

Beispiele fuer Module:

- `STYLE_CORE`: konstanter Stil eines Projekts,
- `FOCUS_PROFILE`: Portrait/Midshot/Wideshot,
- `SCENE_CONTENT`: konkrete Szene.

## Negative Prompt

Negative Prompt enthaelt nur unerwuenschte Merkmale:

- falscher Stil,
- Artefakte,
- falsche Proportionen,
- unerwuenschte Licht-/Renderwirkung.

## EasyDiffusion

Bjoern hat bisher EasyDiffusion genutzt.

Eigenschaften:

- CPU-Unterstuetzung vorhanden,
- keine API/Webhooks fuer Josie,
- Positive-/Negative-Prompt muessen jeweils einzeilig bleiben,
- jede neue Zeile wird als neues Bild behandelt.

Daher fuer EasyDiffusion:

```text
Keine mehrzeiligen Positive-/Negative-Prompts erzeugen.
```

## ComfyUI-CPU

ComfyUI-CPU soll demnaechst installiert werden, weil ComfyUI eine lokale API fuer Josie bereitstellt.

Fuer Josie/Automation ist ComfyUI deshalb der bevorzugte Bildworkflow-Pfad, auch wenn CPU-only langsam ist.

## Konsistenz statt Pipeline-Zwang

Bjoern braucht nicht zwingend eine automatische Bildpipeline. Ziel ist reproduzierbar gute Bildqualitaet, auch wenn der Prozess komplett manuell bleibt.

Stabil halten:

- Modell,
- Sampler,
- Steps,
- CFG Scale,
- Seed,
- Positive Prompt,
- Negative Prompt.

Wenn ein Bild gut ist, Seed und Parameter speichern. Varianten nur kontrolliert und minimal aendern.

Eine ComfyUI-CPU-Pipeline im KI-Netzwerk kann spaeter dazukommen, ist aber nicht Voraussetzung fuer das Ziel.

## Nicht uebernehmen

Aus der alten Quelle nicht als aktuellen Standard uebernehmen:

- SD 1.5 als dauerhaftes Zielmodell,
- konkrete CPU-Aufloesungsannahmen,
- alten Beispielstil als Projektstandard,
- alte Installationshinweise ohne aktuelle Pruefung.
