# Architektur

Ziel: Wartbare Grenzen, Datenfluss und sichere Integrationen festlegen.

Voraussetzung: Anforderungen, vorhandener Stack und relevante Qualitätsziele.

Verantwortung: Codex schlägt reversible Architektur vor; Owner entscheidet größere Betriebskosten.

1. Bestehende Komponenten vor Neubau prüfen.
2. Datenmodell, Schnittstellen, Autorisierung und Fehlerfluss skizzieren.
3. Für SaaS Mandantentrennung und Billing-Wiederholung explizit prüfen.
4. Migration, Kompatibilität, Deployment und Rollback entwerfen.
5. Wesentliche Abwägung mit templates/decision.md dokumentieren.

Ergebnis: Architekturentscheidungen und prüfbare Schnittstellen, bei Bedarf Diagramm.

Abnahme: Anforderungen und Sicherheitsgrenzen sind abgedeckt; Abhängigkeiten begründet.

Übergang: design/implementation; bei hohem Risiko ein isolierter Spike vorab.

Benötigte Skills und Standards: passender Eintrag in [Routing](../core/routes.json). Für kleine Projekte genügen relevante Schritte und belegter Check; Phasen sind iterativ und dürfen überlappen.
