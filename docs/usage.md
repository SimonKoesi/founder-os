# Verwendung

## Neues Projekt

1. Zentralen Checkout oder eine unveränderliche Installation bereitstellen.
2. In dessen Verzeichnis den Initialisierer starten; Ziel außerhalb des Frameworks.
3. `status` und `validate --project` prüfen.
4. Das Zielverzeichnis in Codex öffnen. Bei einer neuen Sitzung wieder hier starten.
5. Ziele und Anforderungen in context konkretisieren; echte Prüfergebnisse in state.

```powershell
python scripts/founder.py init ../mein-saas --name "Mein SaaS" --type saas --size standard --stack Python PostgreSQL
python scripts/founder.py validate --project ../mein-saas
python scripts/founder.py status --project ../mein-saas
python scripts/founder.py route "SaaS-Anforderungen definieren" --project ../mein-saas
```

Typen: idea, saas, automation, software, business. Größen: small, standard, large.
Typen setzen Fokus und Anfangsphase; Größen bestimmen die angemessene Tiefe der
Workflows, erzeugen aber keine zusätzlichen Pflichtdokumente. Stack ist eine Liste
von tatsächlichen Projekttechnologien, keine automatisierte Paketinstallation.

Die erzeugten Dateien enthalten echte Ausgangszustände und nächste Aufgaben.
Produktziele sind bis zur Discovery ausdrücklich unbekannt. Keine leeren src/tests
oder kopierten zentralen Handbücher. Schemas liegen unter `schemas/`; die CLI
implementiert die Vertragsprüfungen ohne externen JSON-Schema-Interpreter.

## Bestehendes Projekt übernehmen

Vorher Git-Diff/Backups und relevante lokale Regeln prüfen. Dann:

```powershell
python scripts/founder.py adopt ../bestehendes-projekt --name "Bestehendes Produkt" --type software
python scripts/founder.py status --project ../bestehendes-projekt
```

Der Befehl ergänzt `.founder`, eine kleine `founder-context`-Bridge, einen markierten
AGENTS-Abschnitt und Ignore-Regeln. Bestehender Quellcode und bestehende Regeln
bleiben erhalten; vorhandene `.founder` oder Bridge-Kollisionen werden abgelehnt.
Danach vorhandene Ziele, Architektur und Tests lesen und in Kontextdateien verlinken.
Die Übernahme selbst behauptet keine bestandenen Produkttests. Abweichungen zentraler
Standards mit Grund und Ablauf-/Reviewdatum in decisions dokumentieren.

## Zentrale Installation und mehrere Computer

```powershell
python scripts/founder.py install ../founder-releases/1.0.0
python ../founder-releases/1.0.0/scripts/founder.py bind --project ../mein-saas --framework ../founder-releases/1.0.0
```

Installation kopiert nur Runtime plus Herkunft/Lizenz und überprüft den Digest;
keine Global-Konfiguration, kein Netzwerk und kein Kopieren in jedes Projekt.
Installationen unverändert lassen. Für identische Projektpins darf `bind` einen
anderen Maschinenpfad setzen. `.founder/local.json` wird nicht versioniert.
Alternativ `FOUNDER_OS_HOME` setzen; diese Variable hat Vorrang vor local.json.
Bei widersprüchlicher Umgebungsvariable diese korrigieren oder entfernen.
Ein gleich benannter Versionsordner allein beweist keine identischen Inhalte;
Version UND Digest müssen passen. CRLF/LF wird im Digest normalisiert.

Codex entdeckt zentrale Skills außerhalb des Projektpfads nicht automatisch.
Die lokale Bridge liest ihre ausgewählten Dateien ausdrücklich. Native `$founder-*`
Auswahl ist im zentralen Repository verfügbar. Optionale Benutzer-Symlinks sind
laut offizieller Dokumentation möglich, werden hier wegen globaler Versionskonflikte
und Windows-Rechten nicht automatisch gesetzt. Kein automatischer globaler Installer.

Offline funktioniert mit erreichbarer lokaler Installation und Projektdateien.
Fehlt diese, können lokale Aufgaben weitergehen; zentrale Konformität bleibt ungeprüft.

## Update, Rückweg und Wiederholung

Neue zentrale Version separat installieren und prüfen. Vorschau ist Standard:

```powershell
python scripts/founder.py update --project ../mein-saas --framework ../founder-releases/1.1.0
# Nach Prüfung der neuen Standards, Changelog und Projekttests:
python scripts/founder.py update --project ../mein-saas --framework ../founder-releases/1.1.0 --apply
```

Es ändern sich nur Framework-Pin und lokaler Pfad. Vorheriger Projektvertrag wird
unter `.founder/history` gesichert; fachliche Projektdateien bleiben erhalten.
Schemaänderungen werden abgelehnt und brauchen eine explizite Migration.
Bei einem Rückweg den gesicherten project.json-Vertrag wiederherstellen und
`bind` zur alten unveränderten Installation ausführen; dann relevante Checks prüfen.
Ein wiederholtes identisches Update erzeugt keine zusätzliche Vertragsänderung.
Ein Initialisiererfehler rollt eigene geschriebene Dateien zurück. Bei hartem
Prozessabbruch erst Lock/Dateien inspizieren; Lock nicht blind entfernen.
Mehrere Prozesse dürfen dieselben Kontextdateien nicht gleichzeitig bearbeiten.

## Fortsetzen und Beispiel-Prompt

> Arbeite in diesem Projekt mit seiner AGENTS.md. Lies den persistenten Kontext,
> prüfe die gebundene Founder-OS-Version und wähle nur relevante Module. Setze die
> nächste offene Aufgabe vollständig um. Erhalte Daten und vorhandene Funktionen,
> prüfe Erfolg, Fehler und Wiederholung soweit betroffen und aktualisiere Zustand
> und Übergabe mit tatsächlich ausgeführten Checks. Frage nur bei blockierenden
> Entscheidungen oder noch nicht autorisierten erheblichen Folgen.
