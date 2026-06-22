---
title: "Proxmox Cluster selber bauen: 3 gebrauchte Mini-PCs im Benchmark-Vergleich ab 42 €"
date: 2026-06-22
draft: true
image: "benchmark-vergleich.svg"
cover:
  image: "benchmark-vergleich.svg"
  alt: "Benchmark-Vergleich von drei Proxmox Mini-PCs: HP ProDesk, Dell OptiPlex, Fujitsu Futro"
  relative: true
tags:
  - proxmox
  - hardware
  - mini-pc
  - benchmark
  - cluster
  - homelab
categories:
  - Hardware
---

**Aktualisiert: Juni 2026 | Lesezeit: 10 Minuten**

Du möchtest dein Homelab auf das nächste Level bringen und mehrere Server zu einem **Proxmox-Cluster** verbinden? Oder du stehst gerade am Anfang und fragst dich, ob ein einzelner Mini-PC reicht – oder ob du lieber gleich mehrere gebrauchte kaufen solltest?

In diesem Artikel habe ich **drei meiner eigenen Proxmox-Server** einem ausführlichen Benchmark-Test unterzogen: einen HP ProDesk 400 G4, einen Dell OptiPlex 3070 Micro und einen Fujitsu Futro S7010. Die Ergebnisse zeigen dir, welcher Server sich für welche Aufgabe am besten eignet – und das alles für **unter 220 Euro Gesamtkosten**.

{{< figure src="rollenverteilung.svg" alt="Rollenverteilung der 3 Proxmox Server" width="800" >}}

<!--more-->

## Warum überhaupt mehrere Server? Ein Beispiel aus dem Alltag

Stell dir vor: Du bist unterwegs und willst mit dem Handy schnell auf deine Fotos, Dokumente oder Filme auf deinem Heim-NAS zugreifen. Dein Homeserver läuft 24/7 – aber wenn du ein Update machst, ein Container abstürzt oder du dein Netzwerk neu konfigurieren musst, bist du **ohne Alternative** komplett offline.

Mit **drei Servern im Cluster** hast du diese Probleme nicht:

- Fällt **ein** Server aus, laufen die anderen Dienste einfach weiter
- Für Wartungsarbeiten migrierst du VMs live auf einen anderen Node – **ohne Ausfallzeit**
- Du kannst verschiedene Aufgaben auf die passende Hardware verteilen
- Du lernst dabei echte **Cluster-Technologie**, wie sie auch in Unternehmen eingesetzt wird

Ein Proxmox-Cluster ist wie eine **Wohngemeinschaft für deine Server**: Jeder hat seine eigene Stärke, aber zusammen sind sie mehr als die Summe ihrer Teile.

## Die 3 Kandidaten – Gebrauchte Mini-PCs aus dem Jahr 2026

Alle drei Server sind **gebrauchte Business-Mini-PCs**, die ursprünglich tausende Euro gekostet haben und heute für kleines Geld auf dem Gebrauchtmarkt zu haben sind.

### 1. HP ProDesk 400 G4 Mini (der Allrounder)

Der HP ProDesk 400 G4 war mein **erster Proxmox-Host** und läuft seit Monaten zuverlässig im Dauerbetrieb.

| Komponente | Details |
|------------|---------|
| **CPU** | Intel Core i5-8500T (6 Kerne, 2,1–3,5 GHz, 35W TDP) |
| **RAM** | 32 GB DDR4 |
| **Preis (gebraucht)** | ~70–90 € |
| **Status** | Live-Homelab-Host (unter Last getestet) |

👉 [HP ProDesk 400 G4 bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=makmatas-homelab-21)

### 2. Dell OptiPlex 3070 Micro (der Leistungsträger)

Der Dell OptiPlex 3070 Micro ist mein **neuester Zugang** und soll die Haupt-VM-Last übernehmen.

| Komponente | Details |
|------------|---------|
| **CPU** | Intel Core i5-9500T (6 Kerne, 2,2–3,7 GHz, 35W TDP) |
| **RAM** | 32 GB DDR4 |
| **Preis (gebraucht)** | ~100 € |
| **Status** | Frisch eingerichtet (unbelastet getestet) |

