# Fehlerbehebung

Ziel: Ursache einmal beheben und Verhalten für Aufrufer erhalten.

Voraussetzung: Reproduzierbarer Fehler oder konkret belegtes Symptom.

Verantwortung: Codex diagnostiziert und korrigiert im Auftrag.

1. Reproduktion und erwartetes Ergebnis festhalten.
2. Alle relevanten Aufrufer der betroffenen Funktion suchen.
3. Ursache eingrenzen, Daten und Nutzereingaben erhalten.
4. Gezielte Regression und bestehenden Erfolgsweg prüfen.
5. Fehler, Fix und tatsächliche Checks in handoff/state sichern.

Ergebnis: Kleiner vollständiger Fix und aussagekräftige Regression.

Abnahme: Fehler reproduzierbar behoben; Wiederholung und Nachbarverhalten intakt.

Übergang: review und vorherige Projektphase; kein vollständiger Lebenszyklus-Neustart.

Benötigte Skills und Standards: passender Eintrag in [Routing](../core/routes.json). Für kleine Projekte genügen relevante Schritte und belegter Check; Phasen sind iterativ und dürfen überlappen.
