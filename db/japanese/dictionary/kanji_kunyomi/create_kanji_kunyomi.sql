CREATE TABLE dictionary.kanji_kunyomi (
    id INTEGER PRIMARY KEY,

    kanji_id INTEGER NOT NULL,
    reading TEXT NOT NULL,

    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (kanji_id) REFERENCES dictionary.kanji(id),

    UNIQUE (kanji_id, reading)
);