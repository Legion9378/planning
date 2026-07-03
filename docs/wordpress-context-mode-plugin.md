# WordPress Context-/Mode-Plugin

Stand: 2026-07-03
Quelle: `/home/work/Archiv_entpackt/KI 2/Chathistory/chatgpt-technik-von-freebitco-in-2026-05-07T01-47-54-549Z.md`

## Entscheidung

Es wird nur das Prinzip und die Art des Aufbaus uebernommen, nicht Design, Code oder konkrete Implementierung einer fremden Website.

Ziel ist, das Grundgeruest einer portal-/gameartigen WordPress-Seite im gewissen Sinne nachzuempfinden, aber mit eigenen Ideen zu verfeinern und moeglicherweise zu verbessern.

## Architekturprinzip

- WordPress bleibt Backend, CMS, Admin- und Account-Basis.
- Das eigene Frontend rendert die oeffentliche Seite.
- Theme = Layout, Platzhalter und grundlegende Darstellung.
- Eigenes Context-/Mode-Plugin = interpretiert den aktiven Seiten-/Menuekontext.
- Eigene Module/Plugins = Spiel-, Blog-, Forum- oder Speziallogik.
- Kritische Entscheidungen laufen serverseitig, nicht nur im Frontend.

## Menue als Kontextgeber

Das obere Hauptmenue ist die zentrale Kontextentscheidung:

- Es legt fest, welcher Content-Modus aktiv ist.
- Es entscheidet, ob ein linkes Submenue existiert.
- Es bestimmt indirekt, welche Art Submenue/Sidebar sinnvoll ist.

Beispielhafte Kontext-Metadaten:

```text
content_mode = blog | forum | game | static | custom
submenu_type = pages | categories | game | forum | none | custom
sidebar_type = widgets | game_stats | latest_posts | none | custom
```

## Resolver-Prinzip

Das Context-/Mode-Plugin loest aus dem Menue-/Seitenkontext ab:

```text
Top-Menuepunkt -> Content-Modus -> Submenue -> Sidebar -> Hauptinhalt-Kontext
```

Beispiele:

- Blog: Kategorien, Tags, letzte Posts.
- Forum: Foren, Unterforen, letzte Threads.
- Browsergame: Inventar, Karte, Stats, Shop, Energie, Events.
- Statische Seiten: Seitenhierarchie oder kein Submenue.

## Abgrenzung

Nicht uebernehmen:

- fremdes Design,
- fremder Code,
- Reverse Engineering,
- konkrete freebitco.in-Implementierung,
- Behauptungen ueber den tatsaechlichen internen Stack fremder Seiten ohne Pruefung.

Uebernehmen:

- klassisches Web-Stack-Prinzip,
- konstantes Layout mit dynamischem Funktionskontext,
- kontextabhaengige Menues/Submenues/Sidebars,
- eigene WordPress-Plugins/Module fuer Logik,
- eigene Ideen und Verbesserungen als eigentliche Produktdifferenzierung.

## Bezug zum Browser-Game-Modul

Das Browser-Game-Modul fuer WordPress nutzt diese Architektur:

- Game ist ein eigener Content-Modus.
- Game-Submenues und Sidebars werden kontextabhaengig gerendert.
- Grundstack bleibt HTML, htmx und JavaScript.
- Canvas oder Game-Engine bleiben spaetere Optionen, nicht Startvoraussetzung.