👉 [Dell OptiPlex 3070 Micro bei Amazon suchen](https://www.amazon.de/s?k=Dell+OptiPlex+3070+Micro&tag=makmatas-homelab-21)

### 3. Fujitsu Futro S7010 (der Sparmeister)

Der Fujitsu Futro S7010 ist der **Überraschungsgast** – ein winziger, extrem stromsparender Mini-PC, der eigentlich als Thin Client gedacht war und nur **42 Euro kostet**.

| Komponente | Details |
|------------|---------|
| **CPU** | Intel Celeron J4125 (4 Kerne, 2,0–2,7 GHz, 10W TDP) |
| **RAM** | 16 GB DDR4 |
| **Preis (gebraucht)** | ~42 € |
| **Status** | Soll OPNSense-Firewall + AdGuard werden |

👉 [Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=makmatas-homelab-21)

---

**Gesamtkosten aller drei Server: ~212 €** – weniger als ein neuer Gaming-Controller, aber du bekommst ein **komplettes Proxmox-Cluster mit 80 GB RAM und 16 CPU-Kernen**. 🎉

## Die Benchmarks – Was wurde getestet und warum?

Ich habe **vier verschiedene Benchmarks** durchgeführt, um ein möglichst vollständiges Bild der Leistungsfähigkeit zu bekommen:

| Benchmark | Testet | Warum wichtig? |
|-----------|--------|----------------|
| **sysbench CPU** | Reine Rechenleistung (Prime-Zahlen) | Zeigt, wie schnell VMs/Container arbeiten |
| **sysbench RAM** | Speicher-Durchsatz | Wichtig für datenbank-lastige Anwendungen |
| **7-Zip Benchmark** | Echte Kompression/ Dekompression | Realwelt-Test: Backup, Datenübertragung |
| **OpenSSL Speed** | Verschlüsselung (AES, SHA) | Entscheidend für VPN, HTTPS, verschlüsselte Verbindungen |

Alle Tests liefen auf **nacktem Proxmox VE** (also ohne laufende VMs/Container) – bis auf den HP ProDesk, der **während des laufenden Homelab-Betriebs** getestet wurde. Das macht die Ergebnisse besonders realistisch!

## Die Ergebnisse im Detail

Hier siehst du alle Benchmark-Ergebnisse auf einen Blick:

{{< figure src="benchmark-vergleich.svg" alt="Vergleich aller Benchmark-Ergebnisse der 3 Proxmox Server" width="800" >}}

### CPU Multi-Core: Der Dell gewinnt klar

Mit **2.617 Events pro Sekunde** liegt der Dell OptiPlex 3070 vorne. Er hat 12 % mehr Leistung als der HP ProDesk (2.339) und 11 % mehr als der Fujitsu Futro (2.359).

Beide i5-Server (HP und Dell) haben **6 Kerne**, der Futro nur **4**. Dass der Futro trotzdem mit dem HP mithalten kann, liegt daran, dass der HP unter **Live-Last** getestet wurde – laufende VMs haben ihm CPU-Zeit geklaut. Ohne diese Last liegt der HP vermutlich gleichauf mit dem Dell.

### CPU Single-Core: Der 42-Euro-Server schlägt alle!

Das ist die größte Überraschung: Der **Fujitsu Futro S7010** erreicht **614 Events pro Sekunde** im Single-Core-Test – und damit **30 % mehr** als der Dell (470) und **47 % mehr** als der HP (417)!

Warum? Der Celeron J4125 im Futro hat nur **10 Watt TDP**. Bei Prime-Berechnung wird er nicht einmal warm und kann **dauerhaft auf vollem Takt** laufen. Die i5-Prozessoren (35W TDP) treffen dagegen auf ihr Power-Limit und müssen den Takt **runterregeln**. Für reine Single-Thread-Aufgaben ist der kleine Futro also **schneller** als die großen Brüder.

**Was das für dich bedeutet:** Für Router, DNS-Server, Firewalls oder einfache Steuerungsdienste ist ein stromsparender Prozessor oft die **bessere Wahl** als ein High-End-Chip.

### RAM-Durchsatz: Dell mit 88 % mehr als Futro

Der Dell OptiPlex schafft **21.663 MiB/sec** – fast doppelt so viel wie der Futro (11.540 MiB/sec). Der HP liegt mit 19.161 MiB/sec dazwischen.

Je mehr VMs gleichzeitig auf einem Server laufen und je mehr sie auf RAM zugreifen (Datenbanken, Dateifreigaben, Nextcloud), desto wichtiger wird die Speicherbandbreite. Der Dell ist hier der **klare Sieger**.

### 7-Zip Kompression: Realwelt-Leistung pur

7-Zip komprimiert echte Daten – das ist kein synthetischer Test, sondern das, was auch bei Backups oder Dateiübertragungen passiert.

- **Dell:** 32.101 Rating 🥇
- **HP:** 27.108 Rating
- **Futro:** 11.671 Rating

Der Dell ist hier **19 % schneller** als der HP und **175 % schneller** als der Futro. Wenn du regelmäßig Backups erstellst oder große Dateien verarbeitest, macht sich der Dell sofort bezahlt.

### Verschlüsselung: AES-256 im Vergleich

Für **VPN-Verbindungen** (OpenVPN, WireGuard) und verschlüsselte Datenübertragung ist AES-Leistung entscheidend.

| Server | AES-256 (MB/s) | 
|--------|:---:|
| 🖥️ Dell OptiPlex 3070 | **5.585** 🥇 |
| 🖥️ HP ProDesk 400 G4 | 3.923 |
| 🖥️ Fujitsu Futro S7010 | 2.842 |

Der Dell verschlüsselt **doppelt so schnell** wie der Futro. Aber auch der Futro mit 2,8 GB/s AES-Durchsatz ist mehr als ausreichend – ein Gigabit-Internet-Anschluss (0,125 GB/s) ist damit **22x unter** der maximalen Verschlüsselungsrate. Selbst für OPNSense auf dem Futro ist das völlig entspannt.

Interessant beim **SHA256-Hashing**: Hier liegt der Futro **gleichauf** mit dem Dell (~2.500 MB/s), weil beide Prozessoren **SHA-NI-Befehle** direkt im Chip haben. Perfekt für Passwort-Hashing und Authentifizierung!

## Was bedeuten die Ergebnisse für dein Homelab?

Die drei Server haben ganz unterschiedliche Stärken – und genau das macht ein Cluster so wertvoll:

### Die optimale Rollenverteilung

| Server | Rolle | Warum? |
|--------|-------|--------|
| 🖥️ **Dell OptiPlex 3070** | **Haupt-Node** | Bester RAM + Multi-Core – ideal für schwere VMs, Docker, Datenbanken |
| 🖥️ **HP ProDesk 400 G4** | **Zweit-Node / Backup** | Solide Allround-Leistung, bewährt im Dauerbetrieb |
| 🖥️ **Fujitsu Futro S7010** | **Firewall / Router** | Single-Core-Stärke und niedriger Stromverbrauch – perfekt für 24/7-Betrieb |

### So greifst du von unterwegs auf deine Daten zu (Einsteiger-Tipp)

Ein Homelab bringt nur etwas, wenn du auch **unterwegs** darauf zugreifen kannst. Die drei Server-Klassen helfen dir dabei:

**1. Über den Futro als Router:**

Der Fujitsu Futro wird später dein **OPNSense-Router** mit WireGuard-VPN. Das bedeutet:

- Du installierst WireGuard auf deinem Handy (App Store / Play Store)
- Scannst einen QR-Code vom Server ein
- **Schon bist du im Heimnetzwerk** – als wärst du zuhause

**2. Aufs NAS zugreifen:**

Hast du einen NAS-Container (z.B. OpenMediaVault oder TrueNAS) auf dem **Dell oder HP**, erreichst du ihn über:
- **SMB/Samba:** Wie ein normaler Netzlaufwerk-Ordner, nur übers Internet
- **Nextcloud:** Wie Google Drive, aber selbst gehostet – mit Datei-Freigabe-Links für Freunde
- **Jellyfin:** Deine eigene Netflix-Alternative – Filme und Serien von zuhause streamen

**3. Notfall-Zugriff:**

Fällt der Dell aus, migrierst du einfach die NAS-VM auf den HP – **ohne dass dein Handy-Zugriff unterbrochen wird**. Das nennt sich **Live-Migration** und ist eine der Kernfunktionen von Proxmox-Clustern.

> **Kurzfassung:** 3 Server = 3-fache Sicherheit. Selbst wenn du Experimente machst und einen Server crasht, bist du nie komplett offline.

## Häufig gestellte Fragen (FAQ)

### Brauche ich wirklich 3 Server? Reicht nicht einer?

Ein einziger Server reicht für den Einstieg völlig aus! Ein **HP ProDesk 400 G4** für ~80 € ist eine perfekte Basis. Wenn du dann merkst, dass dir RAM oder Leistung fehlt, kaufst du einen zweiten dazu. Das Schöne an Proxmox: du kannst dein Cluster **beliebig erweitern**.

### Kann ich auch verschiedene CPU-Typen mischen?

Ja! Proxmox-Cluster funktionieren mit **unterschiedlicher Hardware** – das ist kein Problem. Du solltest nur bei Live-Migration aufpassen: Die CPUs sollten ähnlich genug sein (beide Intel, gleiche Generation), sonst musst du die Migration vorher planen.

### Was kostet mich der Betrieb (Strom)?

- **Futro S7010:** ~10 Watt → ~2 €/Monat (Dauerbetrieb)
- **HP ProDesk:** ~15–25 Watt → ~3–5 €/Monat
- **Dell OptiPlex:** ~15–25 Watt → ~3–5 €/Monat
- **Gesamt:** ~8–12 €/Monat für 3 Server im 24/7-Betrieb

Das ist weniger als ein Streaming-Abo. 😉

### Ist das schwer einzurichten?

Die Grundinstallation von Proxmox dauert **~15 Minuten** pro Server. Einen Cluster aus 3 Nodes einzurichten ist danach eine Sache von **30 Minuten** über die Weboberfläche. Für den Einstieg reichen **grundlegende Linux-Kenntnisse** – und die lernst du schnell dazu.

### Kann ich mit einem Handy auf meine Daten zugreifen?

Ja, absolut! Der einfachste Weg:
1. **Nextcloud** in einem LXC-Container installieren (gibt es fertige Scripts dafür)
2. Über den **Router (Futro)** ein WireGuard-VPN einrichten
3. App auf dem Handy installieren → **fertig**

Dateien öffnen, Fotos hochladen, Musik streamen – alles vom Handy aus, als wärst du zuhause.

## Welche Hardware empfehle ich für dein Homelab?

Je nach Budget und Zielsetzung:

### Einsteiger (bis 100 €)

👉 **[HP ProDesk 400 G4 bei Amazon suchen](https://www.amazon.de/s?k=HP+ProDesk+400+G4+Mini&tag=makmatas-homelab-21)** (~70–90 € gebraucht)
Perfekt für erste Proxmox-Erfahrungen, läuft leise und zuverlässig.

### Fortgeschritten (100–200 €)

👉 **[Dell OptiPlex 3070 Micro bei Amazon suchen](https://www.amazon.de/s?k=Dell+OptiPlex+3070+Micro&tag=makmatas-homelab-21)** (~100 € gebraucht)
Der Leistungsträger – bester RAM-Durchsatz und Multi-Core für deine VMs.

### Low-Budget-Spezial (unter 50 €)

👉 **[Fujitsu Futro S7010 bei Amazon suchen](https://www.amazon.de/s?k=Fujitsu+Futro+S7010&tag=makmatas-homelab-21)** (~42 € gebraucht)
Der 10W-Dauerläufer für Router, DNS, Firewall – stromsparend und überraschend stark im Single-Core.

### Zubehör, das du brauchst

- 👉 **[Samsung 990 Pro NVMe (1 TB)](https://www.amazon.de/s?k=Samsung+990+Pro+NVMe+1TB&tag=makmatas-homelab-21)** – Empfohlene SSD für den Proxmox-Root-Pool
- 👉 **[Crucial DDR4 SODIMM 32 GB](https://www.amazon.de/s?k=Crucial+DDR4+SODIMM+32GB&tag=makmatas-homelab-21)** – RAM-Upgrade für deine Mini-PCs
- 👉 **[USB-C zu Gigabit-Adapter](https://www.amazon.de/s?k=USB-C+Gigabit+Ethernet+Adapter&tag=makmatas-homelab-21)** – Nützlich für den Futro als zweite NIC

## Fazit: 3 gebrauchte Mini-PCs schlagen einen neuen Server

Die Benchmark-Ergebnisse zeigen deutlich: **Jeder der drei Server hat seine eigene Stärke**.

- Der **Dell OptiPlex 3070** ist der **Leistungssieger** (5× Gold) – perfekt für schwere VMs, Datenbanken und Docker-Workloads
- Der **Fujitsu Futro S7010** ist der **Überraschungssieger** (2× Gold) – mit nur 42 € und 10 Watt Stromverbrauch die perfekte Firewall
- Der **HP ProDesk 400 G4** ist der **bewährte Allrounder** – und das unter Dauerlast im Live-Betrieb

Zusammen kosten sie **weniger als 220 Euro** und ersetzen einen Neu-Server für das Vierfache. Du bekommst:

✅ **16 CPU-Kerne** für parallele Workloads  
✅ **80 GB RAM** für viele gleichzeitige VMs  
✅ **Echtes Proxmox-Cluster** mit Live-Migration und Hochverfügbarkeit  
✅ **Redundanz** – fällt einer aus, laufen die anderen weiter  
✅ **Von überall Zugriff** auf deine Daten – per VPN vom Handy aus  

**Meine Empfehlung:** Fang mit einem Server an (z.B. HP ProDesk für ~80 €) und bau dein Cluster nach und nach aus. Der Fujitsu Futro für 42 € ist ein No-Brainer – den kannst du auch als Router oder AdGuard-Host nebenher laufen lassen, während er kaum Strom zieht.

---

## Weiterführende Artikel

- 🔗 [Virtualisierung kostenlos 2026: Proxmox VE als VMware-Alternative](/homelab-blog/posts/virtualisierung-kostenlos-2026-proxmox-vmware-alternative/) — Warum Proxmox die beste kostenlose Virtualisierungsplattform ist
- 🔗 [Mini PC fürs Homelab nach Budget: Von 50€ bis 650€](/homelab-blog/posts/mini-pc-homelab-2025-vergleich/) — Welcher Mini-PC passt zu deinem Budget?

*Als Amazon-Partner verdiene ich an qualifizierten Verkäufen.*
