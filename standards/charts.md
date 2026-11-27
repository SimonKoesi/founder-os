# Premium Charts & Data Visualization

## 1. Mission

Entwickle Datenvisualisierungen, die modern, cool, professionell und wertvoll wirken. Vermeide den Eindruck generischer Excel-Diagramme, veralteter Verwaltungssoftware und ungestylter Bibliotheksdefaults. Premium bedeutet Klarheit, Konsistenz, Datenintegrität und gezielte visuelle Akzente, nicht möglichst viele Effekte.

## 2. Verbindlicher Arbeitsablauf

1. Analysiere vorhandenen Tech-Stack, Design-Tokens, Daten, Zielgruppe und Nutzeraufgabe.
2. Identifiziere ungeeignete Diagrammtypen und visuelle Schwächen.
3. Wähle den Diagrammtyp nach Informationsbedarf, nicht allein nach Ästhetik.
4. Verwende vorhandene Komponenten und Bibliotheken; vermeide unnötige Abhängigkeiten.
5. Implementiere responsive Darstellung, Tooltips, zugängliche Beschriftungen und alle relevanten Zustände.
6. Prüfe echte Daten, Extremwerte, kleine Bildschirme, Light/Dark Mode und Performance.
7. Dokumentiere Änderungen, Annahmen und verbleibende Einschränkungen. Behaupte keine Tests, die nicht durchgeführt wurden.

## 3. Diagrammtransformationen

Die folgenden schematischen Vorschauen verwenden illustrative Werte und sind keine produktionsfertigen Charts. Die moderne Variante soll die Aussage erhalten; zusätzliche Daten dürfen niemals erfunden werden.

### 3.1 Klassisches Balkendiagramm → Rounded Bar Chart

```text
ALT                       PREMIUM
│ ▓   ▓                   Aktivität
│ ▓ ▓ ▓   ▓                  ╭─╮     ╭─╮
│ ▓ ▓ ▓ ▓ ▓              ╭─╮ │ │ ╭─╮ │ │ ╭─╮
└──────────              ╰─╯ ╰─╯ ╰─╯ ╰─╯ ╰─╯
 J F M A M                Jan Feb Mär Apr Mai
```

- Vermeide schwarze Rahmen, massive Achsen, grelle Standardfarben und dominante Gitternetze.
- Nutze leicht gerundete Balkenenden, subtile Hilfslinien und gezielte Hervorhebung.
- Beginne quantitative Balkenachsen grundsätzlich bei null. Verwende horizontale Balken bei langen Kategorienamen.
- Einsatz: Monatswerte, Rankings, Mengen, Kategorievergleiche.

### 3.2 Kreisdiagramm → Donut Chart

```text
ALT                       PREMIUM
   ◉ bunt                    ╭━━━━╮
 50 / 25 / 25              ┃ 100% ┃
                             ╰━━━━╯
                          A 50% · B 25% · C 25%
```

- Keine 3D-Perspektive, explodierten Segmente, schwarzen Konturen oder Regenbogenfarben.
- Nutze einen ruhigen Ring mit zentraler Kennzahl und klarer Legende.
- Nur für nichtnegative Anteile eines sinnvollen Ganzen; bei vielen oder ähnlichen Anteilen horizontale Balken bevorzugen.
- Segmentabstände dürfen kleine Anteile nicht verschlucken.
- Einsatz: Marktanteile, Kategorien, Statusverteilungen.

### 3.3 Standard-Liniendiagramm → Gradient Area Chart

```text
ALT                       PREMIUM
┼─┼─┼─┼─┼                    ▁▃▂▅▃▇
│ /\/\ /                  ▁▂▃▄▅▆▇  Verlauf
┼─┼─┼─┼─┼                 dezente Fläche unter Linie
```

- Klare Linie, optional transparenter Farbverlauf darunter, wenige Hilfslinien.
- Crosshair und Tooltip für exakte Werte; aktuelle Werte optional hervorheben.
- Glättung nur, wenn sie keine künstlichen Extremwerte oder falsche Zwischenwerte erzeugt. Fehlende Daten nicht ungekennzeichnet verbinden.
- Flächencharts benötigen eine sinnvolle Basislinie; bei Bedarf reine Linie wählen.
- Einsatz: Umsatz, Nutzerzahlen, Messwerte, Zeitreihen.

