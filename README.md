
## 🚀 Direkt starten mit Binder - kann einige Zeit dauern

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/RVeh/test/HEAD)


Im Menü `Run| Run all Cells` drücken, um die Programme zu starten.

--- 

## Hypothesentests – Modell, Setzung, Wirkung

Dieses Projekt enthält vier aufeinander aufbauende Programme
zur Darstellung und Untersuchung von Hypothesentests
am Beispiel des Binomialmodells.

Die Programme folgen einer einheitlichen Struktur:

**Modell → Setzung → (ggf.) Beobachtung**

Ziel ist nicht die rechnerische Durchführung,
sondern das Sichtbarmachen der zugrunde liegenden Struktur.

---

## Inhalte - Hypothesentests

### 1. Verteilung
Darstellung der Binomialverteilung
in einem $\sigma$-basierten Bereich um $\mu$.

### 2. Ablehnungsbereich
Darstellung eines zweiseitigen Ablehnungsbereichs
für eine gegebene Setzung $\alpha$.

### 3. Spiegelung
Veranschaulichung der Wirkung eines festen Ablehnungsbereichs
bei Variation des Modellparameters.

### 4. Powerfunktion
Darstellung der Powerfunktion
als Wahrscheinlichkeit $P_p(X \in K)$
in Abhängigkeit vom wahren Parameter p.

---
## Inhalte - Konfidenzintervalle

### 1. Berechnungen
Es werden die WALD-WILSON- und CLOPPER-PERASON-Konfidenzintervalle berechnet und ausgegeben.

### 2. Prognosintervalle
Es wird mithife der Konfidenzellipse ein Prognoseintervall ermittelt.

### 3. Konfidenzintervalle
Es wird mithife der Konfidenzellipse ein Konfidenzintervall ermittelt.

### 4. Simulationen

Es werden $n$ Konfidenzintervalle mithilfe einer Sumulation ermittelt und gafisch dargestellt.

---

## Ausführung

Die Notebooks sind für die Nutzung mit Jupyter / Binder vorbereitet.

Beim ersten Start bitte **Run All Cells** ausführen.
Anschließend können die Parameter angepasst
und einzelne Zellen erneut ausgeführt werden.

---

## Struktur

Die zugrunde liegende Modulstruktur trennt konsequent:

- Modell (Verteilung)
- Geometrie (Ablehnungsbereich)
- Entscheidung (p-Wert)
- Darstellung (Plots)
- Stil (Layout)

Änderungen an Stil oder Setzungen wirken systemweit.

---

## License

© 2026 Reimund Vehling

Dieses Projekt ist als frei zugängliche didaktische Grundlage
für Schule, Hochschule und Weiterbildung gedacht.

Verwendung und Weitergabe sind unter den Bedingungen der
Creative Commons Attribution-NonCommercial 4.0 International License
(CC BY-NC 4.0) gestattet.

https://creativecommons.org/licenses/by-nc/4.0/

