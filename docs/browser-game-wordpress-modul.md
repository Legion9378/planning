# Browser-Game-Modul fuer WordPress

Stand: 2026-06-27
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-spiele-integration-auf-webseiten-2026-05-07T07-48-53-070Z.md`

## Entscheidung

Das Spiel soll als Browser-Game-Modul fuer die WordPress-basierte Website entstehen.

Grundstack:

- HTML,
- htmx,
- JavaScript,
- WordPress als Backend-/CMS-/Admin-Basis,
- eigenes Frontend fuer die oeffentliche Darstellung.

Der Inhalt der Quelle bleibt in der Planung erhalten: Fuer die erste Version wird kein Canvas vorausgesetzt.

## UI-Regel

Erste Umsetzung:

```text
HTML + htmx + JavaScript
```

Nicht zuerst:

```text
Canvas
Phaser/Game Engine
SPA-only Frontend
```

Begruendung:

- echte DOM-Elemente sind leichter zu debuggen,
- Tabellen, Buttons, Inputs und Sections sind direkt inspectable,
- CSS kann normal genutzt werden,
- htmx kann serverseitige HTML-Fragmente nachladen,
- Spiellogik kann sauber von Darstellung und spaeteren Rendering-Varianten getrennt werden.

Canvas bleibt spaeter moeglich, wenn Gameplay/State stabil sind oder einzelne Darstellungsbereiche davon profitieren.

## WordPress-Kontext

Das Modul passt zur inzwischen ausgearbeiteten Website-Architektur:

- WordPress bleibt Backend/Admin/Content-Basis.
- Das eigene Frontend rendert oeffentliche Seiten/Module.
- HTMX dient fuer servergetriebene Interaktion und HTML-Fragmente.
- JavaScript bleibt fuer lokale UI-Interaktion, Tick-/State-Anzeige und notwendige Clientlogik.
- WordPress-Core wird nicht direkt veraendert; Theme, Plugin, Hook, Filter, eigenes Modul oder Micro-Service bevorzugen.
- Das Browsergame ist ein Content-Modus innerhalb der Context-/Mode-Plugin-Architektur.

## Grundgeruest-Prinzip

Aus portal-/gameartigen Referenzseiten wird nur das Prinzip des Aufbaus uebernommen:

- konstantes Grundlayout,
- oberes Hauptmenue als Kontextgeber,
- dynamisches linkes Submenue je nach Modus,
- optional kontextabhaengige rechte Sidebar,
- eigener Hauptinhalt pro Modus.

Nicht uebernommen werden fremdes Design, fremder Code oder konkrete Implementierungen. Das Ziel ist ein eigenes Modul mit eigenen Ideen, das ein bewaehrtes Grundgeruest nutzt und verbessert.

Detailregel: `/home/work/Local-git/planning/docs/wordpress-context-mode-plugin.md`.

## Spielkontext aus der Quelle

Die Quelle erwaehnt ein fruehes Spielkonzept mit:

- Statusbereich,
- Tick/Uhrzeit,
- Coins,
- Energie,
- Faucet,
- SBC-Regale/Rigs,
- Storage/Energiespeicher,
- Actions,
- Buttons wie Kaufen, Reparieren, Verkaufen, Lernen,
- clean/retro/Monospace-Stil.

Diese Begriffe sind Planungs-/Kontextmaterial, kein finaler UI-Code.

## Nicht aus der Quelle ableiten

- Canvas ist nicht grundsaetzlich verboten.
- Phaser.js ist kein gesetztes Ziel.
- Das HTML-Beispiel aus der Quelle ist kein finaler Code.
- Sicherheitsluecke wird aus dieser Datei nicht konkretisiert; dafuer muss die separate Sicherheitsdatei/Quelle geprueft werden.
