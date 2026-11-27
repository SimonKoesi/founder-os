# Review

Ziel: Änderung auf Verhalten, Integrität und Wartbarkeit bewerten.

Voraussetzung: Diff, Akzeptanzkriterien, tatsächliche Prüfergebnisse.

Verantwortung: Codex prüft als eigene Perspektive; unabhängige Agenten nur autorisiert.

1. Diff und betroffene Aufrufer prüfen.
2. Datenverlust, Rechte, Secrets und Doppelwirkungen suchen.
3. Unnötige Komplexität, tote Aktionen und fehlende Rückwege prüfen.
4. Befunde nach Schwere mit Fundstelle dokumentieren.
5. Beauftragte Korrekturen und gezielte Wiederprüfung durchführen.

Ergebnis: Reviewbefunde und Abschluss-/Releaseentscheidung.

Abnahme: Keine ungelösten blockierenden Befunde; Restrisiken benannt.

Übergang: deployment oder implementation.

Benötigte Skills und Standards: passender Eintrag in [Routing](../core/routes.json). Für kleine Projekte genügen relevante Schritte und belegter Check; Phasen sind iterativ und dürfen überlappen.
