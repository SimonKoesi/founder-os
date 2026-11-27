# Founder OS

A modular, AI-native Founder Operating System for building, managing and scaling
projects with Codex.

Das zentrale Framework verbindet Business-Methoden mit Produktentwicklung,
Implementierung, Qualität, Launch und Betrieb. Es lädt Kontext gezielt über
[AGENTS](AGENTS.md) und [Routing](core/context-routing.md). Projekte erhalten nur
ihren eigenen Zustand und eine Bridge zur gebundenen Framework-Version.

Voraussetzung: Python 3.11+, keine zusätzlichen Python-Pakete. Windows/PowerShell
wird lokal geprüft; die CI ist zusätzlich für Ubuntu vorgesehen.

```powershell
# Im founder-os-Verzeichnis: prüfen und neue Projekte separat anlegen
python scripts/founder.py validate
python -m unittest discover -s tests -v
python scripts/founder.py init ../mein-projekt --name "Mein Projekt" --type saas --stack Python
python scripts/founder.py status --project ../mein-projekt
python scripts/founder.py route "Ersten SaaS-Ablauf implementieren" --project ../mein-projekt
```

Danach das Projektverzeichnis in Codex öffnen und dessen AGENTS verwenden.
Das Framework ist keine laufende Hintergrundanwendung und keine dauerhafte
Chat-Erinnerung. Kontextdateien sind die prüfbare Grundlage jeder Fortsetzung.

- [Nutzung: neue und bestehende Projekte, Installation, Updates](docs/usage.md)
- [Architektur und Entscheidungen](docs/architecture.md)
- [Skills, Workflows und Lebenszyklus](docs/catalog.md)
- [Migration, Herkunft und Widersprüche](docs/migration/analysis.md)
- [Codex-Kompatibilität und offizielle Quellen](docs/compatibility.md)
- [Validierung und Grenzen](docs/validation.md)
- [GitHub-Veröffentlichung nach Authentifizierung](docs/publishing.md)
- [Vollständiger Verzeichnisbaum](docs/tree.md)

Die elf migrierten Business-Skills behalten ihre detaillierten Methoden und
vier Offline-Rechenwerkzeuge. Fünf neue Skills ergänzen Produktdefinition,
Softwareentwicklung, Releases, Frameworkpflege und Charts. Simulationen sind
Hypothesen; ein rechnerisch positives Modell beweist keine Marktnachfrage.
Die bestätigte Rechtebasis und erhaltene Urheberhinweise stehen in
[NOTICE](NOTICE.md). Die Originalquelle bleibt unverändert.
