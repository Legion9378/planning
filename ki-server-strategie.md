# Zusammenfassung der KI-Server-Strategie (Stand 29.05.2026)

**Geplante Aufteilung der drei headless Rechner:**

- **Intel NUC (8th Gen, 32 GB)**: Primärer dedizierter Modellserver für deinen Laptop über Netzwerk. Minimales Ubuntu Server + Ollama/LocalAI, maximaler RAM für Modelle.
- **Ryzen 5 4300U (32 GB)**: Haupt-Node für das zukünftige KI-Netzwerk/Cluster.
- **Ace Magic Kron M1 Mini (16 GB)**: Kleiner Worker-Node (z. B. für Whisper-Audio oder kleine Modelle).

**Historische/spätere Option: Mac mini Late 2012**

- Ursprünglich war Agent Brain als Zusatz zu `opencode` geplant, bevor ChatGPT Plus/Codex in den Workflow kam.
- Zielrolle: Code-RAG-/Search-Dienst für Codingmodelle, nicht Modellrunner.
- Geplantes OS: Ubuntu Server.
- Nutzen: AST-aware Code-Indexing, BM25/Vector/Graph-Suche und per-project RAG für Coding-Assistenten.
- Bewertung heute: für Codex nicht zwingend nötig, aber später nützlich als lokaler Retrieval-Dienst für ältere/schwächere Codingmodelle, große Repos oder opencode-Experimente.
- Agent Brain bleibt damit eine optionale Tool-Schicht, keine Pflichtkomponente des KI-Netzwerks.

**Ziel:** Alle drei Rechner komplett headless, nur Betriebssystem + Inference-Software, alles andere raus für maximale RAM-Verfügbarkeit.

Diese Aufteilung priorisiert Stabilität und Einfachheit. Der NUC dient direkt deinem Laptop, die anderen beiden bleiben für Cluster-Experimente frei.
