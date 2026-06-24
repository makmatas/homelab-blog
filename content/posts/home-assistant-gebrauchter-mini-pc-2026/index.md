---
title: "Home Assistant auf dem Mini-PC: Die ultimative Smarthome-Zentrale ab 40€"
date: 2026-06-24
draft: false
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Home Assistant auf einem Mini-PC – Smarthome-Zentrale für unter 100 Euro"
  relative: true
tags:
  - home-assistant
  - smart-home
  - mini-pc
  - low-budget
  - homelab
  - zigbee
  - docker
categories:
  - Smarthome
---

**Aktualisiert: Juni 2026 | Lesezeit: 8 Minuten**

Dein Zuhause soll intelligent werden: Licht schaltet sich automatisch aus, die Heizung regelt sich nach Anwesenheit und die Rollläden fahren bei Sonnenaufgang hoch. Dafür brauchst du eine Zentrale, die alle Geräte steuert.

**Home Assistant** ist die beste Lösung dafür – eine kostenlose Open-Source-Software, die über 2.000 verschiedene Geräte und Dienste miteinander verbindet. Und das Beste: Die Hardware dafür bekommst du als **Refurbished-Mini-PC für 40 bis 150 Euro**. Ein fertiges Home Assistant Green kostet neu 110 € – ein Mini-PC ist günstiger, leistungsstärker und oft sogar stromsparender.

Dieser Artikel zeigt dir, welcher Mini-PC für dein Smart Home am besten geeignet ist, was du außer dem PC noch brauchst und wie du alles in 15 Minuten zum Laufen bringst.

<!--more-->

---

## 🥇 Kurzempfehlung

| Kategorie | Empfehlung | Preis |
|-----------|-----------|-------|
| 🥇 Beste Preis-Leistung | Fujitsu Futro S7010 + 8 GB RAM + Sonoff Zigbee-Stick | ~75 € |
| 🚀 Beste Wahl für große Installationen | HP ProDesk 400 G4 (i5, 2 RAM-Slots) | ~120 € |
| 🏠 Beste Wahl für Home Assistant + KI | Lenovo M720q Tiny (6 Kerne, PCIe-Slot) | ~150 € |
| 🔧 Beste Wahl für Einsteiger (Neugerät) | GMKtec G3S (Garantie, kein Gebrauchtkauf) | ~210 € |

---

## Warum ein Mini-PC statt Raspberry Pi?

Home Assistant läuft auch auf einem Raspberry Pi – aber ein **x86-Mini-PC** ist die klar bessere Wahl. Das zeigt sich besonders mit dem aktuellen **Home Assistant 2026.6**:

| Kriterium | Mini-PC (Refurbished) | Raspberry Pi 5 (neu) |
|-----------|----------------------|----------------------|
| **Preis komplett** | 45–150 € (inkl. RAM, SSD, Netzteil) | ~120 € (nur Board + Gehäuse + SD-Karte + Netzteil) |
| **Speicher** | SSD (schnell, langlebig) | SD-Karte (langsam, fällt bei Dauerbetrieb oft nach 1–2 Jahren aus) |
| **RAM** | 8–16 GB (für große Installationen) | 4–8 GB (bei 8 GB Variante ~150 €) |
| **Stromverbrauch** | 4–14 Watt | 8–15 Watt |
| **Zuverlässigkeit** | Business-Hardware (24/7 ausgelegt) | Consumer-Hardware |
| **Erweiterbarkeit** | RAM+SSD wechselbar, PCIe bei Lenovo | Nur USB + GPIO |

**Der entscheidende Punkt mit HA 2026.6:** Die neue Version bringt massive KI-Integration und Matter-Upgrades – **genau das, was den Raspberry Pi überfordert**. Lokale KI-Sprachassistenten (Whisper) brauchen CPU-Power, und der neue Matter-Server profitiert enorm von RAM-Reserven. Ein Mini-PC mit 8–16 GB RAM und 4–6 Kernen hat dafür die Reserven – der Raspberry Pi mit 4–8 GB und ARM-CPU stößt hier schnell an seine Grenzen.

**Einziger Vorteil Raspberry Pi:** Der GPIO-Anschluss. Für 99 % aller Home-Assistant-Nutzer ist das irrelevant – Zigbee, Z-Wave und WLAN-Geräte werden per USB-Stick angebunden.