### 3.4 Klassischer Tachometer → Radial Progress Chart

```text
ALT                       PREMIUM
  ROT GELB GRÜN              ╭━━━━╮
      ↗                     ┃ 78% ┃
     78%                     ╰━╴  ╯
                            Auslastung
```

- Entferne dekorative Nadeln und überladene Skalen.
- Verwende einen dünnen Fortschrittsring mit klarer zentraler Kennzahl.
- Nutze lineare Fortschrittsbalken für viele parallele Vergleiche. Zeige Zielwerte und Grenzwerte ausdrücklich, wenn relevant.
- Einsatz: Auslastung, Zielerreichung, Speicherplatz, Fortschritt.

### 3.5 Gestapelte Balken → Segmented Progress Bar

```text
ALT                       PREMIUM
[GGGGGG|YYY|RR]           Projektstatus · 60% erledigt
                          ━━━━━━━━━  ━━━━  ━━
                          ● Erledigt      60%
                          ● In Arbeit     25%
                          ● Offen         15%
```

- Nutze kompakte Segmente, semantische Farben und direkte Werte.
- Segmente proportional zur Datenmenge darstellen; Lücken nicht übertreiben.
- Bei absoluten Mengen keine Prozentnormalisierung ohne klare Kennzeichnung.
- Einsatz: Projektstatus, Budgets, Kapazitätsverteilung.

### 3.6 Standard-Scatterplot → Premium Scatter / Bubble Chart

```text
ALT                       PREMIUM
│     · ·                 │        ◯
│  · ·                    │    ○  ◉
│ · ·                     │ ○  ○
└────────                 └─────────
```

- Subtile Achsen, halbtransparente Punkte und sinnvolle Gruppenfarben.
- Bubble Chart nur bei vorhandener dritter quantitativer Variable; Kreisfläche proportional zum Wert skalieren (Radius proportional zur Quadratwurzel).
- Ohne dritte Variable einheitliche Punktgröße verwenden.
- Einsatz: Korrelationen, Cluster, Risiko-Rendite-Vergleiche.

### 3.7 Zahlenkolonnen → Heatmap

```text
ALT                       PREMIUM
1 4 8 2 7                 ░ ▒ █ ░ ▓
5 2 6 9 1                 ▓ ░ ▓ █ ░
3 8 1 4 6                 ▒ █ ░ ▒ ▓
                          Niedrig → Hoch
```

- Nutze abgestufte Farbintensitäten, klare Zeit-/Kategorieachsen und Farblegende.
- Fehlende Daten deutlich von null unterscheiden. Exakte Werte per Tooltip, Tastatur oder Tabelle verfügbar machen.
- Sequentielle Palette für Intensitäten; divergierende Palette für sinnvollen Mittelpunkt.
- Einsatz: Aktivität, Arbeitszeiten, Frequenz, Auslastung.

### 3.8 Einfache Kennzahlen → KPI Cards mit Sparklines

```text
ALT                       PREMIUM
+----------------+        Gesamtumsatz
| Umsatz:        |        24.580 €       ▁▂▁▄▃▆▇
| 24.580 EUR     |        ↗ 12,8 %
| Steigerung 12% |        zum Vormonat
+----------------+
```

- Hierarchie: Bezeichnung, Hauptwert, Veränderung, Bezugszeitraum, optional Sparkline.
- Sparkline aus echten historischen Werten erstellen; nicht als dekorativen Aufwärtstrend erfinden.
- Positive Veränderung ist nicht immer gut (z. B. Kosten oder Fehlerquote).
- Einsatz: Dashboard-Kernmetriken, Umsatz, Conversion, Monitoring.

### 3.9 Klassische Treemap → Bento-style Treemap

```text
ALT                       PREMIUM
+----+----+               ╭────────╮ ╭─────╮
| A  | B  |               │ A 50%  │ │B 25%│
|    +--+-+               │        │ ╰─────╯
|    |C |D|               │        │ ╭──╮╭─╮
+----+--+-+               ╰────────╯ ╰──╯╰─╯
```

