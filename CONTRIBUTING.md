# Contributing

Start with a real reproducible problem and a minimal improvement proposal using
[the proposal contract](templates/improvement.md). Keep canonical rules centralized;
skills link conditional detail. Don't add process without a demonstrated use.
Run `python scripts/founder.py validate` and unittest discovery before review.
Update provenance mapping when changing migrated content and retain MIT notices.
Review redistribution rights before publishing user-supplied material.

Semantic versioning: patch for compatible corrections, minor for additive modules,
major for breaking project/context contracts. Any runtime edit changes its digest;
release a new immutable installation and update projects explicitly. Document data
migrations and rollback before a schema change. Commit no project/customer data.
