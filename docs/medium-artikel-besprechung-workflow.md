# Medium-Artikel-Besprechung Workflow

Stand: 2026-07-06
Status: Planungsregel / Tool-Test offen
Quelle: Chat-History `chatgpt-zugriff-auf-medium-artikel-2026-05-07T01-48-24-769Z.md`

## Ziel

Medium-Artikel sollen so vorbereitet werden, dass sie mit KI besprochen werden koennen, ohne unnoetig viele Tokens durch PDF-Layout, Druckartefakte oder rohe Dokumentstruktur zu verbrauchen.

## Zugriff nach Artikeltyp

### Frei lesbare Artikel

Wenn ein Medium-Artikel frei lesbar ist:

- kann der Artikel normal per Browser/Web-Extraktion gelesen werden;
- eine KI darf denselben frei erreichbaren Inhalt als Quelle nutzen;
- URL-basierte Extraktion ist der bevorzugte erste Weg.

### Mitglieder-/App-Artikel

Wenn ein Artikel nur ueber Medium-Mitgliedszugang oder in der Medium-App lesbar ist, kann die KI ihn nicht direkt lesen.

Dann stellt Bjoern den Artikel manuell lokal bereit:

1. Artikel in der Medium-App auf dem iPhone oeffnen.
2. Artikel in Chrome oeffnen.
3. Druck-Dialog aufrufen.
4. Ueber Teilen die zum Drucken geparste PDF speichern.
5. Diese PDF lokal fuer die KI-Besprechung bereitstellen.

Erst diese lokal gespeicherte PDF ist dann die Arbeitsgrundlage fuer die KI.

## PDF -> Markdown Vorverarbeitung

Vor der KI-Besprechung soll eine gespeicherte Medium-PDF moeglichst nach Markdown konvertiert werden.

Ziele:

- weniger Tokenverbrauch als rohe PDF-/Layout-Erfassung;
- bessere Abschnittsstruktur;
- besser kopier- und zitierbarer Text;
- weniger OCR-/Rendering-Muell;
- bessere Grundlage fuer Zusammenfassung, Kritik und KB-/Planning-Extraktion.

## Bevorzugter Startpfad: MarkItDown

Bjoern hat sich fuer diesen Workflow mental auf **MarkItDown** als bevorzugten Startpfad festgelegt.

Gruende:

- MarkItDown kann mit freien Plugins mehrere Textdokumentformate nach Markdown konvertieren.
- Es soll Textformatierung/Struktur moeglichst erhalten.
- Es passt besser zum Ziel, KI-freundliches Markdown vor der eigentlichen Besprechung zu erzeugen.

MarkItDown ist damit der erste Kandidat fuer praktische Tests. Trotzdem gilt: Ergebnisqualitaet wird geprueft, bevor grosse Batch-Konvertierungen als verlaesslich gelten.

## Tool-Grenzen und Tests

- MarkItDown/Plugins muessen lokal auf dem aktuellen System getestet werden.
- System-Python nicht direkt mit `pip install` veraendern; PEP-668/venv beachten.
- Konvertierte Markdown-Dateien werden stichprobenartig gegen die PDF geprueft:
  - Ueberschriften;
  - Abschnitte;
  - Listen;
  - Code-/Tabellenbereiche;
  - Zitate/Links;
  - verlorene oder doppelte Textteile.
- Calibre ist fuer diesen Medium-PDF-Workflow nicht der bevorzugte Standard.
- Cloud-Konverter sind kein Default.

## Nicht uebernehmen

- Keine alte Xubuntu-24.04-/Python-3.12-Annahme als aktuell.
- Kein LocalRecall als aktiver Zielpfad.
- Keine blinde Massenkonvertierung ohne Qualitaetskontrolle.
- Keine Umgehung von Zugangsbeschraenkungen: Mitgliederartikel werden nur verarbeitet, wenn Bjoern sie selbst lokal als PDF bereitstellt.
