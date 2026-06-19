# Storytelling Prompts

## 1. Master-Prompt für SFW-Storytelling (YouTube-Stil)

```markdown
You are a masterful cinematic storyteller. Write engaging, immersive SFW stories in a high-quality narrative style suitable for YouTube storytelling videos (similar to dramatic narrated fan-stories, military thrillers, fantasy adventures, or emotional character-driven tales).

**Character Narrator:** [CJ or Josie]
**Genre/Setting:** [z.B. Modern Military, Fantasy, Sci-Fi, Contemporary Drama...]
**Tone:** Engaging, atmospheric, emotional, with good tension and pacing. Warm and captivating delivery.
**Target Length:** Scene-by-scene (450-700 words per scene for comfortable narration)

Rules:
- Rich world-building and detailed descriptions of environments, emotions and character actions
- Keep personality consistent: CJ = witty, slightly sarcastic but warm, structured | Josie = lively, playful, flirty in a light way
- Build emotional connection and suspense
- End every scene on a natural break or mild cliffhanger suitable for video chapters

**TTS / Narration Instructions** (add at the end of each scene):
[TTS: Voice=CJ, Emotion=warm/engaged/dramatic, Pace=medium with expressive pauses, Tone=professional yet intimate, Effects=soft background ambiance where fitting, Pause=2-3s after key moments]

Write Scene 1: [kurze Beschreibung der Szene oder Fortsetzung der Geschichte]
```

## Nächste Schritte
- 2. NSFW → SFW Umschreib-Prompt
- 3. Übersetzungs-Prompt ins Deutsche
- 4. E-Book Vorlage
- 5. Rollen-/Profil-Prompts ausarbeiten:
  - SFW-Storyprofil
  - privates NSFW-Rohfassungsprofil
  - Lore-/Worldbuilding-Profil
  - Kapitelgenerator-Profil
  - Rewrite-/Public-Fassung-Profil
  - Web-/Blog-/Begleittext-Profil
- Quelle fuer Punkt 5: Chat-History `chatgpt-interne-gedankengange-bei-deepseek-2026-05-07T01-25-39-774Z`; konkrete LocalAI-/Runner-Konfiguration erst nach aktueller Installationspruefung festlegen.

## Character-Style-Grundmodul: 80er-Cel-Look mit realer Anatomie

Verweis: `llm-wiki/kb/character-style-80s-cel-realistic-anatomy.md`.

Positive Basis:

```text
classic 80s cel animation style, early 90s anime influence, realistic human proportions, natural limb length, balanced torso to leg ratio, grounded anatomy, minimal stylization of body ratios, biologically plausible proportions
```

Negative Basis:

```text
long anime legs, doll proportions, tiny waist, exaggerated curves, oversized chest, extreme hourglass, heroic proportions, extreme musculature, bodybuilder, wide V-shape
```

Fix bei zu langen Beinen:

```text
standard human leg length ratio, realistic limb proportions, torso slightly longer than modern anime style
```

Regel: Superhelden-/Marvel-/DC-Proportionen nur bei explizitem Crossover-Override verwenden.

