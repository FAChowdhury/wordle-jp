#!/usr/bin/env bash
set -euxo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

DB="japanese.db"
rm -f "$DB"

MANIFEST="db_manifest.txt"

echo "Building SQLite database from db_manifest.txt ..."

{
  echo "PRAGMA foreign_keys = ON;"

  while IFS= read -r file; do
    [[ -z "$file" ]] && continue
    [[ "$file" =~ ^# ]] && continue

    echo ".read $file"
  done < "$MANIFEST"

} | sqlite3 "$DB"

echo "Database built successfully"