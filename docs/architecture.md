# Architekturentscheidungen

| Entscheidung | Grund und Konsequenz |
| --- | --- |
| Zentraler, versionierter Runtime-Bestand | Ein Regelbestand; keine vollständige Frameworkkopie pro Projekt |
| Kleine lokale Discovery-Bridge | Codex lädt fremde Repository-Skills nicht allein wegen eines Dateilinks |
| JSON statt eigener YAML-Sprache | Python-Standardbibliothek genügt; Schemas und Typen bleiben eindeutig |
| Version plus Inhaltsdigest | Erkannt werden auch unversionierte Änderungen im zentralen Checkout |
| Unveränderliche Release-Installation | Offline und mehrere Computer ohne unkontrolliertes Drift |
| Vorschau/Apply bei Updates | Nutzer kann den konkreten Wechsel prüfen; keine zentrale Selbstmodifikation |
| Prozess nach Risiko/Größe | Kleines Skript braucht keinen SaaS-Freigabeapparat |
| SKILL als kurzer Einstieg, method als Detail | Erhaltenes Businesswissen ohne lange Metadaten im Startkontext |
| Einfache Schlüsselwort-Routen mit Phasenfallback | Prüfbarkeit ohne Modell-/Netzwerkabhängigkeit; Codex bewertet semantische Eignung |
| Keine verpflichtende Agentendelegation | Rollen sind Perspektiven; Tools, Kosten und Autorisierung variieren |
| Lokales Originalarchiv plus vollständiges Mapping | Informationsverlust überprüfbar; keine vertraulichen Rohdaten unkontrolliert publizieren |

Abhängigkeiten: Projekt-Bridge → Projektvertrag/Status → ausgewählte Route → Workflow
und Skill → optionale Methode/Standard/Tool. Methoden erzeugen Projektartefakte,
die Projektzustand und spätere Aufgaben speisen. Zentrale Regeln werden nur über
reviewte Änderungen, Tests und Versionswechsel übernommen. Navigations-Backlinks
sind keine Ausführungsabhängigkeiten. Business-Artefakte dürfen iterativ entstehen;
`compile.py` lädt ausschließlich das CFO-Werkzeug und Projektdateien, keine Skills.

Die Runtime-Liste in framework.json ist die kanonische Verteilungs- und Digestgrenze.
Tests, Migrationshistorie und Bericht gehören zum Entwicklungsrepository, nicht
zum minimalen Releasepaket. Die Installation erhält LICENSE/NOTICE als Zusatz.
AGENTS bleibt kurz; zentrale Skill-Verfahren werden nur bei passender Route geladen.
Kein Plugin-Manifest wird vorgetäuscht und kein Claude-Marketplace als Codex-Funktion
umbenannt. Native Plugin-Verteilung kann bei echtem Bedarf separat ergänzt werden.
