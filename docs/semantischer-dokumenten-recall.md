# Semantischer Dokumenten-Recall und JobFlow-Mem-Kopplung

Stand: 2026-06-23
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-pdf-reader-und-tokenizer-2026-05-07T02-01-03-874Z.md`

## Entscheidung

Der Recall-Layer wird als universelle Infrastruktur geplant, nicht als isoliertes Story-RAG. Story-RAG ist nur ein Anwendungsfall fuer Story-Pipelines. LLM-Wiki und der spaetere `The Novelist`-Obsidian-Vault erweitern den Anwendungsbereich deutlich.

## Zielbereiche

- LLM-Wiki und Quellenarbeit
- technische Dokumentation
- Planung und Architekturentscheidungen
- E-Mail- und Dokumenten-Recall
- gescannte Papierkorrespondenz
- Story-Pipelines
- The-Novelist-Obsidian-Vault
- Agenten-/Jobwissen

## Mindest-Metadaten fuer Dokumenten-Recall

- `document_id`
- `thread_id` optional
- `chunk_index`
- `prev_chunk_id`
- `next_chunk_id`
- `timestamp`
- `source_type`
- Quelle/Pfad
- Titel/Betreff/Absender, soweit vorhanden

## Chunking-Regeln

- Rekursives Chunking bleibt Default-Prinzip.
- Keine pauschale 256-Token-Grenze aus Mobile-Demos uebernehmen.
- Zielgroesse wird nach Dokumenttyp, Modellfenster und semantischer Struktur bestimmt.
- Fuer 2K-4K-Kontextmodelle sind 800-1500 Token pro Chunk oft sinnvoller.
- Reserven fuer Prompt, mehrere Treffer, Sequenzkontext und Antwort einplanen.

## Pipeline

```text
Query
  -> Embedding
  -> Recall Layer
  -> JobFlow-Mem Layer
  -> Antwortmodell in iterativen Schritten
  -> finale Antwort / Zusammenfassung / Entscheidung
```

## Rollen

### Recall-Layer

- findet relevante Kandidaten
- liefert Chunk-IDs, Metadaten, Text und Sequenzkontext
- bleibt moeglichst stateless

### JobFlow-Mem-Layer

- speichert Kandidaten und Zwischenergebnisse
- verarbeitet groessere Quellenmengen sequenziell
- baut Antworten iterativ zusammen
- verhindert, dass alles gleichzeitig ins Kontextfenster gepresst werden muss

### Antwortmodell

- generiert Sprache
- arbeitet mit kontrolliertem Ausschnitt
- bekommt vom JobFlow-Mem nur den jeweils relevanten Kontext

## Josie-Einarbeitungsregel

Mobile Demo-Parameter sind keine Systemanforderungen. Vor Uebernahme immer pruefen, ob eine Grenze aus Handy-RAM, Akku, Thermik oder Demo-Umgebung stammt oder wirklich fuer Bjoerns stationaere Systeme gilt.