- Ruhige Farbpalette, dezente Abstände, moderate Rundung und lesbare Labels.
- Rechteckflächen müssen Werte proportional abbilden; keine freie Bento-Anordnung als Treemap ausgeben.
- Kleine Kategorien zusammenfassen oder per Drill-down erschließen, wenn fachlich sinnvoll.
- Einsatz: Speicherplatz, Dateiverwaltung, Finanzen, hierarchische Kategorien.

## 3A. Verbindliche Diagrammauswahl: DON'T / DO

Diese Regeln haben Vorrang vor rein dekorativen Designwünschen. **MUST NOT** = nicht einsetzen. **AVOID** = standardmäßig vermeiden, Ausnahme fachlich begründen. **PREFER** = bevorzugte Lösung bei passender Datenstruktur. Ein Diagrammtyp ist nicht allein aufgrund seines Namens hochwertig oder minderwertig. Ersetze ungeeignete Typen, gestalte geeignete Typen neu.

| Nicht verwenden bzw. vermeiden | Stattdessen bevorzugen | Konkrete Auswahlregel |
|---|---|---|
| MUST NOT: perspektivische 3D-Pie-, 3D-Bar-, 3D-Area-Charts für zweidimensionale Daten | Flat Donut, Rounded Bar, Line Chart | Keine perspektivische Verzerrung von Länge, Fläche oder Winkel. |
| AVOID: klassisches buntes Pie Chart, Exploded Pie | Donut Chart oder Horizontal Ranked Bar | Donut für 2–5 deutlich unterscheidbare Teile eines Ganzen; bei vielen oder ähnlichen Anteilen sortierte horizontale Balken. |
| AVOID: ungestyltes Excel-/Standard-Bar-Chart | Rounded Vertical Bar / Horizontal Ranked Bar | Vertikal für wenige kurze Kategorien oder diskrete Zeitperioden; horizontal für Rankings und lange Namen. |
| AVOID: überladenes Line Chart mit Marker an jedem Punkt | Minimal Line / Gradient Area | Linie für Trends und exakte Verläufe; Gradient Area für eine dominante nichtnegative Zeitreihe mit sinnvoller Nullbasis. |
| AVOID: mehrere überlappende und deckende Area Charts | Multi-Line oder Small Multiples | Reihen direkt beschriften; bei Überlagerung getrennte Panels mit gemeinsamer Skala. |
| AVOID: analoger Tachometer mit Nadel, Chromrahmen oder Ampelskala | Radial Progress / Bullet Chart | Ring für einen begrenzten Fortschritt; Bullet für Ist gegen Ziel und Schwellen; echter Gauge nur bei fachlichem Bedarf. |
| AVOID: viele einzelne Fortschrittsringe nebeneinander | Horizontal Progress Bars / Bullet Charts | Gemeinsame Basislinie für präzisen Vergleich vieler Werte. |
| AVOID: klobige gestapelte Balken mit schwarzen Segmentrahmen | Segmented Progress / 100% Stacked Bar | Für Anteile; absolute Stacks nur für additive Mengen. Für genaue Teilvergleiche Grouped Bars oder Small Multiples. |
| AVOID: ungestylter Scatterplot mit massiven Achsen | Premium Scatter | Einheitliche Punktgröße, dezente Achsen, Transparenz bei Überlagerung. |
| MUST NOT: Bubble Chart mit willkürlicher Kreisgröße | Scatter oder datengesteuertes Bubble Chart | Kreisfläche kodiert ausschließlich eine echte dritte quantitative Variable; keine erfundenen Größen. |
| AVOID: reine Zahlenmatrix für Mustererkennung | Matrix Heatmap / Calendar Heatmap | Farbe zeigt Intensität, Legende und zugängliche exakte Werte bleiben verfügbar; Tabelle für genaue Nachschlageaufgaben behalten. |
| AVOID: graue, gerahmte Kennzahlenboxen | KPI Card + Sparkline | Hauptwert, Einheit, Bezugszeitraum und echte historische Entwicklung; ohne Historie keine Sparkline. |
| AVOID: grelle Treemap mit schwarzen Rahmen | Bento-style Treemap | Für hierarchische Teilmengen; Rechteckflächen proportional. Für präzises Ranking horizontale Balken. |
| AVOID: Funnel mit dekorativem Trichter oder unproportionalen Stufen | Horizontal Conversion Funnel / Step Bars | Stufenbreiten proportional zu tatsächlichen Mengen, Konversionsrate und Bezugsbasis angeben. |
| AVOID: Radar mit vielen überlagerten Polygonen | Grouped Bars / Dot Plot / Small Multiples | Radar nur bei wenigen Profilen auf vergleichbaren, sinnvoll normierten Dimensionen. |
| AVOID: Doppelachsen mit unterschiedlichen Einheiten | Aligned Small Multiples | Gemeinsame Zeitachse, eigene beschriftete Wertachsen; keine suggerierte Korrelation durch willkürliche Skalierung. |
| AVOID: Wortwolke für Häufigkeitsvergleich | Horizontal Ranked Bar / Lollipop | Wörter als Labels, Häufigkeit entlang gemeinsamer Achse; Wortwolke höchstens explorativ. |
| AVOID: Kreisflächen oder Piktogramme zum genauen Mengenvergleich | Bar / Dot Plot | Position und Länge für präzise Vergleiche bevorzugen. |
| AVOID: Mittelwertbalken als einzige Verteilungsdarstellung | Histogram / Box Plot / Violin + Punkte | Streuung, Ausreißer und Stichprobengröße sichtbar machen; Histogramm mit nachvollziehbaren Klassen. |
| AVOID: gewöhnliche Balken für additive Zu- und Abgänge | Waterfall Chart | Ausgangs- und Endwert, Zwischensummen, positive und negative Beiträge korrekt darstellen. |
| AVOID: Kreuzungstabellen als alleinige Darstellung von Mengenflüssen | Sankey Diagram | Nur bei echten quantifizierten Flüssen; Richtung, Knoten, Einheiten und proportionale Flussbreite. |
| AVOID: unübersichtlicher Network Graph (Hairball) | Filtered Network / Dependency Tree / Adjacency Matrix | Graph für Beziehungen, Baum für echte Hierarchien, Matrix bei dichten Netzwerken. |
| AVOID: Tabellen als einzige Übersicht über Projektzeiträume | Modern Gantt / Timeline | Start, Ende, Dauer und echte Abhängigkeiten sichtbar; Detailtabelle bei Bedarf behalten. |
| AVOID: Landkarte für nicht geografische Kennzahlen | Ranked Bar / Dot Plot | Karte nur, wenn räumliche Muster relevant sind; Choropleth bevorzugt für geeignete relative Kennzahlen, nicht unkritisch für Rohsummen. |
| MUST NOT: abgeschnittene Balkenachsen, dekorative Fake-Trends, erfundene Werte | Wahrheitsgetreue Skalierung und echte Daten | Auch beim Redesign keine Aussage verändern. |

