CREATE TABLE dictionary__kanji_onyomi (
    id INTEGER PRIMARY KEY,

    kanji_id INTEGER NOT NULL,
    reading TEXT NOT NULL,

    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (kanji_id) REFERENCES dictionary__kanji(id),

    UNIQUE (kanji_id, reading)
);