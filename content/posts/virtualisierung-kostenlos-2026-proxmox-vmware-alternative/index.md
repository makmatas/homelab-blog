---
title: "Virtualisierung kostenlos 2026: Proxmox VE als VMware-Alternative im Homelab"
date: 2026-06-17
draft: false
image: "featured.jpg"
cover:
  image: "featured.jpg"
  alt: "Proxmox VE Dashboard auf einem Server – Virtualisierung kostenlos und Open Source"
  relative: true
tags:
  - proxmox
  - virtualisierung
  - vmware-alternative
  - homelab
  - open-source
categories:
  - Virtualisierung
---

**Aktualisiert: Juni 2026 | Lesezeit: 8 Minuten**

Stell dir vor, du hast zu Hause einen kleinen Server – einen Mini-PC, der leise in der Ecke steht und Tag und Nacht läuft. Darauf sollen mehrere Dienste gleichzeitig laufen: Pi-hole als Werbeblocker fürs ganze Netz, ein Medienserver für Filme (Jellyfin), eine Cloud für deine Fotos (Nextcloud) und vielleicht noch ein Game-Server. Müsstest du für jeden Dienst einen eigenen Rechner kaufen, wärst du schnell bei 500–1.000 € und einem Berg Kabelgewirr.

**Virtualisierung** löst genau dieses Problem – und Proxmox VE ist der einfachste Weg, das kostenlos umzusetzen.

Dieser Artikel richtet sich an **Homelab-Einsteiger ohne Vorkenntnisse**, die eine günstige Alternative zu VMware suchen. Fachbegriffe? Erklären wir kurz und mit einem Bild im Kopf.

<!--more-->

---

## 🥇 Kurzempfehlung: Welcher Weg passt zu dir?

| Kategorie | Empfehlung |
|-----------|-----------|
| 🥇 Beste Preis-Leistung | Proxmox VE auf gebrauchtem HP ProDesk 400 G4 (~90 €) |
| 💰 Günstigster Einstieg | Proxmox VE auf Fujitsu Futro S7010 (~40 €) |
| 🚀 Beste Wahl für lokale KI | Proxmox auf Lenovo M720q (~120 €) + 32 GB RAM |
| 🏠 Beste Wahl für Home Assistant | Proxmox LXC-Container (2 GB RAM reichen) |
| 🔧 Beste Wahl für Proxmox Cluster | 2× Dell Optiplex 3070 Micro (~100 €/Stück) |

---

## Was ist Virtualisierung? (Einfach erklärt)

Stell dir vor, dein Computer ist ein **Mehrfamilienhaus** mit einem einzigen großen Raum. Virtualisierung baut **Zwischenwände ein** – plötzlich können mehrere Familien (VMs oder Container) gleichzeitig im selben Haus wohnen, ohne sich gegenseitig zu stören. Jede Familie hat ihren eigenen Bereich, ihr eigenes Inventar und kann unabhängig ein- und ausziehen.

Es gibt zwei Bauarten für diese "Zwischenwände":

| Typ | Beschreibung | Beispiel |
|-----|-------------|----------|
| **Typ 1 (Bare Metal)** | Läuft direkt auf der Hardware – wie ein Vermieter, der im Erdgeschoss wohnt | Proxmox VE, VMware ESXi |
| **Typ 2 (Gehostet)** | Läuft als Programm in Windows oder Linux – wie ein Untermieter | VirtualBox, VMware Workstation |

Proxmox VE ist ein **Typ-1-Hypervisor**: Er sitzt direkt auf der Hardware und verteilt die Ressourcen (CPU, RAM, Festplatte) effizient auf alle virtuellen Maschinen.

### Was bringt dir das konkret?

- **Isolation:** Ein abgestürzter Dienst reißt die anderen nicht mit – dein Medienserver läuft weiter, auch wenn Pi-hole gerade neu startet
- **Snapshots:** Bevor du eine riskante Änderung machst, knipst du einen Schnappschuss. Läuft was schief? Ein Klick und alles ist wie vorher
- **Kosteneffizienz:** Ein Server ersetzt fünf – weniger Strom, weniger Platz, weniger Lärm
- **Flexibilität:** Du kannst verschiedene Betriebssysteme parallel fahren – Linux für Docker, Windows für bestimmte Anwendungen