### 3A.1 Konkrete Zielgestaltung je bevorzugtem Diagramm

| Premium-Typ | Pflichtmerkmale | Nicht hinzufügen |
|---|---|---|
| Rounded Bar | Nullbasis, 3–6 px Rundung an freien Enden, dezentes Grid, eine Akzentfarbe, beschriftete Kategorien | 3D, dicke Outlines, unnötige Farbwechsel pro Balken |
| Horizontal Ranked Bar | Gemeinsame Nullbasis, bei Rankings absteigende Sortierung, Labels links, Werte direkt am Balken | abgeschnittene Labels, willkürliche Sortierung |
| Donut | Ringstärke ca. 15–25 % des Durchmessers, wenige Segmente, zentrale sinnvolle Kennzahl, Werte und Kategorien außerhalb oder in Legende | 3D, Explosionsabstände, unlesbare Mini-Segmente |
| Minimal Line | 2–3 px Linie, dezente horizontale Hilfslinien, Zeitachse, Einheiten, Crosshair bei Interaktion | Zwangsglättung, Markerflut, Verbindung unbekannter Werte |
| Gradient Area | gut sichtbare Konturlinie, Füllung von ca. 15–25 % Deckkraft bis transparent, sinnvolle Nullbasis | mehrere opake Flächen, erfundene Zwischenwerte |
| Radial Progress | neutraler Hintergrundring, ein farbiger Fortschrittsbogen, zentraler Wert plus Label, bekannte Obergrenze | Nadel, künstlicher Glanz, stilles Abschneiden von Werten über 100 % |
| Segmented Progress | dünner horizontaler Balken, proportionale Segmente, direkte Werte und Statuslabels | Ampelfarben ohne Bedeutung, große Lücken |
| KPI + Sparkline | dominanter Wert, kurze Beschriftung, Vergleichszeitraum, kleine echte Zeitreihe ohne unnötige Achsen | dekorative Aufwärtstrends, irrelevante Prozentangaben |
| Heatmap | einheitliche Zellen, nachvollziehbare Farbskala, Achsen, Legende, Unterscheidung null/fehlend | Regenbogenpalette, zufällige Farben |
| Scatter / Bubble | klare x/y-Einheiten, sparsame Gridlines, einheitliche Punkte bzw. flächenproportionale Bubbles | willkürliche Punktgrößen, künstliche Cluster |
| Treemap | proportionale Flächen, lesbare Kategorien, dezente Abstände und Rundung | frei angeordnete Bento-Kacheln ohne Mengenbezug |
| Bullet | Ist-Balken, Zielmarke, optional dezente Referenzbereiche, gemeinsame Skala | Tachonadel, mehrfach verschachtelte Ringe |
| Sankey | proportionale Flussbreiten, nachvollziehbare Richtung und Labels, Fokus auf relevante Pfade | rein dekorative Ströme, inkonsistente Mengen |
| Waterfall | sichtbare Ausgangs-/Endwerte, semantische Zu-/Abgangsfarben, Verbindungslogik | Verwechslung von Einzelbeiträgen und Summen |
| Small Multiples | gleiche Skala bei direktem Vergleich, identische Panel-Größen, gemeinsame Achsenlogik | automatisch wechselnde Skalen ohne Kennzeichnung |

