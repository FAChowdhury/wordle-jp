CREATE TABLE dictionary.radicals (
    id INTEGER PRIMARY KEY,

    radical_id INTEGER NOT NULL UNIQUE,
    
    en_name TEXT NOT NULL,
    reading TEXT NOT NULL,
    stroke_count INTEGER NOT NULL,

    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (radical_id) REFERENCES characters.radicals(id)
);