---

## Auf einen Blick: Budget-Stufen

| Budget | Gerät | RAM | SSD | Ideal für |
|--------|-------|-----|-----|-----------|
| **~60 €** | Fujitsu Futro S7010 + 8 GB | 8 GB | 64–120 GB | Smarthome mit 15–25 Geräten |
| **~120 €** | HP ProDesk 400 G4 | 8–16 GB | 256 GB NVMe | Große Installation, Kameras, Sprachassistent |
| **~150 €** | Lenovo M720q Tiny | 16 GB | 256 GB NVMe | Smarthome + KI-Modelle (Ollama) |
| **~210 €** | GMKtec G3S (neu) | 16 GB | 512 GB | Neugerät mit Garantie |

> **💡 Einsteiger-Tipp:** Der Monitor-Anschluss bei Thin Clients (Fujitsu Futro) ist **DisplayPort** (eckig, mit abgeschrägter Seite), nicht HDMI. Falls du nur einen HDMI-Monitor hast, brauchst du einen **DisplayPort-auf-HDMI-Adapter für ca. 5–7 €**.
>
> **⚠️ Wichtig beim RAM-Upgrade für den Futro:** Der S7010 braucht für 16 GB zwingend einen **Dual-Rank-Riegel (2Rx8)**. Ein Single-Rank-Riegel (1Rx8) wird nicht erkannt – der Futro bootet dann nicht. Prüf das Datenblatt vor dem Kauf oder kauf einen getesteten Riegel wie den Samsung M471A2K43BB1-CRC.

---

## 💰 Bis 60 € – Fujitsu Futro S7010 (Ultra-Budget)

**Ich betreibe genau dieses 40-Euro-Modell in meinem eigenen Setup.** Der Fujitsu Futro S7010 ist der absolute Preis-Leistungs-Champion: Er ist **lüfterlos** (absolut lautlos), verbraucht kaum Strom und kostet mit Gebraucht-Glück schon **unter 40 €**.

| Komponente | Spezifikation |
|------------|--------------|
| **Prozessor (CPU)** | Intel Celeron J4125 (4 Kerne, 2,0–2,7 GHz, 10 W) |
| **Arbeitsspeicher (RAM)** | 1 Steckplatz DDR4 SODIMM – offiziell max. 8 GB, **16 GB getestet** |
| **Festplatte** | 1× M.2 2280 – **nur SATA** (kein NVMe!) |
| **Netzwerk** | 1× Realtek Gigabit Ethernet |
| **Video** | 1× DisplayPort 1.2 (4K), 1× VGA (über Adapter) |
| **Kühlung** | **Lüfterlos** – absolut lautlos |
| **Stromverbrauch (Idle)** | 4–8 Watt |
| **Preis** | **30–50 € gebraucht** |

**Aus meiner Erfahrung:** Der S7010 läuft seit Monaten stabil mit Home Assistant OS, 16 GB RAM und einer 64 GB M.2 SATA SSD. 15–20 Zigbee-Geräte plus ein paar WLAN-Steckdosen – alles flüssig. Der einzige Moment, wo er nachdenkt: Beim Start von Home Assistant nach einem Update. Aber im laufenden Betrieb merkst du nichts.

**Vorteile:**
*   Günstigster Homelab-Server überhaupt – ab 30 € gemacht für dein Smarthome
*   Lüfterlos – kein Lüftergeräusch, kein Staub
*   Extrem stromsparend (unter 8 W im Leerlauf)
*   16 GB RAM inoffiziell getestet und nutzbar

**Nachteile:**
*   Nur **1 RAM-Slot** – RAM-Tausch statt Upgrade
*   **M.2 SATA only** – keine schnellen NVMe-SSDs
*   Realtek Netzwerk-Chip
*   Für große HA-Installationen (>30 Geräte) wird der Celeron langsam

**Home Assistant Eignung:**
*   **Home Assistant OS:** ✅ Ja – direkt installierbar, läuft flüssig
*   **Home Assistant Container (Docker):** ⚠️ Möglich, aber begrenzt
*   **Empfohlene Geräteanzahl:** 5–25 Zigbee-Geräte
*   **Add-ons:** Zigbee2MQTT, Node-RED, ESPHome – alles machbar
*   **KI-Sprachassistent:** ❌ Nicht empfohlen
*   **Matter:** ✅ Ja, aber bei vielen Thread-Geräten eher langsam

