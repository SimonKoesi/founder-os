# Deployment

Ziel: Kontrollierte Veröffentlichung mit Wiederherstellung ermöglichen.

Voraussetzung: Geprüfter Build/Diff; Zielumgebung und erforderliche Autorisierung.

Verantwortung: Owner autorisiert produktive Folgen; Codex bereitet ausführbare Schritte vor.

1. Secrets/Rechte und Quellrechte prüfen.
2. Migration, Backup und Restore-/Rollbackplan konkretisieren.
3. Lokale/Staging-Prüfungen abschließen.
4. Bereits autorisierte Veröffentlichung ausführen; sonst erst jetzt konkrete Freigabe anfordern.
5. Remote Zustand, Commit und Health prüfen; Erfolg nur nach Bestätigung.

Ergebnis: Releasebeleg, Changelog, Rollback und Betriebsübergabe.

Abnahme: Zielzustand bestätigt; bei Fehler sichere Wiederholung ohne Doppelwirkung.

Übergang: launch/operation; fehlende Authentifizierung mit exakten Nachholschritten dokumentieren.

Benötigte Skills und Standards: passender Eintrag in [Routing](../core/routes.json). Für kleine Projekte genügen relevante Schritte und belegter Check; Phasen sind iterativ und dürfen überlappen.
