# Skills and workflows

| Skill | Aufgabe | Typische Artefakte |
| --- | --- | --- |
| founder-board | Idee mit drei veröffentlichten Denkmodellen prüfen | idea, board brief/memos/verdict |
| founder-competitors | direkte/indirekte Konkurrenz und Ersatzlösungen | competitors CSV/Markdown |
| founder-consumer | simulierte Forschung vorbereiten und zählen | personas, briefs, answers, results |
| founder-pricing | Preisempfindlichkeit, Vergleich und Kostengrenze | pricing, pricing curve |
| founder-offer | Einwände in tragfähiges Angebot übersetzen | offer, versioned pitch |
| founder-cfo | Stückkosten, Ramp, Break-even, Cash und Szenarien | numbers, cfo report, sources |
| founder-marketing | Positionierung, Kanäle und Kampagne | dated marketing plan |
| founder-brand | Name, Stimme, Gestaltungsbrief und Rechteprüfung | brand brief |
| founder-ops | Lieferanten, Personal, SOPs, Pflichten und Risiken | operations and revised costs |
| founder-launch | realer Test, Countdown und erste Betriebswochen | launch runbook |
| founder-plan | Modellurteil und Businessplan aus vorhandenen Daten | summary, plan, one-pager |
| founder-product | Anforderungen, Akzeptanz und Roadmap | project context/tasks |
| founder-build | Architektur, Implementierung, Bugfix, Test und Review | working code and evidence |
| founder-release | Deployment, Betriebsübergabe und Archivierung | release/rollback/operations evidence |
| founder-framework | kontrollierte zentrale Verbesserung/Versionierung | proposal, tested change, update preview |
| founder-charts | wahrheitsgetreue zugängliche Diagramme | chart decision and checked UI |

Separate Projekte erhalten zusätzlich den erzeugten `founder-context`-Bridge-Skill.
Er gehört nicht zum zentralen Katalog von 16 Fach-Skills und dupliziert keine Methoden.

17 Workflows: discovery, validation, strategy, definition, planning, architecture,
design, implementation, testing, review, deployment, launch, operation, optimization,
archive, bugfix und improvement. Jeder benennt Ziel, Voraussetzung, Verantwortung,
Schritte, Artefakte, Abnahme und Übergang. [Routen](../core/routes.json) ordnen Skills
und Standards zu. Optimierung und Skalierung teilen einen Workflow; Ideenfindung
und Problemdefinition teilen Discovery. Recherche ist Bestandteil von Validation.
Die Phasen sind kein erzwungener Wasserfall: ein Bugfix kehrt in die vorherige
Phase zurück, ein kleines Skript kann Definition und Implementierung verbinden.

Vier Offline-Tools: `unit_economics.py`, `panel.py`, `van_westendorp.py`, `compile.py`
liegen jeweils neben ihrer Business-Methode. Der zentrale `scripts/founder.py`
bietet init, adopt, status, route, validate, install, bind, update und fingerprint.
Beispiele zu Businessdaten sind ausdrücklich synthetisch und keine Referenzkunden.
