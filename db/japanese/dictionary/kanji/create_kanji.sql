CREATE TABLE dictionary__kanji (
    id INTEGER PRIMARY KEY,

    kanji_id INTEGER NOT NULL UNIQUE,
    
    en_name TEXT NOT NULL,
    stroke_count INTEGER NOT NULL,

    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (kanji_id) REFERENCES characters__kanji(id)
);