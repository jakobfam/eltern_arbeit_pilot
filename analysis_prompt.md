# Analyse-Prompt: Pilotstudie "Was sollten werdende Eltern wissen?"

## Kontext

Du analysierst die Daten einer **Pilotstudie** (oTree 5, Prolific-Sample, Deutschland). Die Studie untersucht die **finanziellen und beruflichen Erfahrungen von Müttern** rund um die Familiengründung. Ziel ist es, Informationslücken zu identifizieren, die ein geplantes Informationsprogramm für werdende Eltern adressieren soll.

**Zielgruppe:** Frauen in Deutschland, die mindestens ein Kind haben.

**Wichtig:** Dies ist eine Pilotstudie mit kleiner Stichprobe. Das Hauptziel ist die Überprüfung des Instruments (Verständlichkeit, Varianz, fehlende Antwortoptionen), nicht die Ableitung kausaler Schlüsse.

## Datenbeschreibung

Ich gebe dir zwei Dateien:
1. **Codebook** (codebook_pilot_survey.xlsx) — enthält alle Variablen, Labels, Wertebereiche und Anmerkungen
2. **Daten** (CSV oder XLSX-Export aus oTree)

## Aufgaben

### 1. Datenbereinigung
- Entferne Beobachtungen mit `consent = False` (kein Consent)
- Entferne Beobachtungen mit `attention = False` (beide Aufmerksamkeitschecks falsch)
- Entferne Bots (`is_bot = True`)
- Berichte, wie viele Beobachtungen in jedem Schritt entfernt wurden
- Prüfe auf auffällig kurze Bearbeitungszeiten (`time_to_complete`) als weiteres Qualitätskriterium

### 2. Deskriptive Statistik
- **Demografie:** Verteilung von Geburtsjahr, Einkommen, Tätigkeit, Branche
- **Ranking-Fragen (A0b, A3, B2):** Häufigkeit, mit der jedes Item auf Rang 1/2/3 gewählt wurde. Erstelle eine Tabelle mit Item, Anzahl Rang 1, Rang 2, Rang 3, und Gesamtnennungen. Sortiere nach Gesamtnennungen absteigend.
- **Likert/Ordinal-Skalen (A1, A2, B1b, B3, B4, B5, C3):** Häufigkeitsverteilung und Median
- **Checkbox-Fragen (B1c, C2):** Anteil der Befragten, die jedes Item angekreuzt haben
- **Wissensfragen (D1, D2):** Anteil korrekt, falsch, "weiß nicht"

### 3. Offene Textfragen — Qualitative Kurzanalyse
Für jede offene Frage (A0.4 topics, B1, B5b, C1):
- Lies alle Antworten
- Identifiziere die 5–8 häufigsten Themen/Kategorien
- Erstelle eine einfache Häufigkeitstabelle der Kategorien
- Zitiere 2–3 besonders prägnante Antworten wörtlich

### 4. Kreuzanalysen (explorativer Charakter)
- **Einkommen × Vorbereitung (B3):** Fühlen sich einkommensstarke Haushalte besser vorbereitet?
- **Tätigkeit × Wiedereinstieg (A1):** Unterscheiden sich Vollzeit/Teilzeit/Elternzeit in ihren Erwartungen?
- **B1c (Maßnahmen) × Einkommen:** Treffen einkommensstarke Haushalte häufiger finanzielle Vorsorgemaßnahmen?
- **Planungshorizont (B4) × Vorbereitung (B3):** Korrelieren längerer Horizont und bessere Vorbereitung?
- **Wissen (D1, D2) × Vorbereitung (B3):** Hängt finanzielles Wissen mit dem Gefühl der Vorbereitung zusammen?

Nutze geeignete Tests (Chi-Quadrat, Mann-Whitney-U, Spearman-Korrelation), aber berichte bei kleinem N vor allem deskriptive Muster. Markiere klar, wenn Zellbesetzungen zu klein für belastbare Aussagen sind.

### 5. Instrumentenprüfung (Pilot-spezifisch)
- **Varianz:** Gibt es Items mit zu geringer Varianz (>90% auf einer Kategorie)?
- **Fehlende Werte:** Welche Fragen haben auffällig viele Missings?
- **Deckeneffekte:** Gibt es Fragen, bei denen fast alle dasselbe antworten?
- **Freitextanalyse auf fehlende Optionen:** Nennungen bei "Sonstiges"-Feldern (a0b, a3, b2), die auf fehlende Antwortoptionen hindeuten
- **Bearbeitungszeit:** Median und Verteilung. Gibt es Ausreißer?

### 6. Zusammenfassung & Empfehlungen
Fasse die Ergebnisse in 3 Abschnitten zusammen:
1. **Inhaltliche Kernergebnisse:** Die 5 wichtigsten Befunde zu Informationslücken und Erfahrungen von Müttern
2. **Instrumentenqualität:** Was funktioniert gut, was sollte für die Hauptstudie angepasst werden?
3. **Empfehlungen für die Hauptstudie:** Konkrete Vorschläge (Items streichen/ergänzen, Formulierungen anpassen, Skalenänderungen)

## Technische Hinweise
- Verwende Python (pandas, scipy, matplotlib/seaborn)
- Erstelle alle Visualisierungen als Balkendiagramme oder Heatmaps (keine Pie-Charts)
- Beschrifte alle Achsen auf Deutsch
- Exportiere die Zusammenfassung und alle Tabellen als formatierte Excel-Datei

## Verifikation

Nachdem du die Analyse abgeschlossen hast, starte einen Verifikations-Agenten, der Folgendes prüft:
- Stimmen die berichteten N mit den Daten überein?
- Sind alle statistischen Tests korrekt angewendet (richtige Voraussetzungen)?
- Stimmen die berichteten Prozentwerte/Mediane, wenn man sie manuell nachrechnet?
- Gibt es logische Inkonsistenzen in den Ergebnissen?
- Sind die Interpretationen durch die Daten gedeckt oder wird überinterpretiert?

Der Agent soll seinen Bericht als separaten Abschnitt "Verifikationsbericht" ausgeben.