🔍 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=makmatas-homelab-21)

---

## 💰 80–150 € – HP ProDesk 400 G3/G4 oder Dell Optiplex 3060/3070 Micro

Der "richtige" Homelab-Server. Mit einem Intel Core i5 der 7.–9. Generation hast du spürbar mehr Reserven für große Smarthome-Installationen.

### HP ProDesk 400 G4 Mini (~100–180 € gebraucht)

| Komponente | Spezifikation |
|------------|--------------|
| **Prozessor (CPU)** | Intel Core i5-8500T (6 Kerne, 2,1–3,5 GHz, 35 W) oder i7-8700T (6C/12T) |
| **Arbeitsspeicher (RAM)** | 2 Steckplätze DDR4 SODIMM – bis 32 GB offiziell, 64 GB inoffiziell |
| **Festplatte** | 1× M.2 2280 NVMe/SATA + 1× 2,5″ SATA |
| **Netzwerk** | 1× Intel I219-LM Gigabit Ethernet (zuverlässig) |
| **Video** | 2× DisplayPort 1.2 |
| **Kühlung** | Aktiver Lüfter (sehr leise – unter 20 dB im Leerlauf) |
| **Stromverbrauch (Idle)** | 8–14 Watt |
| **Preis** | **100–180 € gebraucht** |

**Vorteile:**
*   6 Kerne (i5/i7) – spürbar mehr Leistung als die Futro-Celerons
*   2 RAM-Slots – nachrüstbar ohne bestehenden Riegel zu ersetzen
*   Intel Netzwerk-Chip – keine Treiber-Probleme
*   NVMe-SSD-Unterstützung – schnellerer Speicher

**Nachteile:**
*   Nicht lüfterlos – aber sehr leise
*   Höherer Stromverbrauch als Futro
*   Kein PCIe-Slot für Erweiterungen

### Dell OptiPlex 3070 Micro (~100–180 € gebraucht)

| Komponente | Spezifikation |
|------------|--------------|
| **Prozessor (CPU)** | Intel Core i5-9500T (6 Kerne, 2,2–3,7 GHz, 35 W) |
| **Arbeitsspeicher (RAM)** | 2 Steckplätze DDR4 SODIMM – bis 32 GB offiziell, 64 GB inoffiziell |
| **Festplatte** | 1× M.2 2230/2280 NVMe + 1× 2,5″ SATA |
| **Netzwerk** | 1× Intel I219-LM Gigabit Ethernet |
| **Video** | 2× DisplayPort 1.4 |
| **Kühlung** | Aktiver Lüfter |
| **Stromverbrauch (Idle)** | 6–12 Watt |
| **Preis** | **100–180 € gebraucht** |

**⚠️ Wichtig beim Dell OptiPlex:** Der M.2-Slot unterstützt sowohl 2230 als auch 2280 (die kürzere 2230-Variante ist teurer und seltener).

**Vorteile:**
*   Sehr stromsparend (oft unter 10 W im Leerlauf)
*   Intel Netzwerk-Chip
*   Große Dell-Community bei Problemen

**Nachteile:**
*   2280-SSDs sind günstiger und weiter verbreitet
*   Kein PCIe-Slot

**Home Assistant Eignung:**
*   **Home Assistant OS:** ✅ Perfekt
*   **Home Assistant Container (Docker):** ✅ Empfohlen – 6 Kerne + 16–32 GB RAM reichen für HA + viele Add-ons
*   **Empfohlene Geräteanzahl:** 25–100+ Geräte
*   **Kameras (Frigate):** ✅ Möglich – die iGPU kann Video-Streams decodieren
*   **KI-Sprachassistent:** ⚠️ Whisper läuft, aber langsam
*   **Matter + Thread:** ✅ Sehr gut geeignet

