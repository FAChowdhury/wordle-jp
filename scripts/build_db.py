#!/usr/bin/env python3
"""Build SQLite database from db_manifest.txt into build/ directory.

This mirrors scripts/build_db.sh behavior but uses Python's sqlite3 module
to execute SQL files listed in db_manifest.txt. The manifest is read from the
repository root (git rev-parse --show-toplevel).
"""
from pathlib import Path
import sqlite3
import subprocess
import sys


def repo_root() -> Path:
	try:
		out = subprocess.run(["git", "rev-parse", "--show-toplevel"], check=True, stdout=subprocess.PIPE, text=True)
		return Path(out.stdout.strip())
	except subprocess.CalledProcessError:
		# fallback to current working directory
		return Path.cwd()


def main() -> int:
	root = repo_root()
	manifest = root / "db_manifest.txt"
	if not manifest.exists():
		print(f"Manifest not found: {manifest}", file=sys.stderr)
		return 2
	# Allow optional output DB path as first argument (used by CMake)
	if len(sys.argv) > 1:
		db_path = Path(sys.argv[1])
		# If a relative path was provided, make it absolute relative to repo root
		if not db_path.is_absolute():
			db_path = root / db_path
		db_path.parent.mkdir(parents=True, exist_ok=True)
	else:
		build_dir = root / "build"
		build_dir.mkdir(parents=True, exist_ok=True)
		db_path = build_dir / "japanese.db"
	if db_path.exists():
		db_path.unlink()

	print(f"Building SQLite database at: {db_path}")

	conn = sqlite3.connect(str(db_path))
	try:
		conn.execute("PRAGMA foreign_keys = ON;")

		with manifest.open("r", encoding="utf-8") as fh:
			for raw in fh:
				line = raw.strip()
				if not line or line.startswith("#"):
					continue

				sql_file = root / line
				if not sql_file.exists():
					print(f"SQL file not found: {sql_file}", file=sys.stderr)
					return 3

				print(f"Executing: {line}")
				sql = sql_file.read_text(encoding="utf-8")
				# executescript allows multiple statements per file
				conn.executescript(sql)

		conn.commit()
	finally:
		conn.close()

	print("Database built successfully")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