### 3A.2 Entscheidungsbaum (vor jedem neuen Diagramm anwenden)

1. Eine einzelne Kennzahl? KPI Card; echte Historie vorhanden → Sparkline ergänzen.
2. Fortschritt gegen festes Maximum? Ein Wert → Radial Progress oder Progress Bar; viele Werte → horizontale Progress Bars; expliziter Zielwert → Bullet.
3. Verlauf über Zeit? Minimal Line; dominante nichtnegative Mengenreihe → optional Gradient Area; diskrete Periodenmengen → Rounded Bar; viele Reihen → Small Multiples.
4. Kategorien vergleichen? Horizontal Ranked Bar oder Dot Plot; wenige kurze Kategorien → Vertical Bar.
5. Teile eines Ganzen? Wenige deutlich verschiedene Anteile → Donut; präzise Vergleiche → Bar; Statusanteile → Segmented Progress; Hierarchie → Treemap.
6. Zusammenhang zweier Variablen? Scatter; dritte quantitative Variable → optional Bubble.
7. Muster nach Tag, Stunde oder Kategorie? Calendar Heatmap oder Matrix Heatmap.
8. Verteilung? Histogram, Box Plot oder Violin Plot; nicht durch einen Mittelwert verschleiern.
9. Veränderungsbeiträge? Waterfall. Mengenflüsse? Sankey. Beziehungen? Network/Tree. Projektzeitraum? Gantt/Timeline.
10. Exakte Werte nachschlagen oder bearbeiten? Tabelle behalten oder ergänzen. Kein Diagramm erzwingen.

### 3A.3 Abnahme für Coding-Agenten

Inventarisiere alle bestehenden Diagramme. Dokumentiere pro Diagramm: Datei/Komponente, aktueller Typ, Nutzeraufgabe, Datenstruktur, Verstoß gegen diese Regeln, gewählter Zieltyp und Begründung. Ersetze MUST-NOT-Varianten; modernisiere AVOID-Varianten oder dokumentiere die fachliche Ausnahme. Verwende keine neue Bibliothek allein wegen einer optischen Änderung. Prüfe vor/nach dem Umbau Werte, Skalierung, Filter, Tooltips, Export, Responsivität und vorhandene Funktionen. Wenn notwendige Daten fehlen, nutze den einfacheren korrekten Typ statt einer erfundenen Premium-Visualisierung.

