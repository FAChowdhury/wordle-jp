CREATE TABLE classification__kanji (
    id INTEGER PRIMARY KEY,

    kanji_id INTEGER NOT NULL UNIQUE,

    jlpt INTEGER,
    grade INTEGER,

    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (kanji_id) REFERENCES characters.kanji(id)
);