---

## Proxmox VE – Die kostenlose Lösung für dein Homelab

Proxmox Virtual Environment (VE) ist eine **komplett kostenlose Virtualisierungsplattform** auf Debian-Basis. Sie vereint zwei Technologien unter einer Weboberfläche:

### KVM-VMs (der "Gästeraum mit eigenem Eingang")

Virtuelle Maschinen mit eigenem BIOS, eigener CPU und eigenem RAM. Ideal, wenn du Windows Server, Ubuntu, Rocky Linux und FreeBSD **gleichzeitig** auf einem Rechner betreiben willst.

### LXC-Container (die "WG mit geteilter Küche")

Container teilen sich den Linux-Kernel des Hosts – das spart enorm Ressourcen. Ein LXC-Container mit Ubuntu braucht nur **~100 MB RAM** statt 2 GB für eine vollständige VM. Das ist der Unterschied zwischen einer möblierten Wohnung (LXC) und einem kompletten Hausbau (KVM).

**Perfekt für:** Docker-Hosts, Pi-hole, n8n, Home Assistant – alles, was schlank laufen soll.

### Die wichtigsten Funktionen auf einen Blick

| Funktion | Beschreibung |
|----------|-------------|
| **Web-UI** | Verwaltung über den Browser – keine Linux-Kenntnisse nötig |
| **Snapshots** | Zustand der VM einfrieren und bei Bedarf zurückrollen |
| **Backup** | Komplettes VM-Backup mit einem Klick (VZDump) |
| **Cluster** | Mehrere Rechner als einen großen Server verwalten |
| **Live-Migration** | VM umziehen, während sie läuft – keine Ausfallzeit |
| **REST API** | Automatisierung per Skript – für Fortgeschrittene |

> 👉 [Proxmox VE bei Amazon suchen (Bücher & Hardware)](https://www.amazon.de/s?k=Proxmox+VE+Virtualisierung&tag=makmatas-homelab-21)

---

## Proxmox vs. VMware ESXi – Der Vergleich 2026

Seit Broadcom VMware übernommen hat, ist Schluss mit der kostenlosen ESXi-Version. Wer VMware weiternutzen will, zahlt **mindestens ~500 € pro Jahr** (vSphere Foundation) – und das ohne Storage-Funktionen wie ZFS oder Ceph.

| Kriterium | Proxmox VE | VMware vSphere (Broadcom) |
|-----------|-----------|--------------------------|
| **Preis** | **0 €** – komplett kostenlos | **Ab ~500 €/Jahr** – nur mit Support-Lizenz |
| **Container** | LXC inkludiert | Nicht vorhanden (nur VMs) |
| **ZFS / Snapshots** | Ja, integriert | Nur mit Zusatzkosten |
| **Ceph Storage** | Integriert (Hochverfügbarkeit) | vSAN ab **~2.000 €/Jahr** |
| **Community** | Aktiv, deutschsprachig | Stark geschrumpft seit Broadcom |
| **Updates** | Kostenlos (Community-Repo) | Nur mit gültigem Support-Vertrag |

**Die Botschaft:** Proxmox bietet mehr Funktionen als der alte ESXi Free – und das völlig kostenlos.

---

## Wie viel Hardware brauchst du für Proxmox?

Proxmox läuft auch auf älteren Rechnern. Anders als VMware (das eine strikte Hardware-Kompatibilitätsliste hat) unterstützt Proxmox praktisch jeden x86_64-Prozessor.

### Minimal-Ausstattung

| Komponente | Minimal | Empfohlen |
|-----------|---------|-----------|
| **CPU** | 4 Kerne (z. B. Intel Core i5-6500, 4C/4T) | 8+ Kerne (Intel i7/i9 oder AMD Ryzen) |
| **RAM** | 8 GB | 32–64 GB |
| **Storage** | 256 GB SSD | 1 TB NVMe + HDD für Backups |
| **Netzwerk** | 1 GbE | 2,5 GbE oder 10 GbE |

> **Tipp:** Proxmox VE 9.2 (basierend auf Debian 13.5 „Trixie“) bringt den modernen Linux-Kernel 7.0, QEMU 11.0, LXC 7.0 sowie ZFS 2.4 – die neueste Version mit Dynamic Load Balancer, erweitertem SDN, HA-Arm/Disarm und verwaltbaren CPU-Profilen.

---

## Gute Hardware für dein Proxmox-Homelab – nach Budget

### 💰 1–50 € – Fujitsu Futro S740 oder S7010

Was du auf dem Gebrauchtmarkt findest: meist mit 8 GB RAM und 64 GB SSD.

- **CPU:** Intel J4125 (S7010, 4 Kerne) oder Intel J4105 (S740, 4 Kerne) – **beide lüfterlos**
- **RAM:** 8 GB DDR4 offiziell, 16 GB getestet – ein einzelner RAM-Slot (SODIMM)
- **Storage:** 64 GB M.2 SATA – SSD austauschbar, aber M.2 SATA only (kein NVMe)
- **Netzwerk:** 1× GbE
- **Upgrade-Fähigkeit:** ❌ Nur ein RAM-Slot, M.2 SATA only (kein NVMe), kein zweiter SSD-Slot
- **KI-Potenzial:** ❌ Für Ollama nicht geeignet – CPU zu schwach, RAM zu knapp
- **Stromverbrauch Idle:** ca. 6–8 Watt – günstiger im Dauerbetrieb als jede Glühbirne
- **USB-C?** Nein
- **Praxis-Tipp:** Läuft bei mir seit Monaten als OPNSense-Firewall und AdGuard-DNS – absolut lautlos

**Ideal für:** Erste Proxmox-Experimente, Pi-hole, AdGuard, DNS/DHCP, Backup-Ziel (PBS), leichte Dienste

👉 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=makmatas-homelab-21)