## 4. Weitere hochwertige Diagrammtypen

| Typ | Geeignete Aufgabe | Premium-Regel |
|---|---|---|
| Sankey Diagram | Mengenflüsse und Übergänge | Flussbreiten proportional; Richtung und Einheiten klar |
| Network Graph | Beziehungen und Abhängigkeiten | Gruppen, Suche und Fokus auf relevante Knoten; kein unlesbarer Knotenball |
| Waterfall Chart | Veränderung eines Ausgangswerts | Positive/negative Beiträge und Summen eindeutig kennzeichnen |
| Radar Chart | Mehrdimensionale Profile | Gemeinsame Skalen; wenige Reihen; bei präzisem Vergleich Balken bevorzugen |
| Calendar Heatmap | Tagesbezogene Aktivitäten | Kalenderlogik, Wochentage, Legende und fehlende Daten beachten |
| Multi-Radial Chart | Wenige unabhängige Fortschritte | Ringe einzeln beschriften; keine irreführenden Summen |
| Lollipop / Dot Plot | Kompakte Rankings | Werte entlang gemeinsamer Achse vergleichen |
| Bullet Chart | Istwert gegen Zielwert | Zielmarke und Referenzbereiche klar trennen |
| Small Multiples | Vergleich vieler Zeitreihen | Identische Skalen und konsistente Zeitachsen |
| Box Plot | Verteilung und Streuung | Quartile, Whisker-Definition und Ausreißer erklären |

## 5. Anti-Patterns und Ersatzregeln

| Vermeiden | Bevorzugen |
|---|---|
| 3D-Kreis- und 3D-Balkendiagramme | Flache Donuts oder Balken |
| Regenbogenfarben ohne Bedeutung | Semantisches, abgestimmtes Farbsystem |
| Dicke schwarze Rahmen | Dezente Konturen oder keine Rahmen |
| Excel-/Bibliotheks-Standarddesign | Gemeinsame Design-Tokens |
| Überladene Legenden | Direkte Beschriftungen, sofern lesbar |
| Harte Gitternetzlinien | Subtile, wenige Hilfslinien |
| Starre Charts ohne Detailzugriff | Sinnvolle Tooltips, Fokus und Datenzugriff |
| Abrupte Aktualisierungen | Kurze, optionale Übergänge |
| Übermäßige Dezimalstellen | Fachlich angemessene Rundung |
| Starke Schatten, Neon und Glaseffekte | Zurückhaltende Akzente und klare Flächen |
| Platzverschwendung | Gezielter Freiraum |
| Uneinheitliche Typografie | Konsistente Größen und tabellarische Ziffern |
| Unnötige Doppelachsen | Separate Charts oder Small Multiples |
| Dekorative, erfundene Daten | Echte Daten und gekennzeichnete Demos |

## 6. Design-System

Nutze bestehende Produkttokens vorrangig. Folgende Werte sind anpassbare Defaults, keine Pflichtpalette.

```css
:root {
  --chart-bg: #ffffff;
  --chart-surface: #f8fafc;
  --chart-text: #0f172a;
  --chart-muted: #475569;
  --chart-grid: #e2e8f0;
  --chart-primary: #4f46e5;
  --chart-secondary: #0f766e;
  --chart-accent: #7c3aed;
  --chart-success: #047857;
  --chart-warning: #a16207;
  --chart-danger: #b91c1c;
  --chart-radius: 12px;
  --chart-bar-radius: 5px;
  --chart-padding: 20px;
  --chart-gap: 16px;
  --chart-line-width: 2.5px;
  --chart-duration: 180ms;
}
[data-theme="dark"] {
  --chart-bg: #0f172a;
  --chart-surface: #1e293b;
  --chart-text: #f1f5f9;
  --chart-muted: #94a3b8;
  --chart-grid: #334155;
  --chart-primary: #818cf8;
  --chart-secondary: #2dd4bf;
  --chart-accent: #c084fc;
  --chart-success: #34d399;
  --chart-warning: #fbbf24;
  --chart-danger: #f87171;
}
@media (prefers-reduced-motion: reduce) {
  :root { --chart-duration: 0ms; }
}
```

