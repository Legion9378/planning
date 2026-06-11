# Sensor Guard Tray Monitor

## Ziel

`Sensor Guard` ist ein leichtgewichtiges Linux-Tray-Tool fuer Ubuntu 24.04+ und Derivate. Es zeigt dauerhaft, ob Mikrofon, Kamera oder Screen-Capture/Screen-Sharing aktiv sind.

Ziel ist ein Smartphone-aehnlicher Privacy-Indikator fuer Desktop-Linux, besonders fuer Xfce/Xubuntu, aber moeglichst desktopuebergreifend.

## Mindestplattform

- Ubuntu 24.04 oder neuer
- Ubuntu-Derivate wie Xubuntu, Kubuntu, Ubuntu MATE, Cinnamon-basierte Setups
- PipeWire
- WirePlumber
- xdg-desktop-portal
- Linux V4L2 fuer `/dev/video*`

Aeltere PulseAudio-/Portal-Sonderfaelle werden nicht als Startziel eingeplant.

## UI-Regel

Drei getrennte Tray-Icons bleiben immer sichtbar:

- Screen Capture: grau = inaktiv, rot = aktiv
- Kamera: grau = inaktiv, gruen = aktiv
- Mikrofon: grau = inaktiv, orange = aktiv

Damit ist sichtbar:

- Monitoring laeuft.
- Ein aktiver Sensor faellt sofort auf.
- Detailinformationen kommen per Tooltip.

## Tooltip-Information

Tooltip pro Sensor:

```text
Microphone active
Process: Firefox
PID: 18322
```

oder:

```text
Camera active
Process: Zoom
```

oder:

```text
Screen capture active
Process: OBS Studio
```

## Logging

Logpfad Kandidat:

```text
~/.local/share/sensor-guard/log.txt
```

Logeintraege sollen mindestens enthalten:

- Zeitstempel
- Sensor
- Event (`activated`, `released`)
- Prozessname, falls ermittelbar
- PID, falls ermittelbar

Beispiel:

```text
2026-03-10 02:14:22 microphone activated firefox pid=18322
2026-03-10 02:14:59 microphone released
2026-03-10 03:02:11 camera activated zoom
```

## Technische Architektur

Empfohlener Start-Stack:

- Sprache: Python
- Tray/UI: PyGObject + AppIndicator/StatusNotifier
- Audio: PipeWire, spaeter direkte API oder fuer Prototyp `pw-dump`/`pw-cli`
- Kamera: V4L2 `/dev/video*`, Prozesspruefung zunaechst via `lsof`
- Screen Capture: xdg-desktop-portal / ScreenCast-API via DBus
- Logging: Python `logging`

Modulstruktur Kandidat:

```text
sensor-guard/
  main.py
  tray.py
  monitor_microphone.py
  monitor_camera.py
  monitor_screencast.py
  logger.py
  icons/
    mic-grey.svg
    mic-orange.svg
    cam-grey.svg
    cam-green.svg
    screen-grey.svg
    screen-red.svg
```

## Icon-Regel

- SVG als Master.
- PNG-Varianten fuer typische Panelgroessen: 12 px, 16 px, 22 px, 24 px.
- Keine Abhaengigkeit von nur einem Desktop-Tray-System.
- StatusNotifier/AppIndicator als bevorzugter Weg.

## Ressourcen-Ziel

Das Tool soll leicht bleiben:

- ca. 10-30 MB RAM als Zielkorridor
- praktisch keine Dauer-CPU-Last
- ereignisorientiert oder sparsames Polling im Prototyp

## Schwieriger Teil

Screen-Capture-Erkennung ist der schwierigste Teil. Browser, OBS, Remote-Desktop und Portal-Implementierungen muessen praktisch getestet werden.

## Naechste Schritte

1. Prototyp fuer dauerhaft sichtbare AppIndicator-Icons bauen.
2. Kamera-Aktivitaet ueber `/dev/video*` und `lsof` pruefen.
3. Mikrofon-Aktivitaet ueber PipeWire-Status pruefen.
4. ScreenCast-/Portal-Ereignisse ueber DBus untersuchen.
5. Logging und Tooltip-Prozessauflistung einbauen.
6. Auf Xubuntu 24.04 zuerst testen, danach KDE/MATE/Cinnamon/GNOME pruefen.

## Quelle

Ausgewertet aus Chat-History:

`chatgpt-gsd-bedeutung-erklaren-2026-05-07T02-38-52-595Z.md`