🔍 [HP ProDesk 400 G4 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=makmatas-homelab-21)
🔍 [Dell OptiPlex 3070 Micro bei Amazon suchen](https://www.amazon.de/s?k=Dell+OptiPlex+3070+Micro&tag=makmatas-homelab-21)

---

## 💰 150–200 € – Lenovo M720q Tiny (Der Erweiterbare)

| Komponente | Spezifikation |
|------------|--------------|
| **Prozessor (CPU)** | Intel Core i5-8500T (6 Kerne, 2,1–3,5 GHz) oder i7-8700T (6C/12T) |
| **Arbeitsspeicher (RAM)** | 2 Steckplätze DDR4 SODIMM – bis 32 GB offiziell, 64 GB getestet |
| **Festplatte** | 1× M.2 2280 NVMe + 1× 2,5″ SATA (Adapter nötig) |
| **Netzwerk** | 1× Intel I219-V Gigabit Ethernet |
| **Video** | 1× DisplayPort 1.2 + 1× HDMI 1.4 |
| **Besonderheit** | **1× PCIe x8 Slot** + **USB-C** |
| **Kühlung** | Aktiver Lüfter |
| **Stromverbrauch (Idle)** | 6–12 Watt |
| **Preis** | **90–200 € gebraucht** |

**Vorteile:**
*   Einziger 1L-PC mit **PCIe-Slot** – für 10-Gbit-Netzwerkkarte, zweite SSD oder SATA-Controller
*   **USB-C** Anschluss
*   6 Kerne (i5-8500T)
*   Große Lenovo-Community

**Nachteile:**
*   Nur 1 GbE onboard
*   Teurer als HP/Dell auf dem Gebrauchtmarkt

**Home Assistant Eignung:**
*   **Home Assistant OS:** ✅ Perfekt
*   **Home Assistant Container:** ✅ Empfohlen
*   **Empfohlene Geräteanzahl:** 50–200+ Geräte
*   **Frigate (Kameras):** ✅ Läuft gut mit 16+ GB RAM
*   **KI-Sprachassistent (Whisper + Ollama):** ✅ Mit 32 GB RAM sind Phi-3-mini (lokal, über 10 Tokens/s) und Llama-3-8B möglich
*   **Matter + Thread:** ✅ Hervorragend
*   **Erweiterung:** PCIe-Slot für Dual-NIC oder 10 GbE

🔍 [Lenovo M720q Tiny bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=makmatas-homelab-21)

---

## 💰 200–230 € – GMKtec G3S (Neugerät, Garantie)

| Komponente | Spezifikation |
|------------|--------------|
| **Prozessor (CPU)** | Intel Alder Lake N95 (4 Kerne, bis 3,4 GHz, 15 W) |
| **Arbeitsspeicher (RAM)** | 1 Steckplatz DDR4 – max. 16 GB, upgradebar |
| **Festplatte** | Bis zu 8 TB M.2 SSD (PCIe & SATA) |
| **Netzwerk** | 1× Gigabit Ethernet |
| **Video** | 2× HDMI 2.0 (max. 4K) |
| **Kühlung** | Aktiver Lüfter |
| **Stromverbrauch (Idle)** | 5–8 Watt |
| **Preis** | **200–230 € neu** |

**Vorteile:** Intel N95 (Alder Lake) – moderner als die gebrauchten Celerons. Neugerät mit Herstellergarantie.
**Nachteile:** Nur 1 RAM-Slot (max 16 GB). Kein PCIe-Slot.

**Ideal für:** Einsteiger, die kein gebrauchtes Gerät kaufen möchten.

🔍 [GMKtec G3S bei Amazon suchen](https://www.amazon.de/s?k=GMKtec+G3S+N95&tag=makmatas-homelab-21)

---

## Vergleichstabelle: Welcher Mini-PC für Home Assistant?

| Gerät | Preis | CPU | RAM | SSD | Lüfterlos? | Idle | Home Assistant |
|-------|-------|-----|-----|-----|-----------|------|----------------|
| **Futro S7010** | ~45 € | J4125 (4C) | 1 Sl. max 16 GB | M.2 SATA only | ✅ Ja | 4–8 W | Basis+ |
| **HP ProDesk G4** | ~120 € | i5-8500T (6C) | 2 Sl. max 32 GB | NVMe + SATA | ❌ Nein | 8–14 W | Perfekt |
| **Dell Optiplex 3070** | ~130 € | i5-9500T (6C) | 2 Sl. max 32 GB | NVMe + SATA | ❌ Nein | 6–12 W | Perfekt |
| **Lenovo M720q** | ~150 € | i5-8500T (6C) | 2 Sl. max 64 GB | NVMe + SATA | ❌ Nein | 6–12 W | Perfekt+KI |
| **GMKtec G3S** | ~210 € | N95 (4C) | 1 Sl. max 16 GB | M.2 NVMe | ❌ Nein | 5–8 W | Gut |

---

## Was brauchst du außer dem Mini-PC?

### 1. Zigbee-USB-Stick (zwingend nötig)

| Stick | Preis | Besonderheit |
|-------|-------|-------------|
| **Sonoff Zigbee 3.0 USB Dongle P** | ~15–20 € | Günstig, zuverlässig, große Community – die erste Wahl |
| **Home Assistant Connect ZBT-2** | ~35 € | Offizielles HA-Zubehör, matter-kompatibel |
| **Conbee II** | ~30–35 € | Sehr ausgereift, aber teurer |
| **TubeZB PoE** | ~40 € | Mit PoE – per LAN-Kabel statt USB |

🔍 [Sonoff Zigbee 3.0 USB Dongle P bei Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=makmatas-homelab-21)

### 2. Empfohlene Sensoren für den Start

| Gerät | Preis | Wofür? |
|-------|-------|--------|
| **Aqara Temperatursensor** | ~12 € | Raumtemperatur + Luftfeuchtigkeit |
| **Aqara Bewegungsmelder** | ~15 € | Licht automatisch schalten |
| **Aqara Fenster-/Türkontakt** | ~10 € | Fenster offen? Alarm? Heizung aus |
| **Sonoff Smart Plug S40** | ~10 € | Steckdose schalten + Strom messen |

> **💡 Meiner Erfahrung nach:** Fang mit einem **Bewegungsmelder** und einem **Temperatursensor** an. Licht schaltet sich automatisch an, wenn du den Raum betrittst – das motiviert ungemein.

### 3. Speicher (SSD) – Achtung Kompatibilität!

| Gerät | SSD-Typ | Empfehlung |
|-------|---------|------------|
| **Fujitsu Futro S7010** | **M.2 SATA only** – kein NVMe! | WD Blue SA510 |
| **HP ProDesk, Dell Optiplex, Lenovo M720q** | M.2 NVMe (schnell) | Kingston NV3 |

> **Wichtig:** Der Futro akzeptiert **keine NVMe-SSD**. Wenn du versehentlich eine NVMe kaufst, passt sie mechanisch – aber der Futro erkennt sie nicht.

---

## Installation: So richtest du Home Assistant auf deinem Mini-PC ein

### Weg 1: Home Assistant OS (empfohlen für Einsteiger)

1. **Lade das Image herunter:** [home-assistant.io/installation](https://www.home-assistant.io/installation/) → "Home Assistant OS" für x86_64
2. **Schreibe auf USB-Stick:** Mit **Balena Etcher** (kostenlos) auf einen USB-Stick (mind. 4 GB)
3. **Anschließen und booten:** Monitor (DisplayPort), Tastatur, LAN-Kabel anschließen, USB-Stick einstecken. Beim Einschalten **F2/F10/F12** drücken → USB als Boot-Laufwerk wählen
4. **Warten:** Nach ~5–10 Minuten ist die Installation fertig
5. **Öffnen:** Browser → **http://homeassistant.local:8123**
6. **Zigbee-Stick einstecken:** Home Assistant erkennt ihn automatisch

### Weg 2: Home Assistant Container (für Fortgeschrittene)

Linux installieren (Ubuntu Server LTS), dann Home Assistant als Docker-Container. Vorteil: Pi-hole, Paperless-ngx und andere Dienste laufen parallel.

> **💡 Meine Empfehlung:** Starte mit Home Assistant OS. Du kannst später auf Container umsteigen – deine Konfiguration bleibt erhalten.

---

## Home Assistant Green vs. DIY-Mini-PC

| Kriterium | Home Assistant Green (~110 €) | Mini-PC (45–150 €) |
|-----------|-------------------------------|-------------------|
| **Preis** | 110 € (fix) | 45–150 € |
| **CPU** | 4 Kerne (Rockchip RK3566, 2,0 GHz) | 4–6 Kerne (Intel Celeron bis Core i5) |
| **RAM** | 4 GB (fest verlötet) | 8–64 GB (aufrüstbar) |
| **Speicher** | 32 GB eMMC (fest) | 64 GB–1 TB SSD (austauschbar) |
| **Strom (Idle)** | ca. 3–5 W | 4–14 W |
| **Garantie** | 2 Jahre | Keine (gebraucht) |
| **Erweiterbar** | ❌ Nein | ✅ RAM, SSD, teils PCIe |
| **Einrichtung** | Plug & Play | 15 Minuten |

**Fazit:** Der Green ist perfekt für absolute Anfänger. Der Mini-PC ist günstiger **(ab 45 €)**, leistungsstärker und erweiterbar.

---

## Drei häufige Fehler beim Start

**1. "Mein Mini-PC bootet nicht vom USB-Stick"** → Direkt nach Einschalten **mehrmals schnell** F2/F10/F12 drücken.

**2. "Home Assistant findet meinen Zigbee-Stick nicht"** → Stick erst **nach** der Installation einstecken. Bei Problemen: USB-2.0-Port probieren (schwarz, nicht blau).

**3. "Ich komme nicht auf die Weboberfläche"** → Mini-PC und Computer im selben Netzwerk. Browser → http://homeassistant.local:8123

---

## FAQ

**Kann Home Assistant auch mit WLAN-Geräten umgehen?** Ja. WLAN-Geräte (TP-Link, Shelly) werden direkt per Netzwerk eingebunden.

**Wie viel RAM brauche ich?** Home Assistant selbst: 1–2 GB. Mit Zigbee2MQTT + Add-ons: 4 GB komfortabel. Ab 8 GB Reserven für Frigate oder KI.

**Kann ich meinen Raspberry Pi umziehen?** Ja. Backup exportieren, auf Mini-PC installieren, Backup wiederherstellen – alle Geräte und Automationen sind sofort da.

---

## Ausblick für Fortgeschrittene: Warum dieser PC mit deinen Aufgaben wachsen kann

Dein Mini-PC kann mehr als nur Home Assistant. Mit **Proxmox** (einer kostenlosen Virtualisierungs-Plattform) machst du aus ihm einen Multi-Server: Home Assistant als VM, Pi-hole als Werbeblocker, Paperless-ngx für deine Dokumente und Ollama für lokale KI – alles auf einem Rechner. Die Geräte-Empfehlungen oben (HP ProDesk, Lenovo M720q) sind dafür optimal, weil sie genug Kerne und RAM-Slots für den Ausbau mitbringen.

---

## 🛒 Einkaufsliste

| Was | Empfehlung | Preis | Link |
|-----|-----------|-------|------|
| **Mini-PC (Budget)** | Fujitsu Futro S7010 | ~45 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=makmatas-homelab-21) |
| **Mini-PC (Empfohlen)** | HP ProDesk 400 G4 | ~120 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=makmatas-homelab-21) |
| **Zigbee-Stick** | Sonoff Zigbee 3.0 Dongle P | ~18 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=Sonoff+Zigbee+3.0+USB+Dongle+P&tag=makmatas-homelab-21) |
| **Adapter** | DisplayPort → HDMI | ~7 € | 🔍 [Amazon suchen](https://www.amazon.de/s?k=DisplayPort+HDMI+Adapter&tag=makmatas-homelab-21) |

---

## Fazit: Welcher Mini-PC für dein Smart Home?

| Budget | Empfehlung | Warum? |
|--------|-----------|--------|
| **~45–75 €** | Fujitsu Futro S7010 + Sonoff-Stick | Günstigster Einstieg. Lüfterlos, stromsparend, leise – perfekt für 10–20 Geräte. |
| **~120–150 €** | HP ProDesk 400 G4 + Sonoff-Stick | Bester Kompromiss. Genug Leistung für Kameras, Sprachassistent und 50+ Geräte. |
| **~150–200 €** | Lenovo M720q + 32 GB RAM | Für Fortgeschrittene: Smarthome + KI-Modelle + PCIe-Erweiterbarkeit. |

Home Assistant auf einem Mini-PC ist **der beste Weg ins Smart Home**: Mehr Leistung als ein Raspberry Pi, günstiger als Home Assistant Green und die Freiheit, später aufzurüsten.

**Meine Klartext-Empfehlung:** Kauf einen Fujitsu Futro S7010 für ~45 € und einen Sonoff Zigbee-Stick für ~18 €. Zusammen 63 € – und du hast eine leise, stromsparende Smart-Home-Zentrale, die mit jeder Fertiglösung mithält. Investiere das gesparte Geld lieber in ein paar Sensoren für den Start.

*Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.*