- Typografie: vorhandene UI-Schrift, alternativ Systemfont; KPI 26–36 px, Titel 14–18 px, Achsen 11–13 px als Startwerte. `font-variant-numeric: tabular-nums` für Kennzahlen.
- Farben: eine primäre Akzentfarbe, wenige ergänzende Farben, neutrale Hintergründe. Dieselbe Kategorie behält chartübergreifend dieselbe Farbe.
- Layout: 4/8-px-Raster, ausreichend Platz für Labels; keine verschachtelten Karten ohne Nutzen.
- Linien: normalerweise 2–3 px, dezente Hilfslinien, sparsame Marker.
- Flächen: optionaler Farbverlauf mit niedriger Deckkraft; niemals zur Verschleierung von Daten.
- Dark Mode: nicht bloß Farben invertieren; Kontraste, Tooltips und Auswahlzustände gesondert prüfen.

## 7. Interaktion und Animation

- Tooltip: Kategorie/Datum, exakter formatierter Wert, Einheit und ggf. Vergleichswert. Nicht außerhalb des Viewports abschneiden.
- Hover und Fokus: subtile Hervorhebung; Touch und Tastatur als gleichwertige Alternativen.
- Legendenfilter, Zoom, Drill-down und Zeitraumwahl nur bei tatsächlichem Mehrwert; Zustand und Reset klar anzeigen.
- Übergänge typischerweise 150–300 ms; bei hoher Aktualisierungsfrequenz Animationen reduzieren oder deaktivieren.
- Keine Endlosschleifen, springenden Kennzahlen oder dramatischen Eintrittsanimationen.
- `prefers-reduced-motion` respektieren.

## 8. Datenintegrität und Accessibility

- Keine erfundenen Messwerte, Trends oder Vergleiche. Demo-Daten kennzeichnen.
- Einheit, Zeitraum, Aggregation, Datenquelle und Aktualität dort sichtbar machen, wo sie relevant sind.
- Null, fehlend, nicht verfügbar und Fehler unterscheiden. Keine Division durch null bei relativen Veränderungen.
- Achsen und Größen proportional darstellen; logarithmische oder abgeschnittene Skalen ausdrücklich kennzeichnen.
- Farben nie als einziges Unterscheidungsmerkmal verwenden; Labels, Symbole, Muster oder Linienarten ergänzen.
- Als Ziel WCAG-AA-Kontraste anstreben: 4,5:1 für normalen Text, 3:1 für großen Text und erforderliche grafische Elemente, sofern anwendbar.
- Aussagekräftige zugängliche Namen, Textzusammenfassung und bei Bedarf Datentabelle anbieten.
- Deutsche Oberfläche: `Intl.NumberFormat('de-DE', ...)` und passende Datumsformatierung; interne Datenwerte unverändert halten.
- Tooltips dürfen keine exklusiven Informationen enthalten, die per Tastatur oder Touch nicht erreichbar sind.

## 9. Responsive Layout und Zustände

- Desktop: flexible Grid-/Bento-Anordnung, gemeinsame Ausrichtung und genügend Plotfläche.
- Tablet: weniger Spalten; Legenden und Beschriftungen umordnen.
- Mobil: einspaltig, weniger Achsenticks, horizontal scrollbare Detailtabellen nur bei Bedarf; keine abgeschnittenen Werte.
- Loading: dezente Skeletons mit stabiler Größe, keine vorgetäuschten Daten.
- Empty: verständliche Erklärung und ggf. sinnvolle nächste Aktion.
- Error: klare Fehlermeldung und ggf. Wiederholen.
- Partial/Stale: Teilverfügbarkeit oder Stand der Daten sichtbar kennzeichnen.
- Teste auch lange Labels, negative Werte, Nullen, fehlende Daten, sehr große Zahlen, einzelne Punkte und viele Kategorien.

## 10. Bibliotheksauswahl

| Bibliothek | Geeigneter Einsatz |
|---|---|
| Apache ECharts | Vielseitige Dashboards und komplexe Visualisierungen |
| Recharts | Deklarative React-Dashboards |
| ApexCharts | Interaktive Business-Charts; Lizenzbedingungen prüfen |
| Nivo | Kreative React-Datenvisualisierung |
| D3.js | Individuelle High-End-Visualisierungen mit höherem Implementierungsaufwand |
| Visx | Maßgeschneiderte React-Visualisierungen |
| Chart.js | Klassische, individuell gestaltete Charts |
| Plotly | Wissenschaftliche und analytische Visualisierungen |

