CREATE TABLE characters__kanji_radicals (
    id INTEGER PRIMARY KEY,

    kanji_id INTEGER NOT NULL,
    radical_id INTEGER NOT NULL,

    radical_order INTEGER NOT NULL,

    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (kanji_id) REFERENCES characters__kanji(id),
    FOREIGN KEY (radical_id) REFERENCES characters__radicals(id),

    UNIQUE (kanji_id, radical_id)
);