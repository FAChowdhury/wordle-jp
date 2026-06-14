import sqlite3
from pathlib import Path
import subprocess
import sys


def repo_root() -> Path:
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"], check=True, stdout=subprocess.PIPE, text=True)
        return Path(out.stdout.strip())
    except subprocess.CalledProcessError:
        return Path.cwd()


# Allow overriding DB path and output directory via command-line arguments.
# Usage: generate_dictionary.py <db_path> <out_dir>
root = repo_root()
if len(sys.argv) > 1:
    db_path = Path(sys.argv[1])
    if not db_path.is_absolute():
        db_path = root / db_path
else:
    # Prefer build output path under the repo root if present (relative, not absolute)
    default_out_db = root / "out" / "build" / "x64-debug" / "japanese.db"
    if default_out_db.exists():
        db_path = default_out_db
    else:
        db_path = root / "database" / "japanese.db"

# Output directory for generated headers (second arg)
if len(sys.argv) > 2:
    out_dir = Path(sys.argv[2])
    if not out_dir.is_absolute():
        out_dir = root / out_dir
else:
    out_dir = root / "code-gen"

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# -----------------------
# COUNT QUERY
# -----------------------
cur.execute("SELECT COUNT(*) FROM characters__kanji")
KANJI_COUNT = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM characters__kanji_radicals")
RADICAL_COUNT = cur.fetchone()[0]

# -----------------------
# 1. constants.hpp
# -----------------------
constants = f"""#pragma once
#include <cstddef>

namespace dictionary {{
    inline constexpr std::size_t KANJI_COUNT {{{KANJI_COUNT}}};
    inline constexpr std::size_t RADICAL_COUNT {{{RADICAL_COUNT}}};
}};
"""


# -----------------------
# 2. radicals.hpp
# -----------------------
cur.execute("""
SELECT
    r.character
FROM characters__kanji_radicals kr
JOIN characters__radicals r
    ON r.id = kr.radical_id
ORDER BY kr.kanji_id, kr.radical_order;
""")

radicals = [r[0] for r in cur.fetchall()]

radicals_hpp = """#pragma once
#include <array>
#include <cstdint>

#include "dictionary_constants.hpp"

namespace dictionary
{
    inline constexpr std::array<char32_t, RADICAL_COUNT> radicals = {
"""

radicals_lines = [f"        U'{r}'" for r in radicals]
if radicals_lines:
    radicals_hpp += ",\n".join(radicals_lines)

radicals_hpp += """
    };
};
"""

# -----------------------
# 3. entries.hpp
# -----------------------
'''
cur.execute("""
SELECT kanji, offset, count
FROM kanji_radical_index
ORDER BY kanji
""")

entries = cur.fetchall()
'''

entries = []
entries_hpp = """#pragma once
#include <array>
#include <cstdint>

#include "dictionary_constants.hpp"

namespace dictionary {
    struct RadicalRange {
        std::uint32_t offset;
        std::uint16_t count;
    };

    struct Entry {
        char32_t kanji;
        RadicalRange radicals;
    };

    inline constexpr std::array<Entry, KANJI_COUNT> entries {
"""

entries_hpp += ",\n".join(
    f"    {{ U'{k}', {{ {o}, {c} }} }}"
    for (k, o, c) in entries
)

entries_hpp += """
    };
};
"""


# -----------------------
# WRITE FILES
# -----------------------
out_dir.mkdir(parents=True, exist_ok=True)

(out_dir / "dictionary_constants.hpp").write_text(constants, encoding='utf-8')
(out_dir / "dictionary_radicals.hpp").write_text(radicals_hpp, encoding='utf-8')
(out_dir / "dictionary_entries.hpp").write_text(entries_hpp, encoding='utf-8')


print("Generated all dictionary headers.")