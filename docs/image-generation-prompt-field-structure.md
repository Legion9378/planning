# Image Generation Prompt Field Structure

Stand: 2026-10-07 (Owner-Review der CPU-Bildworkflow-Praeferenz)
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

Owner-Korrektur im Memory-Review: **ComfyUI-CPU ist fuer KI-Bedienung bevorzugt**, weil es mehr Feinabstimmung des Bildworkflows ermoeglicht. Die lokale API ist fuer Josie/Automation wichtig. „Fine Tuning“ wird hier als Workflow-/Parameter-Feinabstimmung festgehalten, nicht als neuer Modelltrainingsauftrag.

Die fruehere Aussage „demnaechst installieren“ ist keine aktuelle Termin- oder Installationsfreigabe. Zielhost, Modelle, Ressourcen, Installation und API-Bedienung muessen bei einer konkreten Umsetzung geprueft werden; kein aktueller Betriebsnachweis aus dieser Praeferenz.

## FastSDCPU als Alternative

Laut Bjoerns Ergaenzung ist **FastSDCPU ebenfalls eine Moeglichkeit**, weil es im Gegensatz zum bisherigen EasyDiffusion-Pfad einen API-Modus anbietet. ComfyUI-CPU bleibt fuer KI-Bedienung bevorzugt; FastSDCPU ist ein alternativer Kandidat, kein parallel verpflichtend zu installierender Dienst.

Das ist eine Owner-Einordnung, keine neue Hersteller-/Versions- oder API-Pruefung. Vor Nutzung konkrete Version, CPU-/Modellkompatibilitaet, steuerbare Parameter, API-Vertrag, Ressourcenbedarf und reproduzierbaren Generierungsaufruf testen. Die Einordnung des bisherigen EasyDiffusion-Pfads ist keine neu recherchierte pauschale Aussage ueber alle Versionen oder Erweiterungen.

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
