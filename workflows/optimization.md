# Optimierung und Skalierung

Ziel: Nachgewiesene Engpässe verbessern, ohne Integrität zu verlieren.

Voraussetzung: Baseline, Zielmetrik, Budget und beobachteter Engpass.

Verantwortung: Owner entscheidet größere Kosten; Codex vergleicht und testet.

1. Nutzer-/Betriebsdaten statt Vermutungen für Engpass wählen.
2. Hypothese mit Erfolg und Stoppschwelle formulieren.
3. Kleinste reversible Änderung gegen Baseline messen.
4. Kapazität, Unit Economics und Supportlast unter Wachstum simulieren.
5. Nur belegte allgemeine Erkenntnisse zur Framework-Verbesserung vorschlagen.

Ergebnis: Messvergleich, Entscheidung, Rollout und ggf. Kapazitätsplan.

Abnahme: Messbarer Nutzen, keine verschlechterten Schutzmetriken, Rollback vorhanden.

Übergang: operation, weitere Iteration oder architecture für belegte strukturelle Grenze.

Benötigte Skills und Standards: passender Eintrag in [Routing](../core/routes.json). Für kleine Projekte genügen relevante Schritte und belegter Check; Phasen sind iterativ und dürfen überlappen.