---

### 💰 100–150 € – HP ProDesk 400 G3/G4 oder Dell Optiplex 3060/3070 Micro

- **CPU:** Intel Core i5 der 7.–9. Generation (4–6 Kerne) – mit Lüfter
- **RAM:** Bis zu 32 GB DDR4 – zwei RAM-Slots (SODIMM), **nicht verlötet**
- **Storage:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA – zwei Plätze, gut erweiterbar
- **Netzwerk:** 1× GbE
- **Upgrade-Fähigkeit:** ✅ RAM auf 32 GB erweiterbar, zweiter SSD-Slot vorhanden. Kein PCIe-Slot.
- **KI-Potenzial:** ⚠️ Basis möglich. Phi-3-mini (3,8B) läuft mit über 10 Tokens/s auf der CPU – flüssig nutzbar. Llama-3-8B wird langsamer (~4-5 Tokens/s). 16+ GB RAM empfohlen.
- **Stromverbrauch Idle:** ca. 12–18 Watt
- **USB-C?** Nein. Nur USB 3.0 (Typ A).

**Ideal für:** Vollwertigen Proxmox-Host für viele Container und 3–5 VMs, Home Assistant, Jellyfin, Nextcloud

- 🔍 [HP ProDesk 400 G4 Mini bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=makmatas-homelab-21)
- 🔍 [Dell Optiplex 3070 Micro bei Amazon suchen](https://www.amazon.de/s?k=Dell+Optiplex+3070+Micro&tag=makmatas-homelab-21)

---

### 💰 150–200 € – Lenovo M720q Tiny

- **CPU:** Intel Core i5-8500T oder i7-8700T (6 Kerne) – mit Lüfter
- **RAM:** Bis zu 32 GB DDR4 – zwei RAM-Slots (SODIMM)
- **Storage:** 1× M.2 NVMe + 1× 2,5-Zoll-SATA
- **Netzwerk:** 1× GbE
- **Upgrade-Fähigkeit:** ✅ RAM erweiterbar, zweiter SSD-Slot vorhanden. **Plus:** PCIe-Slot (Riser-Karte) für 10GbE oder GPU – das hat kein anderer 1L-PC in dieser Preisklasse.
- **KI-Potenzial:** ✅ Phi-3-mini läuft mit über 10 Tokens/s. Mit 32 GB RAM auch Llama-3-8B nutzbar. Reine CPU-Inferenz, keine GPU nötig.
- **Stromverbrauch Idle:** ca. 12–20 Watt
- **USB-C?** **Ja** – einmal USB-C (DisplayPort-alt). Der einzige 1L-PC in dieser Liga mit USB-C.

**Ideal für:** KI-Spielereien (Ollama, Open WebUI), Cluster-Node mit PCIe-Erweiterung, Home Assistant + Nextcloud + KI alles in einem

- 🔍 [Lenovo M720q Tiny bei Amazon suchen](https://www.amazon.de/s?k=Lenovo+M720q+Tiny&tag=makmatas-homelab-21)

---

### 💰 > 200 € – Minisforum MS-01 (neu)

- **CPU:** Intel Core i9-13900H (14 Kerne: 6P+8E, 20 Threads) – High-End-Prozessor
- **RAM:** Bis zu 96 GB DDR5 – zwei SO-DIMM-Slots
- **Storage:** 3× M.2 NVMe – extrem erweiterbar
- **Netzwerk:** 2× 10GbE (SFP+) + 2× 2,5 GbE
- **Upgrade-Fähigkeit:** ✅ Drei NVMe-Slots, zwei DDR5-Slots. Kein PCIe-Slot intern.
- **KI-Potenzial:** ✅ Ja, geeignet für lokale KI-Modelle dank 14 Kernen und DDR5. Mit 64+ GB RAM sind auch größere Modelle möglich.
- **Stromverbrauch Idle:** Keine exakten Daten vorhanden.
- **USB-C?** Ja

**Ideal für:** Leistungshungrige VMs, Ceph-Cluster, KI-Workloads, 10GbE-Netzwerk – wenn das Budget es hergibt.

👉 [Preis bei Geizhals prüfen](https://geizhals.de/minisforum-ms-01-a3260346.html)

---

## 💾 Günstige SSD-Empfehlung

High-End-SSDs wie die Samsung 990 Pro (150+ €) lohnen sich im Homelab selten. Dein ZFS-Root-Pool wird auch mit einer günstigen NVMe flott:

| Modell | Preis (ca.) | Typ | Besonderheit |
|--------|------------|-----|-------------|
| [Kingston NV3 1 TB](https://geizhals.de/kingston-nv3-nvme-pcie-4-0-ssd-1tb-snv3s-1000g-a3248579.html?hloc=de) | ~139 € | NVMe PCIe 4.0 | Solide Allround-SSD, 6.000 MB/s lesend |
| [WD Blue SA510 1 TB](https://geizhals.de/western-digital-wd-blue-sa510-ssd-1tb-wds100t3b0b-wdbb8h0010bnc-a2736547.html?hloc=de) | ~135 € | SATA (M.2) | Günstiger, aber SATA-Limit (560 MB/s) – fürs Boot-Laufwerk völlig ausreichend |

---

## Proxmox einrichten – Die ersten Schritte (auch für Einsteiger)

Die Installation ist erstaunlich einfach – eine der großen Stärken von Proxmox:

1. **ISO herunterladen** von [proxmox.com](https://www.proxmox.com/downloads) (kostenlos, keine Registrierung nötig)
2. **Auf USB-Stick schreiben** – mit [Rufus](https://rufus.ie/de/) (Windows) oder Balena Etcher (Mac/Linux)
3. **Vom USB-Stick booten** – den Rechner starten, F2/F12 drücken, USB als Boot-Laufwerk auswählen
4. **Installations-Assistent folgen** – dauert etwa 5 Minuten, nur: Festplatte auswählen, Passwort setzen, IP-Adresse eingeben
5. **Web-UI aufrufen:** `https://deine-ip:8006` im Browser – fertig!

> **Keine Linux-Kenntnisse nötig?** Für die Grundnutzung: ja. Das Web-UI ist übersichtlich und selbsterklärend. Erst wenn du ZFS-Tuning, Ceph-Cluster oder Kommandozeilen-Backups machen willst, helfen Linux-Grundlagen.

---

## Das solltest du vor dem Kauf wissen

Bevor du Hardware kaufst, hier ein paar **praktische Fallstricke** aus meiner Erfahrung:

- **RAM richtig planen:** Proxmox selbst braucht kaum RAM (~2 GB). Ein LXC-Container benötigt je nach Anwendung 0,5–4 GB (Pi-hole: ~0,5 GB, Nextcloud: ~2–4 GB). Eine VM startet bei mindestens 4 GB. Mit 32 GB bist du für die meisten Homelabs gut aufgestellt – 16 GB reichen für den Anfang.
- **Eine SSD reicht:** ZFS mag zwei SSDs im Mirror, aber fürs Homelab tut es auch eine. Mach regelmäßige Backups auf eine externe HDD oder einen zweiten Rechner.
- **Netzwerk nicht vergessen:** Ein GbE-Anschluss reicht für die ersten Schritte. Erst wenn du mehrere VMs gleichzeitig stark belastest (z. B. Jellyfin + Nextcloud + Game-Server), wird 2,5 GbE interessant.
- **Gebraucht ist oft besser als neu:** Business-1L-PCs (HP, Dell, Lenovo) sind für den 24/7-Dauerbetrieb ausgelegt. Ein gebrauchtes Modell für 100–150 € läuft meist jahrelang problemlos.

---

## Drei Tools, die dein Homelab auf das nächste Level bringen

### 1. Proxmox Backup Server (PBS) – Kostenlose Backups

Sicherungen deiner VMs und Container – dedupliziert, verschlüsselt, mit Bandbreiten-Limit. Ideal als zweiter LXC-Container auf demselben Host oder einem günstigen Futro.

### 2. Home Assistant via LXC

Home Assistant in einem LXC-Container braucht nur ~2 GB RAM und lässt sich in 10 Minuten einrichten. Perfekt für Smart-Home-Steuerung (Licht, Heizung, Kameras).

### 3. Ollama + Open WebUI für lokale KI

Ab 32 GB RAM kannst du kleine KI-Modelle direkt auf deinem Proxmox-Host laufen lassen. **Phi-3-mini (3,8B Parameter)** läuft mit über 10 Tokens/s auf CPU-only – völlig flüssig für Chat und Textaufgaben. **Llama-3-8B** schafft ~4–5 Tokens/s – langsamer, aber für gelegentliche Nutzung okay. Einrichtung per LXC-Container mit Docker, in 15 Minuten erledigt.

---

## Häufig gestellte Fragen

### Ist Proxmox VE wirklich komplett kostenlos?

Ja. Proxmox VE ist Open Source (GPLv2). Du kannst es unbegrenzt nutzen, ohne zu bezahlen. Es gibt ein Enterprise-Repository (kostenpflichtig), aber das **Community-Repository reicht fürs Homelab völlig aus** – Updates und Sicherheits-Patches inklusive.

### Kann ich meine bestehenden VMware-VMs zu Proxmox migrieren?

Ja. Du hast drei Wege: Export aus VMware als OVF/OVA und Import in Proxmox, Konvertierung per `qemu-img convert` oder das automatisierte `virt-v2v`-Tool. Die meisten Betriebssysteme laufen ohne Anpassungen.

### Brauche ich Linux-Kenntnisse für Proxmox?

Für die ersten Schritte: nein. Die Weboberfläche erlaubt die vollständige Verwaltung per Mausklick. Für Fortgeschrittenes (ZFS-Tuning, Cluster, Kommandozeile) helfen Grundkenntnisse, aber die lernst du mit der Zeit von selbst.

---

## Fazit: Welcher Weg ist der richtige für dich?

| Budget | Empfehlung | Ideal für |
|--------|-----------|-----------|
| **1–50 €** | Fujitsu Futro S740/S7010 (gebraucht) | Erste Schritte, Pi-hole, DNS, Monitoring |
| **100–150 €** | HP ProDesk 400 G4 oder Dell Optiplex 3070 (gebraucht) | Vollwertiger Homelab-Host, Home Assistant, Jellyfin, Nextcloud – läuft auch mit vielen Containern |
| **150–200 €** | Lenovo M720q Tiny (gebraucht) | KI-Spielereien per CPU, Cluster-Node mit PCIe, maximale Erweiterbarkeit |
| **> 200 €** | Minisforum MS-01 (neu) | 10GbE, Ceph-Cluster, KI-Workloads, wenn Geld keine Rolle spielt |

Die VMware-Ära im Homelab ist vorbei. Proxmox ist die logische, kostenlose und leistungsfähigere Alternative – und mit gebrauchter Business-Hardware kommst du günstiger weg als mit jedem Fertig-NAS oder Mini-PC aus dem Laden.

*Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.*
