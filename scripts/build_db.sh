#!/usr/bin/env bash

set -euxo pipefail

DB="japanese.db"

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

rm -f "$DB"

# level 0
sqlite3 "$DB" < db/japanese/characters/kanji/create_kanji.sql
sqlite3 "$DB" < db/japanese/characters/radicals/create_radicals.sql

# level 1
sqlite3 "$DB" < db/japanese/characters/kanji/create_kanji_readings.sql

sqlite3 "$DB" < db/japanese/dictionary/kanji/create_kanji.sql
sqlite3 "$DB" < db/japanese/dictionary/radicals/create_radicals.sql

sqlite3 "$DB" < db/japanese/classification/kanji/create_kanji.sql

# level 2
sqlite3 "$DB" < db/japanese/dictionary/kanji_meaning/create_kanji_meaning.sql
sqlite3 "$DB" < db/japanese/dictionary/kanji_onyomi/create_kanji_onyomi.sql
sqlite3 "$DB" < db/japanese/dictionary/kanji_kunyomi/create_kanji_kunyomi.sql

echo "Database built successfully"