Bevorzuge den vorhandenen Stack. Prüfe installierte Version, API, Lizenz, Rendering, Accessibility und Bundle-Größe vor Einführung einer neuen Bibliothek. Keine unnötigen Bibliothekswechsel. Keine unbestätigten API-Annahmen.

## 11. Architektur und Performance

- Trenne Rohdaten, Validierung, Aggregation, Formatierung, Chart-Konfiguration und Rendering.
- Gemeinsame Chart-Komponenten für Theme, Tooltip, Achsen, Legende und Zustände.
- Nutze zentrale Tokens statt verteilter Farb-Hardcodes.
- Stabile Schlüssel und passende Memoisierung; unnötige Neuberechnungen vermeiden.
- Bei großen Datenmengen geeignete Aggregation, Downsampling oder Canvas/WebGL prüfen. Extreme Werte und Aussage erhalten; Sampling kennzeichnen, wenn relevant.
- Keine Animationen bei jedem Render; Resize sauber behandeln; Ressourcen und Event-Listener bereinigen.
- Bei Redesign fachliche Logik und bestehende Funktionen erhalten, sofern nicht ausdrücklich anders gewünscht.

## 12. Empfohlene Premium-Dashboard-Komposition

```text
╭────────────────────────────────────────────────────╮
│ Analytics                      Zeitraum: 30 Tage   │
├────────────────┬─────────────────┬─────────────────┤
│ Umsatz         │ Nutzer          │ Conversion      │
│ 24.580 €  ▁▃▆  │ 8.420      ▁▂▅  │ 4,8 %      ▁▃▅  │
├──────────────────────────────────┬─────────────────┤
│ Umsatzentwicklung                │ Verteilung      │
│           ▁▃▂▅▃▇                 │      ◉          │
│ Gradient Area                    │ Donut           │
├───────────────────────┬──────────┴─────────────────┤
│ Kategorien           │ Aktivität                  │
│ Rounded Bars          │ ░▒▓░██▒░                   │
│                       │ ▓░▒██░▒▓  Heatmap          │
╰───────────────────────┴────────────────────────────╯
```

Diese Kombination ist ein Ausgangspunkt, kein starres Schema. Wähle KPI Cards, Zeitreihen, Balken, Donuts und Heatmaps nur, wenn sie die tatsächliche Nutzeraufgabe unterstützen. Nicht jeden Diagrammtyp gleichzeitig einsetzen.

## 13. Definition of Done

- [ ] Der Diagrammtyp passt zur fachlichen Fragestellung.
- [ ] Echte Werte werden korrekt und proportional dargestellt.
- [ ] Titel, Einheit und relevante Zeiträume sind eindeutig.
- [ ] Kein ungeprüftes Bibliotheksdefault-Design.
- [ ] Farben und Typografie entsprechen dem Produktdesign.
- [ ] Layout, Achsen und Labels sind ruhig und lesbar.
- [ ] Tooltips und erforderliche Aktionen funktionieren per Maus, Touch und Tastatur.
- [ ] Kontraste, alternative Datenzugriffe und reduzierte Bewegung geprüft.
- [ ] Loading-, Empty-, Error- und relevante Teilzustände implementiert.
- [ ] Responsive Verhalten und gegebenenfalls beide Themes geprüft.
- [ ] Extremwerte und fehlende Daten getestet.
- [ ] Keine unnötigen Abhängigkeiten oder Performance-Regressionsquellen eingeführt.
- [ ] Tatsächlich ausgeführte Tests und verbleibende Einschränkungen dokumentiert.

## 14. Leitprinzip

Ein einfaches, präzises und sorgfältig gestaltetes Balkendiagramm ist wertvoller als eine spektakuläre, aber unverständliche Visualisierung. Premium-Qualität entsteht durch die Kombination aus fachlicher Genauigkeit, visueller Ruhe, konsistenter Gestaltung und funktionaler Interaktion.
