# LAN-Discovery und Node-Erkennung

Stand: 2026-07-08
Status: Planungsnotiz
Quelle: Chat-History `chatgpt-lan-scanner-fur-ubuntu-2026-05-07T01-31-16-958Z.md`

## Ziel

Bjoern braucht einen schnellen Weg, um zu erkennen, ob ein neuer Rechner/Node korrekt bootet und im Heimnetz erkannt wird, ohne jedes Mal:

- die FRITZ!Box-Weboberflaeche zu oeffnen;
- manuelle Terminalabfragen auszufuehren;
- IPs haendisch zu erraten.

Das Tool ist kein Security-Portscanner als Selbstzweck, sondern ein praktischer Node-Discovery-/Boot-Verifikationshelfer fuer das KI-Netzwerk und die Heimnetz-Infrastruktur.

## Heimnetz-Kontext

- FRITZ!Box ist DHCP-/DNS-Quelle.
- Zielzugriff erfolgt bevorzugt ueber `hostname.fritz.box`.
- Lange DHCP-Leases sind Bjoerns Wartungsstrategie.
- Korrektur: FRITZ!Box 7690 mit aktuellem FRITZ!OS erlaubt maximal 3650 Tage Lease, also knapp 10 Jahre.
- IPs koennen sich theoretisch aendern und sind Fallback, nicht Identitaet.

## Gewuenschte Funktionen

Minimal:

- lokales Subnetz scannen oder bekannte Hosts pruefen;
- Hostname, IPv4, IPv6, MAC, Antwortstatus anzeigen;
- SSH-Port/HTTP(S)-Port fuer bekannte Node-Typen pruefen;
- neue oder verschwundene Geraete hervorheben;
- `hostname.fritz.box`-Aufloesung testen;
- Ergebnis als kleine Tabelle ausgeben.

Spaeter optional:

- bekannte Nodes aus Planning/Inventar laden;
- zuletzt gesehen / zuerst gesehen speichern;
- einfache Web-/PWA-Ansicht;
- Benachrichtigung, wenn ein erwarteter Node nach Boot nicht erreichbar ist;
- Integration in Hermes/Josie als Tool.

## Moegliche technische Wege

- `arp-scan` fuer Layer-2-Erkennung im LAN;
- `nmap -sn` fuer Ping-/Host-Discovery;
- `getent hosts` / mDNS/DNS fuer `*.fritz.box`;
- `ssh -o BatchMode=yes` fuer Key-Login-Readiness;
- FRITZ!Box-/TR-064-Abfrage nur falls spaeter sinnvoll und sicher.

## Nicht aus dieser Quelle uebernehmen

- LocalAGI-/MCP-Begriffe als aktuelle Architektur.
- 10000-Tage-Lease; aktueller Wert ist maximal 3650 Tage.
- Pi400/Pi5/Mac Mini/Bmax als aktuelle Pflichtliste.
- nmap/arp-scan als bereits gesetzte Implementierung ohne Test.
