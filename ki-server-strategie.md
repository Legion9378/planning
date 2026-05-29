# Zusammenfassung der KI-Server-Strategie (Stand 29.05.2026)

**Geplante Aufteilung der drei headless Rechner:**

- **Intel NUC (8th Gen, 32 GB)**: Primärer dedizierter Modellserver für deinen Laptop über Netzwerk. Minimales Ubuntu Server + Ollama/LocalAI, maximaler RAM für Modelle.
- **Ryzen 5 4300U (32 GB)**: Haupt-Node für das zukünftige KI-Netzwerk/Cluster.
- **Ace Magic Kron M1 Mini (16 GB)**: Kleiner Worker-Node (z. B. für Whisper-Audio oder kleine Modelle).

**Ziel:** Alle drei Rechner komplett headless, nur Betriebssystem + Inference-Software, alles andere raus für maximale RAM-Verfügbarkeit.

Diese Aufteilung priorisiert Stabilität und Einfachheit. Der NUC dient direkt deinem Laptop, die anderen beiden bleiben für Cluster-Experimente frei.